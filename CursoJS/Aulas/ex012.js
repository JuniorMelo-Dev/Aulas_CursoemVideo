// Condições aninhadas com hora do sistema

var atual = new Date()
var hora = atual.getHours() 
console.log(`A hora atual é ${hora} horas`)

if (hora < 12) {
    console.log('Bom dia')
}else if (hora <= 18) {
    console.log('Boa tarde')
}else {
    console.log('Boa noite')
}