<%-- 
    Document   : visor
    Created on : 02/02/2018, 07:26:05 AM
    Author     : Admin
--%>


<%@tag description="Visor Geoportal" pageEncoding="UTF-8"%>
<%@attribute name="titulo" fragment="true" %>
<%@attribute name="estilos" fragment="true" %>
<%@attribute name="scripts" fragment="true" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" type="image/png" href="${pageContext.request.contextPath}/img/favicon.png" />
    <title>Infraestructura de Datos Espaciales - <jsp:invoke fragment="titulo"/></title>

    <link href="${pageContext.request.contextPath}/librerias/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/openLayers/ol.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/mgDialog/mgDialog.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/visor.css" rel="stylesheet">
    <jsp:invoke fragment="estilos"/>
</head>
<body>
    <jsp:doBody/>  

    <script src="${pageContext.request.contextPath}/librerias/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/bootstrap/js/bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/openLayers/ol.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/proj4js/proj4.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/mgDialog/mgDialog.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.5/jspdf.debug.js"></script>
    <script src="${pageContext.request.contextPath}/js/visor.js"></script>
    <jsp:invoke fragment="scripts"/>   
</body>
</html>
