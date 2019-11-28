<template>
  <el-main id="row_data">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>
          <i class="el-icon-s-grid" />&nbsp;RowData
        </span>
      </div>
      <functionBtn @execute="processCriteria" @loadDefault="loadDefaultData"></functionBtn>
      <el-table
        highlight-current-row
        stripe
        v-loading="loading"
        element-loading-text="Loading..."
        element-loading-spinner="el-icon-loading"
        element-loading-background="rgba(0, 0, 0, 0.5)"
        @current-change="handleCurrentChange"
        ref="filterTable"
        :data="tableData"
        style="width: 100%"
        max-height="515"
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="ID" label="ID" width="100"></el-table-column>
        <el-table-column prop="flightNumber" label="FlightNumber" width="115"></el-table-column>
        <el-table-column prop="craftTypeCode" label="CraftTypeCode" width="125"></el-table-column>
        <el-table-column prop="traAirport" label="TraAirport" width="110"></el-table-column>
        <el-table-column prop="departureDate" label="DepartureDate" width="125"></el-table-column>
        <el-table-column prop="arrivalDate" label="ArrivalDate" width="115"></el-table-column>
        <el-table-column prop="cabinClass" label="CabinClass" width="110"></el-table-column>
        <el-table-column prop="priceClass" label="PriceClass" width="110"></el-table-column>
        <el-table-column prop="price" label="Price" width="110"></el-table-column>
        <el-table-column prop="rate" label="Rate" width="110"></el-table-column>
        <el-table-column prop="createDate" label="CreateDate" width="115"></el-table-column>
        <el-table-column prop="dateDifference" label="DateDifference" width="125"></el-table-column>
        <infinite-loading
          slot="append"
          @infinite="infiniteHandler"
          force-use-infinite-wrapper=".el-table__body-wrapper"
        ></infinite-loading>
      </el-table>
    </el-card>
  </el-main>
</template>

<script>
import functionBtn from "./button.vue";
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";
import { isArray, isNull } from "util";

export default {
  components: {
    functionBtn,
    InfiniteLoading
  },
  data() {
    return {
      // basicApi: "https://flight-117bd.firebaseio.com/.json",
      // deafultSuffix: "?orderBy=%22$key%22",
      basicApi: "http://localhost:8066/api",
      deafultSuffix: "/orderBy=%22$key%22",
      tableData: [],
      loading: true,
      rows: 100,
      currentURL: "",
      orderUrlPrefix: "&limitToFirst="
    };
  },
  methods: {
    checkArgs(args) {
      var valueArr = Object.values(args);
      for (let i = 0; i < valueArr.length; ++i) {
        if (null == valueArr[i] || "" == valueArr[i]) {
          this.$options.methods.sendAlert.bind(this)(
            "Please select something!"
          );
          return false;
        }
      }
      return true;
    },
    genOrderPrefix(argv) {
      if (argv.order == "asce") {
        this.orderUrlPrefix = "&limitToFirst=";
      } else {
        this.orderUrlPrefix = "&limitToLast=";
      }
    },
    processCriteria(argv) {
      var flag = this.$options.methods.checkArgs.bind(this)(argv);
      this.$options.methods.genOrderPrefix.bind(this)(argv);
      if (flag) {
        var querySuffixUrl = "";
        if (Array.isArray(argv.filter)) {
          //slide button clicked
          querySuffixUrl =
            '?orderBy="' +
            argv.column +
            '"&startAt=' +
            argv.filter[0] +
            "&endAt=" +
            argv.filter[1];
        } else {
          //text contain button clicked
          querySuffixUrl =
            '?orderBy="' +
            argv.column +
            '"&startAt="' +
            argv.filter +
            '"&endAt="\uf8ff"';
        }

        this.currentURL = this.basicApi + querySuffixUrl;
        this.$options.methods.getDataByUrl.bind(this)(querySuffixUrl);
      }
    },
    handleCurrentChange(val) {
      this.currentRow = val;
    },
    getDataByUrl(suffixUrl) {
      this.loading = true;
      console.log(this.basicApi + suffixUrl + this.orderUrlPrefix + this.rows);
      axios({
        method: "GET",
        url: this.basicApi + suffixUrl + this.orderUrlPrefix + this.rows
      }).then(
        result => {
          if (result.data != null) {
            if (result.data instanceof Array) {
              this.tableData = result.data;
            } else {
              this.tableData = Object.values(result.data);
            }
            this.$options.methods.sendTips.bind(this)(
              "Load Data Successfully."
            );
            this.loading = false;
          } else {
            this.$options.methods.sendAlert.bind(this)(
              "The query's result is null"
            );
            this.loading = false;
          }
        },
        error => {
          this.$options.methods.sendAlert.bind(this)(
            "Something wrong about the request"
          );
          this.loading = false;
        }
      );
    },
    sendTips(msg) {
      this.$message({
        message: msg,
        type: "success",
        duration: 2000
      });
    },
    sendAlert(msg) {
      this.$message({
        message: msg,
        type: "warning",
        duration: 2000
      });
    },
    infiniteHandler($state) {
      this.rows += 100;
      axios({
        method: "GET",
        url: this.currentURL + this.orderUrlPrefix + this.rows
      }).then(
        result => {
          if (result.data instanceof Array) {
            this.tableData = result.data;
          } else {
            this.tableData = Object.values(result.data);
          }
          this.loading = false;
          $state.loaded();
        },
        error => {
          this.$options.methods.sendAlert.bind(this)(
            "Load following data failed!"
          );
        }
      );
    },
    loadDefaultData() {
      this.currentURL = this.basicApi + this.deafultSuffix;
      this.rows = 100;
      this.orderUrlPrefix = "&limitToFirst=";
      this.$options.methods.getDataByUrl.bind(this)(this.deafultSuffix);
    }
  },
  mounted() {
    this.currentURL = this.basicApi + this.deafultSuffix;
    this.$options.methods.getDataByUrl.bind(this)(this.deafultSuffix);
  }
};
</script>

<style scoped>
#row_data {
  padding-top: 37px;
  left: 10%;
  text-align: left;
  z-index: 2;
}
pre {
  font-family: Helvetica, sans-serif;
  color: #797474;
}
.el-card >>> .el-card__header {
  background-color: #e6e6e69d;
}
.box-card {
  color: #5f5555;
  border-radius: 4px 4px 4px 4px;
  border: 1px solid #dcdfe6;
}
</style>