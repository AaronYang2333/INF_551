<template>
  <div id="app">
    <el-container>
    <Header/>
    <Nav/>
    </el-container>
  </div>
</template>

<script>
import Header from './preview/header.vue'
import Nav from './preview/nav.vue'
export default {
  components:{
    Header,
    Nav,
  }
};
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom:0;
}

</style>
