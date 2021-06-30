<template>
  <!-- <v-parallax dark src="https://picsum.photos/1920/1080?random" :height="windowHeight"> -->
  <v-container :style="myStyle" fill-height fluid>
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <h1 style="font-size:40pt; font-family:Roboto;">싸 이 코</h1>
        <h4 style="font-size:20pt; color:grey">싸우자 이기자 COVID-19</h4><br><br><br><br>
        <div style="color:grey;">코로나 시대에 들어서면서 
          <span class="emp">다수의 유동인구</span>
          를 통한 감염병의 전파가 이슈가 되었습니다.<br><br>
          최대한 이동을 자제하는 것이 이상적이나 서로의 목적에 의해
          <span class="emp">이동은 불가피</span>합니다. <br><br>
          그로인해 우리는 
          <span class="emp">유동인구를 분산</span>
          시키기 위한 코로나 예방 서비스를 만들고자 <span class="emp" style="font-size:20pt;">싸이코 프로젝트</span>
          를 개발하게 되었습니다.</div>
      </v-col>
    </v-row>
  </v-container>
  <!-- </v-parallax> -->
</template>

<script>
export default {
  data() {
    return {
      myStyle : {
        height: window.innerHeight,
        width: "100%"
      }
    };
  },
  created() {
    this.initSize();
  },

  methods: {
    initSize() {
      let myheight = window.innerHeight;
      let mywidth = "100%";
      this.myStyle.height = myheight + "px";
      this.myStyle.width = mywidth;
    }
  }
};
</script>
<style scoped>
  .emp {
    margin: 0 3px;
    font-family: Maple;
    font-size: 12pt;
  }
</style>>