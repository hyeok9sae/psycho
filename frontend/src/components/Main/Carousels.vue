<template>
  <v-carousel cycle :height="windowHeight" hide-delimiters>
    <v-carousel-item>
      <v-img src="../../assets/hero01.png">
        <div class="display-33">우리는 늘 이겨냈고</div>
      </v-img>
    </v-carousel-item>

    <v-carousel-item>
      <v-img src="../../assets/hero02.png">
        <div class="display-33">이번에도 함께 이겨낼 것입니다.</div>
      </v-img>
    </v-carousel-item>

    <v-carousel-item>
      <v-img src="../../assets/hero03.jpg">
        <div class="display-33">힘든 시기를 헤쳐 나가는</div>
      </v-img>
    </v-carousel-item>

    <v-carousel-item>
      <v-img src="../../assets/hero04.jpg">
        <div class="display-33">모든 분들을</div>
      </v-img>
    </v-carousel-item>

    <v-carousel-item>
      <v-img src="../../assets/hero05.jpg">
        <div class="display-33">응원합니다!</div>
      </v-img>
    </v-carousel-item>

    <!-- <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <v-sheet height="100%">
        <v-row> SLIDE </v-row>
        <v-row class="fill-height" align="center" justify="center">
          <v-img src="../../assets/hero01.png">
            <div class="display-3">{{ slide }}</div>
          </v-img>
        </v-row>
      </v-sheet>
    </v-carousel-item> -->
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      windowHeight: window.innerHeight - 64,
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4",
      ],
      // slides: ["우리는 늘 이겨냈고","이번에도 함께 이겨낼 것입니다.", "힘든 시기를 헤쳐 나가는", "모든 분들을", "응원합니다!"],
    };
  },
};
</script>

<style>
.carousel-img {
  background-color: white;
  opacity: 0.6;
}
.display-33 {
  color: black;
  font-family: Maple;
  font-size: 60pt;
  font-style: oblique;
  text-align: center;
  margin-top: 300px;
}
</style>