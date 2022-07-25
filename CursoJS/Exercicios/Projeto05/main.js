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
        valores.push(Number(number.value))
        let item = document.createElement('option')
        item.text = `Valor ${number.value} adicionado!`
        lista.appendChild(item)
        resultado.innerHTML = ''
    } else {
        alert('Valor inválido ou já encontrado na lista!')
    }
    number.value = ''
    number.focus()
}

function finalizar() {
    if (valores.length == 0) {
        alert('Adicione valores antes de finalizar!')
    } else{
        let total = valores.length
        let maior =  valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for (let position in valores) {
            soma += valores[position]
            if (valores[position] > maior)
                maior = valores[position]
            if (valores[position] < menor)
                menor = valores[position]
        }
        media = soma / total
        resultado.innerHTML = ''
        resultado.innerHTML += `<p>Ao todo, temos ${total} números cadastrados.</p>`
        resultado.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        resultado.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        resultado.innerHTML += `<p>Somando todos os valores, temos ${soma}</p>`
        resultado.innerHTML += `<p>A média dos valores digitados foi ${media}</p>`
    }
}