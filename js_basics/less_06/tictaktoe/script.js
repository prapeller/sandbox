'use strict';
const ticTacToe = {
    gameTableElement: document.getElementById('game'),
    status: 'playing',
    phase: 'X',
    mapValues: [
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ],

    init() {
        this.renderMap();
        this.initEventHandlers();
    },

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
    },

    initEventHandlers() {
        this.gameTableElement
            .addEventListener('click', (event) => this.cellClickHandler(event));
    },

    cellClickHandler(event) {
        if (!this.isCorrectClick(event)) return;

        this.fillCell(event);

        if (this.hasWon()) {
            this.status = 'stopped';
            this.sayWonPhrase();
        }

        this.togglePhase();
    },


    sayWonPhrase() {
        const figure = this.phase === 'X' ? 'Крестики' : 'Нолики';
        alert(figure + ' выйграли!');
    },

    isCorrectClick(event) {
        return this.isStatusPlaying()
            && this.isClickByCell(event)
            && this.isCellEmpty(event);
    },

    isStatusPlaying() {
        return this.status === 'playing';
    },

    isClickByCell(event) {
        return event.target.tagName === 'TD';
    },

    isCellEmpty(event) {
        const row = +event.target.dataset.row;
        const col = +event.target.dataset.col;

        return this.mapValues[row][col] === '';
    },

    fillCell(event) {
        const row = +event.target.dataset.row;
        const col = +event.target.dataset.col;

        this.mapValues[row][col] = this.phase;
        event.target.textContent = this.phase;
    },

    togglePhase() {
        this.phase = this.phase === 'X' ? '0' : 'X';
    },

    hasWon() {
        let col0 = this.mapValues.reduce((result, row) => result + row[0], '')
        let col1 = this.mapValues.reduce((result, row) => result + row[1], '')
        let col2 = this.mapValues.reduce((result, row) => result + row[2], '')
        let row0 = this.mapValues[0].reduce((result, col) => result + col, '')
        let row1 = this.mapValues[1].reduce((result, col) => result + col, '')
        let row2 = this.mapValues[2].reduce((result, col) => result + col, '')
        let diag1 = '' + this.mapValues[0][0] + this.mapValues[1][1] + this.mapValues[2][2]
        let diag2 = '' + this.mapValues[0][1] + this.mapValues[1][1] + this.mapValues[2][0]

        const vars = [col0, col1, col2, row0, row1, row2, diag1, diag2]
        return (vars.includes('XXX') || vars.includes('000'))
    }

};

ticTacToe.init();
