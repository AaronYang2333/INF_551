<template>
  <div id="buttons">
    <el-popover placement="bottom" width="200" trigger="click" @show="clearAllArgs">
      <p>Column</p>
      <el-select
        v-model="numColumn"
        @change="updateSliderValue"
        placeholder="Choose a column"
        style="margin-top: 5px;"
      >
        <el-option
          v-for="item in numOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        ></el-option>
      </el-select>
      <el-divider></el-divider>
      <p>Sort</p>
      <el-button
        class="sort_btn"
        type="text"
        @click="sortFunc('asce')"
        icon="el-icon-upload2"
        v-bind:disabled="isAsceDisabled"
      >Sort Ascending</el-button>
      <el-button
        class="sort_btn"
        type="text"
        @click="sortFunc('desc')"
        icon="el-icon-download"
        v-bind:disabled="isDsceDisabled"
      >Sort Descending</el-button>
      <el-divider></el-divider>
      <p>Filter</p>
      <el-slider
        v-model="value"
        range
        @input="sliderValueChange"
        :show-tooltip="false"
        style="margin-left: 10px; width: 90%"
      ></el-slider>
      <p>
        <span style="float: left;">{{sliderMin}}</span>
        <span style="float: right;">{{sliderMax}}</span>
      </p>
      <el-divider></el-divider>
      <div style="text-align: right; margin-top: 5px;">
        <el-button type="danger" size="mini" @click="clearAllArgs">Clear</el-button>
        <el-button type="primary" size="mini" @click="executeSort('numeric')">Apply</el-button>
      </div>
      <el-button slot="reference" icon="el-icon-s-data" circle></el-button>
    </el-popover>
    <el-popover placement="bottom" width="220" trigger="click" @show="clearAllArgs">
      <p>Column</p>
      <el-select
        v-model="textColumn"
        @change="clearTextField"
        placeholder="Choose a column"
        style="margin-top: 5px;"
      >
        <el-option
          v-for="item in textOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        ></el-option>
      </el-select>
      <el-divider></el-divider>
      <p>Sort</p>
      <el-button
        class="sort_btn"
        type="text"
        @click="sortFunc('asce')"
        icon="el-icon-upload2"
        v-bind:disabled="isAsceDisabled"
      >Sort Ascending</el-button>
      <br />
      <el-button
        class="sort_btn"
        type="text"
        @click="sortFunc('desc')"
        icon="el-icon-download"
        v-bind:disabled="isDsceDisabled"
      >Sort Descending</el-button>
      <el-divider></el-divider>
      <p>Filter</p>
      <el-input placeholder="keywords" v-model="keyword" style="margin-top: 5px;">
        <template slot="prepend">EqualTo</template>
      </el-input>
      <el-divider></el-divider>
      <div style="text-align: right; margin-top: 5px;">
        <el-button type="danger" size="mini" @click="clearAllArgs">Clear</el-button>
        <el-button type="primary" size="mini" @click="executeSort('text')">Apply</el-button>
      </div>
      <el-button slot="reference" icon="el-icon-search" circle></el-button>
    </el-popover>
    <el-button class="filter_btn" @click="clearFilter" icon="el-icon-refresh" circle></el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      numOptions: [
        {
          label: "Price",
          value: "price"
        },
        {
          label: "Rate",
          value: "rate"
        }
      ],
      numColumn: "",
      mixColumn: "",
      textOptions: [
        {
          label: "Flight Number",
          value: "flightNumber"
        },
        {
          label: "Craft Type",
          value: "craftTypeCode"
        },
        {
          label: "Price Class",
          value: "priceClass"
        }
      ],
      textColumn: "",
      //sorting info
      isAsceDisabled: false,
      isDsceDisabled: false,
      sortValue: "",
      //slider info
      value: [0, 100],
      sliderMin: 1000,
      sliderMax: 2000,
      dataMin: 1000,
      dataMax: 2000,
      //text filter
      keyword: ""
    };
  },
  methods: {
    sortFunc(value) {
      this.sortValue = value;
      if (value === "asce") {
        this.isAsceDisabled = true;
        this.isDsceDisabled = false;
      } else {
        this.isAsceDisabled = false;
        this.isDsceDisabled = true;
      }
    },
    sliderValueChange(value) {
      const step = ((this.dataMax - this.dataMin) / 100).toPrecision(1);
      this.sliderMin = this.dataMin + value[0] * step;
      this.sliderMax = this.dataMin + value[1] * step;
    },
    clearTextField() {
      this.keyword = "";
      this.isAsceDisabled = false;
      this.isDsceDisabled = false;
    },
    clearFilter() {
      this.$options.methods.clearAllArgs.bind(this)();
      this.$emit("loadDefault", null);
    },
    updateSliderValue(column) {
      if (column === "price") {
        this.value = [0, 100];
        this.dataMin = 235;
        this.dataMax = 6410;
        this.sliderMin = 235;
        this.sliderMax = 6410;
        this.isAsceDisabled = false;
        this.isDsceDisabled = false;
      } else {
        this.value = [0, 100];
        this.dataMin = 0.01;
        this.dataMax = 1;
        this.sliderMin = 0.01;
        this.sliderMax = 1;
        this.isAsceDisabled = false;
        this.isDsceDisabled = false;
      }
    },
    clearAllArgs() {
      //clear all the argument and load the first 100 rows
      this.numColumn = "";
      this.textColumn = "";
      this.keyword = "";
      this.sortValue = "";
      this.isAsceDisabled = false;
      this.isDsceDisabled = false;
      this.value = [0, 100];
      this.sliderMin = this.dataMin;
      this.sliderMax = this.dataMax;
    },
    executeSort(type) {
      var criterion = { order: this.$data.sortValue };
      if (type === "numeric") {
        criterion["column"] = this.numColumn;
        criterion["filter"] = [this.$data.sliderMin, this.$data.sliderMax];
      } else {
        criterion["column"] = this.textColumn;
        criterion["filter"] = this.$data.keyword;
      }
      this.$emit("execute", criterion);
    }
  }
};
</script>


<style scoped>
.el-divider {
  margin-bottom: 10px;
}
p {
  margin: 0;
  color: #909399;
  font: 14px "microsoft yahei";
}
.sort_btn {
  margin: 0;
}
.filter_btn {
  overflow: hidden;
  margin-top: 15px;
  z-index: 6;
  margin-left: 10px;
}
</style>