var tabla;

$(document).ready(function () {
    tabla = $('#publicaciones').dataTable({
        "ajax": {
            "url": RutaBase + "/info/noticias.json",
            "type": "GET"
        }, 
        processing: true,
        "columns": [  
            { "data": "usuario"},
            { "data": "fecha"},   
            { "data": "categoria"},             
            { "data": "titulo"}, 
            { "mData": "estado", "sClass": "celda", "bSearchable": false, "width":"50px", "bSortable": false, "mRender": function ( data, type, full ) 
                { 
                    if(full.estado)
                        return "<button class='btn btn-success btn-sm' type='button' onclick='Estado("+full.id+", false);'><i class='fa fa-eye'></i></button> ";
                    else
                        return "<button class='btn btn-danger btn-sm' type='button' onclick='Estado("+full.id+", true);'><i class='fa fa-eye-slash'></i></button> ";
                    
                }           
            },
            { "mData": "id", "sClass": "celda", "bSearchable": false, "width":"70px", "bSortable": false, "mRender": function ( data, type, full ) 
                { 
                    return '<div class="btn-group" role="group" aria-label="...">'+                                
                                '<a href="'+RutaBase+'/admin/post/modificar?id='+full.id+'" class="btn btn-primary btn-sm"><i class="fa fa-pencil"></i></a>'+
                                '<button type="button" class="btn btn-danger btn-sm" onclick="Eliminar('+full.id+');"><i class="fa fa-times"></i></button>'+
                            '</div>';
                    
                }           
            }      
        ],
        "order": [],
        "oLanguage":  
        {
            "sLengthMenu": "_MENU_ &nbsp;Registros",
            "sInfo": "Mostrando  <strong>_START_</strong> a <strong>_END_</strong> de <strong>_TOTAL_</strong>",
            "sSearch": "Buscar&nbsp;:",
            "sEmptyTable": "No Existen Datos",
            "sInfoEmpty": "Mostrando 0 datos",
            "sProcessing": "Cargando datos...",
            "sZeroRecords": "No se encontraron registros",
            "oPaginate": {
                "sFirst": "Inicio",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": "Final"
            }
        }
    });    
});

function Estado(ide, nuevo)
{
    //$("#cargando").show();
    $.ajax({
        url : RutaBase+"/estadopost",
        type : 'GET',
        data : {
            'id' : ide,
            'estado': nuevo
        },            
        dataType:'json',
        success : function(data) { 
                              
            tabla.dataTable().api().ajax.reload();                 

            //$("#cargando").hide();
            
        },
        error : function(request,error)
        {
            //errorAlert(request.responseText);
            //$("#cargando").hide();
        }
    }); 
}

function Eliminar(ide)
{
    if(confirm("Esta seguro que desea eliminar?"))
    {
        $.ajax({
            url : RutaBase+"/estadopost",
            type : 'POST',
            data : {
                'id' : ide
            },            
            dataType:'json',
            success : function(data) { 

                tabla.dataTable().api().ajax.reload();                 

                //$("#cargando").hide();

            },
            error : function(request,error)
            {
                //errorAlert(request.responseText);
                //$("#cargando").hide();
            }
        }); 
    }
}