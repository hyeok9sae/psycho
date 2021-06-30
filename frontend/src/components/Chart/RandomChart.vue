<template>
  <div class="small">
    <line-chart :chart-data="datacollection"></line-chart>
    <!-- <doughnut-chart></doughnut-chart>
    <bar-chart></bar-chart>-->
    <button @click="fillData()">코로나현황</button>
  </div>
</template>

<script>
import LineChart from "./LineChart.js";
import DoughnutChart from "./DoughnutChart.js";
import BarChart from "./BarChart.js";

export default {
  components: {
    LineChart,
    // DoughnutChart,
    // BarChart,
  },
  data() {
    return {
      count: 0,
      datacollection: null,
    };
  },
  mounted() {
    this.fillData();
  },
  methods: {
    fillData() {
      this.count += 1;
      if (this.count % 2 == 0) {
        this.datacollection = {
          labels: [
            this.getRandomInt(),
            this.getRandomInt(),
            this.getRandomInt(),
          ],
          datasets: [
            {
              label: "Data One",
              backgroundColor: "#A5D6A7",
              data: [
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
              ],
            },
            {
              label: "Data Two",
              backgroundColor: "#E6EE9C",
              data: [
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
              ],
            },
          ],
        };
      } else {
        this.datacollection = {
          labels: [
            this.getRandomInt(),
            this.getRandomInt(),
            this.getRandomInt(),
            this.getRandomInt(),
          ],
          datasets: [
            {
              label: "Data One",
              backgroundColor: "#A5D6A7",
              data: [
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
              ],
            },
            {
              label: "Data Two",
              backgroundColor: "#E6EE9C",
              data: [
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
              ],
            },
            {
              label: "Data Three",
              backgroundColor: "#E6EE9C",
              data: [
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
                this.getRandomInt(),
              ],
            },
          ],
        };
      }
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
  },
};
</script>

<style>
.small {
  max-width: 200px;
  max-height: 200px;
  margin: 150px auto;
}
</style>