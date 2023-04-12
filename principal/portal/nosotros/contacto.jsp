<%-- 
    Document   : contacto
    Created on : 22/01/2018, 07:31:40 AM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Contáctanos</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body> 
    <style>
       #map {
        height: 450px;
        width: 100%;
       }
    </style>
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Contáctanos</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/contacto.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Contacto</li>
                  </ol>
            </div>
        </div>
    </div>
        <div class="container">  
            <div class="row">
                <div class="col-md-2">     
                </div>  
                <div class="col-md-8">
                    <div class="titulo-cont">
                        <h3>Formulario de contacto</h3>
                    </div>        
                </div> 
                <div class="col-md-2">     
                </div> 
            </div>
            <div class="row">
                <div class="col-md-1">     
                </div> 
                <div class="col-md-10">
                    <div class="row">
                        <div class="col-md-6">
                            <form class="form-horizontal">
                                <div  class="form-group">
                                    <label class="col-sm-2 control-label">Nombre</label>
                                    <div class="col-sm-10">
                                        <input type="text" class="form-control" placeholder="Ingrese su nombre completo">
                                    </div>
                                </div>
                                <div  class="form-group">
                                    <label class="col-sm-2 control-label">Correo</label>
                                    <div class="col-sm-10">
                                        <input type="email" class="form-control" placeholder="ejemplo@correo.com">
                                    </div>
                                </div>
                                <div  class="form-group">
                                    <label class="col-sm-2 control-label">Asunto</label>
                                    <div class="col-sm-10">
                                    <input type="text" class="form-control">
                                    </div>
                                </div>
                                <div  class="form-group">
                                    <label class="col-sm-2 control-label">Mensaje</label>
                                    <div class="col-sm-10">
                                        <textarea class="form-control" style="max-width: 100%; min-width: 100%" rows="4"></textarea>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="col-md-12" >
                                      <button type="submit" class="btn btn-default btn-success" >ENVIAR MENSAJE</button>
                                    </div>
                                  </div>
                            </form>
                        </div>
                        <div class="col-md-6">
                            <div class="contact-l">
                                <div class="icon-contact"><i class="fa fa-map-marker"></i></div><div class="text-contact">Esquina Jr. Ancash con Jr. Tacna C-10</div>
                            </div>
                            <div class="contact-l">
                                <div class="icon-contact"><i class="fa fa-envelope-o"></i></div><div class="text-contact">sgacondicionamiento@regionmadrededios.gob.pe</div>
                            </div>
                            <div class="contact-l">
                                <div class="icon-contact"><i class="fa fa-phone"></i></div><div class="text-contact">082 564512</div>
                            </div>
                            <div class="contact-l">
                                <div class="icon-contact"><i class="fa fa-globe"></i></div><div class="text-contact">ide.regionmadrededios.gob.pe</div>
                            </div>
                        </div>
                    </div> 
                </div>                        
                <div class="col-md-1">     
                </div> 
            </div>                
        </div>
                    <br>
    <div>
        <div id="map"></div>
        
        <script>
      function initMap() {
        var uluru = {lat: -12.592975, lng: -69.186484};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 16,
          center: uluru
        });
        
        
        var contentString = '<div>'+           
            '<p><b>Infraestructura de Datos Espaciales (IDE) - Madre de Dios</b></p>'+          
            '<p style="text-align: center;">Esquina Jr. Ancash con Jr. Tacna C-10,<br>(Ref. al frente del Instituto de ingles - CBPNA)<br> Puerto Maldonado, Madre de Dios</p>'+
            '</div>';

        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });
        
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        
        infowindow.open(map, marker);
        
        
        
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCmWtrkyW9aEoKIDS0X8UNpRRxFjJj-1kA&callback=initMap">
    </script>
    </div>
 
</jsp:body>        
</tags:base>

