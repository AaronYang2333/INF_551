<template>
  <el-main id="navigator_row">
    <el-tabs type="card" v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="Description" name="desc">
        <DATADESC />
      </el-tab-pane>
      <el-tab-pane label="Metadata" name="metadata">
        <METADATA></METADATA>
      </el-tab-pane>
      <el-tab-pane label="RawData" name="rawdata">
        <DATA />
      </el-tab-pane>
      <el-tab-pane label="Price Prediction" name="prediction">
        <IPYNB />
      </el-tab-pane>
    </el-tabs>
  </el-main>
</template>

<script>
import DATADESC from "./datadesc.vue";
import METADATA from "./metadata.vue";
import DATA from "./data.vue";
import IPYNB from "./charts.vue";
export default {
  components: {
    DATADESC,
    METADATA,
    DATA,
    IPYNB
  },
  data() {
    return {
      activeName: "desc"
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
};
</script>

<style scoped>
#navigator_row {
  border: 1px solid #dcdfe6;
  border-radius: 0 0 4px 4px;
  width: 80%;
  left: 10%;
  right: 10%;
  height: 80%;
  position: fixed;
  margin-top: 180px;
  background-color: #ffffff;
  text-align: center;
  padding: 0;
}
.el-tabs >>> .el-tabs__nav-scroll {
  position: fixed;
  background-color: #ffffff;
  border-bottom: 1px solid #dcdfe6;
  width: 80%;
  left: 10%;
  z-index: 3;
  margin-top: 6px;
}
</style>