'use strict'

// 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

let num = 1
while (num <= 100) {
    let i = 2
    let isPrime = true
    while (i <= num / 2) {
        if (num % i === 0) {
            isPrime = false
            break
        }
        i++
    }
    if (isPrime && num !== 1) {
        console.log(num)
    }
    num++
}
