'use strict';
// let i = 0;
// console.log('start');
// while (i < 3) {
//     console.log(i);
//     i++;
// }
// console.log('end');

// let i = 0;
// console.log('start');
// do {
//     console.log(i);
//     i++;
// } while (i < 3);
// console.log('end');

// for (let i = 0; i < 3; i++) {
// for (let i = 0, b = 7; i < 3 && b > 0; i++, b--) {
//     console.log(i);
// }

// while (true) {
// //     some code
// }

// do {
//     // some code
// } while (true);

// for (;;) {}

// for (let i = 0;; i++) {
//     if (i > 10) break; // Выход из цикла
//     if (i % 2 === 1) continue; // завершение итерации
//     console.log(i);
// }

// outerLoop: for (let a = 0; a < 3; a++) {
//         console.log('Upper cycle is running');
//         for (let b = 0; b < 3; b++) {
//             console.log('Inner cycle is running');
//             if (b >= 1) {
//                 console.log('Breaking inner cycle');
//                 break outerLoop;
//             }
//         }
//     }

// let arr = []
// console.log(arr)
// let arr = new Array(6, 7, 3, 9);
// let arr = [6, 7, 3, 9];
// console.log(arr, arr.length);
// arr.length = 100;
// arr[50] = 50;
// // arr.length = 2;
// console.log(arr, arr.length);
// console.log(arr[3]);
// arr.length = 0;
// arr[arr.length] = 9;
// delete arr[2];
// console.log(arr, arr.length);
// console.log(arr[2]);


// let arr = [
//     [1, 5, 'hi', false],          // 0
//     [55, true, 1, 100],           // 1
//     [true, 'string', NaN, 32],    // 2
// ];
//
// console.log(arr);
// console.log(arr[2][1]);

// let nested = [1, 6, [134, [5, 7]], [4, 8]] /// => [1, 6, 134, 5, 7, 4, 8];
// console.log(nested)

// let arr = [true, 'string', NaN, 32];
//
// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
// }

// for (const index in arr) {
//     console.log(arr[index]);
// }
// for (const value of arr) {
//     console.log(value);
// }

// для обработки n-мерных массивов можно использовать рекурсию

let arr = [32, true, 'string', NaN, 1, 4];
// console.log(arr.find(isNaN));
// console.log(arr.indexOf(NaN));
// console.log(arr.indexOf(1));
// const even = (element) => element % 2 === 0;
// console.log(arr.some(even));
// const reducer = (accumulator, currentValue) => accumulator + currentValue;
// console.log(arr.reduce(reducer));
// console.log(arr.map(x => x * 2));
// console.log(arr.filter(x => isNaN(x)));
// console.log(arr.includes(32));

// let arr = [true, 'string', NaN, 32];

// console.log(arr.push('finish'), arr);
// console.log(arr.unshift('start'), arr);
// console.log(arr.pop(), arr);
// console.log(arr.shift(), arr);
// console.log(arr.splice(1, 1), arr);
// console.log(arr.splice(1, 1, '123'), arr);
// console.log(arr.splice(1, 0, '123'), arr);

// let arr = [true, 'string', NaN, 32, [1, 2, 3], {1: 2, 2: 2}];

// let arrCopy = arr; // doesnt create copy
// console.log(arr === arrCopy);

// let arrCopy = Array.from(arr); //create a copy
// console.log(arrCopy)
// console.log(arr === arrCopy);

// let arrCopy = JSON.parse(JSON.stringify(arr));
// console.log(arrCopy)
// console.log(arr === arrCopy);
// arrCopy.push(123);
// console.log(arrCopy, arr);
