<%-- Document: quienes Created on: 18/01/2018, 10:21:11 AM Author: Admin --%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nosotros</title>
    <%@page contentType="text/html" pageEncoding="UTF-8" %>
    <%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>
</head>
<body>
    <tags:base>
        <jsp:attribute name="titulo">Nosotros</jsp:attribute>
        <jsp:attribute name="estilos"></jsp:attribute>
        <jsp:attribute name="scripts"></jsp:attribute>

        <jsp:body>
            <div class="header-inf">
                <div class="espaciador">
                    <h2>¿Quiénes somos?</h2>
                </div>
                <img src="${pageContext.request.contextPath}/img/nosotros.jpg" alt="Nosotros"></img>
                <div class="ruta">
                    <div class="ruta-aux">
                        <ol class="breadcrumb">
                            <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                            <li class="active">¿Quiénes somos?</li>
                        </ol>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <img src="${pageContext.request.contextPath}/img/logo-principal.png" style="max-width: 300px; display: table; margin-left: auto; margin-right: auto;">
                        <br>
                        <div class="titulo-cont">
                            <h3>DEFINICIÓN DEL SISTEMA REGIONAL DE GESTIÓN TERRITORIAL</h3>
                        </div>
                        <p class="justificar">
                            El Sistema Regional de Gestión Territorial busca recopilar la información geográfica que se genera en el departamento de Madre de Dios para usarlas como insumo para la generación de herramientas de gestión para el monitoreo eficiente del territorio de Madre de Dios.
                        </p>
                        <p class="justificar">El Sistema Regional de Gestión Territorial está definido con un sistema integrado y coordinado de personas, equipos y procedimientos que transforman los datos geográficos del departamento de Madre de Dios en información útil que permita llevar de manera más eficiente actividades del Gobierno Regional Madre de Dios tales como operaciones, administración y toma de decisiones.</p>
                        <p class="justificar">El Sistema Regional de Gestión Territorial plantea brindar herramientas de planificación del territorio debidamente aprobados por las entidades competentes, e implementar instrumentos normativos-cartográficos para el eficiente monitoreo, reporte y verificación del territorio de Madre de Dios.</p>
                    </div>
                </div>
                <br>
                <br>
            </div>
        </jsp:body>
    </tags:base>
</body>
</html>
