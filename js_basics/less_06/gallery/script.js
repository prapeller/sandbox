'use strict';
const gallery = {
    settings: {
        previewSelector: '',
        screenBoxClass: 'screenBox',
        screenBox__imageClass: 'screenBox__image',
        screenBox__screenClass: 'screenBox__screen',
        screenBox__closeBtnClass: 'screenBox__close',
        screenBox__closeBtnSrc: 'images/gallery/close.png',
    },

    init(userSettings = {}) {
        Object.assign(this.settings, userSettings);

        document.querySelector(this.settings.previewSelector).addEventListener('click', (event) => {
            if (event.target.tagName !== 'IMG') return;
            this.openImage(event.target.dataset.full_image_url);
        });
    },

    openImage(src) {
        // console.log(src)
        this.createScreenBox().querySelector(`.${this.settings.screenBox__imageClass}`).src = src;
    },

    createScreenBox() {
        const screenBox = document.createElement('div');
        screenBox.classList.add(this.settings.screenBoxClass);

        const screen = document.createElement('div');
        screen.classList.add(this.settings.screenBox__screenClass);
        screenBox.appendChild(screen);

        const closeBtn = new Image();
        closeBtn.classList.add(this.settings.screenBox__closeBtnClass);
        closeBtn.src = this.settings.screenBox__closeBtnSrc;
        closeBtn.addEventListener('click', () => this.close());
        screenBox.appendChild(closeBtn);

        const image = new Image();
        image.classList.add(this.settings.screenBox__imageClass);
        screenBox.appendChild(image);

        document.body.appendChild(screenBox);

        return screenBox;
    },

    close() {
        document.querySelector(`.${this.settings.screenBoxClass}`).remove();
    },
};

gallery.init({previewSelector: '.galleryPreviewBox'})
