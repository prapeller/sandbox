'use strict'

// 2. С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть сущность корзины.
// Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров.
// Товары в корзине хранятся в массиве.
// Задачи:
// a) Организовать такой массив для хранения товаров в корзине;
// b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.

let basket = [['name1', 2, 200], ['name2', 3, 300], ['name3', 2, 100]]
function countBasketPrice(basket) {
    let total = 0
    basket.forEach(elem => total += elem[1]*elem[2])
    return total
}

console.log(countBasketPrice(basket))

function countBasketPrice2(basket) {
    return basket.reduce((total, currentItem) => total + currentItem[1] * currentItem[2], 0)
}

console.log(countBasketPrice2(basket))
