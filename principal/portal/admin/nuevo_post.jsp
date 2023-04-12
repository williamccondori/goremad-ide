<%-- 
    Document   : nuevo_post
    Created on : 22/01/2018, 05:22:43 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="DATOS.Categoria_post, java.util.List"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>
          
<% 
 Categoria_post categorias=new Categoria_post();
 String tex1 ="";
 for (Categoria_post elem : categorias.listar()) {        
    tex1+="<option value='"+elem.getId()+"'>"+elem.getNombre()+"</option>";
 }
 request.setAttribute("categorias", tex1);
%>
    
<tags:admin>
    <jsp:attribute name="titulo">
    Nueva Publicación
    </jsp:attribute>
    <jsp:attribute name="estilos">  
        <link href="${pageContext.request.contextPath}/librerias/bootstrap-datepicker/css/bootstrap-datepicker3.min.css" rel="stylesheet">
        <link href="${pageContext.request.contextPath}/librerias/summernote/summernote.css" rel="stylesheet">
    </jsp:attribute>
    <jsp:attribute name="scripts">
        <script src="${pageContext.request.contextPath}/librerias/bootstrap-datepicker/js/bootstrap-datepicker.min.js"></script>
        <script src="${pageContext.request.contextPath}/librerias/bootstrap-datepicker/locales/bootstrap-datepicker.es.min.js"></script>
        
        <script src="${pageContext.request.contextPath}/librerias/summernote/summernote.js"></script>
        <script src="${pageContext.request.contextPath}/js/nuevo_post.js"></script>
    </jsp:attribute>
    <jsp:body> 
        <div class="row">
            <div class="col-lg-12">
                <h2 class="page-header">Nueva Publicación</h2>
            </div>
        </div>          
        <div class="row">  
            <form id="formulario" enctype="multipart/form-data" action="${pageContext.request.contextPath}/publicar" method="POST">
            <div class="col-md-8">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <b>Datos</b>                        
                    </div>
                    <div class="panel-body"> 
                        <jsp:include page="/paginas/mensaje.jsp"></jsp:include>             
                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group required">
                                    <label class="control-label" for="fecha">Fecha</label>
                                    <div class="input-group date" id="fecha">
                                        <input type="text" class="form-control validar_texto" name="fecha">
                                        <span class="input-group-addon"><i class="glyphicon glyphicon-th"></i></span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-8">
                                <div class="form-group">
                                    <label class="control-label" for="categoria">Categoria</label>
                                    <select class="form-control" name="categoria">
                                        ${categorias}
                                    </select>
                                </div>
                            </div>
                        </div>                        
                        <div class="form-group required">
                            <label class="control-label" for="titulo">Titulo</label>
                            <input type="text" class="form-control validar_texto" id="titulo" name="titulo" placeholder="">
                        </div>
                        <div class="form-group required">
                            <label class="control-label" for="resumen">Resumen</label>
                            <textarea class="form-control validar_texto" id="resumen" name="resumen" ></textarea>
                        </div>
                        <div class="form-group required">
                            <label class="control-label" for="contenido">Contenido</label>
                            <textarea class="form-control validar_texto" id="contenido" name="contenido" ></textarea>
                        </div>
                        <div>
                            <button type="submit" class="btn btn-success" >Cuardar</button>
                            <a href="${pageContext.request.contextPath}/admin/post" class="btn btn-danger">Cancelar</a>
                        </div>
                    </div>
                </div>            
            </div> 
            <div class="col-md-4">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <b>Imagen</b>                        
                    </div>
                    <div class="panel-body">  
                        <img id="image-template-aux" src="${pageContext.request.contextPath}/img/no-picture.png" style="display: none;">
                        <div class="img-aux">
                            <img id="image-template"  src="${pageContext.request.contextPath}/img/no-picture.png">
                        </div>
                        <div class="file-aux">
                            <input id="updload-image-template" type="file" name="image-upload" >
                        </div>
                    </div>
                </div>
            </div>
            </form>
        </div>
    </jsp:body>        
</tags:admin>