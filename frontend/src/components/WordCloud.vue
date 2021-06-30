<template>
  <div id="App">
    <cloud 
    nameKey="text"
    valueKey="value"
    :data="words" 
    :fontSizeMapper="fontSizeMapper"
    :width="width"
    :height="height"
    :font="fontType"
    :colors="myColors"   
    ></cloud>
  </div>
</template>
 
<script>
import Cloud from 'vue-d3-cloud'
 
export default {
    name: 'App',
    components: {
        Cloud,
    },
    data() {
        return {
            myColors: ['#ff0000', '#000000', '#f5b4b6', '#6c6c6c'],
            width: window.innerWidth * 0.8,
            height: 450,
            fontType: "Roboto",
            words:[],
            fontSizeMapper: word => Math.log2(word.value) * 5,
        }
    },
    created() {
        this.getWordCloud()
    },
    methods: {
        getWordCloud() {
            let wordList = new Array;
            d3.csv("keyword.csv", function(error, data) {
                if(error) throw error;
                for(var i = 0; i < data.length; i++){
                    wordList.push({text: data[i].tag, value: data[i].count * 100})
                }
            });
            this.words = wordList;
        }
    }
}
</script>