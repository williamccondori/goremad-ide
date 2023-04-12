$(document).ready(function () {
     
    $("#s_listado_wms").html("");
    for (var i = 0; i < servicios_wms.length; i++) {
        $("#s_listado_wms").append(
            '<tr>'+
                '<td>'+servicios_wms[i].nombre+'</td>'+
                '<td>'+servicios_wms[i].tema+'</td>'+
                '<td class="tabla-boton"><button class="btn btn-sm btn-primary" onclick="Mostrar('+i+',\'WMS\');">Ver</button></td>'+
            '</tr>');
    }  
    
    $("#s_listado_wfs").html("");
    for (var i = 0; i < servicios_wfs.length; i++) {
        $("#s_listado_wfs").append(
            '<tr>'+
                '<td>'+servicios_wfs[i].nombre+'</td>'+
                '<td>'+servicios_wfs[i].tema+'</td>'+
                '<td class="tabla-boton"><button class="btn btn-sm btn-primary" onclick="Mostrar('+i+',\'WFS\');">Ver</button></td>'+
            '</tr>');
    } 
    
    /*$("#s_listado_wcs").html("");
    for (var i = 0; i < servicios_wcs.length; i++) {
        $("#s_listado_wcs").append(
            '<tr>'+
                '<td>'+servicios_wcs[i].nombre+'</td>'+
                '<td>'+servicios_wcs[i].tema+'</td>'+
                '<td class="tabla-boton"><button class="btn btn-sm btn-primary" onclick="Mostrar('+i+',\'WCS\');">Ver</button></td>'+
            '</tr>');
    }*/
});

function Mostrar(indice, servicio)
{
    var serv_temp = null;
    
    if(servicio=="WMS")
        var serv_temp = servicios_wms;
    else if(servicio=="WFS")
        var serv_temp = servicios_wfs;   
    else if(servicio=="WCS")
        var serv_temp = servicios_wcs;   
    
    if(serv_temp != null)
    {
        $("#s_nombre").html(serv_temp[indice].nombre);
        $("#s_tipo").html("Servicio "+servicio);
        $("#s_url").val(serv_temp[indice].url);
        $("#elModal").modal("show");
    }  
}

function Copiar(boton)
{
    var clase = $(boton).closest(".servicios" );
    var input = clase.find("input")[0];
    input.select();
    document.execCommand("copy");    
}
