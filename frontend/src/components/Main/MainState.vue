<template>
    <v-card :height="windowHeight">
        <v-layout class="state-layout" fill-height align-center justify-center >
            <v-flex v-scroll-reveal.reset="{ delay: 300 }" class="state" align-center indigo lighten-5>
              <div><v-img src="../../assets/worldwide.png" height="200px" width="200px"></v-img></div>
              <div>전 세계 총 확진자 수</div><br/>
              <div>34,909,703</div><br/>
            </v-flex>
            <v-flex v-scroll-reveal.reset="{ delay: 500 }" class="state" indigo lighten-4>
              card02
            </v-flex>
            <v-flex v-scroll-reveal.reset="{ delay: 700 }" class="state" blue lighten-4>
              card03
            </v-flex>
        </v-layout>
    </v-card>
</template>

<script>
  export default {
    data () {
      return {
        windowHeight: window.innerHeight,
        worldCnt: 0,
        maxWorldCnt: 34909703,
        is_comma: true
      }
    },

    filters: {
      addComma (val) {
        return val.toLocaleString()
      }
    },

  }
</script>

<style>
.state-layout {
  padding: 100px;
}
.state {
  font-size: 30px;
  width: 200px;
  height: 100%;
  text-align: center;
  margin: 20px;
}
</style>