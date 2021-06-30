<template>
  <div id="ChartForm">
    <corona-total-chart :chart-data="ChartData" :width="5" :height="2" />
    <input id="startDate" v-model="startDate" type="date" />
    <input id="endDate" v-model="endDate" type="date" />
  </div>
</template>

<script>
import CoronaTotalChart from "./CoronaTotalChart"
import CoronaApi from "../../api/CoronaApi"

export default {
  components: {
    CoronaTotalChart,
  },
  data: () => {
    return {
      startDate: null,
      endDate: null,
      data: null,
      ChartData: {},
      options: {
        title: {
          display: true,
          text: "코로나 일반 현황",
        },
        legend: {
          display: true,
        },
      },
    }
  },
  watch: {
    startDate: function() {
      this.getChart()
    },
    endDate: function() {
      this.getChart()
    },
  },
  mounted() {
    let defday = new Date()
    defday.setDate(defday.getDate() - 1)
    this.endDate = this.getFormatDate(defday)
    defday.setMonth(defday.getMonth() - 1)
    this.startDate = this.getFormatDate(defday)
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
      let s = this.startDate.split("-")
      let e = this.endDate.split("-")
      this.data = {
        syear: s[0] * 1,
        smonth: s[1] * 1,
        sday: s[2] * 1,
        eyear: e[0] * 1,
        emonth: e[1] * 1,
        eday: e[2] * 1,
      }
      this.getDatasets(this.data)
    },
    getDatasets(data) {
      CoronaApi.requestCorona(
        data,
        (res) => {
          this.ChartData = {
            labels: [],
            datasets: [
              {
                label: "누적 확진자",
                borderColor: "#f48c8c",
                backgroundColor: "rgba(244, 140, 140, 0.3)",
                data: [],
              },
              {
                label: "누적 격리해제",
                borderColor: "#8cf48c",
                backgroundColor: "rgba(140, 244, 140, 0.5)",
                data: [],
              },
              {
                label: "누적 사망자",
                borderColor: "#8c8cf4",
                backgroundColor: "rgba(140, 140, 244, 1)",
                data: [],
              },
            ],
          }
          for (var i = 0; i < res.data.length; i++) {
            this.ChartData.labels.push(res.data[i].stateDt)
            this.ChartData.datasets[0].data.push(res.data[i].decideCnt)
            this.ChartData.datasets[1].data.push(res.data[i].clearCnt)
            this.ChartData.datasets[2].data.push(res.data[i].deathCnt)
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
#startDate,
#endDate {
  text-align-last: center;
  margin: 10px;
}

#ChartForm {
  border: 1px solid gray;
  text-align: center;
  margin: 20px auto;
  width: 90%;
}
</style>
