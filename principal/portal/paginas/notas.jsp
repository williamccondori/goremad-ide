<%-- 
    Document   : notas
    Created on : 18/01/2018, 03:49:23 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Notas</jsp:attribute>
    
<jsp:attribute name="estilos">
    <link href="${pageContext.request.contextPath}/librerias/datatables/css/dataTables.bootstrap.min.css" rel="stylesheet">
</jsp:attribute>
    
<jsp:attribute name="scripts">
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/jquery.dataTables.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/dataTables.bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/listar_notas.js"></script>
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
                                <table id="tabla-datos" class="table">
                                </table>
                            
                            <br>
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
                        <div style="display: inline-block;vertical-align: top;">
                            <div class="fb-share-button" data-href="http://ide.regionmadrededios.gob.pe/portal/notas" data-layout="button" data-size="large" data-mobile-iframe="true"><a class="fb-xfbml-parse-ignore" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fide.regionmadrededios.gob.pe%2Fportal%2Fnotas&amp;src=sdkpreparse">Compartir</a></div>
                        </div>
                        <div style="display: inline-block;vertical-align: top;">
                            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false" data-size="large">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                        </div>
                        <div style="display: inline-block;vertical-align: top;">
                            <div class="g-plus" data-action="share" data-annotation="none" data-height="28" data-href="http://ide.regionmadrededios.gob.pe/portal/notas"></div>
                        </div>
                                                                
                    </div>
                    <br>
                </div>
            </div>
                
        </div>
 
</jsp:body>        
</tags:base>

