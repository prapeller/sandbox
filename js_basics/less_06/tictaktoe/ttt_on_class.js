'use strict';

class TicTacToe {
    constructor() {
        this.gameTableElement = document.getElementById('game');
        this.status = 'playing';
        this.phase = 'X';
        this.mapValues = [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ];
        this.init();
    }

    static sum(a, b) {
        return a + b;
    }

    init() {
        this.renderMap();
        this.initEventHandlers();
    }

    renderMap() {
        for (let row = 0; row < 3; row++) {
            const tr = document.createElement('tr');
            this.gameTableElement.appendChild(tr);

            for (let col = 0; col < 3; col++) {
                const td = document.createElement('td');
                tr.appendChild(td);
                td.dataset.row = row.toString();
                td.dataset.col = col.toString();
            }
        }
    }

    initEventHandlers() {
        this.gameTableElement
            .addEventListener('click', (event) => this.cellClickHandler(event));
    }

    cellClickHandler(event) {
        if (!this.isCorrectClick(event)) return;

        this.fillCell(event);

        if (this.hasWon()) {
            this.setStatusStopped();
            this.sayWonPhrase();
        }

        this.togglePhase();
    }

    setStatusStopped() {
        this.status = 'stopped';
    }

    sayWonPhrase() {
        const figure = this.phase === 'X' ? 'Крестики' : 'Нолики';

        alert(figure + ' выйграли!');
    }

    isCorrectClick(event) {
        return this.isStatusPlaying()
            && this.isClickByCell(event)
            && this.isCellEmpty(event);
    }

    isStatusPlaying() {
        return this.status === 'playing';
    }

    isClickByCell(event) {
        return event.target.tagName === 'TD';
    }

    isCellEmpty(event) {
        const row = +event.target.dataset.row;
        const col = +event.target.dataset.col;

        return this.mapValues[row][col] === '';
    }

    fillCell(event) {
        const row = +event.target.dataset.row;
        const col = +event.target.dataset.col;

        this.mapValues[row][col] = this.phase;
        event.target.textContent = this.phase;
    }

    togglePhase() {
        this.phase = this.phase === 'X' ? '0' : 'X';
    }

    hasWon() {
        var col0 = this.mapValues.reduce((result, row) => result + row[0], '')
        var col1 = this.mapValues.reduce((result, row) => result + row[1], '')
        var col2 = this.mapValues.reduce((result, row) => result + row[2], '')
        var row0 = this.mapValues[0].reduce((result, col) => result + col, '')
        var row1 = this.mapValues[1].reduce((result, col) => result + col, '')
        var row2 = this.mapValues[2].reduce((result, col) => result + col, '')
        var diag1 = '' + this.mapValues[0][0] + this.mapValues[1][1] + this.mapValues[2][2]
        var diag2 = '' + this.mapValues[0][1] + this.mapValues[1][1] + this.mapValues[2][0]

        const vars = [col0, col1, col2, row0, row1, row2, diag1, diag2]
        return (vars.includes('XXX') || vars.includes('000'))
    }
}

const game = new TicTacToe();
