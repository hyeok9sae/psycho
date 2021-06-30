<template>
  <v-card class="pa-5">
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :display="3"
      :width="windowWidth - 300"
      :height="windowHeight"
    >
      <slide v-for="(slide, i) in slides" :key="i" :index="i">
        <figure>
          <v-layout column>
            <v-flex class="news-publisher">네이버 뉴스</v-flex>
            <v-divider class="mx-6 black"></v-divider>
            <v-layout row>

                <v-flex xs6>
                  <v-layout column>
                  <v-flex class="news-title">{{news[3*i].title}}
                    <a :href="news[3*i].url" target="_blank">
                      <img class="link-img" src="../../assets/link.png">
                    </a>
                  </v-flex>
                  
                  <img class="MainArticle" :src="news[3*i].img"/>
                  <div class="news-contents">{{news[3*i].content}}</div>
                  </v-layout>
                </v-flex>
                <v-flex xs6>
                  <v-layout column>
                  <div class="Article2">
                  <img class="SubArticle" :src="news[3*i+1].img" align="left"/>
                  <span class="Sub-title">{{news[3*i+1].title}}</span>
                  <a :href="news[3*i+1].url" target="_blank">
                    <img class="link-img" src="../../assets/link.png">
                  </a>
                  <div class="Sub-contents">{{news[3*i+1].content}}</div>
                  </div>
                  <div class="Article2">
                  <img class="SubArticle" :src="news[3*i+2].img" align="left" />
                  <span class="Sub-title">{{news[3*i+2].title}}</span>
                  <a :href="news[3*i+2].url" target="_blank">
                    <img class="link-img" src="../../assets/link.png">
                  </a>
                  <div class="Sub-contents">{{news[3*i+2].content}}</div>
                  </div>
                  </v-layout>
                </v-flex>
              
            </v-layout>
            
          </v-layout>
          <figcaption>
            COSAT
          </figcaption>
        </figure>
      </slide>
    </carousel-3d>
  </v-card>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  data() {
    return {
      windowWidth: window.innerWidth,
      windowHeight: window.innerHeight,
      slides: 3,
      news: [],
    };
  },
  components: {
    Carousel3d,
    Slide,
  },
  created() {
    const axios = require("axios");
    const cheerio = require("cheerio");
    const log = console.log;
    
    const getHtml = async () => {
        try {
            console.log("good")
            return await axios.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=46&start=0&refresh_start=0");
        } catch (error) {
            console.error(error);
        }
    };

    getHtml()
        .then(html => {
            let ulList = [];
            const $ = cheerio.load(html.data);
            const $bodyList = $("div.news ul.type01").children("li");
            
            $bodyList.each(function(i, elem){
                ulList[i] = {
                    // title: $(this).find('strong.tit-news').text(),
                    title: $(this).find('dl dt a').attr('title'),
                    url: $(this).find('dl dt a').attr('href'),
                    public: $(this).find('span._sp_each_source').text(),
                    img: $(this).find('div a img').attr('src'),
                    content: $(this).find('dl dd:nth-child(3)').text(),
                };
            });

            const data = ulList.filter(n => n.title);
            return data;
        })
        .then(res => {
          console.log(res)
          this.news = res;

          for (var i = 0; i < this.news.length; i++) {
            this.news[i].img = this.news[i].img.split('&')[0];
          }
          
          console.log(this.news)
          console.log(this.news[0].img.split('&')[0])
        });
  },
};
</script>

<style>

.carousel-3d-container figure {
  margin: 0;
  height: 80%;
}

.carousel-3d-container figure .MainArticle {
  width: 85%;
  height: 350px;
  float: left;
  margin: 20px auto;
} 

.carousel-3d-container figure .SubArticle {
  width: 40%;
  height: 200px;
  float: left;
  margin: 10px 20px;
} 

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  text-align: right;
  box-sizing: border-box;
}

.carousel-3d-slide {
  max-height: 98%;
  background-color: #f0f0f0;
  box-shadow: 10px 10px 0px #e0e0e0,
            10.5px 9.5px 0px black,
            9.5px 10.5px 0px black;
  }

.news-publisher {
  font-size: 30px;
  margin: 20px;
}

.news-title {
  text-align: center;
  font-size: 20px;
  margin: 10px;
}

.Sub-title {
  text-align: center;
  font-size: 15pt;
  width: 150px;
  margin-top: 20px;
}

.news-contents {
  font-size: 12pt;
  margin: 20px 30px;
}
.Sub-contents {
  font-size: 12pt;
  margin-top: 30px;
}
.Article2 {
  padding: 20px 30px 40px 0;
}
.carousel-3d-container figure .link-img{
  width: 20px;
  height: 20px;
  margin-left: 5px;
}
</style>
