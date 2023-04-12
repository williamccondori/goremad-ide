$(document).ready(function() {
    
    $('#fecha').datepicker({
        format: "dd/mm/yyyy",
        todayBtn: "linked",
        language: "es",
        autoclose: true,
        todayHighlight: true
    });
    
    //$("#fecha").datepicker("setDate", new Date());
    
    
    $("#updload-image-template").change(function(){
        readURL(this);
    });
    
    $("#formulario").submit(function(e)
    {
        if(!Validar("#formulario"))
            e.preventDefault();
    });
    
    $("#contenido").summernote({
        height: 300,
        tabsize: 2
      });
});

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image-template').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
    else
    {
        var aux = $('#image-template-aux').attr('src');
        $('#image-template').attr('src', aux);
    }
}


