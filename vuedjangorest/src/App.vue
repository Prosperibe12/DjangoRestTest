<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
import Posts from './components/Posts.vue'
import TheWelcome from './components/TheWelcome.vue'
import WelcomeItem from './components/WelcomeItem.vue';
</script>

<template>
  <header>
    <div>
      <Posts/>
    </div>
  </header>
  <TheWelcome />
  <WelcomeItem />

</template>

<style scoped>

</style>
