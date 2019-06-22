
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
        $("#conteudo-modal-registro").text("É necessário preencher todos os campos")
        openModal("#modal-registro")
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
                        ", já foi realizado o cadastrado com seu e-mail em nossa base de dados. Pode registrar sua presença com e-mail " + 
                        email)
                } else {
                    modal_conteudo.text("Erro ao cadastrar o usuário "+email+ ". Por favor, consultar alguém do Ministério de Ensino." +
                    " Se possível informe o seguinte erro: " + response.result)
                }
                openModal("#modal-registro")
             },
             "error": function(error){
                 $("#conteudo-modal-registro").text("Erro de comunição com servidor: " + error.statusText)
                 openModal("#modal-registro")
                }
        });
    }
    clearInput("email")
    clearInput("name")
    clearInput("phone")
    clearInput("cell")
}

function checkPresence(){
    var email = $("#email").length > 0 ? $("#email").val() : null;
    var data = {"email": email}
    validated = !email
    var modal_conteudo = $("#conteudo-modal-presenca")
    if (validated){
        modal_conteudo.text("Preencha seu e-mail para realizar a inscrição.")
        openModal("#modal-presenca")
    }else{
        $.post(
            {"url":"/class/register", 
             "data": data,
             "success": function(response){
                if (response.result && response.result.includes("success")){
                    modal_conteudo.text("Presença de "+ email +" confirmada com sucesso. Obrigado! ")
                } else if (response.result && response.result == "duplicated"){
                    modal_conteudo.text("Sua presença já foi registrada hoje!")
                } else if (response.result && response.result == "user not found"){
                    modal_conteudo.text("Seu usuário ainda não foi registrado! Vá até a nossa página de registro de usuários.")
                } else {
                    modal_conteudo.text("Erro ao registrar presença. Por favor informar o seguinte erro: " + response.result)
                }
                openModal("#modal-presenca")
             },
             "error": function(error){
                modal_conteudo.text("Erro de comunição com servidor: " + error.statusText)
                 openModal("#modal-presenca")
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
function openModal(elem){
    $(elem).modal('open');
}