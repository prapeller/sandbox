'use strict'

// 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999, мы должны получить на выходе
// объект, в котором в соответствующих свойствах описаны единицы, десятки и сотни. Например, для числа 245 мы должны
// получить следующий объект: {‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо выдать
// соответствующее сообщение с помощью console.log и вернуть пустой объект.

function getObjFromInt(integer) {
    let int = integer
    if (int > 999 || int < 0) {
        console.log('integer should be not less then 0 and no more then 999')
        return {}
    }
    let units = int % 10
    let tens = (int % 100 - units) / 10
    let hundreds = (int % 1000 - 10 * tens - units) / 100
    return {
        units,
        tens,
        hundreds,
    }
}

console.log(getObjFromInt(0))
console.log(getObjFromInt(1))
console.log(getObjFromInt(10))
console.log(getObjFromInt(25))
console.log(getObjFromInt(100))
console.log(getObjFromInt(245))
console.log(getObjFromInt(990))
console.log(getObjFromInt(999))
let a = getObjFromInt(1000)
console.log(a)