function tabuada() {
    let numero = document.getElementById('txtnum')
    let tabuada = document.getElementById('sel-tab')

    if (numero.value.length == 0) {
        window.alert('Por favor, digite um número!')
    } else {
        let number = Number(numero.value)
        let cont = 1
        tabuada.innerHTML = ' '
        while (cont <= 10) {
            let item = document.createElement('option')
            item.text = `${number} x ${cont} = ${
            number*cont}`
            item.value = `tabuada${cont}`
            tabuada.appendChild(item)
            cont++
        }
    }

}