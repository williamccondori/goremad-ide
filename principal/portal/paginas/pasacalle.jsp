<%@page contentType="text/html" pageEncoding="UTF-8" %>
<%@taglib prefix="tags" tagdir="/WEB-INF/tags" %>

        <tags:base>
            <jsp:attribute name="titulo">🎊 Pasacalle 2023</jsp:attribute>
            <jsp:attribute name="estilos"></jsp:attribute>
            <jsp:attribute name="scripts"></jsp:attribute>
            <jsp:body>
                <div class="header-inf">
                    <div class="espaciador">
                        <h2>🎊 Pasacalle 2023</h2>
                    </div>
                    <img src="${pageContext.request.contextPath}/img/notas.jpg"></img>
                    <div class="ruta">
                        <div class="ruta-aux">
                            <ol class="breadcrumb">
                                <li><a href="${pageContext.request.contextPath}/">Inicio</a></li>
                                <li class="active">🎊 Pasacalle 2023</li>
                            </ol>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <h3>📑 Documentos:</h3>
                        </div>
                        <div class="col-md-12">
                            <div class="col-md-4 col-xl-4">
                                <a href="${pageContext.request.contextPath}/files/bases.docx" target="_blank"
                                    class="btn btn-info">DESCARGAR BASES</a>
                            </div>
                            <div class="col-md-4 col-xl-4">
                                <a href="${pageContext.request.contextPath}/files/anexo.pdf" target="_blank"
                                    class="btn btn-info">DESCARGAR FICHA PDF</a>
                            </div>
                            <div class="col-md-4 col-xl-4">
                                <a href="${pageContext.request.contextPath}/files/anexo.docx" target="_blank"
                                    class="btn btn-info">DESCARGAR FICHA WORD</a>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <h3>🚍 Recorrido de carros alegóricos:</h3>
                        </div>
                        <div class="col-md-12 col-xl-12" style="margin-bottom: 4rem">
                            <img src="${pageContext.request.contextPath}/img/recorrido.png" alt="recorrido"
                                style="width: 100%;">
                        </div>
                        <br>
                    </div>
                </div>
            </jsp:body>
        </tags:base>