<template>
  <div id="ChartForm">
    <corona-gender-chart :chart-data="ChartData" :options="options" />
    <input id="date" v-model="date" type="date" />
  </div>
</template>

<script>
import CoronaGenderChart from "./CoronaGenderChart";
import CoronaApi from "../../api/CoronaApi";

export default {
  components: {
    CoronaGenderChart,
  },
  data: () => {
    return {
      date: null,
      data: null,
      ChartData: {},
      options: {
        title: {
          display: true,
          text: "성별 확진자 합계 현황",
        },
        legend: {
          display: false,
        },
      },
    };
  },
  watch: {
    date: function () {
      this.getChart();
    },
  },
  mounted() {
    let defday = new Date();
    defday.setDate(defday.getDate() - 1); //하루 전날 데이터를 기본 데이터로
    this.date = this.getFormatDate(defday);
    this.getChart();
  },
  methods: {
    getFormatDate(date) {
      var year = date.getFullYear();
      var month = 1 + date.getMonth();
      month = month >= 10 ? month : "0" + month;
      var day = date.getDate();
      day = day >= 10 ? day : "0" + day;
      return year + "-" + month + "-" + day;
    },
    getChart() {
      let d = this.date.split("-");
      this.data = {
        syear: d[0] * 1,
        smonth: d[1] * 1,
        sday: d[2] * 1,
        eyear: d[0] * 1,
        emonth: d[1] * 1,
        eday: d[2] * 1,
        gubun: "성",
      };
      this.getDatasets(this.data);
    },
    getDatasets(data) {
      CoronaApi.requestCoronaGenAge(
        data,
        (res) => {
          this.ChartData = {
            labels: ["남성", "여성"],
            datasets: [
              {
                label: "확진자",
                backgroundColor: ["#8c8cf4", "#f48c8c"],
                data: [0, 0],
              },
            ],
          };
          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i].gubun == "남성") {
              this.ChartData.datasets[0].data[0] = res.data[i].confCase;
              // this.ChartData.datasets[0].data.push(res.data[i].death);
            } else if (res.data[i].gubun == "여성") {
              this.ChartData.datasets[0].data[1] = res.data[i].confCase;
              // this.ChartData.datasets[1].data.push(res.data[i].death);
            }
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
};
/*
요청 json 형식
{
    "syear": 2020, //시작년도
    "smonth": 9, //시작월
    "sday": 4, //시작일
    "eyear": 2020, //끝년도
    "emonth": 9, //끝월
    "eday": 4, //끝일
}
*/
</script>

<style scoped>
#date {
  margin-top: 10px;
}
#ChartForm {
  text-align: center;
  width: 33%;
  height: 430px;
}
</style>