// 1. Дан код:
// Почему код даёт именно такие результаты?
// var a = 1, b = 1, c, d;
// c = ++a; alert(c);           //  2
// приоритет за плюсами в начале, сначала увеличивается 'a' ('а' стало = 2), потом присваем это значение для 'c' ('c' стало = 2)

// d = b++; alert(d);           //  1
// приоритет за операцией присвоения значения для 'd'. сначала присваиваем для 'd' значение 'b' ('d' стало = 1), потом увеличиваем значение 'b' ('b' стало = 2)

// c = (2+ ++a); alert(c);      //  5
// сначала увеличиваем а на 1 ('а' стало = 3), прибавляем к 'а' 2 и присваиваем это значение 'c' ('c' стало = 5)

// d = (2+ b++); alert(d);      //  4
// сначала присваиваем к 'b' 2, присваиваем значение 'b' + 2 ('d' стало = 4), затем увеличиваем и b. ('b' стало = 3)

// alert(a);                    //  3
// 'а' стало = 3 на строке 10

// alert(b);                    //  3
//'b' стало = 3 на строке 13


// 2. Чему будет равен x в примере ниже?
// var a = 2;
// var x = 1 + (a *= 2);
// console.log(x)               //  5
// console.log(a)               //  4

// 3. Объявить две целочисленные переменные a и b и задать им произвольные начальные значения. Затем написать скрипт, который работает по следующему принципу:
// если a и b положительные, вывести их разность;
// если а и b отрицательные, вывести их произведение;
// если а и b разных знаков, вывести их сумму; ноль можно считать положительным числом.

function getRandomInt(a, b) {
    return Math.round(Math.random() * (b - a) + a)
}
let a = getRandomInt(-10, 10)
let b = getRandomInt(-10, 10)
console.log(`a = ${a}, b = ${b}`)

if (a >= 0 && b >= 0) {
    console.log(`difference: ${a - b}`)
}
else if (a < 0 && b < 0) {
    console.log(`product: ${a * b}`)
}
else {
    console.log(`sum: ${a + b}`)
}


// 4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch организовать вывод чисел от a до 15.
let randomInt = getRandomInt(0, 16)
switch (a){
    case (0):
        console.log(0)
        ++a
    case (1):
        console.log(1)
        ++a
    case (2):
        console.log(2)
        ++a
    case (3):
        console.log(3)
        ++a
    case (4):
        console.log(4)
        ++a
    case (5):
        console.log(5)
        ++a
    case (6):
        console.log(6)
        ++a
    case (7):
        console.log(7)
        ++a
    case (8):
        console.log(8)
        ++a
    case (9):
        console.log(9)
        ++a
    case (10):
        console.log(10)
        ++a
    case (11):
        console.log(11)
        ++a
    case (12):
        console.log(12)
        ++a
    case (13):
        console.log(13)
        ++a
    case (14):
        console.log(14)
        ++a
    case (15):
        console.log(15)
        ++a
}

// 5. Реализовать основные 4 арифметические операции в виде функций с двумя параметрами. Обязательно использовать оператор return.
function getSum(a, b) {
    return a + b
}
function getDiff(a, b) {
    return a - b
}
function getProduct(a, b) {
    return a * b
}
function getQuot(a, b) {
    return a / b
}

// 6. Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), где arg1, arg2 – значения аргументов, operation – строка с названием операции. В зависимости от переданного значения операции выполнить одну из арифметических операций (использовать функции из пункта 5) и вернуть полученное значение (использовать switch).
function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            return getSum(arg1, arg2)
        case '-':
            return getDiff(arg1, arg2)
        case '*':
            return getProduct(arg1, arg2)
        case '/':
            return getQuot(arg1, arg2)
    }
}
// 7. *Сравнить null и 0. Попробуйте объяснить результат.
// console.log(null == 0) //false
// console.log(null === 0) //false
// console.log(typeof null) // "object"
// console.log(typeof 0) // "number"
// //два разных типа данных, null - специальный примитив

// 8. *С помощью рекурсии организовать функцию возведения числа в степень. Формат: function power(val, pow), где val – заданное число, pow – степень.

function power(val, pow) {
    if (pow === 0) {
            return 1
        }
    if (pow === 1) {
            return val
        }

    if (pow > 0) {
        return val * power(val, pow - 1)
    }
    else {
        return  1 / val * power(val, pow + 1)
    }
}

console.log(power(2, -3))