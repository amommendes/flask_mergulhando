
function postStudent(){
    var email = $("#email").length > 0 ? $("#email")[0] : null;
    var name = $("#name").length > 0 ? $("#name")[0]    : null;
    var phone = $("#phone").length > 0 ? $("#phone")[0] : null;
    var cell = $("#cell").length > 0 ? $("#cell")[0]    : null;
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
        $.ajax(
            {"url":"/register", 
             "data":data
        });
    }
    


}

