<template>
  <el-main id="visualzation">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>
          <i class="el-icon-s-data" />&nbsp;Linear Rgression Ipynb
        </span>
      </div>

      <el-collapse>
        <el-collapse-item title="Price Prediction (high related feature)">
          <div class="pdf_imgs">
            <el-image v-for="url in high_urls" :key="url" :src="url"></el-image>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Price Prediction (real case)">
          <div class="pdf_imgs">
            <el-image v-for="url in real_urls" :key="url" :src="url"></el-image>
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </el-main>
</template>
  </el-main>
</template>

<script>
export default {
  data() {
    return {
      high_urls: [
        "https://user-images.githubusercontent.com/24391143/69693241-94b9f400-1089-11ea-94d9-65b8e9c42c71.PNG",
        "https://user-images.githubusercontent.com/24391143/69693253-997ea800-1089-11ea-8ef9-cd12d18136d9.PNG",
        "https://user-images.githubusercontent.com/24391143/69693259-9b486b80-1089-11ea-8f7e-733e44671393.PNG",
        "https://user-images.githubusercontent.com/24391143/69693264-9c799880-1089-11ea-98e5-35f1f69a5f49.PNG",
        "https://user-images.githubusercontent.com/24391143/69693266-9daac580-1089-11ea-947c-ccf11e9f200f.png",
        "https://user-images.githubusercontent.com/24391143/69693269-9f748900-1089-11ea-8ac4-6cbd2286e4e6.png",
        "https://user-images.githubusercontent.com/24391143/69693273-a13e4c80-1089-11ea-8925-c39202ac25ee.png"
      ],
      real_urls: [
        "https://user-images.githubusercontent.com/24391143/69828420-ac4fc480-11d0-11ea-9897-9a44d1518fa0.png",
        "https://user-images.githubusercontent.com/24391143/69828422-ad80f180-11d0-11ea-8549-b59f1054c808.png",
        "https://user-images.githubusercontent.com/24391143/69828423-aeb21e80-11d0-11ea-9644-9ad2a73261df.png",
        "https://user-images.githubusercontent.com/24391143/69828425-afe34b80-11d0-11ea-9af7-f1245e15ff22.png",
        "https://user-images.githubusercontent.com/24391143/69828436-bb367700-11d0-11ea-9636-81aef00ca15b.png",
        "https://user-images.githubusercontent.com/24391143/69828438-bc67a400-11d0-11ea-9402-404e5200d898.png",
        "https://user-images.githubusercontent.com/24391143/69828440-be316780-11d0-11ea-9963-8a4b0bf1099b.png",
        "https://user-images.githubusercontent.com/24391143/69828442-c093c180-11d0-11ea-8da9-e918d4dcfae5.png",
        "https://user-images.githubusercontent.com/24391143/69828447-c25d8500-11d0-11ea-9636-d1f33f86bd21.png",
        "https://user-images.githubusercontent.com/24391143/69828456-cb4e5680-11d0-11ea-9f0a-4b5e13766aeb.png",
        "https://user-images.githubusercontent.com/24391143/69828457-cbe6ed00-11d0-11ea-9e5e-2cefc55fda93.png"
      ]
    };
  }
};
</script>

<style scoped>
#visualzation {
  padding-top: 37px;
  left: 10%;
  text-align: left;
  z-index: 2;
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