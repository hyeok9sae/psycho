import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  data:() => ({
    chartdata: {
      labels: ['January', 'February', 'April', 'May', 'June'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: ['#f87979','#f87900','#d10101','#f80101','#f82222'],
          data: [40, 35, 30, 25, 45]
        }
      ]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true
    }
  }),

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}