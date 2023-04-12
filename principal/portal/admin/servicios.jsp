<%-- 
    Document   : servicios
    Created on : 05-nov-2018, 9:19:11
    Author     : jose
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
    
    if(privi!=3)
        response.sendRedirect(request.getContextPath()+"/admin");
                     
%>

<tags:admin>
    <jsp:attribute name="titulo">
     Publicaciones
    </jsp:attribute>
     <jsp:attribute name="estilos">        
    </jsp:attribute>
    <jsp:attribute name="estilos_lib">                
    </jsp:attribute>
    <jsp:attribute name="scripts">
        <script src="${pageContext.request.contextPath}/js/Servicios_GeoServer.js"></script>
        <script src="${pageContext.request.contextPath}/js/listar_servicios.js"></script>
    </jsp:attribute>
    <jsp:body> 
        <div class="row">
            <div class="col-lg-12">
                <h2 class="page-header">Servicios Adicionales</h2>
            </div>
        </div>          
        <div class="row">            
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <b>Servicios</b>
                    </div> 
                    <div class="panel-body">
                        
                        <ul class="nav nav-tabs">
                            <li class="active"><a href="#wms" data-toggle="tab" aria-expanded="true">WMS</a>
                            </li>
                            <li><a href="#wfs" data-toggle="tab" aria-expanded="false">WFS</a>
                            </li>
                            <li><a href="#wcs" data-toggle="tab">WCS</a>
                            </li>
                        </ul>
                        
                        <div class="tab-content">
                            <div class="tab-pane fade active in" id="wms">
                                <br>
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered table-hover">
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
                            </div>
                            <div class="tab-pane fade" id="wfs">
                                
                                <br>
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered table-hover">
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
                                
                            </div>
                            <div class="tab-pane fade" id="wcs">
                                
                                <br>
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered table-hover">
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
                                </div>
                                
                            </div>                            
                        </div>
                        
                    </div>                        
                </div>            
            </div> 
        </div>
        
        
        <div id="elModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="s_nombre">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                        <h4 class="modal-title" id="s_nombre">-</h4>
                    </div>
                    <div class="modal-body">
                        <label><b id="s_tipo">-</b></label>
                        <div class="input-group servicios">
                            <input id="s_url" type="text" class="form-control" value="-" readonly="">
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
        </div>
    </jsp:body>        
</tags:admin>
