<template>
  <div>

      <div class="container-fluid">
        <h1>Ajmide Static Tool {{where}}</h1>

      <h2>Receive:</h2>

        <el-button  style="margin-bottom: 20px" type="danger"  @click="clean">clear data</el-button>

        <el-table border :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
          <el-table-column fixed prop="date" label="ID" width="60">
          </el-table-column>
          <el-table-column prop="name" label="URL" width="600">
          </el-table-column>
          <el-table-column prop="address" label="body">
          </el-table-column>
          <!--<el-table-column prop="t1" label="t1">-->
          <!--</el-table-column>-->
          <el-table-column :key='fruit' v-for='(fruit,index) in formThead' :prop="fruit" :label="fruit">
          </el-table-column>

          <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="deleteRow(scope.$index, tableData)"
                type="danger"
                size="small">
                移除
              </el-button>
            </template>
          </el-table-column>
        </el-table>

    </div>
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
        total: 0,
        where: 'where',
        tse: 'tsee  asd ddd',
        tableData: [],
        formThead: ['t1', 'vlu'],
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
      },
      deleteRow(index, rows) {
        this.tableData.splice(index, 1);
      },
      tableRowClassName({row, rowIndex}) {
        var k = (row.t1 === "error");
        var l = typeof(row.t1) == undefined;

        console.log(rowIndex + '|' + k + '|' + row.t1 + '|' + l);
        console.log(row);
        if (k) {
          return 'warning-row';
        } else {
          return 'success-row';
        }
      }

      ,
      intitial: function (data) {

        this.formThead = data;
      }
      ,
      clean: function () {

        this.tableData = [];

      },
      addLog: function (a, b, c, t1, msg) {

        msg.date = a;
        msg.name = b;
        msg.address = c;
        this.tableData.unshift(
          msg
        );
      },
    },
    created() {

      this.getRandom();
      var namespace = '/test';

      this.where = (location.protocol + '//' + document.domain + ':' + location.port + namespace);
    },
    sockets: {
      connect() {
        console.log('socket connected')
        this.$socket.emit('my_event', {data: 'I\'m connected!'});

      },
      init(msg) {
        console.log('socket init')
        this.intitial(msg);

      },
      my_response(msg) {
        console.log('socket my_response msg:' + msg.t1);
        console.log('socket my_response msg:' + msg.body);
        this.total++
        this.addLog(this.total, msg.data, msg.body, msg.t1, msg);

      },

    }
  }
</script>
<style>
  .el-table .warning-row {
    background: #FF5151;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

  .el-table .no-row {
    background: #00ffff
  }


</style>
