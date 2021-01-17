<template>
  <div class="hoja">


    <Navbar />

    <div class="container-fluid">

      <div class="row">

        <div class="column"></div>

        <div class="col-sm-12 col-md-8">


          <h1 class="tituloHoja">{{hoja.titulo}}</h1> 

          <br> <br>

          <div class="row">


            <div class="column">

              <button v-on:click="actualizar" class="hvr-grow-shadow btn success block">Guardar cambios</button>

            </div>


            <div class="column">

              <button v-on:click="eliminar" class="hvr-grow-shadow btn danger block">Eliminar</button>

            </div>
            
          </div>


          <br>


          <div class="row fj-center">

            <div class="col-4 col-md-3">

              <button v-on:click="mas" class="hvr-grow-shadow btn info block rounded">+</button>
              
            </div>

            <div class="col-4 col-md-3">

              <button v-on:click="menos" class="hvr-grow-shadow btn primary block rounded">-</button>
              
            </div>
            
          </div>

          <br> <br>

          <div id="spreadsheet"></div>
          

        </div>

        <div class="column"></div>

      </div>

    </div>




  </div>
</template>

<script>

import Navbar from '@/components/Navbar.vue'
import jexcel from 'jexcel';

export default {
  name: 'Hoja',

  data(){

    return{

      columnsExcel: null,

      hoja: {},

      id: null,

      filas: [

          [],

      ],

    }
  },

  components: {
    Navbar,
  },

  mounted: function () {

      this.id = this.$route.params.id;



      let id = this.id;

      fetch('https://excel-back.herokuapp.com/polls/getHoja/',{
        method: 'POST',
        headers: new Headers({}),
        body: JSON.stringify({id: id}),
      })
      .then(response => response.json())
      .then((data) => {

        this.hoja = data.Hoja[0].fields;




        let columnas = this.hoja.columnas;

        let columnasParse = JSON.parse(columnas.replace(/'/g, '"'))

        let i;

        let columnsExcel = [];

        for (i = 0; i < columnasParse.length; i++) {

          let tipo = columnasParse[i].tipo;

          let titulo = columnasParse[i].nombre;

          if(tipo=="numeric"){

            columnsExcel.push({type: tipo, title: titulo, width: 90, mask:"$ #.##,00", decimal:","});

          }else if(tipo=="color"){

            columnsExcel.push({type: tipo, title: titulo, width: 90, render:'square'});

          }else{

            columnsExcel.push({type: tipo, title: titulo, width: 90});

          }

        }

        this.columnsExcel = columnsExcel;






        if(this.hoja.celdas=="[]"){

          this.filas[0] = this.filaNula()

        }else{

          let celdas = this.hoja.celdas;

          this.filas = JSON.parse(celdas.replace(/'/g, '"').replace(/T/g, 't').replace(/F/g, 'f'))

        }





        this.excel();

      })


  },

  methods: {

    eliminar(){

      let id = this.id;

      fetch('https://excel-back.herokuapp.com/polls/borrar/',{
        method: 'POST',
        headers: new Headers({}),
        body: JSON.stringify({id: id}),
      })
      .then(response => response.text())
      .then((data) => {


        this.$router.push({ path: `/verHojas/` })


      });

    },

    actualizar(){


      let id = this.id;

      let filas = this.filas;

      fetch('https://excel-back.herokuapp.com/polls/actualizar/',{
        method: 'POST',
        headers: new Headers({}),
        body: JSON.stringify({id: id, filas: filas}),
      })
      .then(response => response.text())
      .then((data) => {


      });




    },

    filaNula(){

      let filaNula = [];

      let i;

      for (i = 0; i < this.columnsExcel.length; i++) {

          let nulo;

          switch (this.columnsExcel[i].type) {
              case 'color':
                  nulo = '#eb34ae'
                  break;
              case 'text':
                  nulo = ''
                  break;
              case 'calendar':
                  nulo = '2020-02-12'
                  break;
              case 'checkbox':
                  nulo = true
                  break;
              case 'numeric':
                  nulo = '$ 1.000,00'
                  break;
          }

          filaNula.push(nulo)

      }


      return filaNula;


    },

    excel(){

      document.getElementById('spreadsheet').innerHTML = "";

      jexcel(document.getElementById('spreadsheet'), {
          data: this.filas,
          columns: this.columnsExcel,
      });

    },

    mas(){

      this.filas.push(this.filaNula());

      this.excel();

    },

    menos(){

      this.filas.pop();

      this.excel();

    },

  },

}


</script>



<style>

  .hoja{
    position: relative;
  }

  .tituloHoja{
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
