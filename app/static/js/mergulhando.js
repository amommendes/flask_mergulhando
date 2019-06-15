
function postStudent(){
    var email = $("#email").length > 0 ? $("#email").val() : null;
    var name = $("#name").length > 0 ? $("#name").val()    : null;
    var phone = $("#phone").length > 0 ? $("#phone").val() : null;
    var cell = $("#cell").length > 0 ? $("#cell").val()    : null;
    
    data = {
        "email": email,
        "name":name,
        "phone":phone,
        "cell":cell
    }
    validated = !email && !name && !phone && !cell
    if (validated){
        alert("É necessário preencher todos os campos")
    }else{
        $.post(
            {"url":"/user", 
             "data": data,
             "success": function(response){
                 console.log(response)
             }
        });
    }
    clearInput("email")
    clearInput("name")
    clearInput("phone")
    clearInput("cell")
}

function clearInput(input){
    $("#"+input).val("")
}

