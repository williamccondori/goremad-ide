<%-- 
    Document   : web
    Created on : 17-sep-2018, 7:51:33
    Author     : jose
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Servicios</jsp:attribute>
    
<jsp:attribute name="estilos">
    <link href="${pageContext.request.contextPath}/librerias/datatables/css/dataTables.bootstrap.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/servicios.css" rel="stylesheet">
</jsp:attribute>
    
<jsp:attribute name="scripts">
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/jquery.dataTables.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/datatables/js/dataTables.bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/listado.js"></script>   
</jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Servicios de Interoperabilidad</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/servicios.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Servicios</li>
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
                        El Gobierno Regional de Madre de Dios, por medio de Infraestructura de Datos Espaciales (IDE) de Madre de Dios, pone a disposición del público en general un listado de Servicios Web Geográficos producidos por la IDE.  
                    </p>
                </div>
                <div class="col-md-8">
                    <div class="titulo-cont">
                        <h3>Listado de Servicios Interoperables</h3>
                    </div> 
                    <div class="">
                        <ul class="nav nav-tabs" role="tablist">
                            <li class="active"><a data-toggle="tab" role="tab" href="#wms">Servicios WMS</a></li>
                            <li><a data-toggle="tab" role="tab" href="#wfs">Servicios WFS</a></li>  
                            <%-- <li><a data-toggle="tab" role="tab" href="#wcs">Servicios WCS</a></li>  --%>
                        </ul>
                        <div class="tab-content panel panel-default" style="border-top: 0;">
                            <div id="wms" class="tab-pane panel-body active">
                                <table class="table table-bordered table-striped">
                                    <thead>
                                        <tr>
                                            <th>Nombre del Servicio</th>                                   
                                            <th>Tema</th>
                                            <th></th>
                                        </tr>
                                    </thead>
                                    <tbody id="s_listado_wms">   
                                        <tr>
                                            <td colspan="3">Servicios en proceso</td>
                                        </tr>                                    
                                    </tbody>
                                </table>                               
                            </div>
                            <div id="wfs" class="tab-pane panel-body">
                                <table class="table table-bordered table-striped">
                                    <thead>
                                        <tr>
                                            <th>Nombre del Servicio</th>                                   
                                            <th>Tema</th>
                                            <th></th>
                                        </tr>
                                    </thead>
                                    <tbody id="s_listado_wfs">   
                                        <tr>
                                            <td colspan="3">Servicios en proceso</td>
                                        </tr>                                     
                                    </tbody>
                                </table>
                            </div>
                            <%-- <div id="wcs" class="tab-pane panel-body">
                                <table class="table table-bordered table-striped">
                                    <thead>
                                        <tr>
                                            <th>Nombre del Servicio</th>                                   
                                            <th>Tema</th>
                                            <th></th>
                                        </tr>
                                    </thead>
                                    <tbody id="s_listado_wcs">     
                                        <tr>
                                            <td colspan="3">Servicios en proceso</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div> --%>
                        </div>  
                    </div>
                </div>
                
            </div>
            <br>              
            <div id="elModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="s_nombre">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                            <h4 class="modal-title" id="s_nombre">-</h4>
                        </div>
                        <div class="modal-body">
                            <label><b id="s_tipo">-</b></label>
                            <div class="input-group servicios">
                                <input id="s_url" type="text" class="form-control" value="-" readonly>
                                <span class="input-group-btn">
                                  <button class="btn btn-default" type="button" onclick="Copiar(this)">Copiar</button>
                                </span>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-danger" data-dismiss="modal">Cerrar</button>
                        </div>                        
                    </div><!-- /.modal-content -->
                </div><!-- /.modal-dialog -->
            </div><!-- /.modal -->      
        </div>
 
</jsp:body>        
</tags:base>
