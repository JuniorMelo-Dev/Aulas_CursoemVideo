function contar() {
    let inicio = document.getElementById('txtinicio')
    let fim = document.getElementById('txtfim')
    let passo = document.getElementById('txtpasso')
    let result = document.getElementById('result')

    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        result.innerHTML = `Impossível contar...`
    } else {
        result.innerHTML = `Contando...  <br>`
        let start = Number(inicio.value)
        let stop = Number(fim.value)
        let step = Number(passo.value)
        if (step <= 0) {
            window.alert(`Passo inválido! Contando a partir de 1`)
            step = 1
        }

        if (start < stop) {
            //Contagem crescente
            for (let cont = start; cont <= stop; cont += step) {
                result.innerHTML += `${cont} \u{1f449}` //emoji
            }
        } else {
            //Contagem decrescente
            for (let cont = start; cont >= stop; cont -= step) {
                result.innerHTML += `${cont} \u{1f449}`
            }
        }
        result.innerHTML += `\u{1f3c1}` //código emoji
    }
}