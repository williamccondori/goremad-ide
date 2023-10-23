<%-- 
    Document   : ide
    Created on : 18/01/2018, 03:17:32 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">IDE</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Que es IDE</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/que.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Que es IDE</li>
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
                                <h3>¿Que entendemos por <b>IDE</b> Madre de Dios?</h3>
                            </div>  
                            <p class="justificar">
                                Una <b>Infraestructura de Datos Espaciales (IDE) </b> es el conjunto de políticas, estándares, organizaciones, recursos humanos y recursos tecnológicos que facilitan el intercambio, la producción, obtención, uso y acceso de la información espacial a nivel regional y nacional, a fin de apoyar el desarrollo territorial del departamento de Madre de Dios para favorecer la oportuna toma de decisiones.
                            </p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Componentes de la <b>IDE</b> Madre de Dios</h3>
                            </div>  
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-users" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>Personal</h4>
                                    <p class="justificar">
                                        Se componen de actores interesados en su puesta en marcha, ya sea por el hecho de producir datos, ser usuarios o simplemente pertenecer a comunidades de difusión y apoyo. 
                                        Tipos de personal que surgen en una IDE son: productores de datos, productores de servicio, desarrolladores de software, universidades, centros de investigación y usuarios finales.
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-database" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>Datos</h4>
                                    <p class="justificar">
                                        Los datos geográficos se clasifican en <b>1. Datos de referencia</b>, sirven de base para construir otro dato fundamental o temático, y <b>2. Datos temáticos</b>, son elaborados a partir de datos de referencia, a los que se añade otras informaciones, que describen determinados temas concretos sobre el territorio.
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-globe" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>Servicios</h4>
                                    <p class="justificar">
                                        Los servicios de información geográfica son accesibles desde un simple navegador a través de internet y consisten principalmente en la visualización, consulta, análisis y descarga de datos geográficos.
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-file-text-o" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>Metadatos</h4>
                                    <p class="justificar">
                                        Son datos que describen los conjuntos de datos geográficos y los servicios de información geográfica, y que hacen posible localizarlos, inventariarlos y utilizarlos, es decir, son los datos sobre los propios datos o servicios, que informan sobre el contenido del conjunto de datos o las operaciones del servicio donde incluye su nombre y resumen, cuando fue creado el conjunto de datos y otras características que sirven para caracterizar datos. 
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-handshake-o" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>Políticas</h4>
                                    <p class="justificar">
                                        Permite <b>1.</b> La creación del comité coordinador de infraestructura de datos espaciales del Gobierno Regional de Madre de Dios, <b>2.</b> Aprobación de un marco legal que promueva y regule la implantación de una IDE, <b>3.</b> Realización de convenios y acuerdos de colaboración y <b>4.</b> Acuerdos entre los productores de información geográfica para coordinar la generación y mantenimiento de la información geográfica.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                     <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>¿Que servicios brinda la <b>IDE</b> Madre de Dios?</h3>
                            </div>  
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-object-group" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>SERVICIO DE MAPAS WEB</h4>
                                    <p class="justificar">
                                        El <b>servicio de mapas web (WMS)</b>, permite superponer visualmente datos vectoriales y ráster, en diferentes formas, con distintos sistemas de referencia y coordenadas y en distintos servidores.
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-file-text-o" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>SERVICIO DE CATÁLOGO DE METADATOS</h4>
                                    <p class="justificar">
                                        El <b> servicio de catálogo de metadatos (CSW)</b>, permite la publicación y búsqueda de información (metadatos) que describen datos, servicios, aplicaciones y en general todo tipo de recursos. 
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="componente-icono"><i class="fa fa-cloud-download" aria-hidden="true"></i></div>
                                </div>
                                <div class="col-md-9">
                                    <h4>SERVICIO DE PUBLICACIÓN Y DESCARGA DE OBJETOS GEOGRÁFICOS</h4>
                                    <p class="justificar">
                                        El <b> servicio publicación y descarga de objetos geográficos (WFS)</b>, permite recuperar y modificar datos espaciales en formato vectorial. A través de los servicios WFS es posible descargar la información geográfica vectorial completa, su geometría y tabla de atributos asociada.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <br>
                    <br>
                </div>
                <div class="col-md-4">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>¿Que son datos espaciales?</h3>
                            </div> 
                            <p class="justificar">
                                Datos espaciales, también conocidos como datos geoespaciales o datos geográficos, es el conjunto de datos relacionado con las características, la localización y atributos de los elementos geográficos, así como su relación entre ellos y atributo temático.  
                            </p>
                            <p class="justificar">
                                Representa la localización, tamaño y forma de un objeto en el planeta tierra, como por ejemplo ciudades, ríos, carreteras, centros poblados, concesiones forestales, etc.
                            </p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Beneficios de la <b>IDE</b></h3>
                            </div> 
                            <ul class="lista-d">
                                <li class="justificar">
                                    Facilita la integración, el acceso e intercambio de información geoespacial, tanto a nivel institucional y empresarial como de los propios ciudadanos.
                                </li>
                                <li class="justificar">
                                    Permite la reducción de costos y evita la duplicación de esfuerzos en hacer mapas, planos, cartas, imágenes satelitales, estudios territoriales, catastro, etc.
                                </li>
                                <li class="justificar">
                                    Mejora la planificación, gestión y toma de decisiones en el Gobierno Regional de Madre de Dios.
                                </li>
                                <li class="justificar">
                                    Promueve la implementación de nuevos sistemas de información como el Sistema de Gestión Territorial. 
                                </li>
                                <li class="justificar">
                                    Brinda información que sirve para la ubicación de servicios como por ejemplo los centros poblados, educación, entre otros.
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
 
</jsp:body>        
</tags:base>
