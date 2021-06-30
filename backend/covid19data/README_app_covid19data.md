# app_covid19data

- 기능

  - 공공데이터 포털 기반 데이터 매일 갱신
  - API 기능 (Only READ?)
  - 또 없나..

- 사용하는 데이터

  - ## 공공데이터포털 Open API

    - 보건복지부 코로나19 시·도발생 현황

    - http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=(YOUR_API_KEY)&pageNo=1&numOfRows=1&startCreateDt=20200923&endCreateDt=20200923&

    - 매일 오전 10시 경 갱신

    - 구분 필드[검역, 제주, 경남, 경북, 전남, 전북, 충남, 충북, 강원, 경기, 세종, 울산, 대전, 광주, 인천, 대구, 부산, 서울, 합계] 19개

    - 샘플 데이터

      ```json
      <createDt>2020-09-23 10:11:17.386</createDt>
      <deathCnt>0</deathCnt>
      <defCnt>1459</defCnt>
      <gubun>검역</gubun>
      <gubunCn>隔離區</gubunCn>
      <gubunEn>Lazaretto</gubunEn>
      <incDec>6</incDec>
      <isolClearCnt>1366</isolClearCnt>
      <isolIngCnt>93</isolIngCnt>
      <localOccCnt>0</localOccCnt>
      <overFlowCnt>6</overFlowCnt>
      <qurRate>-</qurRate>
      <seq>4510</seq>
      <stdDay>2020년 09월 23일 00시</stdDay>
      <updateDt>null</updateDt>
      ```

    - #### 출력결과(Response Element)

      |              항목명(국문)               |  항목명(영문)  | 항목크기 | 항목구분 |       샘플데이터        |                항목설명                 |
      | :-------------------------------------: | :------------: | :------: | :------: | :---------------------: | :-------------------------------------: |
      |                결과코드                 |   resultCode   |    2     |   필수   |           00            |                결과코드                 |
      |               결과메시지                |   resultMsg    |    50    |   필수   |           OK            |               결과메시지                |
      |            한 페이지 결과 수            |   numOfRows    |    4     |   필수   |           10            |            한 페이지 결과 수            |
      |               페이지 번호               |     pageNo     |    4     |   필수   |            1            |               페이지번호                |
      |              전체 결과 수               |   totalCount   |    4     |   필수   |            3            |              전체 결과 수               |
      | 게시글번호(국내 시도별 발생현황 고유값) |      SEQ       |    30    |   필수   |           130           | 게시글번호(국내 시도별 발생현황 고유값) |
      |              등록일시분초               |   CREATE_DT    |    30    |          | 2020-04-10 11:15:59.026 |              등록일시분초               |
      |                사망자 수                |   DEATH_CNT    |    15    |          |           204           |                사망자 수                |
      |              시도명(한글)               |     GUBUN      |    30    |          |          부산           |              시도명(한글)               |
      |             시도명(중국어)              |    GUBUN_CN    |    30    |          |          null           |             시도명(중국어)              |
      |              시도명(영어)               |    gubunEn     |    30    |          |          null           |              시도명(영어)               |
      |            전일대비 증감 수             |    INC_DEC     |    15    |          |           39            |            전일대비 증감 수             |
      |              격리 해제 수               | ISOL_CLEAR_CNT |    15    |          |          6973           |              격리 해제 수               |
      |             10만명당 발생률             |    QUR_RATE    |    30    |          |          20.10          |             10만명당 발생률             |
      |                기준일시                 |    STD_DAY     |    30    |          |  2020년 3월 13일 00시   |                기준일시                 |
      |              수정일시분초               |   UPDATE_DT    |    30    |          |          null           |              수정일시분초               |

      > defCnt = 확진자
      >
      > incDec = 추가 확진자
      >
      > isolClearCnt = 퇴원
      >
      > isolIngCnt = 치료중
      >
      > localOccCnt = Domestic Origin (국내 기원)
      >
      > overFlowCnt = Overseas Origin (국제 기원)

  - ## 보건복지부 코로나19 감염 현황

    - http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=(YOUR_API_KEY)&pageNo=1&numOfRows=10&startCreateDt=20200923&endCreateDt=20200923&

    - 매일 오전 10시 경 갱신

    - 샘플 데이터

      ```json
      <accDefRate>1.0381099387</accDefRate>
      <accExamCnt>2256899</accExamCnt>
      <accExamCompCnt>2236372</accExamCompCnt>
      <careCnt>2178</careCnt>
      <clearCnt>20650</clearCnt>
      <createDt>2020-09-23 10:10:59.643</createDt>
      <deathCnt>388</deathCnt>
      <decideCnt>23216</decideCnt>
      <examCnt>20527</examCnt>
      <resutlNegCnt>2213156</resutlNegCnt>
      <seq>270</seq>
      <stateDt>20200923</stateDt>
      <stateTime>00:00</stateTime>
      <updateDt>null</updateDt>
      ```

    - #### 출력결과(Response Element)

      |        항목명(국문)         |   항목명(영문)    | 항목크기 | 항목구분 |       샘플데이터        |          항목설명           |
      | :-------------------------: | :---------------: | :------: | :------: | :---------------------: | :-------------------------: |
      |          결과코드           |    resultCode     |    2     |   필수   |           00            |          결과코드           |
      |         결과메시지          |     resultMsg     |    50    |   필수   |           OK            |         결과메시지          |
      |      한 페이지 결과 수      |     numOfRows     |    4     |   필수   |           10            |      한 페이지 결과 수      |
      |         페이지 번호         |      pageNo       |    4     |   필수   |            1            |         페이지번호          |
      |        전체 결과 수         |    totalCount     |    4     |   필수   |            3            |        전체 결과 수         |
      | 게시글번호(감염현황 고유값) |        SEQ        |    30    |   필수   |           74            | 게시글번호(감염현황 고유값) |
      |           기준일            |     STATE_DT      |    30    |   필수   |        20200315         |           기준일            |
      |          기준시간           |    STATE_TIME     |    30    |   필수   |          00:00          |          기준시간           |
      |          확진자 수          |    DECIDE_CNT     |    15    |   필수   |          8162           |          확진자 수          |
      |         격리해제 수         |     CLEAR_CNT     |    15    |   필수   |           834           |         격리해제 수         |
      |         검사진행 수         |     EXAM_CNT      |    15    |   필수   |          16272          |         검사진행 수         |
      |          사망자 수          |     DEATH_CNT     |    15    |   필수   |           75            |          사망자 수          |
      |       치료중 환자 수        |     CARE_CNT      |    15    |   필수   |          7253           |       치료중 환자 수        |
      |        결과 음성 수         |  RESUTL_NEG_CNT   |    15    |   필수   |         243778          |        결과 음성 수         |
      |        누적 검사 수         |   ACC_EXAM_CNT    |    15    |   필수   |         268212          |        누적 검사 수         |
      |      누적 검사 완료 수      | ACC_EXAM_COMP_CNT |    15    |   필수   |         251940          |      누적 검사 완료 수      |
      |         누적 환진률         |   ACC_DEF_RATE    |    30    |   필수   |      3.2396602365       |         누적 환진률         |
      |        등록일시분초         |     CREATE_DT     |    30    |   필수   | 2020-03-15 10:01:22.000 |        등록일시분초         |
      |        수정일시분초         |     UPDATE_DT     |    30    |   필수   |          null           |        수정일시분초         |

  - ## 보건복지부 코로나19 연령별·성별감염 현황

    - http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson?serviceKey=(YOUR_API_KEY)&pageNo=1&numOfRows=1&startCreateDt=20200923&endCreateDt=20200923&

    - 매일 오후 2시~4시경 갱신

    - 샘플 데이터

      ```json
      <confCase>555</confCase>
      <confCaseRate>2.39</confCaseRate>
      <createDt>2020-09-23 14:14:20.925</createDt>
      <criticalRate>0</criticalRate>
      <death>0</death>
      <deathRate>0.00</deathRate>
      <gubun>0-9</gubun>
      <seq>3544</seq>
      <updateDt>null</updateDt>
      ```

    - #### 출력결과(Response Element)

      |             항목명(국문)              |  항목명(영문)  | 항목크기 | 항목구분 |       샘플데이터        |               항목설명                |
      | :-----------------------------------: | :------------: | :------: | :------: | :---------------------: | :-----------------------------------: |
      |               결과코드                |   resultCode   |    2     |   필수   |           00            |               결과코드                |
      |              결과메시지               |   resultMsg    |    50    |   필수   |           OK            |              결과메시지               |
      |           한 페이지 결과 수           |   numOfRows    |    4     |   필수   |           10            |           한 페이지 결과 수           |
      |              페이지 번호              |     pageNo     |    4     |   필수   |            1            |              페이지번호               |
      |             전체 결과 수              |   totalCount   |    4     |   필수   |            3            |             전체 결과 수              |
      | 게시글번호(확진자 성별,연령별 고유값) |      SEQ       |    30    |   필수   |           134           | 게시글번호(확진자 성별,연령별 고유값) |
      |          구분(성별, 연령별)           |     GUBUN      |    30    |   필수   |           0-9           |          구분(성별, 연령별)           |
      |                확진자                 |   CONF_CASE    |    30    |   필수   |           132           |                확진자                 |
      |                확진률                 | CONF_CASE_RATE |    30    |   필수   |          1.25           |                확진률                 |
      |                사망자                 |     DEATH      |    30    |   필수   |            0            |                사망자                 |
      |                사망률                 |   DEATH_RATE   |    30    |   필수   |          0.00           |                사망률                 |
      |                치명률                 | CRITICAL_RATE  |    30    |   필수   |            0            |                치명률                 |
      |             등록일시분초              |   CREATE_DT    |    30    |   필수   | 2020-04-13 10:22:29.663 |             등록일시분초              |
      |             수정일시분초              |   UPDATE_DT    |    30    |   필수   |          null           |             수정일시분초              |

  - 보건복지부 코로나19 해외발생 현황

    - 해외데이터? 보류

  - 수집한 데이터

    - 곧 정리 하겠음

- 고민중인 문제

  - api 키 git에 노출되지 않게 어떻게 하노 : 코치님 답변

    > 별도 json 파일로 관리하는 방식, 해당 파일은 gitignore
    >
    > 배포환경에선 aws에 같은 값을 파일로두어 읽어들여 사용하는 방식으로 사용
    >
    > dotenv라는 환경변수에 저장해서 사용하는 방식도 있음
    >
    > https://velog.io/@yvvyoon/python-env-dotenv

- 할일

  - 최근까지 데이터 DB에 저장

    - 공공데이터api결과 json -> csv -> db import

  - 매일 데이터 갱신시키는 코드 작성

    - 공공데이터 사이트에 제공하는 샘플코드 있음. 참고

    ```python
    # from urllib import urlencode, quote_plus
    # from urllib2 import Request, urlopen
    # 파이썬3부터 밑에 코드로 바뀜 ㅡ_ㅡ
    from urllib.parse import urlencode, quote_plus
    from urllib.request import Request, urlopen
    ```

    ```python
    ##############################제공 샘플코드에 추가##############################
    # - api key decoding
    # - today
    import requests
    from datetime import datetime
    api_key = "YOUR_API_KEY"

    api_key_decode = requests.utils.unquote(api_key) # 키 디코딩
    today = datetime.today().strftime("%Y%m%d") # 현재날짜 문자열 요청 양식에 맞게 생성
    ##############################################################################
    ```

  - rest api 코드 작성

  -
