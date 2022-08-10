// Aula de vetores

let num = [1, 2, 7, 28, 32]

num.push(50) // inclui um valor ao final do array
num.sort() // ordena os valores em ordem crescente

console.log(num) // retornar o valores internos do array

let pos = num.indexOf(225) //retorna buscar de valor específico
    if (pos == -1) {
        console.log(`O valor não foi encontrado`)
    } else {
        console.log(`O valor ${num[pos]} está na posição ${pos}`)
    }

console.log(`O vetor tem ${num.length} posições`) //template string com o tamanho do array
console.log(`O primeiro valor do vetor é ${num[0]}`) // template string com verificação de posição atravéz do indice