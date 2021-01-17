<template>
  <div class="verHojas">

  	<Navbar />

    <div class="container-fluid">

      <div class="row">

      <div class="column"></div>

      <div class="col-sm-12 col-md-8">


        <h1 class="titulo">Mis hojas excel</h1>

        <br>


        <router-link to="/nueva">

          <button class="hvr-grow-shadow btn danger block">Agregar nueva hoja de excel</button>

        </router-link>


        <br>


        <div class="row">

          <div v-for="hoja in hojas" :key="hoja.pk" class="col-6 col-md-4 hojaExcel">

            <router-link :to="{ name: 'Hoja', params: { id: hoja.pk }}">

                <div class="hvr-float-shadow card shadow bg-warning">
                  <div class="card-header bg-warning">
                    <h4 class="card-title">{{hoja.fields.titulo}}</h4>
                  </div>

                  <div class="card-body bg-warning">
                    <img height="100px" src="@/assets/excel02.png">
                  </div>

                </div>

            </router-link>

            
          </div>

        </div>


      </div>

      <div class="column"></div>

      </div>

    </div>

  </div>
</template>

<script>

import Navbar from '@/components/Navbar.vue'

export default {
  name: 'verHojas',
  data(){

    return{

      hojas: [],

    }
  },
  components: {

  	Navbar,

  },
  mounted: function () {


    fetch('https://excel-back.herokuapp.com/polls/getHojas/',{
      method: 'GET',
      headers: new Headers({}),
    })
    .then(response => response.json())
    .then((data) => {

      this.hojas = data.Resultados;

    })


  },
   methods: {

		}
	}

</script>



<style>

  .verHojas{
    overflow-x: hidden;
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


  

  .hvr-float-shadow {
    display: inline-block;
    vertical-align: middle;
    -webkit-transform: perspective(1px) translateZ(0);
    transform: perspective(1px) translateZ(0);
    box-shadow: 0 0 1px rgba(0, 0, 0, 0);
    position: relative;
    -webkit-transition-duration: 0.3s;
    transition-duration: 0.3s;
    -webkit-transition-property: transform;
    transition-property: transform;
  }
  .hvr-float-shadow:before {
    pointer-events: none;
    position: absolute;
    z-index: -1;
    content: '';
    top: 100%;
    left: 5%;
    height: 10px;
    width: 90%;
    opacity: 0;
    background: -webkit-radial-gradient(center, ellipse, rgba(0, 0, 0, 0.35) 0%, rgba(0, 0, 0, 0) 80%);
    background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.35) 0%, rgba(0, 0, 0, 0) 80%);
    -webkit-transition-duration: 0.3s;
    transition-duration: 0.3s;
    -webkit-transition-property: transform, opacity;
    transition-property: transform, opacity;
  }
  .hvr-float-shadow:hover, .hvr-float-shadow:focus, .hvr-float-shadow:active {
    -webkit-transform: translateY(-5px);
    transform: translateY(-5px);
  }
  .hvr-float-shadow:hover:before, .hvr-float-shadow:focus:before, .hvr-float-shadow:active:before {
    opacity: 1;
    -webkit-transform: translateY(5px);
    transform: translateY(5px);
  }




  .titulo{
    margin-top: 10px;
    color: white;
  }


  .verHojas{
    position: relative;
  }

  .card{

    margin-bottom: 20px;
    color: black;

  }


</style>