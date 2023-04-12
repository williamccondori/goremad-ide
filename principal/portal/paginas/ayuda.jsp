<%-- 
    Document   : ayuda
    Created on : 18/01/2018, 04:34:43 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Ayuda</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Documentación de Ayuda</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/ayuda.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Ayuda</li>
                  </ol>
            </div>
        </div>
    </div>
        <div class="container">            
            <div class="row">
                <div class="col-md-2">
                    
                </div>
                <div class="col-md-8">
                    <h1 style="font-weight: bold; text-align: center;">EN CONSTRUCCIÓN</h1>
                    <p style="text-align: center;">Estamos trabajando para tener listo el sitio web pronto.</p>
                    <img src="${pageContext.request.contextPath}/img/construccion.png" style="width: 90%;"></img>
                    
                </div>
                <div class="col-md-2">
                    
                </div>
            </div>
                    <br>
        </div>
 
</jsp:body>        
</tags:base>

