'use strict'

// 2.Продолжить работу с интернет-магазином:
// 2.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?
// 2.2. Реализуйте такие объекты.
// 2.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.

const spam = {
    name: 'spam',
    price: 200,
    qty: 1
}
const eggs = {
    name: 'eggs',
    price: 300,
    qty: 1,
}
const potato = {
    name: 'potato',
    price: 100,
    qty: 1,
}

let basket = {
    items: [],
    init() {
        return this
    },
    addItem(item) {
        let e = this.items.find(e => e.name === item.name)
        e ? e['qty'] += 1 : this.items.push(item)
    },
    removeItem(item) {
        let e = this.items.find(e => e.name === item.name)
        e ? this.items.splice(this.items.indexOf(e), 1) : null
    },
    minusItem(item) {
        if (this.items.filter(e => e.name === item.name).length > 0) {
            this.items[this.items.indexOf(item)]['qty'] -= 1
        }
        if (this.items[this.items.indexOf(item)]['qty'] === 0) {
            this.removeItem(item)
        }
    },
    isEmpty() {
        return this.items.length === 0
    },
    countBasketPrice() {
        let total = 0
        this.items.forEach(el => total += el.price * el.qty)
        return total
    },
    showItems() {
        return this.items
    }
}

// // 3.* Подумать над глобальными сущностями. К примеру, сущность «Продукт» в интернет-магазине актуальна не только для
// // корзины, но и для каталога. Стремиться нужно к тому, чтобы объект «Продукт» имел единую структуру для различных
// // модулей сайта, но в разных местах давал возможность вызывать разные методы.

const user = {
    name: 'unregistered',
    status: 'unregistered',
    email: 'no email',
    credit: 0,
    basket: basket.init(),
    register(name, email) {
        this.name = name
        this.status = 'registered'
        this.email = email
        return this
    },
    addToBasket(item) {
        this.basket.addItem(item)
        console.log(`${this.name} added ${item.name} to basket`)
    },
    minusFromBasket(item) {
        this.basket.minusItem(item)
        console.log(`${this.name} reduced ${item.name} from basket`)
    },
    removeFromBasket(item) {
        this.basket.removeItem(item)
        console.log(`${this.name} removed ${item.name} from basket`)
    },
    addCredit(amount) {
        this.credit += amount
        console.log(`${this.name} added ${amount} to her credit, now his/her credit is ${this.credit}`)
    },
    checkout() {
        let itemsToPurchase = this.basket.showItems()
        let basketAmount = this.basket.countBasketPrice()
        if (this.basket.isEmpty()) {
            console.log('your basket is empty')
        }
        else if (this.credit >= basketAmount && !this.basket.isEmpty()) {
            this.credit -= basketAmount
            console.log(`${this.name} purchased ${itemsToPurchase} for ${basketAmount}`)
            this.basket.items = []
        }
        else {
            console.log(`sorry, your credit is not enough for proceeding this order`)
        }
    }
}

let tetyaGlasha = user
console.log(tetyaGlasha.name)
tetyaGlasha.register('tёtya Glasha', 'sexygirl@gmail.com')
console.log(tetyaGlasha.name)
console.log(tetyaGlasha.basket.showItems())
tetyaGlasha.addToBasket(potato)
tetyaGlasha.addToBasket(potato)
tetyaGlasha.addToBasket(spam)
tetyaGlasha.addToBasket(spam)
tetyaGlasha.addToBasket(eggs)
tetyaGlasha.minusFromBasket(eggs)
tetyaGlasha.removeFromBasket(spam)
tetyaGlasha.addCredit(200)
console.log(tetyaGlasha.basket.showItems())
tetyaGlasha.checkout()
console.log(tetyaGlasha.credit)
tetyaGlasha.checkout()
tetyaGlasha.addToBasket(potato)
tetyaGlasha.addToBasket(potato)
tetyaGlasha.addToBasket(spam)
tetyaGlasha.addToBasket(spam)
console.log(tetyaGlasha.credit)
tetyaGlasha.addCredit(890)
tetyaGlasha.checkout()
tetyaGlasha.addCredit(10)
tetyaGlasha.checkout()
console.log(tetyaGlasha.credit)

