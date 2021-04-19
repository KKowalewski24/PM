<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Products/>
  </div>
</template>

<script>
import Products from './components/Products.vue'

export default {
  name: 'app',
  components: {
    Products
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
