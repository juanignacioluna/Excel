<template>
  <div class="nueva">


    <Navbar />

    <div class="container-fluid">

      <div class="row">

        <div class="column"></div>

        <div class="col-12 col-sm-10 col-xl-8">
          
            <h1 class="tituloNueva">Creando hoja de excel</h1>

            <br>

            <div class="row">

              <div class="column"></div>

              <div class="col-sm-12 col-md-6">
                
                  <div class="sample">

                    <div class="group">
                      <input v-model="titulo" class="input" type="text" placeholder="Titulo">
                    </div>

                    <hr>

                    <h4 class="subtitulo">Columnas</h4>

                    <div class="row">

                      <div class="col-6">

                        <button v-on:click="mas" class="hvr-grow-shadow btn success block">+</button>
                        
                      </div>

                      <div class="col-6">

                        <button v-on:click="menos" class="hvr-grow-shadow btn danger block">-</button>
                        
                      </div>

                    </div>


                    <div v-for="columna in columnas" :key="columna.id" class="row">

                          <div class="col-6">

                              <div class="group">
                                <input v-model="columna.nombre" class="input" type="text" placeholder="Nombre">
                              </div>
                            
                          </div>

                          <div class="col-6">

                              <div class="group">
                                  <select v-model="columna.tipo" class="input">
                                    <option value="text">Texto</option>
                                    <option value="calendar">Fecha</option>
                                    <option value="checkbox">Checkbox</option>
                                    <option value="color">Color</option>
                                    <option value="numeric">Dinero</option>
                                  </select>
                              </div>
                            
                          </div>

                    </div>

                    <br>
                    
                    <button v-on:click="crear" class="hvr-grow-shadow btn secondary block">CREAR</button>

                    <br><br>



                  </div>

              </div>

              <div class="column"></div>
              

            </div>



        </div>
        
        <div class="column"></div>

      </div>

    </div>






  </div>
</template>

<style>

  .nueva{
    overflow-x: hidden;
  }

  .subtitulo{

    color: white;

  }

  .nueva{

    position: relative;

  }

  .tituloNueva{
    color: white;
    margin-top: 10px;
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
  name: 'Nueva',

  data(){

    return{

      titulo: "",

      columnas: [
                  {id:1},
                ],

    }
  },

  components: {
    Navbar,
  },

  mounted: function () {

  },

  methods: {

    crear(){

            let titulo = this.titulo;

            let columnas = this.columnas;

            fetch('https://excel-back.herokuapp.com/polls/nueva/',{
              method: 'POST',
              headers: new Headers({}),
              body: JSON.stringify({titulo: titulo, columnas: columnas}),
            })
            .then(response => response.text())
            .then((data) => {

              console.log(data)

              this.$router.push({ path: `/hoja/${data}` })

            })

    },

    mas(){

      if(!(this.columnas.length==4)){

        let id = (this.columnas.length + 1);

        this.columnas.push({id: id});

        console.log(this.columnas)

      }

    },

    menos(){

      this.columnas.splice((this.columnas.length - 1), 1);

      console.log(this.columnas)

    },

  },
}
</script>
