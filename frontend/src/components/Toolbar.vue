<template>
  <v-app-bar color="white" id="app-toolbar" elevation="0">
    <v-spacer v-if="!responsive" />

    <v-toolbar-title @click="goSearchPage('home')">싸이코</v-toolbar-title>
    <div v-if="!responsive" class="ml-5 mt-1 subtitle">
      <span style="color: #f08c8c; font-size: 15pt;">싸</span>우자 
      <span style="color: #f08c8c; font-size: 15pt;">이</span>기자 
      <span style="color: #f08c8c; font-size: 15pt;">코</span>로나
    </div>
    <v-spacer />

    <v-app-bar-nav-icon
      v-if="responsive"
      @click.stop="onClickDrawer"
    ></v-app-bar-nav-icon>

    <v-layout v-if="!responsive" justify-end>
      <v-menu rounded>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="gray"
            depressed
            width="300px"
            left
            v-bind="attrs"
            v-on="on"
          >
            {{ searchItem }}
          </v-btn>
        </template>

        <v-list style="text-align: center;
            margin: 0; padding: 0;
            background-image: linear-gradient(180deg, rgba(240, 140, 140, 0.5) 0%, rgba(240,140,140,0.2) 35%, rgba(255, 255, 255, 0.6) 100%);
            background-repeat: no-repeat;  
            background-size: 100% 100%;
            font-family: Maple;">
          <v-list-item v-for="(item, i) in items.slice(0,10)" :key="i">
            <v-list-item-title>{{i + 1}}위 {{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn text color="#f08c8c" @click="goSearchPage('search')">
        <img src="../assets/search.png" height="17px" width="17px">&nbsp;
        <span>지도검색</span>
      </v-btn>

      <v-btn text color="#f08c8c" @click="goSearchPage('statistic')">
        <img src="../assets/coronaData.png" height="17px" width="17px">&nbsp;
        <span>코로나는 지금..</span>
      </v-btn>
    </v-layout>

    <v-spacer v-if="!responsive" />
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false,
    searchItem: "",
    interval: {},
    items: [],
  }),
  computed: {
    ...mapState("app", ["drawer"]),
  },
  mounted() {
    this.onResponsiveInverted();
    this.changeSearchItem();
    window.addEventListener("resize", this.onResponsiveInverted);
    this.getRank()
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    ...mapMutations("app", ["setDrawer"]),
    onClickDrawer() {
      this.setDrawer(!this.drawer);
    },
    onResponsiveInverted() {
      if (window.innerWidth < 900) {
        this.responsive = true;
      } else {
        this.responsive = false;
      }
    },
    changeSearchItem() {
      let itemNum = 1;
      this.interval = setInterval(() => {
        if (itemNum === 11) {
          return (itemNum = 1);
        }
        let word = this.items[itemNum].title;
        if (word.length > 8) word = word.slice(0, 8) + "...";

        // console.log(word);

        this.searchItem = itemNum + ". " + word;
        itemNum += 1;
      }, 2000);
    },
    goSearchPage(page) {
      this.$router.push(page);
    },
    getRank() {
            let wordList = new Array;
            d3.csv("keyword.csv", function(error, data) {
                if(error) throw error;
                for(var i = 0; i < data.length; i++){
                    wordList.push({title: data[i].tag})
                }
            });
            this.items = wordList;
        }
  },
};
</script>

<style scoped>
@font-face { 
    font-family: 'Maple'; 
    src: url(../assets/font/Maplestory_Bold.ttf) format('truetype'); 
}

.v-list-item {
  border-bottom: 1px solid rgb(230, 230, 230);
}
</style>