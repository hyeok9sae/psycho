import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  data:() => ({
    chartData: {
    datasets: [
      {
        label: 'r1',
        backgroundColor: ['#ff0000','#773333','#aa9999'],
        data: [40, 20, 30]
      },
      {
        label: 'r2',
        backgroundColor: ['#f08c8c','#ff0000','#773333'],
        data: [40, 15, 30]
      },
      {
        label: 'r3',
        backgroundColor: ['#ff0000','#f08c8c','#aa9999'],
        data: [40, 5, 5]
      }
    ],
    labels: [
        '확진자',
        '치료중',
        '완치자'
    ]
  }
}),
  props: ['options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}