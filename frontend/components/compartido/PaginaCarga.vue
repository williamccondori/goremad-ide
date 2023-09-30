<template>
  <div id="loading-page">
    <div class="container">
      <h1 style="text-align: center; margin-top: 1rem">
        <Titulo style="margin-bottom: 1rem" />
        <a-spin />
      </h1>
      <div class="bird-container">
        <img class="bird" src="/pajaro.svg" />
      </div>
      <img class="background" src="/fondo.svg" />
      <div class="gradient-background" />
    </div>
  </div>
</template>
<script>
import Titulo from '../compartido/Titulo.vue';
export default {
  components: { Titulo },
};
</script>
<style scoped>
#loading-page {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1001;
  background-color: white;
}
.container {
  width: 100%;
  height: 100%;
}
.background {
  width: auto;
  height: 100%;
}
.bird-container {
  height: 300px;
  left: calc(50% - 130px);
  overflow: hidden;
  position: absolute;
  top: 30%;
  width: 306px;
  z-index: 1;
}
.bird {
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
.gradient-background {
  width: 100%;
  height: 100%;
  filter: alpha(opacity=40);
  -khtml-opacity: 0.4;
  -moz-opacity: 0.4;
  opacity: 0.4;
  -ms-filter: 'progid:DXImageTransform.Microsoft.Alpha(Opacity=40)';
  color: #fff;
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #00ff00 #23a6d5);
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
