<template>
  <div id="animacionCargando">
    <div class="contenedor">
      <div class="contenedor-pajaro">
        <img class="pajaro" src="/pajaro.svg" />
      </div>
      <img class="fondo" src="/fondo.svg" />
      <div class="fondo-gradiente" />
    </div>
  </div>
</template>

<style scoped>
#animacionCargando {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color: white;
}
.contenedor {
  width: 100%;
  height: 100%;
}

/** Fondo */
.fondo {
  width: auto;
  height: 100%;
}

/** Pájaro */
.contenedor-pajaro {
  height: 300px;
  left: calc(50% - 130px);
  overflow: hidden;
  position: absolute;
  top: 30%;
  width: 306px;
  z-index: 1;
}
.pajaro {
  -webkit-animation: fly 0.9s steps(10) infinite;
  -moz-animation: fly 0.9s steps(10) infinite;
  -o-animation: fly 0.9s steps(10) infinite;
  animation: fly 0.9s steps(10) infinite;
}
@-webkit-keyframes fly {
  0% {
    transform: translate(0, 0);
    -webkit-transform: translate(0, 0);
    -o-transform: translate(0, 0);
    -moz-transform: translate(0, 0);
  }
  100% {
    transform: translate(-3064px, 0);
    -webkit-transform: translate(-3064px, 0);
    -o-transform: translate(-3064px, 0);
    -moz-transform: translate(-3064px, 0);
  }
}
@-moz-keyframes fly {
  0% {
    transform: translate(0, 0);
    -webkit-transform: translate(0, 0);
    -o-transform: translate(0, 0);
    -moz-transform: translate(0, 0);
  }
  100% {
    transform: translate(-3064px, 0);
    -webkit-transform: translate(-3064px, 0);
    -o-transform: translate(-3064px, 0);
    -moz-transform: translate(-3064px, 0);
  }
}
@keyframes fly {
  0% {
    transform: translate(0, 0);
    -webkit-transform: translate(0, 0);
    -o-transform: translate(0, 0);
    -moz-transform: translate(0, 0);
  }
  100% {
    transform: translate(-3064px, 0);
    -webkit-transform: translate(-3064px, 0);
    -o-transform: translate(-3064px, 0);
    -moz-transform: translate(-3064px, 0);
  }
}

/** Fondo gradiente */
.fondo-gradiente {
  width: 100%;
  height: 100%;
  filter: alpha(opacity=40);
  -khtml-opacity: 0.4;
  -moz-opacity: 0.4;
  opacity: 0.4;
  -ms-filter: 'progid:DXImageTransform.Microsoft.Alpha(Opacity=40)';
  color: #fff;
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  -webkit-animation: Gradient 10s ease infinite;
  -moz-animation: Gradient 10s ease infinite;
  animation: Gradient 10s ease infinite;
  position: absolute;
  top: 0px;
  left: 0px;
  z-index: 0;
}
@-webkit-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@-moz-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
