<template>
  <div class="container">
    <h3 class="text-center">
        View Our Books
      </h3>
    <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-for="posts in APIData" :key="posts.id" class="col-md-4">
          <div class="col">
            <div class="card h-100">
              <img src="../assets/imgcard.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">{{posts.name}}</h5>
                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt, obcaecati.</p>
                <!-- <a href="#" class="btn btn-primary">View Details</a> -->
                <RouterLink to="/about/{{posts.id}}" class="btn">View Details</RouterLink>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import { getAPI } from '../axios-api'
  export default {
    name: 'Posts',
    data () {
      return {
          APIData: []
        }
    },
    created () {
        getAPI.get('/',)
          .then(response => {
            console.log('Post API has recieved data')
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
</script>

<style scoped>


</style>
