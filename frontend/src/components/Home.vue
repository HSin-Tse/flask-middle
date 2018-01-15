<template>
  <div>

    <div class="container-fluid">
      <h1>Ajmide Static Tool {{where}}</h1>

      <h2>Receive:</h2>
      <download-excel
        class="btn btn-primary"
        :data="tableData"
        type="csv"
        name="tse.csv">
        Download data
      </download-excel>
      <el-button type="danger" @click="clean">clear data</el-button>
      <el-button type="success" @click="show">debug</el-button>

      <el-table border :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
        <el-table-column fixed prop="ID" label="ID" width="60">
        </el-table-column>
        <el-table-column prop="URL" label="URL" width="600">
        </el-table-column>
        <el-table-column prop="body" label="body">
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
  import JsonExcel from 'vue-json-excel';

  Vue.component('downloadExcel', JsonExcel);
  Vue.use(VueSocketio, location.protocol + '//' + document.domain + ':5001' + namespace);
  export default {
    data() {
      return {
        randomNumber: 0,
        total: 0,
        where: 'where',
        tse: '',
        tableData: [],
        clickitems: [],
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
      getClicksItems() {
        const path = `http://localhost:5001/api/clickitems/v2`;
        axios.get(path)
          .then(response => {
//            console.log('response.data:'+response.data[30].t1);
            this.clickitems = response.data
            // 快速的代码

// for 循环
            var length = this.clickitems.length;
            for (var i = 0; i < length; i++) {
              console.log(this.clickitems[i]);
            }
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

//        console.log(rowIndex + '|' + k + '|' + row.t1 + '|' + l);
//        console.log(row);
        if (k) {
          return 'warning-row';
        } else {
          return 'success-row';
        }
      }

      ,
      intitial: function (data) {

        this.formThead = data;
      },
      show: function () {


//        alert(""+this.formThead)
        alert("" + this.clickitems)
      }
      ,
      clean: function () {

        this.tableData = [];

      },
      addLog: function (msg) {





        msg.ID = this.total;


        this.tableData.unshift(
          msg
        );
      },
    },
    created() {

      this.getClicksItems();
      this.getRandom();
      var namespace = '/test';

      this.where = (location.protocol + '//' + document.domain + ':' + location.port + namespace);
    },
    sockets: {
      connect() {
        console.log('socket connected')
//        this.$socket.emit('my_event', {data: 'I\'m connected!'});

      },
      init(msg) {
        console.log('socket init')
        this.intitial(msg);

      },
      my_response(msg) {
        this.total++
        this.addLog(msg);

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
