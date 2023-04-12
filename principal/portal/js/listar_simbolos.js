var tabla;

$(document).ready(function () {
           
    tabla = $('#tabla-datos').dataTable({
        "ajax": {
            "url": RutaBase + "/listarpost?id=5",
            "type": "GET"
        }, 
        processing: true,
        "columns": [  
            { "mData": "id", "sClass": "listado-datos", "bSortable": false, "mRender": function ( data, type, full ) 
                { 
                    return '<div class="media">'+
                            '<div class="media-left">'+(full.imagen!=null?'<a href="'+RutaBase+'/files/'+full.imagen+'" download> <img alt="64" class="media-object" style="width: 64px;" src="'+RutaBase+'/img/file.png" data-holder-rendered="true"> </a>':'<a> <img alt="64" class="media-object" style="width: 64px;" src="'+RutaBase+'/img/file-n.png" data-holder-rendered="true"> </a> ')+'</div> '+
                            '<div class="media-body" style="text-align: justify;"><h4 class="media-heading">'+full.titulo+'</h4> '+full.resumen+'<br><span class="text-muted">Fecha: '+full.fecha+'</span></div>'+
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