//Formato email
var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

$(document).ready(function(){
    $("#fEnviar").click(function(){

        var nombre = $("#fname").val();
        var email = $("#femail").val();
        var sujeto = $("#fsubject").val();
        var mensaje = $("#fmenssage").val();

        //Validacion de nombre
        if (nombre == ""){
            $("#mensaje1").fadeIn();      
            return false;
        }else{
            $("#mensaje1").fadeOut();     
            //Validacion de apellido
            if(email == "" || !expr.test(email)){
                $("#mensaje2").fadeIn();        
                return false;
            }else{
                $("#mensaje2").fadeOut();     
                if (sujeto == ""){
                    $("#mensaje3").fadeIn();      
                    return false;
                }else{
                    $("#mensaje3").fadeOut();
                    //Validacion de correo
                    if (mensaje == ""){
                        $("#mensaje4").fadeIn();      
                        return false;
                    }else{
                        $("#mensaje4").fadeOut();    
                    }
                }
            }
        }
    })
})