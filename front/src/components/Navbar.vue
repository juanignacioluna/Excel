<template>

  <div id="navbar">


              <nav class="navbar expand-md default-nav bg-warning">
                <div class="container">

                  <div class="brand">
                    <router-link to="/">
                      <a>Excel generator</a>
                    </router-link>
                  </div>

                  <div class="menu-box" id="mainNav2">

                    <ul class="menu mx-auto">
                      <router-link to="/verHojas">
                        <li class="nav-item"><a class="nav-link">Ver Hojas excel</a></li>
                      </router-link>
                      <router-link to="/nueva">
                        <li class="nav-item"><a class="nav-link">Crear nueva hoja excel</a></li>
                      </router-link>
                    </ul>

                  </div>

                </div>
              </nav>

    
  </div>

</template>

<script>


  
export default {
  name: 'Navbar',
	data(){
    return{

    }
	},
	mounted: function () {



	},
	methods: {

	},


}
</script>


<style>

.brand{
  margin-top: 10px;
  margin-bottom: 12px;
}



</style>
