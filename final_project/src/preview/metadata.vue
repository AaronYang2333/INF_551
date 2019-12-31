<template>
  <el-main id="metadata">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>
          <i class="el-icon-info" />&nbsp;Metadata
        </span>
      </div>
      <div>
        <b>Usage Information</b>
        <br />
        <pre>               License:                                      Data files © Original Authors</pre>
        <pre>               Visibility:                                     <i class="el-icon-view" />&nbsp;Public</pre>
        <br />
        <b>Maintainers</b>
        <br />
        <pre>               Dataset owner:                          <el-avatar
  shape="square"
  :size="22"
  :src="author_pisaller"
></el-avatar>pisaller</pre>
        <pre>               Original URL:                              <el-link
  type="primary"
  :href="original_url"
  target="_blank"
>Kaggle</el-link></pre>
        <br />
        <b>Updates</b>
        <br />
        <pre>               Expected update frequency:      Not specified</pre>
        <pre>               Last updated:                             2019-07-23</pre>
        <pre>               Date created:                             2019-07-23</pre>
        <pre>               Current version:                         Version 1</pre>
        <br />
      </div>
    </el-card>
    <br />
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>
          <i class="el-icon-s-opportunity" />&nbsp;Columns Info
        </span>
      </div>
      <div>
        <i class="el-icon-star-on" style="margin-bottom: 15px;"></i>&nbsp;<b>ID </b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Data ID<br/>
        <i class="el-icon-tickets" style="margin-bottom: 15px;"></i>&nbsp;<b>flightNumber </b>&emsp;&emsp;Flight Number<br/>
        <i class="el-icon-tickets" style="margin-bottom: 15px;"></i>&nbsp;<b>craftTypeCode </b>&emsp;&nbsp;Aircraft<br/>
        <i class="el-icon-tickets" style="margin-bottom: 15px;"></i>&nbsp;<b>traAirport </b>&emsp;&emsp;&emsp;&nbsp;&nbsp;Transit Airport<br/>
        <i class="el-icon-date" style="margin-bottom: 15px;"></i>&nbsp;<b>departureDate </b>&emsp;&nbsp;Departure Date<br/>
        <i class="el-icon-date" style="margin-bottom: 15px;"></i>&nbsp;<b>arrivalDate </b>&emsp;&emsp;&emsp;Arrival Date<br/>
        <i class="el-icon-tickets" style="margin-bottom: 15px;"></i>&nbsp;<b>cabinClass </b>&emsp;&emsp;&nbsp;&nbsp;&nbsp;CabinClass, Y= Econ, C = Business, F= First<br/>
        <i class="el-icon-tickets" style="margin-bottom: 15px;"></i>&nbsp;<b>priceClass </b>&emsp;&emsp;&emsp;OTA Price Level<br/>
        <i class="el-icon-s-data" style="margin-bottom: 15px;"></i>&nbsp;<b>price </b>&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;Price<br/>
        <i class="el-icon-s-data" style="margin-bottom: 15px;"></i>&nbsp;<b>rate </b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;Discount Rate<br/>
        <i class="el-icon-date" style="margin-bottom: 15px;"></i>&nbsp;<b>createDate </b>&emsp;&emsp;&emsp;Booking Date<br/>
        <i class="el-icon-s-data" style="margin-bottom: 15px;"></i>&nbsp;<b>dateDifference </b>&emsp;&nbsp;Day Difference Between Booking date and Departure Date<br/>
      </div>
    </el-card>
  </el-main>
</template>

<script>
export default {
  data() {
    return {
      author_pisaller:
        "https://user-images.githubusercontent.com/24391143/66885903-a25c6400-ef8a-11e9-81a2-c782d25c5dd8.png",
      original_url:
        "https://www.kaggle.com/lpisallerl/air-tickets-between-shanghai-and-beijing"
    };
  }
};
</script>

<style scoped>
#metadata {
  padding-top: 37px;
  left: 10%;
  text-align: left;
  z-index: 2;
}
.box-card {
  color: #5f5555;
  border-radius: 4px 4px 4px 4px;
  border: 1px solid #dcdfe6;
}
pre {
  font-family: Helvetica, sans-serif;
  color: #797474;
}
.el-card >>> .el-card__header {
  background-color: #e6e6e69d;
}
</style>