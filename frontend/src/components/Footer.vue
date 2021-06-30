<template>
  <v-footer
    dark
    padless
  >
    <v-card
      flat
      tile
      color="#f08c8c"
      class="white--text text-center"
      width="100%"
    >
      <v-card-text width class="black--text pt-10">
         이용약관 | 개인정보없음<br>
         <span style="font-size:10pt; color:#303030;">본 사이트의 콘텐츠를 무단 전재, 복사, 배포 등을 금합니다.</span><br>
         Copyright© COSAT TEAM All Rights Reserved.
      </v-card-text>

      <v-divider light></v-divider>

      <v-card-text class="black--text">
        {{ new Date().getFullYear() }} — <strong>COSAT</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>