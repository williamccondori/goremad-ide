var RutaBase = '/SRGT';
var proyeccion = 'EPSG:4326';
var mddLonLat = [-70.455322, -11.700652];//EPSG:4326

var capasBase = [
    new ol.source.OSM(),//carretera
    new ol.source.BingMaps({//aereo
        key: 'Av9hT1p3hgCS7zVAx1pgv76i6akUnZLOCi7rZ7mUxczMhVjoPETyHTGWiGRJO_Ur',
        imagerySet: 'Aerial'
    }),
    new ol.source.BingMaps({//aereo con etiquetas
        key: 'Av9hT1p3hgCS7zVAx1pgv76i6akUnZLOCi7rZ7mUxczMhVjoPETyHTGWiGRJO_Ur',
        imagerySet: 'AerialWithLabels'
    }),
    new ol.source.Stamen({//TERRENO
        layer: 'terrain'
    }),
    new ol.source.Stamen({//TONER
        layer: 'toner'
    }),
    new ol.source.XYZ({
        url: 'https://{a-c}.tile.opentopomap.org/{z}/{x}/{y}.png'
    })
];

var baseActual=0;

var map;
var mddZoom=8;
var maxZoom=1;

var v_capas;
var v_mapas;
var v_leyendas;
var v_imprimir;

$( document ).ready(function() { 
          
           
    var container = document.getElementById('popup');  
      
    var marker = new ol.Overlay({
        positioning: 'center-center',
        element: document.getElementById('popup'),
        stopEvent: false,
        position: mddLonLat
    });
    
    var base = new ol.layer.Tile({ 
        source: new ol.source.OSM() 
    });
    
    /*var tiled = new ol.layer.Tile({
        visible: false,
        source: new ol.source.TileWMS({
            url: 'http://localhost:8081/geoserver/geojaz/wms',
            params: {
                LAYERS: 'geojaz:Limites'                
            },
            serverType: 'geoserver'
        })
    });*/
    
    var wmsSource = new ol.source.ImageWMS({
        url: 'http://localhost:8081/geoserver/geojaz/wms',
        params: {'LAYERS': 'geojaz:Limites'},
        serverType: 'geoserver',
        crossOrigin: 'anonymous'
      });
      
     var wmsLayer = new ol.layer.Image({
        source: wmsSource
      });
    

    /*var vector = new ol.layer.Vector({
      source: new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: function(extent) {
          return  'http://localhost:8081/geoserver/geojaz/wfs?' +
                  'service=WFS&' +
                  'version=1.0.0&request=GetFeature&typename=geojaz:Limites&'+
                  'outputFormat=application/json';
        },
        projection: 'EPSG:32719',
      })
    });
    */
   
    map = new ol.Map({
        controls: [],
        target: 'map',//html
        renderer: 'canvas',//tipo de render
        layers: [ base, wmsLayer ],
        overlays: [ marker ],
        view: new ol.View({  
            projection: proyeccion,
            center: mddLonLat,
            zoom: mddZoom
        })
    });   
    
    
    /**/
    v_capas = $('#v-capas').dialog({
        width:300,
        top : 100,
        left : 80,
        hasMask : false,
        hotKeys : false
    });
    
    v_mapas = $('#v-mapas').dialog({
        width:300,
        top : 100,
        left : 80,
        hasMask : false,
        hotKeys : false
    });
    
    v_leyendas = $('#v-leyendas').dialog({
        width: 300,
        top : 100,
        left : 80,
        hasMask : false,
        hotKeys : false
    });
    
    v_imprimir = $('#v-imprimir').dialog({
        width: 300,
        top : 100,
        left : 80,
        hasMask : false,
        hotKeys : false
    });
    
});


/*function mover()
{
    map.getView().setRotation(80);
}*/

/*---------------------------------------------------------------------C-BOTONES----*/
function home () {
    map.getView().setCenter(mddLonLat);
    map.getView().setZoom(mddZoom);   
}

function zoomOut () {     
    var auxZoom = map.getView().getZoom(); 
    if(auxZoom>=maxZoom)
        map.getView().setZoom(auxZoom-1);  
}

function zoomIn() {    
    var auxZoom = map.getView().getZoom(); 
    if(auxZoom<=15)
        map.getView().setZoom(auxZoom+1);    
}

function jpg() {
    map.once('postcompose', function(event) {
          var canvas = event.context.canvas;
          if (navigator.msSaveBlob) {
            navigator.msSaveBlob(canvas.msToBlob(), 'map.png');
          } else {
            canvas.toBlob(function(blob) {
              saveAs(blob, 'map.png');
            });
          }
        });
        map.renderSync();
}
/*---------------------------------------------------------------------M-BOTONES----*/

function capas() {	
    v_capas.open();
}

function leyendas() {	
    v_leyendas.open();
}

function mapas() {	
    v_mapas.open();
}

function imprimir() {	
    v_imprimir.open();
}

function cambiarBase(indice)
{
    if(baseActual!=indice)
    {
        //reemplazamos la fuente de la primera capa
        var aux_l = map.getLayers().getArray()[0];
        aux_l.setSource(capasBase[indice]);
        baseActual=indice;
        
        $(".lista-boxes .item-boxes").each(function () {
            if($(this).data("ind")==indice)            
                $(this).addClass("activo");            
            else
                $(this).removeClass("activo");
        });
    }
}



function layers() {
    
    var d1_1 = $.dialog({
            content : 'A Basic Dialog<br><br>asda dadasd',
            width:300,
            height : 300,
            top : 100,
            left : 80,
            hasMask : false,
            hotKeys : false
	});
	
d1_1.open();
            
}




