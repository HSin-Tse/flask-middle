<template>
  <div>

    <div class="container-fluid">
      <h1>Ajmide Static Tool {{where}}</h1>

      <h2>Receive:{{ conected}}</h2>
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
        <el-table-column fixed prop="busi" label="busi" width="120">
        </el-table-column>
        <el-table-column prop="URL" label="URL" width="600">
        </el-table-column>
        <el-table-column prop="body" label="body">
        </el-table-column>
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

  var namespace = '/page';
  import VueSocketio from 'vue-socket.io';
  import JsonExcel from 'vue-json-excel';

  Vue.component('downloadExcel', JsonExcel);
  Vue.use(VueSocketio, location.protocol + '//' + document.domain + ':5001' + namespace);
  export default {
    data() {
      return {
        conected: 'disconnect',
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
            this.clickitems = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      getClickRules() {
        const path = `http://localhost:5001/api/page/v2`;
        axios.get(path)
          .then(response => {
            console.log('response.data:'+response.data);
            console.log('response.data:'+response.data);
            console.log('response.data:'+response.data);

            this.formThead = response.data
          })
          .catch(error => {
            console.log(error)
            console.log('error:'+error);
            console.log('error:'+error);
            console.log('error:'+error);
          })
      },      deleteRow(index, rows) {
        this.tableData.splice(index, 1);
      },
      tableRowClassName({row, rowIndex}) {
        var k = (row.t1 === "error");
        if (k) {
          return 'warning-row';
        } else {
          return 'success-row';
        }
      }

      ,
      show: function () {
        alert("" + this.clickitems)
      }
      ,
      clean: function () {
        this.tableData = [];
      },
      addLog: function (msg) {


        var length = this.clickitems.length;
        for (var i = 0; i < length; i++) {
//          console.log(this.clickitems[i]);
          var isbt = this.clickitems[i].bt == msg.bt
          var isctl = this.clickitems[i].ctl == msg.ctl
          var ispg = this.clickitems[i].pg == msg.pg
          var isblk = this.clickitems[i].blk == msg.blk
          if (isbt & isctl & ispg & isblk) {
            msg.busi = i + ':' + this.clickitems[i]["埋点业务"]
            break
          } else {
            msg.busi = "nonono"

          }
        }

        msg.ID = this.total;


        this.tableData.unshift(
          msg
        );
      },
    },
    created() {

      this.getClickRules();
      this.getClicksItems();
      this.getRandom();

      this.where = (location.protocol + '//' + document.domain + ':' + location.port + namespace);
    },
    sockets: {
      connect() {
        console.log('connect')

        this.conected = (' connected')
      },
      disconnect() {
        console.log('disconnect')

        this.conected = ('server disconnect')
      },
      init(msg) {
        console.log('socket init')
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
