let number = document.querySelector('input#f-num')
let lista = document.querySelector('select#f-lista')
let resultado = document.querySelector('div#resultado')
let valores= []

function isNumber(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}

function inLista(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar() {
    if (isNumber(number.value) && !inLista(number.value, valores)) {
        
    } else {
        window.alert('Valor inválido ou já encontrado na lista!')
    }
}