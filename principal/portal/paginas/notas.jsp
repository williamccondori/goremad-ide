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
                        <!-- Facebook -->
                        <a href="http://www.facebook.com/sharer.php?u=https://ide.regionmadrededios.gob.pe/noticias" id="facebook">
                            <i class="fa fa-facebook-official" style="font-size: 30px; color: #3b5998;"></i>
                        </a>
                        <br />
                        <!-- Twitter -->
                        <a href="https://twitter.com/share?url=https://ide.regionmadrededios.gob.pe/noticias" id="twitter">
                            <i class="fa fa-twitter-square" style="font-size: 30px; color: #00aced;"></i>
                        </a>
                        <br>
                    </div>
                </div>
            </div>
                
        </div>
 
</jsp:body>        
</tags:base>

