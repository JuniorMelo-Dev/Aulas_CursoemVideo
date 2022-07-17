function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var anoNasc = document.getElementById('txtano')
    var resultado = document.querySelector('div#resultado')

    if (anoNasc.value.length == 0 || Number(anoNasc.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var formSex = document.getElementsByName('radsex')
        var idade = ano - Number(anoNasc.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (formSex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 12) {
                //Criança
                img.setAttribute('src', './img/crianca-m.jpg')
            } else if (idade < 18) {
                //Adolescente
                img.setAttribute('src', './img/adolescente-m.jpg')
            } else if (idade < 50) {
                //Adulto
                img.setAttribute('src', './img/adulto-m.jpg')
            } else {
                //Idoso
                img.setAttribute('src', './img/idoso-m.jpg')
            }
        } else if (formSex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 12) {
                //Criança
                img.setAttribute('src', './img/crianca-f.jpg')
            } else if (idade < 18) {
                //Adolescente
                img.setAttribute('src', './img/adolescente-f.jpg')
            } else if (idade < 50) {
                //Adulto
                img.setAttribute('src', './img/adulto-f.jpg')
            } else {
                //Idoso
                img.setAttribute('src', './img/idoso-f.jpg')
            }
        }
        resultado.style.textAlign = 'center'
        resultado.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        resultado.appendChild(img)
    }

}