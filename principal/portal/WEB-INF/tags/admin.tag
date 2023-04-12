<%-- 
    Document   : admin
    Created on : 22/01/2018, 11:30:29 AM
    Author     : Admin
--%>

<%@tag description="Pagina Admin" pageEncoding="UTF-8" %>
<%@attribute name="titulo" fragment="true" %>
<%@attribute name="estilos" fragment="true" %>
<%@attribute name="estilos_lib" fragment="true" %>
<%@attribute name="scripts" fragment="true" %>

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="${pageContext.request.contextPath}/img/favicon.png" />       
    <title>Panel Administrador - <jsp:invoke fragment="titulo"/></title>
    <!--ESTILOS REQUERISO -->
    <link href="${pageContext.request.contextPath}/librerias/bootstrap/css/bootstrap.min.css" rel="stylesheet">    
    <link href="${pageContext.request.contextPath}/librerias/sb_admin/metisMenu/metisMenu.min.css" rel="stylesheet">
    <jsp:invoke fragment="estilos_lib"/>
    <link href="${pageContext.request.contextPath}/librerias/sb_admin/css/sb-admin-2.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/librerias/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link href="${pageContext.request.contextPath}/css/admin.css" rel="stylesheet" type="text/css">
    <!--ESTILOS ADICIONALES -->
    <jsp:invoke fragment="estilos"/>

</head>
<body>    
    <div id="wrapper">
        <!-- Navigation -->
        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="${pageContext.request.contextPath}/" style="padding: 10px 15px;"><img src="${pageContext.request.contextPath}/img/favicon.png" style="display: inline-block;"> SRGT</a>
            </div>
            <!-- /.navbar-header -->
            <ul class="nav navbar-top-links navbar-right"> 
                <!-- /.dropdown -->
                <li class="dropdown" style="float: right">
                    <input id="current_empleado_id" type="hidden" value="<%                    
                                Cookie[] cookies= request.getCookies();
                                
                                if(cookies !=null)
                                {
                                  for(Cookie cookie : cookies)
                                  {
                                    if(cookie.getName().equals("empleado_id"))
                                        out.println(cookie.getValue());                                    
                                  }
                                }
                            %>">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#"><div style="display: inline-block;max-width: 200px;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;vertical-align: bottom;">
                        <i class="fa fa-user fa-fw"></i>    
                            <%  if(cookies !=null)
                                {
                                  for(Cookie cookie : cookies)
                                  {
                                    if(cookie.getName().equals("empleado_nombre"))
                                        out.println(cookie.getValue());                                    
                                  }
                                }  %>
                        </div>
                         <i class="fa fa-caret-down"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-user">
                        
                        <li><a href="${pageContext.request.contextPath}/validarlogin"><i class="fa fa-sign-out fa-fw"></i> Salir</a></li>
                    </ul>
                    <!-- /.dropdown-user -->
                </li>
                <!-- /.dropdown -->
            </ul>
            <!-- /.navbar-top-links -->

            <div class="navbar-default sidebar" role="navigation">
                <div class="sidebar-nav navbar-collapse">
                    <ul class="nav" id="side-menu">
                        <li>
                            <a href="${pageContext.request.contextPath}/admin" ><i class="fa fa-home"></i> Inicio</a>                            
                        </li> 
                        <%  if(cookies !=null)
                            {                            
                                int privi = 0;
                                for(Cookie cookie : cookies)
                                {
                                    if(cookie.getName().equals("empleado_privilegio"))
                                        privi = Integer.parseInt(cookie.getValue());                                  
                                }
                                
                                if(privi==2)
                                {
                                    out.println("<li><a href='"+request.getContextPath()+"/admin/post'><i class='fa fa-pencil-square-o'></i> Publicaciones</a></li>");   
                                }
                                
                                if(privi==3)
                                {
                                    out.println("<li><a href='"+request.getContextPath()+"/admin/servicios'><i class='fa fa-globe'></i> Servicios</a></li>");                                       
                                }
                            }  
                        %>                       
                    </ul>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
            <!-- /.navbar-static-side -->
        </nav>

        <!-- Page Content -->
        <div id="page-wrapper">
            <jsp:doBody/>            
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->
    <!--SCRIPTS NECESARIOS-->
    <script src="${pageContext.request.contextPath}/librerias/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/bootstrap/js/bootstrap.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/sb_admin/metisMenu/metisMenu.min.js"></script>
    <script src="${pageContext.request.contextPath}/librerias/sb_admin/js/sb-admin-2.js"></script>      
    <script src="${pageContext.request.contextPath}/js/admin.js"></script>    
    <!--SCRIPTS ADICIONALES-->    
    <jsp:invoke fragment="scripts"/>   
</body>
</html>