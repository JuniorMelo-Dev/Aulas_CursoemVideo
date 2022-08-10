//Exemplo de OBJETO em JavaScript

let eu = {nome: 'Junior',
sexo: 'M',
idade: 32,
envelhecer(i=0){
    console.log('Ficou velho!!')
    this.idade += i
}}

eu.envelhecer(2)
console.log(`${eu.nome} tem ${eu.idade} anos`)