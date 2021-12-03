// 2. Не выполняя кода, ответить, что выведет браузер и почему:

"use strict"

// if (!("a" in window)) {
//     var a = 1;
// }
// console.log(a)
//undefined bcz var a was declared but wasn't assigned


// var b = function a(x) {
//     x && a(--x);
// };
// console.log(a)
//a is not defined, bcz interpreter cant see name of function in function expression


// function a(x) {
//     return x * 2;
// }
// var a
// console.log(a)
// declaration of already existing variable (function a), so already existing variable will be logged in console


// function b(x, y, a) {
//     console.log(arguments)
//     arguments[2] = 10;
//     console.log(arguments)
//     console.log(arguments[2])
//     console.log(arguments)
//     console.log(a)
// }
// b(1, 2, 3)
// Parameters are variables listed as a part of the function definition. (x, y, a) - Parameters
// Arguments are values passed to the function when it is invoked. (1, 2, 3) - Arguments
// (Arguments) is object that is being built when funcion declared. You can modify values of its parameters, but you cant change function parameters.


// function a() {
//     console.log(this)
// }
//
// console.log(a)
// // function: a
//
// console.log(a())
// // undefined ('this' is function 'caller', nothing calls function, 'this' is undefined)
// // undefined (output of void function return is 'undefined')
//
//
// a.call(null)
// // null (first arg of 'call' is caller. 'this' is caller)
//
//
// console.log(null)
// // null