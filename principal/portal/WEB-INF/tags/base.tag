<%@tag description="Pagina Base" pageEncoding="UTF-8"%>
<%@attribute name="titulo" fragment="true" %>
<%@attribute name="estilos" fragment="true" %>
<%@attribute name="scripts" fragment="true" %>
<%@attribute name="mensaje" required="false" type="java.lang.String" rtexprvalue="true"%>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" type="image/png" href="${pageContext.request.contextPath}/img/favicon.png" />
    <title>IDE - Gobierno Regional de Madre de Dios</title>
    <link href="${pageContext.request.contextPath}/librerias/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/camera-slider/camera.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/base.css" rel="stylesheet">
    <jsp:invoke fragment="estilos"/> 
</head>
<body>
    <nav id="menu-superior" class="navbar navbar-default" >
        <div class="container">
            <div class="container-fluid">                
                <div id="navbar-superior" class="navbar-collapse">
                    <ul class="nav navbar-nav izquierda">
                        <li><a href="${pageContext.request.contextPath}/admin/post"><i class="fa fa-cogs"></i> Administrador</a>|</li>
                        <li><a href="${pageContext.request.contextPath}/ayuda"><i class="fa fa-book"></i> Ayuda</a></li>                      
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="https://www.facebook.com/gestionterritorialmdd" target="_blank"><i class="fa fa-facebook"></i></a></li>
                        <li><a href="https://www.youtube.com/channel/UCB51hiUIR_wOMEj3f5-RUYg" target="_blank"><i class="fa fa-youtube-play"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>

    <div class="header">
        <div id="particle"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <div class="imagen-contendor">
                        <img src="${pageContext.request.contextPath}/img/logo-principal.png" alt="logo-principal">
                    </div>
                </div>
                <div class="col-md-9">
                    <ul class="menu-intermedio">
                        <li class="item-superior boton-s" style="padding-top: 15px;">
                            <a href="https://geogoremad.ide.regionmadrededios.gob.pe" class="boto-superior" target="_blank"><i class="fa fa-globe"></i> GEOGOREMAD</a>
                        </li>
                        <li class="item-superior">
                            <div class="logo-superior">
                                <i class="fa fa-envelope-o"></i>
                            </div>
                            <div class="texto-superior">
                                <span class="titulo-superior">Correo</span>
                                <span class="cont-superior"style="line-height: 13px;word-break: break-all;">sgacondicionamiento@regionmadrededios.gob.pe</span>
                            </div>
                        </li>
                        <li class="item-superior">
                            <div class="logo-superior">
                                <i class="fa fa-map-marker"></i>
                            </div>
                            <div class="texto-superior">
                                <span class="titulo-superior">Dirección</span>
                                <span class="cont-superior">Jr. Tacna C-10</span>
                            </div>
                        </li
                    </ul>
                </div>
            </div>         
        </div>        
    </div>
    
    <nav id="menu-inferior" class="navbar navbar-inverse" >
        <div class="espacio-inferior"></div>
        <div class="container">            
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-inferior" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Menú</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
            <a class="navbar-brand visible-xs" href="#">Menú de Navegación</a>
            </div>
            <div  id="navbar-inferior" class="navbar-collapse collapse">                    
                <ul class="nav navbar-nav navbar-right">
                    <li class="<% if(request.getRequestURI().endsWith("/")) out.println("active"); %>"><a href="${pageContext.request.contextPath}/">INICIO</a></li>
                    <li class="dropdown <% if(request.getRequestURI().endsWith("ide")|request.getRequestURI().endsWith("nosotros")|request.getRequestURI().endsWith("antecedentes")|request.getRequestURI().endsWith("contacto")) out.println("active"); %>">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="dropdownMenu1" role="button" aria-haspopup="true" aria-expanded="false">NOSOTROS <span class="caret"></span></a>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
                            <li><a href="${pageContext.request.contextPath}/ide">¿Que es la <b style="color: green;">IDE</b>?</a></li> 
                            <li><a href="${pageContext.request.contextPath}/nosotros">¿Quiénes Somos?</a></li>
                            <li><a href="${pageContext.request.contextPath}/contacto">Contáctanos</a></li> 
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">SERVICIOS <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="https://geogoremad.ide.regionmadrededios.gob.pe" style="color: orange; font-weight: bold;" target="_blank">GEOGOREMAD</a></li>
                            <li><a href="${pageContext.request.contextPath}/servicios">Servicio de Interoperabilidad</a></li>
                            <li><a href="https://ide.regionmadrededios.gob.pe/geonetwork" target="_blank">Servicio de Visualización de Metadatos</a></li>
                            <li><a href="https://ide.regionmadrededios.gob.pe/geoserver" target="_blank">Servicio de Visualización de Mapas</a></li>
                            <li><a href="https://centrospoblados.regionmadrededios.gob.pe/" target="_blank">Servicio de Categorización de Centros Poblados</a></li>    
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">DOCUMENTACIÓN <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="${pageContext.request.contextPath}/pasacalle">🎊 Pasacalle 2023</a></li>
                            <li><a href="${pageContext.request.contextPath}/mapas">Descarga de Mapas</a></li>
                            <li><a href="${pageContext.request.contextPath}/simbolos">Catálogo de Objetos y Símbolos</a></li>
                            <li><a href="${pageContext.request.contextPath}/manuales">Manuales y Normas</a></li>
                        </ul>
                    </li>
                </ul>                    
            </div>
        </div>
    </nav>

    <jsp:doBody/>  
    
    <div class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-3" style="text-align: center;">
                    <img src="${pageContext.request.contextPath}/img/logo.png" alt="logo" style="width: 95%;">
                    <p class="f-img-b" style="text-align: center;"><b>Sub Gerencia de Acondicionamiento Territorial</b> <br> Gobierno Regional de Madre de Dios</p> 
                </div>
                <div class="col-md-3">
                    <h4 class="f-titulo">SERVICIOS</h4>
                    <ul class="f-links">
                        <li><a href="https://geogoremad.ide.regionmadrededios.gob.pe" style="color: orange; font-weight: bold;" target="_blank">GEOGOREMAD</a></li>
                        <li><a href="${pageContext.request.contextPath}/servicios">Servicio de Interoperabilidad</a></li>
                        <li><a href="https://ide.regionmadrededios.gob.pe/geonetwork" target="_blank">Servicio de Visualización de Metadatos</a></li>
                        <li><a href="https://ide.regionmadrededios.gob.pe/geoserver" target="_blank">Servicio de Visualización de Mapas</a></li>
                        <li><a href="https://centrospoblados.regionmadrededios.gob.pe/" target="_blank">Servicio de Categorización de Centros Poblados</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h4 class="f-titulo">ENLACES EXTERNOS</h4>
                    <ul class="f-links">
                        <li><a href="https://www.gob.pe/regionmadrededios" target="_blank">Gobierno Regional Madre de Dios</a></li>
                        <li><a href="https://www.gob.pe/idep" target="_blank">Infraestructura de Datos Espaciales del Perú</a></li>
                        <li><a href="https://www.idep.gob.pe" target="_blank">Infraestructura Nacional de Información Geoespacial Fundamental del Perú</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <div class="f-icons">
                        <a href="https://www.facebook.com/gestionterritorialmdd" target="_blank">
                            <div class="f-icon">
                                <i class="fa fa-facebook"></i>
                            </div>
                        </a>
                        <a href="https://www.youtube.com/channel/UCB51hiUIR_wOMEj3f5-RUYg" target="_blank">
                            <div class="f-icon">
                                <i class="fa fa-youtube-play"></i>
                            </div>
                        </a>
                    </div>
                    <div class="f-info">
                        <a href="https://ide.regionmadrededios.gob.pe">ide.regionmadrededios.gob.pe</a>
                    </div>
                    <div class="f-info">
                        <a href="mailto:ide@regionmadrededios.gob.pe">sgacondicionamiento@regionmadrededios.gob.pe</a>
                    </div>
                    <div class="f-info">
                        Esquina Jr. Ancash con Jr. Tacna C-10
                    </div>
                    <div class="f-info">
                        Puerto Maldonado - Madre de Dios
                    </div>
                </div>
            </div>
        </div>
        <div class="extra-footer">
           <script>
                var fecha = new Date();
                var anio = fecha.getFullYear();
                document.write("&copy; " + anio + " - Gobierno Regional de Madre de Dios. Todos los derechos reservados.");
            </script>
        </div>
    </div>
    <script src="${pageContext.request.contextPath}/librerias/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/bootstrap/js/bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/camera-slider/jquery.easing.1.3.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/camera-slider/camera.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/particles/particles.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/base.js"></script>
    <jsp:invoke fragment="scripts"/>   
</body>
</html>
