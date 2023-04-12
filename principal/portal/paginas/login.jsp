<%-- 
    Document   : login
    Created on : 22/01/2018, 11:05:03 AM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<tags:base>
<jsp:attribute name="titulo">Login</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Login</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/login.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Login</li>
                  </ol>
            </div>
        </div>
    </div>
        <div class="container">            
            <div class="row">
                <div class="col-md-4">
                    
                </div>
                <div class="col-md-4" style="margin: 60px 0 100px 0">
                    <form id="formulario" role="form" action="${pageContext.request.contextPath}/validarlogin" method="POST">
                    <div class="panel panel-default">
                        <div class="panel-heading">Inicio de sesión</div>
                        <div class="panel-body">
                            <div class="form-group">
                                <div class="input-group">
                                    <span class="input-group-addon"><i class="fa fa-user"></i></span>
                                    <input type="text" class="form-control" id="nombre" name="usuario" placeholder="Nombre" autofocus required>                                
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <span class="input-group-addon"><i class="fa fa-lock"></i></span>
                                    <input type="password" class="form-control" id="password" name="password" placeholder="Contraseña" required>                                
                                </div>
                            </div>
                            <div style="display: table; width: 100%">
                                <div style="display: table-cell;vertical-align: middle;">
                                    <div class="checkbox">
                                        <label>
                                          <input id="remember" name="remember" type="checkbox"> Recordarme
                                        </label>
                                    </div>                                    
                                </div>
                                <div style="display: table-cell; vertical-align: middle; text-align: right;">
                                    <button type="submit" class="btn btn-primary">Ingresar</button>             
                                </div>
                            </div>    
                        </div>
                    </div> 
                    </form>
                    
                    <jsp:include page="/paginas/mensaje.jsp"></jsp:include>                    
                </div>
                <div class="col-md-4">
                    
                </div>
            </div>
                
        </div>
 
</jsp:body>        
</tags:base>
