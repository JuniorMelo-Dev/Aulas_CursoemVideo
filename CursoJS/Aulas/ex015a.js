
let valores = [8, 7, 56, 48, 16, 5, 20, 37]
valores.sort()

/*for (let position = 0; position < valores.length; position++) {
    console.log(`A posição ${position} tem o valor ${valores[position]}`)
}*/

//simplificando
for (let position in valores) {
    console.log(`A posição ${position} tem o valor ${valores[position]}`)
}