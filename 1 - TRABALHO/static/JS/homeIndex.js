function embedGlobalScope () {
    const routerButtonLogin = document.querySelector('#Login')
    const routerButtonCreateAccount = document.querySelector('#CreateAccount')

    routerButtonLogin.addEventListener('click', (e) => {
        window.location.href="{{ url_for('login') }}"
    })
    routerButtonCreateAccount.addEventListener('click', (e) => {
        window.location.href
    })
}
embedGlobalScope()