function embedGlobalScope() {
    const getMenuSideBar = document.querySelector('.menu').addEventListener('click', (e) => {
        const getMenu = document.querySelector('.sidenav').style.width = "250px";
    })

    const closebtn = document.querySelector('.closebtn').addEventListener('click', (e) => {
        const getMenu = document.querySelector('.sidenav')
        getMenu.style.width = "0px";
    })

    const checkResizeNavbarOpen = window.addEventListener('resize', (e) => {
        const getMenu = document.querySelector('.sidenav');
        const getStyle = window.getComputedStyle(getMenu);

        if (getStyle.width > "0") {
            getMenu.style.width = "0px";
        }
    })

    const closeNavbarOnClick = window.addEventListener('click', (e) => {
        if (!e.target.classList.contains("sidenav") && !e.target.classList.contains("menu") ) {
            const getMenu = document.querySelector('.sidenav');
            const getStyle = window.getComputedStyle(getMenu);

            if (getStyle.width > "0") {
                getMenu.style.width = "0px";
            }
        }
    })
}
embedGlobalScope()