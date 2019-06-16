
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
                var modal_conteudo = $("#conteudo-modal-registro")
                if (response.result && response.result == "success"){
                    modal_conteudo.text("Usuário "+email+ " cadastrado com sucesso. Pode registrar sua presença com e-mail: " + email)
                } else if (response.result && response.result == "duplicated"){
                    modal_conteudo.text(name + 
                        ", você já esta cadastrado em nossa base de dados. Pode registrar sua presença com  e-mail " + 
                        email)
                } else {
                    modal_conteudo.text("Erro ao cadastrar o usuário "+email+ ". Por favor, consultar alguém do Ministério de Ensino." +
                    " Se possível informe o seguinte erro: " + response.result)
                }
                $('.modal').modal('open');
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

function fillTestData(){
    $("#email").val("amommendes@mergulhando.com.br"+Math.round(Math.random()*100));
    $("#name").val("Amom Mendes"+Math.ceil(Math.random()*100))
    $("#phone").val("11-972291656"+Math.ceil(Math.random()*100))
    $("#cell").val("Ceret"+Math.ceil(Math.random()*100))
}