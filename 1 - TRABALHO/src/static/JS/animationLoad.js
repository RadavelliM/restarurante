function embedGlobalScope() {
    function IndexAnimation() {
        this.start = () => {
            this.renderBoxInfoOnDOMContentLoad()
            this.renderFoodsMenuOnDOMContentLoad()
            this.renderAboutOnDOMContentLoad()
            this.renderSocialMediaOnDOMContentLoad()
            this.renderAddressOnDOMContentLoad()
        }

        this.renderFoodsMenuOnDOMContentLoad = () => {

            console.log(123)
            const getFoodsMenu = document.querySelectorAll('.foodsMenus')

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.5
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            getFoodsMenu.forEach(div => {
                observer.observe(div);
            });

        }

        this.renderBoxInfoOnDOMContentLoad = () => {

            console.log(123)
            const getBoxInfo = document.querySelectorAll('.BoxInfo')

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.5
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            getBoxInfo.forEach(div => {
                observer.observe(div);
            });

        }

        this.renderAboutOnDOMContentLoad = () => {

            console.log(123)
            const getAbout = document.querySelectorAll('.about')

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.5
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            getAbout.forEach(div => {
                observer.observe(div);
            });

        }

        this.renderSocialMediaOnDOMContentLoad = () => {

            console.log(123)
            const getSocialMedia = document.querySelectorAll('.socialMedias')

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.5
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            getSocialMedia.forEach(div => {
                observer.observe(div);
            });

        }

        this.renderAddressOnDOMContentLoad = () => {

            console.log(123)
            const getAddress = document.querySelectorAll('.address')

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.5
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            getAddress.forEach(div => {
                observer.observe(div);
            });

        }
    }

    const callback = document.addEventListener('DOMContentLoaded', (e) => {
        const renderAnimation = new IndexAnimation;
        renderAnimation.start()
    })
}
embedGlobalScope()