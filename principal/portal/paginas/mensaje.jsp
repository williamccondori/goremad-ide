<%-- 
    Document   : mensaje
    Created on : 22/01/2018, 12:31:48 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<% 
if(request.getParameter("error") != null) 
    out.println("<div class=\"alert alert-danger alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+request.getParameter("error")+"</div>");
else if(request.getParameter("success") != null)
    out.println("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+request.getParameter("success")+"</div>");
%> 

