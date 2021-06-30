<template>
  <div id="ChartForm">
    <corona-age-chart :chart-data="ChartData" :options="options" />
    <input id="date" v-model="date" type="date" />
  </div>
</template>

<script>
import CoronaAgeChart from "./CoronaAgeChart";
import CoronaApi from "../../api/CoronaApi";

export default {
  components: {
    CoronaAgeChart,
  },
  data: () => {
    return {
      date: null,
      data: null,
      ChartData: {},
      options: {
        title: {
          display: true,
          text: "연령별 확진자 합계 현황",
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
        gubun: "0",
      };
      this.getDatasets(this.data);
    },
    getDatasets(data) {
      CoronaApi.requestCoronaGenAge(
        data,
        (res) => {
          this.ChartData = {
            labels: [
              "0-9",
              "10-19",
              "20-29",
              "30-39",
              "40-49",
              "50-59",
              "60-69",
              "70-79",
              "80-",
            ],
            datasets: [
              {
                label: "확진자",
                backgroundColor: [
                  "#FFF8E1",
                  "#FFECB3",
                  "#FFE082",
                  "#FFD54F",
                  "#FFCA28",
                  "#FFB300",
                  "#FFA000",
                  "#FF8F00",
                  "#FF6F00",
                ],
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0],
              },
            ],
          };
          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i].gubun == "0-9") {
              this.ChartData.datasets[0].data[0] = res.data[i].confCase;
            } else if (res.data[i].gubun == "10-19") {
              this.ChartData.datasets[0].data[1] = res.data[i].confCase;
            } else if (res.data[i].gubun == "20-29") {
              this.ChartData.datasets[0].data[2] = res.data[i].confCase;
            } else if (res.data[i].gubun == "30-39") {
              this.ChartData.datasets[0].data[3] = res.data[i].confCase;
            } else if (res.data[i].gubun == "40-49") {
              this.ChartData.datasets[0].data[4] = res.data[i].confCase;
            } else if (res.data[i].gubun == "50-59") {
              this.ChartData.datasets[0].data[5] = res.data[i].confCase;
            } else if (res.data[i].gubun == "60-69") {
              this.ChartData.datasets[0].data[6] = res.data[i].confCase;
            } else if (res.data[i].gubun == "70-79") {
              this.ChartData.datasets[0].data[7] = res.data[i].confCase;
            } else if (res.data[i].gubun == "80 이상") {
              this.ChartData.datasets[0].data[8] = res.data[i].confCase;
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