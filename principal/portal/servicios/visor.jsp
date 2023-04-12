<%-- 
    Document   : visor
    Created on : 29/01/2018, 02:12:55 PM
    Author     : Admin
--%>


<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:visor>
<jsp:attribute name="titulo">Visor</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body>   
    
<div class="contenedor-principal">
        <div id="map"></div>
        
</div>
<div class="datos-principal" style="display: none;">

    asdasdasdas
</div>
    
<div class="controles">
    <div class="c-menu">
        <ul>
            <li>
                <a href="${pageContext.request.contextPath}/">
                    <div class="m-boton-big">
                        <img src="${pageContext.request.contextPath}/img/gore.png">
                    </div>
                </a>
            </li> 
            <li><a href="javascript:capas();" title="Lista de Capas"><div class="m-boton bl"><i class="fa fa-object-ungroup"></i></div></a></li>
            <li><a href="javascript:mapas();" title="Mapas Base"><div class="m-boton bl"><i class="fa fa-map"></i></div></a></li>
            <li><a href="javascript:leyendas();" title="Leyendas"><div class="m-boton bl"><i class="fa fa-tag"></i></div></a></li> 
            <li><a href="javascript:imprimir();" title="Imprimir"><div class="m-boton wi"><i class="fa fa-print"></i></div></a></li>             
        </ul>        
    </div>
    
    <div class="c-buscador">
        <div class="input-group">
            <span class="input-group-btn">
              <button class="btn btn-default" type="button">Go!</button>
            </span>
            <input type="text" class="form-control" placeholder="Buscar...">
        </div>
    </div>
    
    <div class="c-botones" >
        <ul>
            <li><a href="javascript:home();"><div class="c-boton"><i class="fa fa-home"></i></div></a></li>                     
        </ul>
        <ul>
            <li><a href="javascript:zoomIn();"><div class="c-boton"><i class="fa fa-plus"></i></div></a></li>
            <li><a href="javascript:zoomOut();"><div class="c-boton"><i class="fa fa-minus"></i></div></a></li>                       
        </ul>        
    </div>
                    
    <div class="c-ventanas">
        <div id="v-leyendas" class="mgDialog">
            <div class="mgDialog_header mgDialog_align_left"><div data-role="title" class="mgDialog_title">Leyendas</div><i class="mgDialog_cross" data-role="btn:cancel,close">×</i></div>
            <div data-role="content" class="mgDialog_content">
              Panel content
            </div>
        </div>
        
        <div id="v-capas" class="mgDialog">
            <div class="mgDialog_header mgDialog_align_left"><div data-role="title" class="mgDialog_title">Lista de Capas</div><i class="mgDialog_cross" data-role="btn:cancel,close">×</i></div>
            <div data-role="content" class="mgDialog_content">
                <div class="loading-v">
                    <div class="aux-center">
                    <div class="load-aux"><i class="fa fa-cog fa-spin"></i></div>
                    </div>
                </div>
                Panel content
            </div>
        </div>
        
        <!--SELECCIONAR MAPA BASE-->   
        <div id="v-mapas" class="mgDialog">
            <div class="mgDialog_header mgDialog_align_left"><div data-role="title" class="mgDialog_title">Mapas Base</div><i class="mgDialog_cross" data-role="btn:cancel,close">×</i></div>
            <div data-role="content" class="mgDialog_content">
                <div class="lista-boxes">
                    <a href="javascript:cambiarBase(0);">
                        <div class="item-boxes activo" data-ind="0">
                            <img src="${pageContext.request.contextPath}/img/m-calle.jpg" alt="---">
                            <p>Calles</p>
                        </div>
                    </a>
                    <a href="javascript:cambiarBase(1);">
                        <div class="item-boxes" data-ind="1">
                            <img src="${pageContext.request.contextPath}/img/m-aereo.jpg" alt="---">
                            <p>Imágen aereo</p>
                        </div>
                    </a>
                </div>
                <div class="lista-boxes">
                    <a href="javascript:cambiarBase(2);">
                        <div class="item-boxes" data-ind="2">
                            <img src="${pageContext.request.contextPath}/img/m-aereo-etiquetas.jpg" alt="---">
                            <p>Imágen aereo con etiquetas</p>
                        </div>
                    </a>
                    <a href="javascript:cambiarBase(3);">
                        <div class="item-boxes" data-ind="3">
                            <img src="${pageContext.request.contextPath}/img/m-terreno.jpg" alt="---">
                            <p>Terreno</p>
                        </div>
                    </a>
                </div>
                <div class="lista-boxes">
                    <a href="javascript:cambiarBase(4);">
                        <div class="item-boxes" data-ind="4">
                            <img src="${pageContext.request.contextPath}/img/m-toner.jpg" alt="---">
                            <p>Toner</p>
                        </div>
                    </a>
                    <a href="javascript:cambiarBase(5);" >
                        <div class="item-boxes" data-ind="5">
                            <img src="${pageContext.request.contextPath}/img/m-topo.jpg" alt="---">
                            <p>Topográfico</p>
                        </div>
                    </a>
                </div> 
            </div>
        </div>
        <!--IMPRIMIR-->                    
        <div id="v-imprimir" class="mgDialog">
            <div class="mgDialog_header mgDialog_align_left"><div data-role="title" class="mgDialog_title">Imprimir</div><i class="mgDialog_cross" data-role="btn:cancel,close">×</i></div>
            <div data-role="content" class="mgDialog_content">
                <div class="form-group">
                    <label>Resolución</label>
                    <select id="resolution" class="form-control">
                        <option value="72">72 dpi (fast)</option>
                        <option value="150">150 dpi</option>
                        <option value="300">300 dpi (slow)</option>
                    </select>
                </div>
                <button id="export-pdf" class="btn btn-primary">Export PDF</button>
            </div>
        </div>
        
    </div>
</div>
    
    
    
    
    <div id="popup" class="ol-popup">
        asdadadasdasdasd
      <a href="#" id="popup-closer" class="ol-popup-closer"></a>
      <div id="popup-content">s</div>
    </div>
 
</jsp:body>        
</tags:visor>
