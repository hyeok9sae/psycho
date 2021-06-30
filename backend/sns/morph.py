from datetime import datetime

import pandas as pd

from selenium import webdriver

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request

import time
from tqdm import tqdm_notebook
from konlpy.tag import *
import warnings

from collections import Counter
import re
import shutil

warnings.filterwarnings('ignore')
okt = Okt()

def instagram_login(id, pw):
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.get(url)
    print("[login complete]")


def main_search(keyword):
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.clear()
    search.send_keys(keyword)
    search_list1 = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
    search_list1.click()


def scroll_page():
    post_link.clear()
    popularPost_len.clear()
    while True:
        pageString = driver.page_source  # page_source : 현재 렌더링된 페이지의 Elements를 모두 가져옴
        bsObj = bs(pageString, 'lxml')

        for postline in bsObj.find_all(name='div', attrs={"class": "Nnq7C weEfm"}):
            a_len = len(postline.select('a'))
            popularPost_len.append(a_len)
            # 인스타그램 게시물은 행별로 최대 3개까지 확인할 수 있는데, 최근게시물이나 마지막 게시물은 1,2개가 나올 수도 있어서 len 지정
            for post in range(a_len):
                item = postline.select('a')[post]
                link = item.attrs['href']
                if link not in post_link:  # 스크롤을 내리고 중복된 것을 제  거하지 않고 누적시키기 때문에 없는 것만 추가
                    post_link.append(link)

        last_height = driver.execute_script('return document.body.scrollHeight')  # 자바스크림트로 스크롤 길이를 넘겨줌
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # selenium에서 scroll 기능 사용
        time.sleep(SCROLL_PAUSE_TIME)
        # 프로세스 자체를 지정시간동안 기다려줌(무조건 지연)
        # driver.implicitly_wait(SCROLL_PAUSE_TIME)
        # 브라우저 엔진에서 파싱되는 시간을 기다려줌(요소가 존재하면 지연없이 코드 실행)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            # driver.implicitly_wait(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue


def popularPostSum():
    popularPost = 0
    for i in range(3):
        popularPost += popularPost_len[i]
    return popularPost


# 인기게시물은 시간순으로 나타나는 것이 아니므로
# 여기에 나타나는 항목들은 시간순으로 데이터프레임 만다는 데서 제외시키기 위한 함수​

def to_timestamp(std_date):
    date_string = std_date
    date = datetime.strptime(date_string, "%Y.%m.%d")
    time_tuple = date.timetuple()
    std_timestamp = time.mktime(time_tuple)
    return int(std_timestamp)


def date_based_crawling(std_date):
    id_list.clear()
    like_list.clear()
    tag_list.clear()
    link_list.clear()
    date_list.clear()
    month_list.clear()
    day_list.clear()
    content_list.clear()

    post_linkx = post_link[popularPostSum():]  # 스크롤 내리면서 모은 데이터 중 인기 게시물은 제외시킴
    num_of_postx = len(post_linkx)

    std_timestamp = to_timestamp(std_date)
    # 기준 날짜를 지나면 크롤링이 멈추도록 작동

    for i in tqdm_notebook(range(num_of_postx)):
        req = Request("https://www.instagram.com" + post_linkx[i], headers={'User-Agent': 'Mozila/5.0'})
        postpage = urlopen(req).read()

        post_body = bs(postpage, 'lxml', from_encoding='utf-8')
        post_core = post_body.find('meta', attrs={'property': "og:description"})
        contents = post_core['content']

        # break할 시간 비교
        posttxt = str(postpage)
        timestamp = int(posttxt[posttxt.find('taken_at_timestamp') + 20: posttxt.find('taken_at_timestamp') + 30])

        if (std_timestamp > timestamp) and (to_timestamp(date_list[-1][:10]) - timestamp) > 86400:
            pass
        if (std_timestamp > timestamp) and (to_timestamp(date_list[-1][:10]) - timestamp) < 86400:
            break
        # 게시글 중간에 오래된 게시글이 올라오는 경우가 있어서 이전 게시글과 하루 이상 차이(timestamp 86400)가 나면
        # outlier로 간주하고 pass

        # 시간
        date_list.append(datetime.fromtimestamp(timestamp).strftime('%Y.%m.%d %H:%M'))
        month_list.append(datetime.fromtimestamp(timestamp).strftime("%m"))
        day_list.append(datetime.fromtimestamp(timestamp).strftime("%d"))

        # 본문내용
        content_list.append([])
        try:  # 여러 태그중 첫번째([0]) 태그를 선택
            content = contents[contents.find(":") + 1:]
            content = clean_str(content)
            content_list[i].append(content)
            # 첫 게시글 본문 내용이 <div class="C4VMK"> 임을 알 수 있다.
            # 태그명이 div, class명이 C4VMK인 태그 아래에 있는 span 태그를 모두 선택.
        except:
            content = ' '

def clean_str(text):
    pattern = '[^\w\s]'
    text = re.sub(pattern=pattern, repl='', string=text)
    return text

def get_tags(text, ntags=50):
    spliter = Twitter()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list

SCROLL_PAUSE_TIME = 1.0
post_link = []
popularPost_len = []
id_list = []
like_list = []
tag_list = []
link_list = []
date_list = []
month_list = []
day_list = []
content_list = []

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/85.0.4183.102 Safari/537.36")
options.add_argument("--ignore-urlfetcher-cert-requests")
options.add_argument("lang=ko_KR")
url = 'https://www.instagram.com/explore/tags/%EC%BD%94%EB%A1%9C%EB%82%98/'
path = 'C:\\Users\\multicampus\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(path, chrome_options=options)

instagram_login(" ", " ")
scroll_page()
date_based_crawling("2020.09.20")
num_of_post = len(post_link)

print('총 {0}개의 게시글을 수집합니다.'.format(num_of_post))

text = ""
for i in range(0, len(content_list)):
    text += content_list[i][0].replace('그램', '').replace('스타', '')

df = pd.DataFrame(get_tags(text))
print(df)
dd = pd.DataFrame(content_list)
print(dd)
df.to_csv("keyword.csv", mode='w', encoding='utf-8', index=False)
dd.to_csv("content.csv", mode='w', encoding='utf-8', index=False)
shutil.copy2("./keyword.csv", "../../frontend/public/keyword.csv")
shutil.copy2("./content.csv", "../../frontend/public/content.csv")
driver.quit()
