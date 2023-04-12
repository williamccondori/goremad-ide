<%@page contentType="text/html" pageEncoding="UTF-8" import="DATOS.*, java.util.List" %>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>
<%-- <% request.setCharacterEncoding("UTF-8"); Post oPost=new Post(); String tex1="<div class='row'>" ; int
cont=0; List<Post> lista = oPost.listar_publico(1);
for (Post elem : lista)
{
if ((cont % 2) == 0)
{
tex1 +="</div>
<div class='row'>";
    }
    tex1+="<div class='col-md-6'>"+
        "<div class='noticia-item'>"+
            "<div class='n-sup'>"+
                "<div class='n-fecha'>"+
                    "<div class='n-f-left'>"+elem.getFechaf()+"</div>"+
                    "<div class='n-f-center'></div>"+
                    "<div class='n-f-right'>"+elem.getId()+"</div>"+
                    "</div>"+
                "</div>"+
            "<div class='n-img'><img
                    src='"+(elem.getImagen()!=null?"files/"+elem.getImagen():"img/no-picture.png")+"'
                    alt=''></div>"+
            "<div class='n-cont'>"+
                "<h4>"+elem.getTitulo()+"</h4>"+
                "<p>"+elem.getResumen()+"</p>"+
                "</div>"+
            "<div class='n-foot'>"+
                "<a href='"+request.getContextPath()+"/nota?id="+elem.getId()+"'>Ver más...</a>"+
                "</div>"+
            "</div>"+
        "</div>";
    cont++;
    }
    tex1 +="</div>";
request.setAttribute("noticias", tex1);
%> --%>

<tags:base>
    <jsp:attribute name="titulo">
        Inicio
    </jsp:attribute>
    <jsp:attribute name="estilos">
    </jsp:attribute>
    <jsp:attribute name="scripts">
        <script src="${pageContext.request.contextPath}/js/inicio.js"></script>
    </jsp:attribute>
    <jsp:body>
        <div class="slider-aux">
            <div class="camera_wrap" id="camera_wrap_1">
                <%-- <div data-src="img/menu-1.jpg"></div>
                <div data-src="img/background-2.jpg"></div> --%>
            </div>
            <div class="clearfix"></div>
        </div>
        <div class="container">
            <div class="row" style="margin-bottom: 30px;">
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://geogoremad.ide.regionmadrededios.gob.pe">
                            <img src="${pageContext.request.contextPath}/img/s-visor-3.png">
                            <h3  style="color: orange; font-weight: bold;">GEOGOREMAD</h3>
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
                        <p>El <b>Servicio de Interoperabilidad (WMS, WFS y WCS)</b>, permite descargar la información geográfica vectorial completa, sugeometría y tabla de atributos asociada.</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://ide.regionmadrededios.gob.pe/geonetwork">
                            <img src="${pageContext.request.contextPath}/img/s-metadata.png">
                            <h3>Servicio de Visualización de Metadatos</h3>
                        </a>
                        <p>El <b>Servicio de Visualización de Metadatos</b>, permite la publicación y búsqueda de información (metadatos) que describen datos, servicios, aplicaciones y en general todo tipo de recursos.</p>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="servicio-p">
                        <a href="https://centrospoblados.regionmadrededios.gob.pe">
                            <img src="${pageContext.request.contextPath}/img/s-visor-5.png"
                                style="margin-bottom: 20px; margin-top: 15px;">
                            <h3>Servicio de Categorización de Centros Poblados</h3>
                        </a>
                        <p>El <b>Servicio de Categorización de Centros Poblados</b>, permite la publicación y búsqueda de información que describen datos, servicios basicos, actividades economicas y otros recursos referente a los centros poblados.</p>
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

                    <!--INICIO NOTICIAS-->

                    ${noticias}

                    <!--FIN NOTICIAS-->

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
                                            <img
                                                src="${pageContext.request.contextPath}/img/documents2.png">
                                        </div>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                    <%-- <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Síguenos</h3>
                            </div>
                            <div class="fb-page" data-href="https://www.facebook.com/gestionterritorialmdd"
                                data-small-header="false" data-adapt-container-width="true"
                                data-hide-cover="false" data-show-facepile="true">
                                <blockquote cite="https://www.facebook.com/gestionterritorialmdd"
                                    class="fb-xfbml-parse-ignore"><a
                                        href="https://www.facebook.com/gestionterritorialmdd">IDE</a>
                                </blockquote>
                            </div>

                        </div>
                    </div> --%>
                    <%-- <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Videos</h3>
                            </div>
                            <iframe width="100%" height="250"
                                src="https://www.youtube.com/embed/UkvErzbNMzg" frameborder="0"
                                allowfullscreen></iframe>
                        </div>
                    </div> --%>
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
                        <iframe width="100%" height="450" src="https://embed.windy.com/embed2.html?lat=-13.795&lon=-70.752&detailLat=-11.870&detailLon=-70.513&width=650&height=450&zoom=6&level=surface&overlay=wind&product=ecmwf&menu=&message=true&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1" frameborder="0"></iframe>                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" data-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>
    </jsp:body>
</tags:base>