function embedGlobalScope() {

    function Index() {

        this.start = () => {
            this.removeDraggableImage()
            this.openNavBar()
            this.closeNavBar()
            this.closeNavBarOnResize()
            this.closeNavbarOnClickOutside()
        }


        this.removeDraggableImage = () => {
            const getAllImages = document.querySelectorAll('img')
            getAllImages.forEach(image => {
                image.setAttribute('draggable', 'false')
            });
        }

        this.openNavBar = () => {
            const getMenuSideBar = document.querySelector('.menu').addEventListener('click', (e) => {
                const getMenu = document.querySelector('.sidenav').style.width = "250px";
            })
        }

        this.closeNavBar = () => {
            const closebtn = document.querySelector('.closebtn').addEventListener('click', (e) => {
                const getMenu = document.querySelector('.sidenav')
                getMenu.style.width = "0px";
            })
        }

        this.closeNavBarOnResize = () => {
            const checkResizeNavbarOpen = window.addEventListener('resize', (e) => {
                const getMenu = document.querySelector('.sidenav');
                const getStyle = window.getComputedStyle(getMenu);

                if (getStyle.width > "0") {
                    getMenu.style.width = "0px";
                }
            })
        }

        this.closeNavbarOnClickOutside = () => {
            // é por esse motivo que javascript e minha linguagem preferida, que coisa linda de se ver esse codigo
            const closeNavbarOnClick = window.addEventListener('click', (e) => {
                if (!e.target.classList.contains("sidenav") && !e.target.classList.contains("menu")) {
                    const getMenu = document.querySelector('.sidenav');
                    const getStyle = window.getComputedStyle(getMenu);

                    if (getStyle.width > "0") {
                        getMenu.style.width = "0px";
                    }
                }
            })
        }
    }

    const callback = window.addEventListener('DOMContentLoaded', (e) => {
        const renderIndex = new Index()
        renderIndex.start()
    })
}
embedGlobalScope()




