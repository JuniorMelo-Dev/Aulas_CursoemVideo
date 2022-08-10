//Função com parâmetros e retornos

/*
function parImpar(n) {
    if (n % 2 == 0) {
        return 'Par'
    } else {
        return 'Ímpar'
    }
}
console.log(parImpar())


function somar(n1, n2) {
    return n1 + n2
}
console.log(somar(3))


//Função fatorial de número
function fatorial(number) {
    let fator = 1
    for (let cont = number; cont > 1; cont--) {
        fator *= cont
    }
    return fator
}
console.log(fatorial(3))
*/

//Função fatorial RECURSIVA
function fatorial(number) {
    if (number ==  1) {
        return 1
    } else {
        return number * fatorial(number-1)
    }
}
console.log(fatorial(7))