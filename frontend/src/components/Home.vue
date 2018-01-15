<template>
  <div>
    <h1>Ajmide Static Tool</h1>
    <el-button type="danger">危险按钮</el-button>
    <h1>Home {{where}}</h1>
    <p>Home {{tse}}</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
  import axios from 'axios';
  import Vue from 'vue';
  var namespace = '/test';
  import VueSocketio from 'vue-socket.io';
  Vue.use(VueSocketio, location.protocol + '//' + document.domain + ':5001' + namespace);
  export default {
    data() {
      return {
        randomNumber: 0,
        where: 'where',
        tse: 'tsee  asd ddd'
      }
    },
    methods: {
      getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min
      },
      getRandom() {
        // this.randomNumber = this.getRandomInt(1, 100)
        this.randomNumber = this.getRandomFromBackend()
      },
      getRandomFromBackend() {
        const path = `http://localhost:5001/api/random`;
        axios.get(path)
          .then(response => {
            this.randomNumber = response.data.randomNumber
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      this.getRandom();
      var namespace = '/test';

      this.where = (location.protocol + '//' + document.domain + ':' + location.port + namespace);
    },
    sockets: {
      connect() {
        console.log('socket connected')
      },
      init() {
        console.log('socket init')
      },
      my_response(msg) {
        console.log('socket my_response msg:'+msg.t1);
        console.log('socket my_response msg:'+msg.body);
      },

    }
  }
</script>
