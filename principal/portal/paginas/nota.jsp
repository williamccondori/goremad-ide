<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="DATOS.*, java.util.List" %>
<%@ taglib prefix="tags" tagdir="/WEB-INF/tags" %>
<%@ page import="java.util.List" %>

<tags:base>
    <jsp:attribute name="titulo">
        Noticias y Actividades
    </jsp:attribute>
    <jsp:attribute name="scripts">
        <script>
            function obtenerFechaActual() {
                var fecha = new Date();
                var dia = fecha.getDate();
                var mes = fecha.getMonth() + 1;
                var anio = fecha.getFullYear();
                
                return dia + "/" + mes + "/" + anio;
            }

            function obtenerNoticiaPorId(id) {
                return listaDeNoticias.find(function(noticia) {
                    return noticia.id === id;
                });
            }

            function mostrarNoticia(id) {
                var noticia = obtenerNoticiaPorId(id);

                if (noticia) {
                    document.getElementById('noticia-titulo').textContent = noticia.titulo;
                    document.getElementById('noticia-contenido').innerHTML = noticia.contenido;
                    document.getElementById('noticia-imagen').src = noticia.imagen;
                    document.getElementById('noticia-autor').textContent = "Autor: " + noticia.autor;
                    document.getElementById('noticia-fecha').textContent = noticia.fecha;
                } else {
                    console.error("No se encontró la noticia con el ID: " + id);
                }
            }

            var listaDeNoticias = [{
                id: 1,
                titulo: "Lanzamiento del Geoportal GEOGOREMAD",
                resumen: "¡Estamos emocionados de anunciar el lanzamiento del nuevo Geoportal GOREMAD! Accede a datos geoespaciales y servicios de mapas de manera fácil y eficiente.",
                contenido: "¡Estamos emocionados de anunciar el lanzamiento del nuevo Geoportal GOREMAD! Accede a datos geoespaciales y servicios de mapas de manera fácil y eficiente. Nuestro nuevo Geoportal te brinda acceso a una amplia gama de información geográfica que te ayudará en la toma de decisiones y en la gestión territorial. Explora mapas interactivos, consulta datos actualizados y descubre herramientas poderosas para análisis espaciales. El Geoportal GEOGOREMAD es una herramienta indispensable para profesionales, investigadores y tomadores de decisiones que trabajan en el ámbito geoespacial. Te invitamos a explorar todas las características y posibilidades que ofrece este emocionante recurso. Únete a nosotros en este emocionante viaje hacia el mundo de la información geoespacial de Madre de Dios.",
                imagen: "${pageContext.request.contextPath}/img/noticias/geoportal.png",
                autor: "admin",
                fecha: obtenerFechaActual()
            }];

            var urlParams = new URLSearchParams(window.location.search);
            var id = parseInt(urlParams.get("id"));

            var facebook = document.getElementById("facebook");
            var twitter = document.getElementById("twitter");
            facebook.href = "http://www.facebook.com/sharer.php?u=https://www.ide.goremad.gob.pe/paginas/nota?id=" + id;
            twitter.href = "https://twitter.com/share?url=https://www.ide.goremad.gob.pe/paginas/nota?id=" + id;

            mostrarNoticia(id);
        </script>
    </jsp:attribute>
    <jsp:body>
        <div class="header-inf">  
            <div class="espaciador">
                <h2>Noticias y Actividades</h2>
            </div>        
            <img src="${pageContext.request.contextPath}/img/notas.jpg"></img>
            <div class="ruta">
                <div class="ruta-aux">
                    <ol class="breadcrumb">
                        <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                        <li class="active">Noticias y Actividades</li>
                    </ol>
                </div>
            </div>
        </div>
        <div class="container">     
            <div class="row">
                <div class="col-md-8">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Noticias y Actividades</h3>
                            </div>        
                        </div>                    
                    </div>
                    <div class="noticia-item">
                        <div class="n-sup">
                            <div class="n-fecha">
                                <div class="n-f-left" id="noticia-fecha">
                                </div>
                                <div class="n-f-center"></div>
                                <div class="n-f-right" id="noticia-autor">
                                </div>
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-12">
                                <div class="n-img" style="margin-bottom: 15px;">
                                    <img src="" alt="" id="noticia-imagen">
                                </div>
                            </div>
                            <div class="col-md-12">
                                <div class="n-cont">
                                    <h4 id="noticia-titulo"></h4>
                                    <p id="noticia-contenido"></p>
                                </div>
                                <div class="n-foot">
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div> 
                </div>
                <div class="col-md-4">
                    <div class="titulo-cont">
                        <h3>Detalles</h3>
                    </div>    
                    <div>                        
                        <p style="text-align: justify">
                            La <b>IDE</b> de Madre de Dios realiza diversas actividades para dar a conocer acerca de la Getión Territorial y promover el uso de herramientas de información geográfica, que proporcionen información oportuna para la toma de decisiones.
                        </p>        
                        
                        <h4>Compartir</h4>                                                   
                        <!-- Facebook -->
                        <a href="http://www.facebook.com/sharer.php?u=https://www.ide.goremad.gob.pe/paginas/nota?id=" id="facebook">
                            <i class="fa fa-facebook-official" style="font-size: 30px; color: #3b5998;"></i>
                        </a>
                        <br />
                        <!-- Twitter -->
                        <a href="https://twitter.com/share?url=https://www.ide.goremad.gob.pe/paginas/nota?id=&text=" id="twitter">
                            <i class="fa fa-twitter-square" style="font-size: 30px; color: #00aced;"></i>
                        </a>
                        <br>
                    </div>
                </div>
            </div>
        </div>
    </jsp:body>
</tags:base>
