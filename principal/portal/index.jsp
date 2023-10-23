<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="DATOS.*, java.util.List" %>
<%@ taglib prefix="tags" tagdir="/WEB-INF/tags" %>
<%@ page import="java.util.List" %>

<tags:base>
    <jsp:attribute name="titulo">
        Inicio
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

            var listaDeNoticias = [{
                id: 1,
                titulo: "Lanzamiento del Geoportal GEOGOREMAD",
                resumen: "¡Estamos emocionados de anunciar el lanzamiento del nuevo Geoportal GOREMAD! Accede a datos geoespaciales y servicios de mapas de manera fácil y eficiente.",
                imagen: "${pageContext.request.contextPath}/img/noticias/geoportal.png",
                autor: "admin",
                fecha: obtenerFechaActual()
            }];

            // Encuentra el contenedor de noticias en tu página (reemplaza 'lista-noticias' con el ID correcto).
                var listaNoticiasContainer = document.getElementById("lista-noticias");

                // Recorre la lista de noticias y crea elementos HTML para cada una.
                for (var i = 0; i < listaDeNoticias.length; i++) {
                    var noticia = listaDeNoticias[i];

                    // Crea un nuevo elemento div para la noticia.
                    var noticiaDiv = document.createElement("div");
                    noticiaDiv.className = "col-md-6";

                    // Construye el contenido de la noticia utilizando la concatenación de cadenas.
                    var contenidoNoticia =
                        '<div class="n-sup">' +
                        '<div class="n-fecha">' +
                        '<div class="n-f-left">' + noticia.fecha + '</div>' +
                        '<div class="n-f-center"></div>' +
                        '<div class="n-f-right">Autor: ' + noticia.autor + '</div>' +
                        '</div>' +
                        '</div>' +
                        '<div class="n-img"><img src="' + noticia.imagen + '" alt="' + noticia.imagen + '"></div>' +
                        '<div class="n-cont">' +
                        '<h4>' + noticia.titulo + '</h4>' +
                        '<p>' + noticia.resumen + '</p>' +
                        '</div>' +
                        '<div class="n-foot">' +
                        '<a href="${pageContext.request.contextPath}/nota?id=' + noticia.id + '">Ver más...</a>' +
                        '</div>';

                    // Establece el contenido HTML de la noticia.
                    noticiaDiv.innerHTML = contenidoNoticia;

                    // Agrega la noticia al contenedor de noticias.
                    listaNoticiasContainer.appendChild(noticiaDiv);
                }
        </script>
    </jsp:attribute>
    <jsp:body>
        <div class="slider-aux">
            <div class="camera_wrap" id="camera_wrap_1">
                <div data-src="${pageContext.request.contextPath}/img/menus/menu.jpg"></div>
                <div data-src="${pageContext.request.contextPath}/img/menus/menu2.jpg"></div>
                <div data-src="${pageContext.request.contextPath}/img/menus/menu3.jpg"></div>
                <div data-src="${pageContext.request.contextPath}/img/menus/menu4.jpg"></div>
            </div>
            <div class="clearfix"></div>
        </div>
        <div class="container">
            <div class="row" style="margin-bottom: 30px;">
                <%-- Servicios --%>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://geogoremad.ide.regionmadrededios.gob.pe" target="_blank">
                            <img src="${pageContext.request.contextPath}/img/s-visor-3.png">
                            <h3 style="color: orange; font-weight: bold;">GEOGOREMAD</h3>
                        </a>
                        <p>El <b>Visor <span style="color: orange; font-weight: bold;">GEOGOREMAD</span></b>, permite superponer visualmente datos vectoriales
                            y ráster, en diferentes formas, con distintos sistemas de referencia y
                            coordenadas y en distintos servidores.</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="${pageContext.request.contextPath}/servicios">
                            <img src="${pageContext.request.contextPath}/img/s-visor.png">
                            <h3>Servicio de Interoperabilidad</h3>
                        </a>
                        <p>El <b>Servicio de Interoperabilidad (WMS, WFS y WCS)</b>, permite descargar la información geográfica vectorial completa, su geometría y tabla de atributos asociada.</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://ide.regionmadrededios.gob.pe/geonetwork" target="_blank">
                            <img src="${pageContext.request.contextPath}/img/s-metadata.png">
                            <h3>Servicio de Visualización de Metadatos</h3>
                        </a>
                        <p>El <b>Servicio de Visualización de Metadatos</b>, permite la publicación y búsqueda de información (metadatos) que describen datos, servicios, aplicaciones y en general todo tipo de recursos.</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://centrospoblados.regionmadrededios.gob.pe" target="_blank">
                            <img src="${pageContext.request.contextPath}/img/s-visor-5.png"
                                style="margin-bottom: 20px; margin-top: 15px;">
                            <h3>Servicio de Categorización de Centros Poblados</h3>
                        </a>
                        <p>El <b>Servicio de Categorización de Centros Poblados</b>, permite la publicación y búsqueda de información que describe datos, servicios básicos, actividades económicas y otros recursos referentes a los centros poblados.</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-8">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>NOTICIAS Y ACTIVIDADES</h3>
                            </div>
                        </div>
                    </div>
                    <div id="lista-noticias"></div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="end-cont">
                                <a href="${pageContext.request.contextPath}/noticias">Ver Todas <i class="fa fa-angle-right" aria-hidden="true"></i><i class="fa fa-angle-right" aria-hidden="true"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>OTROS SERVICIOS</h3>
                            </div>
                            <div class="servicios">
                                <a data-toggle="modal" data-target="#myModal">
                                    <div class="servicio-item">
                                        <div class="servicio-titulo">
                                            <h4>Servicio Meteorológico</h4>
                                            <p>Visualización de Mapa Meteorológico del Departamento de Madre de Dios.</p>
                                        </div>
                                        <div class="servicio-icono">
                                            <img src="${pageContext.request.contextPath}/img/m-mapa.png">
                                        </div>
                                    </div>
                                </a>
                                <a href="${pageContext.request.contextPath}/mapas">
                                    <div class="servicio-item">
                                        <div class="servicio-titulo">
                                            <h4>Descarga de Mapas</h4>
                                            <p>Descarga y comparte mapas producidos por la IDE.</p>
                                        </div>
                                        <div class="servicio-icono">
                                            <img src="${pageContext.request.contextPath}/img/s-mapas.png">
                                        </div>
                                    </div>
                                </a>
                                <a href="${pageContext.request.contextPath}/simbolos">
                                    <div class="servicio-item">
                                        <div class="servicio-titulo">
                                            <h4>Catálogo de Objetos y Símbolos</h4>
                                            <p>Definición de los objetos y la simbología utilizada en los mapas.</p>
                                        </div>
                                        <div class="servicio-icono">
                                            <img src="${pageContext.request.contextPath}/img/s-objeto.png">
                                        </div>
                                    </div>
                                </a>
                                <a href="${pageContext.request.contextPath}/manuales">
                                    <div class="servicio-item">
                                        <div class="servicio-titulo">
                                            <h4>Manuales y Normas</h4>
                                            <p>Descarga documentos de carácter geográfico producidos por la IDE.</p>
                                        </div>
                                        <div class="servicio-icono">
                                            <img src="${pageContext.request.contextPath}/img/documents2.png">
                                        </div>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <br>
        </div>
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
            aria-hidden="true">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title" id="myModalLabel">Servicio Meteorológico - Madre de Dios
                        </h4>
                    </div>
                    <div class="modal-body">
                        <iframe width="100%" height="450" src="https://embed.windy.com/embed2.html?lat=-13.795&lon=-70.752&detailLat=-11.870&detailLon=-70.513&width=650&height=450&zoom=6&level=surface&overlay=wind&product=ecmwf&menu=&message=true&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1" frameborder="0"></iframe>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" data-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>
    </jsp:body>
</tags:base>
