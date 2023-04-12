<%-- 
    Document   : posts
    Created on : 22/01/2018, 11:39:15 AM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" %>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>
    
<% 
    
    Cookie[] cookies= request.getCookies();
    int privi = 0;
    
    if(cookies !=null)
    {                      
        for(Cookie cookie : cookies)
        {
            if(cookie.getName().equals("empleado_privilegio"))
                privi = Integer.parseInt(cookie.getValue());                                  
        }
    }
    
    if(privi!=2)
        response.sendRedirect(request.getContextPath()+"/admin");
                     
%>

<tags:admin>
    <jsp:attribute name="titulo">
     Publicaciones
    </jsp:attribute>
     <jsp:attribute name="estilos">        
    </jsp:attribute>
    <jsp:attribute name="estilos_lib">        
        <link href="${pageContext.request.contextPath}/librerias/datatables/css/dataTables.bootstrap.min.css" rel="stylesheet">
    </jsp:attribute>
    <jsp:attribute name="scripts">
        <script src="${pageContext.request.contextPath}/librerias/datatables/js/jquery.dataTables.min.js"></script>
        <script src="${pageContext.request.contextPath}/librerias/datatables/js/dataTables.bootstrap.min.js"></script>
        <script src="${pageContext.request.contextPath}/js/listar_post.js"></script>
    </jsp:attribute>
    <jsp:body> 
        <div class="row">
            <div class="col-lg-12">
                <h2 class="page-header">Publicaciones</h2>
            </div>
        </div>          
        <div class="row">            
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <b>Litado</b>
                        <div class="button-heading"><a href="${pageContext.request.contextPath}/admin/post/nuevo" class="btn btn-primary btn-sm">NUEVO</a></div>
                    </div> 
                    <div class="panel-body">
                        <div class="table-responsive">
                            <table id="publicaciones" class="table table-bordered table-striped">
                                <thead>
                                    <tr>
                                        <th>Usuario</th>
                                        <th>Fecha</th>
                                        <th>Categoria</th>
                                        <th>Titulo</th>
                                        <th>Estado</th>
                                        <th></th>
                                    </tr>
                                </thead>

                            </table>
                        </div>
                    </div>                        
                </div>            
            </div> 
        </div>
    </jsp:body>        
</tags:admin>