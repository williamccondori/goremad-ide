<%-- 
    Document   : nota
    Created on : 26/01/2018, 05:09:11 PM
    Author     : Admin
--%>

<%@page import="DATOS.Post"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

<%      
    request.setCharacterEncoding("UTF-8");
    String id = request.getParameter("id");
    String imagen="";
    Post oPost=new Post();
    Post encontrado = oPost.obtener(Integer.parseInt(id));
    if(encontrado.getImagen()!=null)
        imagen=request.getContextPath()+"/files/"+encontrado.getImagen();
    else
        imagen=request.getContextPath()+"/img/no-picture.png";
            
    
    request.setAttribute("noticia", encontrado);  
    request.setAttribute("imagen", imagen);  
%> 

<tags:base>
<jsp:attribute name="titulo">Nota</jsp:attribute>
    
<jsp:attribute name="estilos"></jsp:attribute>
    
<jsp:attribute name="scripts"></jsp:attribute>  
    
<jsp:body> 
    <div class="header-inf">  
        <div class="espaciador">
            <h2>Noticias y Actividades</h2>
        </div>        
        <img src="${pageContext.request.contextPath}/img/notas.jpg"></img>
        <div class="ruta">
            <div class="ruta-aux">
                <ol class="breadcrumb">
                    <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                    <li class="active">Noticias y Actividades</li>
                  </ol>
            </div>
        </div>
    </div>
        <div class="container">            
            <div class="row">
                <div class="col-md-8">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="titulo-cont">
                                <h3>Noticias y Actividades</h3>
                            </div>        
                        </div>                    
                    </div>
                    <div>
                        <div class="noticia-item">
                            <div class="n-sup">
                                <div class="n-fecha">
                                    <div class="n-f-left">
                                        ${noticia.getFechaf()}
                                    </div>
                                    <div class="n-f-center"></div>
                                    <div class="n-f-right">
                                        ${noticia.getId()}
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="n-img" style="margin-bottom: 15px;">
                                        <img src="${imagen}" alt="">
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="n-cont">
                                        <h4>${noticia.getTitulo()}</h4>
                                        <p>${noticia.getContenido()}</p>
                                    </div>
                                    <div class="n-foot">                                        
                                        <br>
                                    </div>
                                </div>
                            </div> 
                        </div>                                                
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="titulo-cont">
                        <h3>Detalles</h3>
                    </div>    
                    <div>                        
                        <p style="text-align: justify">
                            La <b>IDE</b> de Madre de Dios realiza diversas actividades para dar a conocer acerca de la Getión Territorial y promover el uso de herramientas de información geográfica, que proporcionen información oportuna para la toma de decisiones.
                        </p>        
                        
                        <h4>Compartir</h4>                                                   
                        <div style="display: inline-block;vertical-align: top;">
                            <div class="fb-share-button" data-href="http://ide.regionmadrededios.gob.pe/portal/nota?id=${noticia.getId()}" data-layout="button" data-size="large" data-mobile-iframe="true"><a class="fb-xfbml-parse-ignore" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fide.regionmadrededios.gob.pe%2Fportal%2Fnota%3Fid%3D${noticia.getId()}&amp;src=sdkpreparse">Compartir</a></div>
                        </div>
                        <div style="display: inline-block;vertical-align: top;">
                            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false" data-size="large">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
                        </div>
                        <div style="display: inline-block;vertical-align: top;">
                            <div class="g-plus" data-action="share" data-annotation="none" data-height="28" data-href="http://ide.regionmadrededios.gob.pe/portal/nota?id=${noticia.getId()}"></div>
                        </div>
                                                                
                    </div>  
                    <br>
                </div>
            </div>
                
        </div>
 
</jsp:body>        
</tags:base>


