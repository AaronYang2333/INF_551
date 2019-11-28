<template>
  <el-main id="basic_info">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span><i class="el-icon-s-opportunity"/>&nbsp;Licence Info</span>
      </div>
      <div>
        <i class="el-icon-suitcase-1" />&nbsp;
        <b>Usability</b> 6.8
        <br />
        <i class="el-icon-guide" />&nbsp;
        <b>License</b> Data files © Original Authors
        <br />
        <i class="el-icon-setting" />&nbsp;
        <b>Tag</b> Classification, health, time series, machine learning, regression analysis
      </div>
    </el-card>
    <br />
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span><i class="el-icon-s-comment"/>&nbsp;Text Description</span>
      </div>
      <div>
        <b>Context</b>
        <br />
        <i>*There's a story behind every dataset and here's your opportunity to share yours. *</i>
        <br />
        <br />
        <b>Content</b>
        <br />The column name themselves are already explanatory. In cabinClass: Y = Econ Class, C = Business Class , F = First Class In rate: ranged from 0 to 1, stands for discount rate, lower is cheaper. In createDate: the actual date this data is generated In dateDifference: the date difference between the create d date and the actual departure date. For example, if the dateDifference = 7, it simply means I am booking the ticket one week ahead.
        <br />
        <br />
        <b>Inspiration</b>
        <br />Your data will be in front of the world's largest data science community. What questions do you want to see answered?
      </div>
    </el-card>
  </el-main>
</template>

<script>
export default {};
</script>

<style scoped>
#basic_info {
  padding-top: 37px;
  left: 10%;
  color: #5f5555;
  text-align: left;
  z-index: 2;
}
.box-card {
  color: #5f5555;
  border-radius: 4px 4px 4px 4px;
  border: 1px solid #dcdfe6;
}
.el-card >>> .el-card__header{
  background-color: #e6e6e69d;
}
</style>