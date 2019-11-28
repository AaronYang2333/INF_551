<template>
  <el-header>
    <p id="header_text">{{title}}</p>
    <p id="header_sub_text">{{subtitle}}</p>
    <div style="padding-top: 7px;">
      <div id="author1">
        <el-avatar shape="square" :size="33" :src="author1_avator_path"></el-avatar>
        <span>·{{author1}}</span>
      </div>
      <div id="author2">
        <el-avatar shape="square" :size="33" :src="author2_avator_path"></el-avatar>
        <span>·{{author2}}</span>
      </div>
      <el-button id="download_btn" icon="el-icon-download" type="primary" @click="download">.JSON File</el-button>
    </div>
  </el-header>
</template>

<script>
import firebase from "firebase";
export default {
  data() {
    return {
      title: "Air_Tickets_Between_Shanghai_and_Beijing",
      subtitle: "A real-world time-series data set with high cleanse.",
      author1: "Bo Yang",
      author1_avator_path:
        "https://user-images.githubusercontent.com/24391143/66885874-848eff00-ef8a-11e9-9476-b68946292275.png",
      author2: "Xihao Zhou",
      author2_avator_path:
        "https://user-images.githubusercontent.com/24391143/66885892-92448480-ef8a-11e9-9e21-6536053e5757.jpg"
    };
  },
  methods: {
    download() {
      window.open("https://github.com/AaronYang2333/INF_551/files/3898206/data.txt");
    }
  }
};
</script>

<style scoped>
p,
span {
  color: rgb(248, 248, 248);
  text-align: left;
}
.el-header {
  border-radius: 4px 4px 0 0;
  left: 10%;
  position: absolute;
  right: 10%;
  top: 20px;
  width: 80%;
  height: 167px !important;
  z-index: 1;
  background-color: rgb(226, 225, 225);
  opacity: 0.9;
  background-image: url("../assets/dataset-cover.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  background-size: 100% 167px;
}
#header_text {
  margin-top: 45px;
  margin-bottom: 7px;
  font-size: 22px;
  font-weight: 600;
}
#header_sub_text {
  font-size: 16px;
  font-weight: 200;
  margin-bottom: 7px;
}
#author1,
#author2 {
  left: 20px;
  position: absolute;
  display: inline;
  font-size: 16px;
  font-weight: 200;
}
#author2 {
  left: 150px !important;
}
#download_btn {
  float: right;
  overflow: hidden;
  margin-top: 15px;
  padding: 3px 15px;
  z-index: 6;
}
</style>