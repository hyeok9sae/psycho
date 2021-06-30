<template>
    <div class=test-body>
        <div class=test-container>
          <span class=small-container>
            <span style="font-size:80%;">확진환자</span>
            <br><span id="counter1"></span></span>
          <span class=small-container>
            <span style="font-size:80%;">격리해제</span>
            <br><span id="counter2"></span></span>
          <span class=small-container>
            <span style="font-size:80%;">사망</span><br>
            <span id="counter3"></span></span>
        </div>
    </div>
</template>

<script>
  function numberCounter(target_frame, target_number) {
    this.count = 0; this.diff = 0;
    this.target_count = parseInt(target_number);
    this.target_frame = document.getElementById(target_frame);
    this.timer = null;
    this.counter();
  }
  numberCounter.prototype.counter = function() {
    var self = this;
    this.diff = this.target_count - this.count;
     
    if(this.diff > 0) {
        self.count += Math.ceil(this.diff / 5);
    }
     
    this.target_frame.innerHTML = this.count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
     
    if(this.count < this.target_count) {
        this.timer = setTimeout(function() { self.counter(); }, 60);
    } else {
        clearTimeout(this.timer);
    }
};
export default {
  mounted() {
    new numberCounter("counter1", 24353);
    new numberCounter("counter2", 22334);
    new numberCounter("counter3", 425);
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Montserrat');

.test-body {
    font-family: Montserrat;
    font-size: 12px;
    text-align: center;
    padding: 50px;
    background: #1c1c1c;
    display: flex;
    align-items: center;
    justify-content: center;
} 

.test-count {
  display: block;
  font-size: 24px;
  color: #f2f2f2;
  padding: 60px;
  font-weight: 600;
  width: 120px;
}

.test-container {
  width: 100%;
  display: flex;
  text-align: center;
  color: #f2f2f2;
  font-size: 2.5rem;
}

.small-container {
  width: 34%;
}
</style>