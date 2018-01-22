<template>
  <div>

    <div class="container-fluid">
      <h1>Ajmide Static Tool {{where}}</h1>
      <h1>{{tse}}</h1>



    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import Vue from 'vue';

  var namespace = '/page';
  import VueSocketio from 'vue-socket.io';
  import JsonExcel from 'vue-json-excel';

  Vue.component('downloadExcel', JsonExcel);
  Vue.use(VueSocketio, location.protocol + '//' + document.domain + ':5001' + namespace);
  export default {
    data() {
      return {
        where: 'where',
        tse: '',
      }
    },
    methods: {

      getClickRules() {
        const path = `http://localhost:5001/api/h5`;
        axios.get(path)
          .then(response => {

            this.tse = response.data
          })
          .catch(error => {
          })
      },
    },
    created() {

      this.getClickRules();

      this.where = (location.protocol + '//' + document.domain + ':' + location.port + namespace);
    },

  }
</script>
<style>


</style>
