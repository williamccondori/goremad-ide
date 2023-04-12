var RutaBase="/portal";

$(document).ready(function () {
    mayuscula();
    entero();
    decimal();
});

function mayuscula() {
    $(".mayuscula").unbind("keyup");
    $(".mayuscula").keyup(function () {
        var start = this.selectionStart,
            end = this.selectionEnd;
        $(this).val($(this).val().toUpperCase());
        this.setSelectionRange(start, end);
    });
}

function entero() {
    $(".entero").unbind("keypress");
    $(".entero").keypress(function (event) {
        if (event.which < 48 || event.which > 57) {
            event.preventDefault();
        }
    });
}

function decimal() {
    $(".decimal").unbind("keypress");
    $(".decimal").keypress(function (event) {
        if ((event.which != 46 || $(this).val().indexOf('.') != -1) && (event.which < 48 || event.which > 57)) {
            event.preventDefault();
        }
        else if (event.which == 46 && $(this).val().trim() == "") {
            event.preventDefault();
        }
        else {
            var separados = $(this).val().split('.');
            if (separados.length > 1) {
                if (separados[1].length > 1)
                    event.preventDefault();
            }
        }
    });
}

function Limpiar(principal, rem) {
    
    $(principal+' .validar_texto').each(function(){
        if(rem)
            $(this).val("");
        
        var form_group=$(this).closest(".form-group");        
        form_group.removeClass("has-error");    
        form_group.find(".help-block").remove();         
    });

    $(principal+' .validar_select').each(function(){
               
        var form_group=$(this).closest(".form-group");        
        form_group.removeClass("has-error");    
        form_group.find(".help-block").remove();   
    });


    
    

}


function Validar(principal) {
    var res = true;

    $(principal+' .validar_texto').each(function(){
        var form_group=$(this).closest(".form-group");
        if($(this).val().trim()=="")
        {
            res=false;
            form_group.addClass("has-error");
            form_group.find(".help-block").remove();
            form_group.append('<span class="help-block">Este campo es requerido</span>');
        }
        else
        {
            form_group.removeClass("has-error");    
            form_group.find(".help-block").remove(); 
        }
    });

    $(principal+' .validar_select').each(function(){
        
        var form_group=$(this).closest(".form-group");
        if($(this).val()=="" | $(this).val()=="0")
        {
            res=false;
            form_group.addClass("has-error");
            form_group.find(".help-block").remove();
            form_group.append('<span class="help-block">Este campo es requerido</span>');
        }
        else
        {
            form_group.removeClass("has-error");    
            form_group.find(".help-block").remove(); 
        }   
    });


    return res;
}

function ValidarHorizontal(principal) {
    var res = true;

    $(principal+' .validar_texto').each(function()
    {
        var form_group=$(this).closest(".form-group");
        var primer_div=$(this).closest("div");

        if($(this).val().trim()=="")
        {
            res=false;
            form_group.addClass("has-error");
            form_group.find(".help-block").remove();
            primer_div.append('<span class="help-block">Este campo es requerido</span>');
        }
        else
        {
            form_group.removeClass("has-error");    
            form_group.find(".help-block").remove(); 
        }
    });

    return res;
}


