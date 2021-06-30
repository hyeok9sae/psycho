<template>
  <div id="kakaoMap">
    <div id="map" :style="myStyle"></div>
  </div>
</template>

<script>
export default {
  name: "kakaoMap",
  props: {
    storeList: Array,
  },
  data() {
    return {
      myStyle: {
        height: "",
        width: "" 
      },
      map: "",
      geocoder: "",

      curPosition: {
        pos_x: 0,
        pos_y: 0
      },
      
      clickPosition: {
        address: "",
        pos_x: 0,
        pos_y: 0,
      }
    };
  },
  created() {
    this.initSize();
  },

  watch: {
    storeList: function() {
      this.setMakers();
    }
  },

  mounted() {
    this.initMap();
    this.setCurPosition();
  },

  methods: {
    initSize() {
      let myheight = window.innerHeight - 112;
      let mywidth = "100%";
      this.myStyle.height = myheight + "px";
      this.myStyle.width = mywidth;
    },

    initMap() {

      console.log("initMap");
      this.map = new kakao.maps.Map(document.getElementById("map"), {
        center: new kakao.maps.LatLng(36.2683, 127.6358), // 지도의 중심좌표
        level: 6, // 지도의 확대 레벨
      });

      this.geocoder = new kakao.maps.services.Geocoder();

      var marker = new kakao.maps.Marker();
      var infowindow = new kakao.maps.InfoWindow({zindex:1}); // 클릭한 위치에 대한 주소를 표시할 인포윈도우입니다


      // 지도를 클릭했을 때 클릭 위치 좌표에 대한 주소정보를 표시하도록 이벤트를 등록합니다
      kakao.maps.event.addListener(this.map, 'click', (mouseEvent) => {
          this.searchDetailAddrFromCoords(mouseEvent.latLng, (result, status) => {              
              if (status === kakao.maps.services.Status.OK) {

                  this.clickPosition.address = result[0].address.address_name
                  this.clickPosition.pos_x = mouseEvent.latLng.getLng()
                  this.clickPosition.pos_y = mouseEvent.latLng.getLat()

                  console.log(this.clickPosition);

                  marker.setPosition(mouseEvent.latLng);
                  marker.setMap(this.map);

                  this.$emit('getClickPostion', this.clickPosition)
              }   
          });
      });
    },

    setMakers() {
      console.log("setMakers");

      if (this.storeList.length == 0) return;

      // 마커 클러스터러를 생성합니다
      var clusterer = new kakao.maps.MarkerClusterer({
        map: this.map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
        averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
        minLevel: 5, // 클러스터 할 최소 지도 레벨
        calculator: [5, 15, 40], // 클러스터의 크기 구분 값, 각 사이값마다 설정된 text나 style이 적용된다
        texts: ["안전", "조금 안전", "조금 위험", "위험"], // texts는 ['삐약', '꼬꼬', '꼬끼오', '치멘'] 이렇게 배열로도 설정할 수 있다
        styles: [
          {
            // calculator 각 사이 값 마다 적용될 스타일을 지정한다
            width: "60px",
            height: "60px",
            background: "rgba(000, 153, 000, .8)",
            borderRadius: "30px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "61px",
          },
          {
            width: "50px",
            height: "50px",
            background: "rgba(102, 102, 255, .8)",
            borderRadius: "25px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "51px",
          },
          {
            width: "40px",
            height: "40px",
            background: "rgba(255, 153, 0, .8)",
            borderRadius: "20px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "41px",
          },
          {
            width: "30px",
            height: "30px",
            background: "rgba(255, 051, 051, .8)",
            borderRadius: "15px",
            color: "#000",
            textAlign: "center",
            fontWeight: "bold",
            lineHeight: "31px",
          },
        ],
      });

      var markers = this.storeList.map(function (store, i) {
        return new kakao.maps.Marker( {
          position: new kakao.maps.LatLng(store.pos_y, store.pos_x),
        });
      });

      this.map.setCenter(new kakao.maps.LatLng(this.storeList[0].pos_y, this.storeList[0].pos_x));

      clusterer.addMarkers(markers);
    },

    displayMarker(locPosition, message) {
      var marker = new kakao.maps.Marker({
        map: this.map,
        position: locPosition,
      });

      var iwContent = message;
      var iwRemoveable = true;

      var infowindow = new kakao.maps.InfoWindow({
        content: iwContent,
        removable: iwRemoveable,
      });

      infowindow.open(this.map, marker);
      this.map.setCenter(locPosition);
    },

    setCurPosition() {
      var displayMarker = this.displayMarker;
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {

          var lat = position.coords.latitude; // 위도
          var lon = position.coords.longitude; // 경도

          var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            message = '<div style="padding:5px;">내 위치</div>'; // 인포윈도우에 표시될 내용입니다

          // 마커와 인포윈도우를 표시합니다
          displayMarker(locPosition, message);
        });
      } else {
        var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
          message = "geolocation을 사용할수 없어요..";

        this.displayMarker(locPosition, message);
      }
    },

    searchAddrFromCoords: function(coords, callback) {
        // 좌표로 행정동 주소 정보를 요청합니다
        this.geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);         
    },

    searchDetailAddrFromCoords: function(coords, callback) {
        // 좌표로 법정동 상세 주소 정보를 요청합니다
        this.geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
    },

  },
};
</script>