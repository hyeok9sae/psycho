<template>
	<div>
        <div class="box">
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
            <div @click="onCovidClick"> </div>
        </div>
        <h2><span style="font-size:70pt; color:#f08c8c;">싸</span>우자<br>
        <span style="font-size:70pt; color:#f08c8c;">&emsp;&emsp;이</span>기자<br>
        <span style="font-size:70pt; color:#f08c8c;">&emsp;&emsp;&emsp;&emsp;코</span>로나</h2>
    </div>
</template>

<script>
export default {
    methods: {
        onCovidClick() {
            console.log("click")
            this.$router.push("/home")
        }
    }
}
</script>

<style scoped>
@font-face { 
    font-family: 'Maple'; 
    src: url(../assets/font/Maplestory_Bold.ttf) format('truetype'); 
}

* {
margin: 0;
padding: 0;
}
.box {
width: 100%;
height: 100vh;
/* linear-gradient(180deg, rgba(240, 140, 140, 0.5) 0%, rgba(240,140,140,0.2) 35%, rgba(255, 255, 255, 0.6) 100%) */
background-image: linear-gradient(180deg, rgba(240, 140, 140, 0.3) 0%, rgba(240,140,140,0.2) 35%, rgba(0, 0, 0, 0.4) 100%)
,url("../assets/strange2.png");
background-repeat: no-repeat, no-repeat;  
background-size: 100% 100%;
}

h2 {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%,-50%);
color: #cccccc;
font-family: Maple;
font-weight: 900;
text-transform: uppercase;
font-size: 60px;
}

.box div {
height: 60px;
width: 60px;
position: absolute;
top: 10%;
left: 10%;
animation: animate 4s linear infinite;
background-image: url("../assets/covid.png");
background-size: 100% 100%;
border-radius: 30px;
}

.box div:hover {
    background-image: url("../assets/covidRemove.png");
}

.box div:nth-child(1) {
top: 20%;
left: 20%;
animation: animate 8s linear infinite;
}
.box div:nth-child(2) {
top: 26%;
left: 89%;
animation: animate 10s linear infinite;
}
.box div:nth-child(3) {
top: 80%;
left: 90%;
animation: animate 5s linear infinite;
}
.box div:nth-child(4) {
top: 65%;
left: 75%;
animation: animate 7s linear infinite;
}
.box div:nth-child(5) {
top: 90%;
left: 10%;
animation: animate 9s linear infinite;
}
.box div:nth-child(6) {
top: 30%;
left: 60%;
animation: animate 5s linear infinite;
}
.box div:nth-child(7) {
top: 70%;
left: 33%;
animation: animate 8s linear infinite;
}
.box div:nth-child(8) {
top: 75%;
left: 60%;
animation: animate 10s linear infinite;
}
.box div:nth-child(9) {
top: 23%;
left: 50%;
animation: animate 6s linear infinite;
}
.box div:nth-child(10) {
top: 35%;
left: 7%;
animation: animate 10s linear infinite;
}
@keyframes animate {
0% {
transform: scale(0) translateY(0) rotate(50deg);
}
100% {
transform: scale(1.6) translateY(-250px) rotate(360deg);
}
}

</style>