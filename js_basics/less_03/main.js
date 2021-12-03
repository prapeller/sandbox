'use strict';
let generatedNumbers = [];
let attemptsCount = 0;

function resetGame() {
    attemptsCount = 0;
    generatedNumbers = [];

    while (generatedNumbers.length < 4) {
        const part = Math.floor(Math.random() * 10);
        if (!generatedNumbers.includes(part)) generatedNumbers.push(part);
    }

    console.log(generatedNumbers);
}

function startGame() {
    while (true) {
        const guess = prompt('Угадайте 4 разных целых положительных числа, загаданных компьютером. Введите -1 чтобы выйти');

        if (guess === '-1') return alert('Game Over!');

        if (!isValidGuess(guess)) continue;

        attemptsCount++;

        const result = getGuessResult(guess);

        if (result[0] !== 4) {
            alert('Быки: ' + result[0] + '; Коровы: ' + result[1]);
            continue;
        }

        alert('Поздравляем! Вы угадали число. Количество попыток: ' + attemptsCount);

        if (!confirm('Хотите сыграть еще?')) return alert('Game Over!');

        resetGame();
    }
}

function isValidGuess(guess) {
    if (guess.length !== 4) return false;

    for (let i = 0; i < guess.length; i++) {
        if (isNaN(parseInt(guess[i]))) return false;
    }

    return true;
}

function getGuessResult(guess) {
    const result = [0, 0];

    for (let i = 0; i < guess.length; i++) {
        if (+guess[i] === generatedNumbers[i]) result[0]++;
        else if (generatedNumbers.includes(+guess[i])) result[1]++;
    }

    return result;
}

resetGame();
startGame();

// let basket = [['title1', 5, 300], ['title2', 2, 500], [...]];
