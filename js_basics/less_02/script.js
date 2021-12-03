// https://docs.google.com/document/d/14hImGe6HYJjYImL52FpLFyqPSMR4em42SMfRRP28xuk/edit
// https://youtu.be/E7Npkqlz6ts

'use strict';

// let goodsCount = 10;

// if (goodsCount > 0) {
//     console.log('количество товаров: ' + goodsCount);
// } else {
//     console.log('Корзина пуста');
// }

// if (goodsCount > 0) console.log('количество товаров: ' + goodsCount)
// else console.log('Корзина пуста')

// goodsCount > 0
//     ? console.log('количество товаров: ' + goodsCount)
//     : console.log('Корзина пуста');

// let result = goodsCount > 0
//     ? 'количество товаров: ' + goodsCount
//     : 'Корзина пуста';
//
// console.log(result);

// console.log(goodsCount > 0
//     ? 'количество товаров: ' + goodsCount
//     : 'Корзина пуста');

// let result;
//
// if (goodsCount > 0) {
//     result = 'количество товаров: ' + goodsCount;
// } else {
//     result = 'Корзина пуста';
// }
//
// console.log(result);
// let good = 'Яблоки';

// if (good === 'Бананы') {
//     console.log('Стоимость бананов 50р.');
// } else {
//     if (good === 'Манго') {
//         console.log('Стоимость манго 80р.');
//     } else {
//         if (good === 'Яблоки' || good === 'Груши') {
//             console.log('Стоимость яблок и груш 40р.');
//         } else {
//             console.log('Неизвестный фрукт');
//         }
//     }
// }

// if (good === 'Бананы') {
//     console.log('Стоимость бананов 50р.');
// } else if (good === 'Манго') {
//     console.log('Стоимость манго 80р.');
// } else if (good === 'Яблоки' || good === 'Груши') {
//     console.log('Стоимость яблок и груш 40р.');
// } else {
//     console.log('Неизвестный фрукт');
// }
// let good = 'Яблоки';

// switch (good) {
//     case 'Бананы':
//         console.log('Стоимость бананов 50р.');
//         break;
//     case 'Манго':
//         console.log('Стоимость манго 80р.');
//         break;
//     case 'Яблоки':
//     case 'Груши':
//         console.log('Стоимость яблок и груш 40р.');
//         break;
//     default:
//         console.log('Неизвестный фрукт');
// }
// let good = 'Яблоки';

// function sayPrice(good) {
//     switch (good) {
//         case 'Бананы':
//             console.log('Стоимость бананов 50р.');
//             break;
//         case 'Манго':
//             console.log('Стоимость манго 80р.');
//             break;
//         case 'Яблоки':
//         case 'Груши':
//             console.log('Стоимость яблок и груш 40р.');
//             break;
//         default:
//             console.log('Неизвестный фрукт');
//     }
// }

// let good = 'Яблоки';
//
// function getGoodPrice(good) {
//     switch (good) {
//         case 'Бананы': return 50;
//         case 'Манго': return 80;
//         case 'Яблоки':
//         case 'Груши': return 40;
//         default: return null;
//     }
// }

// let applesPrice = getGoodPrice(good);
// console.log(applesPrice);
// console.log(getGoodPrice('Бананы'));
// console.log(getGoodPrice());

// function getPriceByCount(good, count = 1) {
//     let goodPrice = getGoodPrice(good);
//
//     if (goodPrice == null) return null;
//
//     return goodPrice * count;
// }
//
// // console.log(getPriceByCount(good, 10));
// console.log(getPriceByCount('Бананы'));
// foo();
// var foo = function () {
//     console.log('function expression');
// }
// foo();
//
// function foo(a, b) {
//     console.log(arguments);
// }
//
// foo(1, 5, 7);

// function recursion(x) {
//     if (x <= 0 || !Number.isInteger(x)) return 'Задайте целое число больше 0';
//
//     if (x === 1) return '1';
//
//     return recursion(x - 1) + ' ' + x; // recursion(2) + ' ' + 3; => ((2 - 1) + 2) + 3
// }
//
// console.log(recursion(10));

let number;
let attempts;

function resetGame() {
    attempts = 0;
    number = Math.floor(Math.random() * 100);

    console.log(number);
}

function tryGuessNumber() {
    const userAnswer = parseInt(prompt('Введите число от 0 до 100, для выхода наберите -1'));

    if (userAnswer === -1) return alert('Game Over!');

    if (isNaN(userAnswer)) {
        alert('Необходимо ввести целое число от 0 до 100.');
        tryGuessNumber();
        return;
    }

    attempts++;

    if (userAnswer > number) {
        alert('Попробуйте число меньше.');
    } else if (userAnswer < number) {
        alert('Попробуйте число больше.');
    } else {
        alert('Поздравляем! Вы угадали число. Количество попыток: ' + attempts);

        if (!confirm('Хотите сыграть еще раз?')) return alert('Game Over!');

        resetGame();
    }

    tryGuessNumber();
}

resetGame();
tryGuessNumber();
