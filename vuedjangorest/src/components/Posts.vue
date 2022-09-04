<script setup>
    // defineProps({
    //   msg: {
    //     type: String,
    //     required: true
    //   }
    // })
</script>
    
  <template>
      <nav class="navbar navbar-expand-lg bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand text-white" href="">BookApp</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item px-2">
                <RouterLink to="/" class="text-white text-decoration-none">Home</RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  </template>
    
<style scoped>

</style>
    