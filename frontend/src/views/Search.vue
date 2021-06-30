<template>
  <v-container fluid class="pa-0 search-container" fill-height>
    <v-layout column>
      <v-flex>
        <v-app-bar dense elevation="2" color="white">
          <v-layout>
            <v-btn text color="gray" @click="clickNavbar(true)">
              <span>맛집검색</span>
            </v-btn>

            <v-btn text color="gray" @click="clickNavbar(false)">
              <span>숙소검색</span>
            </v-btn>
          </v-layout>
        </v-app-bar>
      </v-flex>
      <v-flex>
        <v-layout row>
          <v-flex xs8 class="map">
            <kakao-map 
              :storeList="stores"
              @getClickPostion="clickEnvet"></kakao-map>
          </v-flex>

          <v-flex xs4 style="background-color: #fce8e8;">
            <!-- 들어가야 하는 정보: 성별, 나이, 필요없는 기타 정보 -->
            <div class="container">
              <form @submit.prevent="submitForm">
                <img src="../assets/location.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectCity">
                  <option disabled value="">도시입력</option>
                  <option>서울특별시</option><option>부산광역시</option>
                  <option>대구광역시</option><option>인천광역시</option>
                  <option>광주광역시</option><option>대전광역시</option>
                  <option>울산광역시</option><option>세종특별자치시</option>
                  <option>경기도</option><option>강원도</option>
                  <option>충청북도</option><option>충청남도</option>
                  <option>전라북도</option><option>전라남도</option>
                  <option>경상북도</option><option>경상남도</option>
                  <option>제주특별자치도</option>
                  </select>
                </span>
                <img src="../assets/age.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectAge">
                  <option disabled value="">나이입력</option>
                  <option value="1.10대">10대</option>
                  <option value="2.20대">20대</option>
                  <option value="3.30대">30대</option>
                  <option value="4.40대">40대</option>
                  <option value="5.50대">50대</option>
                  <option value="6.60대">60대</option>
                  <option value="7.70대이상">70대이상</option>
                  </select>
                </span>
                <img src="../assets/sex.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectSex">
                  <option disabled value="">성별입력</option>
                  <option value="1.남성">남자</option>
                  <option value="2.여성">여자</option>
                  </select>
                </span>
                <!-- <button type="submit">추천을 받아볼까나..?</button> -->
                
              </form>
            </div>
            <!--  -->
            <card>
              <v-container py-0>
                <v-layout wrap>
                  <v-flex xs12 md12>
                    <div v-if="this.params.address == ''" md6 style="text-align: center; font-family:Maple; font-size:15pt;">
                      지도에서 찾고싶은 위치를 클릭해주세요!
                    </div>
                    <div v-else md6 style="text-align: center; font-family:Maple; font-size:17pt;">
                      {{ params.address }}
                    </div>
                  </v-flex>
                  <v-flex xs12 md12>
                    <div md6 style="text-align: center; font-family:Maple; font-size:17pt;">
                      당신은?!&nbsp;{{ selectCity }}&nbsp;{{ selectAge }}&nbsp;{{ selectSex }}
                    </div>
                  </v-flex>
                  <br><br>
                  <v-flex xs12 text-center>
                    <!-- <v-btn
                      rounded
                      text color="#f08c8c"
                      @click="onSubmit"
                    >내가 가야만 한다면 이 글을 눌러서 추천</v-btn> -->
                    <div v-if="this.searching">
                        <div style="background-color: gray; padding:10px; 
                        border-radius: 10px; color: white; font-family:Maple; font-size:20pt;">
                        분석중입니다...</div> 
                    </div>
                    <div v-else-if="this.params.address === '' || this.selectCity==='' || this.selectAge==='' || this.selectSex===''">
                        <div style="background-color: #f08c8c; padding:10px; 
                        border-radius: 10px; color: white; font-family:Maple; font-size:20pt;">
                        선택해야 추천받을 수 있어~</div> 
                    </div>
                    <div v-else> 
                        <v-btn @click="onSubmit" type="submit"  style="background-color: #f08c8c; padding:10px; 
                        border-radius: 10px; color: white; font-family:Maple; font-size:20pt; outline:none;">
                        추천을 받아볼까나..?</v-btn>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
          </card>
          <v-divider class="mx-4" />
          <!-- 장식용 -->
          <v-list
            three-line
            v-infinite-scroll="loadMore"
            infinite-scroll-disabled="loading"
            infinite-scroll-distance="10"
            style="max-height: calc(100vh - 280px);background-color: #fce8e8" 
            class="overflow-y-auto">
          <v-list-item v-for="(item, n) in this.stores" :key="n">
          <v-card style="width:100%;">
            <v-card-text class="text-center">
              <p class="display-1 font-weight-bold">{{item.name}}</p>
              <p class="subtitle-1 font-italic">{{item.category}}</p>
            </v-card-text>
            <v-footer color="white">
              <v-col class="text-center">
                <span class="grey--text caption font-italic">{{item.address1}}</span>
              </v-col>
            </v-footer>
          </v-card>
          </v-list-item>
          </v-list>
          <!-- 장식용 -->
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import KakaoMap from "@/components/KakaoMap";
import Card from "@/components/Card";
import StoreApi from "@/api/StoreApi";
import HotelApi from "@/api/HotelApi";

export default {
  components: {
    KakaoMap,
    Card,
  },
  data: () => ({
    selectSex: "",
    selectAge: "",
    selectCity: "",
    searching: false,
    loading: true,
    page: 0,
    pageSize: 10,
    dataSet: [],
    stores: [],
    params: {
      pos_x: 0,
      pos_y: 0,
      gender : "",
      age: "",
      address: "",
    },
    isStoreSearch: true,
  }),
  computed: {},
  methods: {
    onSubmit: async function() {
      console.log("onSubmit");
      this.stores = []
      this.page = 0
      this.searching = true
      this.params.gender = this.selectSex;
      this.params.age = this.selectAge;
      if(this.isStoreSearch) {
        await StoreApi.requestRecStore(
          this.params,
          (res) => { 
            this.dataSet = res.data
            console.log(res);
            this.pagination()
            this.searching = false
            this.loading = false
          },
          (error) => {console.log(error)}
        )
      } else {
        await HotelApi.requestRecHotel(
        this.params,
        (res) => { 
          this.dataSet = res.data
          console.log(res);
          this.pagination()
          this.searching = false
          this.loading = false
        },
        (error) => {console.log(error)}
      )
      }
    },

    loadMore: async function() {
      console.log("loadMore");
      this.loading = true;
      if (this.page < 10) {
        this.pagination()
      }
      setTimeout(() => {
        this.loading = false
      }, 500);
      console.log(this.page);
    },

    pagination: function() {
      console.log("pagination");
      var curPage = this.page * this.pageSize
      for (var i = curPage; i < curPage + this.pageSize; i++){
        this.stores.push(this.dataSet[i]);
      }
      this.page++
    },

    clickEnvet: function(clickPosition) {
      this.params.pos_x = clickPosition.pos_x;
      this.params.pos_y = clickPosition.pos_y;
      this.params.address = clickPosition.address;
    },

    clickNavbar: function(value) {
      this.isStoreSearch = value;
      console.log(this.isStoreSearch);
    }
  },
};
</script>

<style>
@font-face { 
    font-family: 'Maple'; 
    src: url(../assets/font/Maplestory_Bold.ttf) format('truetype')
}
select:focus {
  outline: none;
	box-shadow: none;
}
option {
  text-align: center;
}
select {
  width: 25%;
  color: #505050;
  font-family: "Maple";
  text-align: center;
  margin: 0 auto;
}
.search-container {
  width: 100%;
  margin: 0;
  padding: 0;
}
.search {
  width: 35%;
}
</style>
