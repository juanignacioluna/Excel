<template>
  <div class="home">

    <Navbar />


    <div class="container-fluid">

              <br> <br>

              <div class="row">

                <div class="column"></div>

                <div class="col-sm-12 col-md-8">


                  <div class="card bg-danger text-white">
                    <div class="card-header bg-danger">
                      <h1 class="card-title">Bienvenido a Excel Generator</h1>
                    </div>
                    <div class="card-body bg-danger">
                      <h4>Con esta app usted va a poder crear hojas al estilo de Excel :)</h4>
                      <br>
                      <router-link to="/verHojas">
                        <button class="hvr-grow-shadow btn warning rounded btn-lg">VER HOJAS</button>
                      </router-link>
                      <router-link to="/nueva">
                        <button class="hvr-grow-shadow btn warning rounded btn-lg">CREAR NUEVA HOJA</button>
                      </router-link>
                    </div>
                  </div>
                  
                </div>

                <div class="column"></div>
                

              </div>
            
      
    </div>


  </div>
</template>

<style>

  .card-body button{

    margin-right: 20px;

    margin-bottom: 20px;

  }

  .hvr-grow-shadow {
    display: inline-block;
    vertical-align: middle;
    -webkit-transform: perspective(1px) translateZ(0);
    transform: perspective(1px) translateZ(0);
    box-shadow: 0 0 1px rgba(0, 0, 0, 0);
    -webkit-transition-duration: 0.3s;
    transition-duration: 0.3s;
    -webkit-transition-property: box-shadow, transform;
    transition-property: box-shadow, transform;
  }
  .hvr-grow-shadow:hover, .hvr-grow-shadow:focus, .hvr-grow-shadow:active {
    box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.5);
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }


</style>

<script>

import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Home',

  components: {
    Navbar,
  },

  mounted: function () {

  },

  data(){

    return{

    }
  },
}
</script>
