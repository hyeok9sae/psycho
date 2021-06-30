<template>
  <div id="ChartForm">
    <corona-Sido-chart :chart-data="ChartData" :options="options" />
    <input id="date" v-model="date" type="date" />
  </div>
</template>

<script>
import CoronaSidoChart from "./CoronaSidoChart"
import CoronaApi from "../../api/CoronaApi"

export default {
  components: {
    CoronaSidoChart,
  },
  data: () => {
    return {
      date: null,
      data: null,
      ChartData: {},
      options: {
        title: {
          display: true,
          text: "지역별 신규 확진자 발생 현황",
        },
        legend: {
          display: false,
        },
      },
    }
  },
  watch: {
    date: function() {
      this.getChart()
    },
  },
  mounted() {
    let defday = new Date()
    defday.setDate(defday.getDate() - 1) //하루 전날 데이터를 기본 데이터로
    this.date = this.getFormatDate(defday)
    this.getChart()
  },
  methods: {
    getFormatDate(date) {
      var year = date.getFullYear()
      var month = 1 + date.getMonth()
      month = month >= 10 ? month : "0" + month
      var day = date.getDate()
      day = day >= 10 ? day : "0" + day
      return year + "-" + month + "-" + day
    },
    getChart() {
      let d = this.date.split("-")
      this.data = {
        syear: d[0] * 1,
        smonth: d[1] * 1,
        sday: d[2] * 1,
        eyear: d[0] * 1,
        emonth: d[1] * 1,
        eday: d[2] * 1,
        gubun: "",
      }
      this.getDatasets(this.data)
    },
    getDatasets(data) {
      CoronaApi.requestCoronaSido(
        data,
        (res) => {
          this.ChartData = {
            labels: ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"],
            datasets: [
              {
                label: "일별 증가 확진자",
                backgroundColor: [
                  "#318074",
                  "#388F79",
                  "#3F9F7C",
                  "#46AF7D",
                  "#4DBE7C",
                  "#55CD7A",
                  "#5CDB76",
                  "#64EA71",
                  "#6DF86C",
                  "#8CFA79",
                  "#A8FC87",
                  "#C1FE94",
                  "#D7FFA3",
                  "#E9FFB1",
                  "#F6FFC0",
                  "#FFFFCF",
                  "#FFFCDF",
                ],
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              },
            ],
          }

          for (var i = 0; i < res.data.length; i++) {
            switch (res.data[i].gubun) {
              case "서울":
                this.ChartData.datasets[0].data[0] = res.data[i].incDec
                break
              case "부산":
                this.ChartData.datasets[0].data[1] = res.data[i].incDec
                break
              case "대구":
                this.ChartData.datasets[0].data[2] = res.data[i].incDec
                break
              case "인천":
                this.ChartData.datasets[0].data[3] = res.data[i].incDec
                break
              case "광주":
                this.ChartData.datasets[0].data[4] = res.data[i].incDec
                break
              case "대전":
                this.ChartData.datasets[0].data[5] = res.data[i].incDec
                break
              case "울산":
                this.ChartData.datasets[0].data[6] = res.data[i].incDec
                break
              case "세종":
                this.ChartData.datasets[0].data[7] = res.data[i].incDec
                break
              case "경기":
                this.ChartData.datasets[0].data[8] = res.data[i].incDec
                break
              case "강원":
                this.ChartData.datasets[0].data[9] = res.data[i].incDec
                break
              case "충북":
                this.ChartData.datasets[0].data[10] = res.data[i].incDec
                break
              case "충남":
                this.ChartData.datasets[0].data[11] = res.data[i].incDec
                break
              case "전북":
                this.ChartData.datasets[0].data[12] = res.data[i].incDec
                break
              case "전남":
                this.ChartData.datasets[0].data[13] = res.data[i].incDec
                break
              case "경북":
                this.ChartData.datasets[0].data[14] = res.data[i].incDec
                break
              case "경남":
                this.ChartData.datasets[0].data[15] = res.data[i].incDec
                break
              case "제주":
                this.ChartData.datasets[0].data[16] = res.data[i].incDec
                break
              default:
            }
          }
        },
        (error) => {
          console.log(error)
        }
      )
    },
  },
}
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
