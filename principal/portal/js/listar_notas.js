var tabla;

$(document).ready(function () {
           
    tabla = $('#tabla-datos').dataTable({
        "ajax": {
            "url": RutaBase + "/listarpost?id=1",
            "type": "GET"
        }, 
        processing: true,
        "columns": [  
            { "mData": "id", "sClass": "listado-datos", "bSortable": false, "mRender": function ( data, type, full ) 
                { 
                    return '<div class="noticia-item">'+
                            '<div class="n-sup">'+
                                '<div class="n-fecha">'+
                                    '<div class="n-f-left">'+full.fecha+'</div>'+
                                    '<div class="n-f-center"></div>'+
                                    '<div class="n-f-right">'+full.id+'</div>'+
                                '</div>'+
                            '</div>'+
                            '<div class="row">'+
                                '<div class="col-md-4">'+
                                    '<div class="n-img">'+
                                        (full.imagen!=null?'<img src="'+RutaBase+'/files/'+full.imagen+'" alt="">':'<img src="'+RutaBase+'/img/no-picture.png" alt="">')+
                                    '</div>'+
                                '</div>'+
                                '<div class="col-md-8">'+
                                    '<div class="n-cont">'+
                                        '<h4>'+full.titulo+'</h4>'+
                                        '<p>'+full.resumen+'</p>'+
                                    '</div>'+
                                    '<div class="n-foot">'+
                                        '<a href="'+RutaBase+'/nota?id='+full.id+'">Ver más...</a>'+
                                    '</div>'+
                                '</div>'+
                            '</div> '+
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