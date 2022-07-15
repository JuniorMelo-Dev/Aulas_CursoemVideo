//Switch case (casos de uso)

var hoje = new Date()
var estudar_hoje = hoje.getDay()


if (estudar_hoje == 0) {
    console.log('Hoje é Domingo, Vá descansar!!')
}else {
    console.log('Estudar')
}

switch(estudar_hoje) {
    case 0:
        console.log(estudar_hoje)
        break
    case 1:
        console.log('HTML5 e CSS3')
        break
    case 2:
        console.log('Python')
        break
    case 3:
        console.log('Lógica Programação')
        break
    case 4:
        console.log('MySql')
        break
    case 5:
        console.log('POO')
        break
    case 6:
        console.log('Javascript')
        break
    default:
        console.log('[ERRO] dia inválido!')
}