<%-- 
    Document   : mapas
    Created on : 29/01/2018, 02:17:04 PM
    Author     : Admin
--%>


<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Mapas</jsp:attribute>
    
<jsp:attribute name="estilos">
    <link href="${pageContext.request.contextPath}/librerias/datatables/css/dataTables.bootstrap.min.css" rel="stylesheet">
</jsp:attribute>
    
<jsp:attribute name="scripts">
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/jquery.dataTables.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/dataTables.bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/listar_mapas.js"></script>
</jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Servicio de Mapas</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/mapas.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Mapas</li>
                  </ol>
            </div>
        </div>
    </div>
        <div class="container"> 
            <div class="row">
                <div class="col-md-4">
                    <div class="titulo-cont">
                        <h3>Detalles</h3>
                    </div> 
                    <p class="justificar">
                        El Gobierno Regional de Madre de Dios, por medio de Infraestructura de Datos Espaciales (IDE) de Madre de Dios, pone a disposición del público en general un catálogo de mapas geográficos producidos por el IDE.  
                    </p>
                </div>
                <div class="col-md-8">
                    <div class="titulo-cont">
                        <h3>Catálogo de Mapas</h3>
                    </div> 
                    <div class="table-responsive">
                        <table id="tabla-datos" class="table">
                            
                        </table>
                    </div>
                </div>
                
            </div>
            <br>
        </div>
 
</jsp:body>        
</tags:base>
