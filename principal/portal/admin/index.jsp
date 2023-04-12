<%-- 
    Document   : index
    Created on : 05-nov-2018, 8:51:33
    Author     : jose
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" %>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>
    
<tags:admin>
    <jsp:attribute name="titulo">
     Panel de Administración
    </jsp:attribute>
     <jsp:attribute name="estilos">        
    </jsp:attribute>
    <jsp:attribute name="estilos_lib">        
    </jsp:attribute>
    <jsp:attribute name="scripts">        
    </jsp:attribute>
    <jsp:body>         
        <div class="row">
            <div class="col-lg-12">
                <div class="container-fluid">
                    <div class="jumbotron" style="margin-top: 30px;">
                        <h1>Panel de Administración</h1>
                        <p>Seleccione una opción del menú lateral para empezar.</p>
                    </div>                
                </div>
            </div>         
        </div>
    </jsp:body>        
</tags:admin>
