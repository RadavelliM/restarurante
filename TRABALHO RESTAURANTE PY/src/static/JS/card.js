function embedGlobalScope() {

    function IndexCard() {

        this.start = () => {
            this.setupBuyButtons()
        }

        this.setupBuyButtons = () => {
            const buttons = document.querySelectorAll('.buttonBuy')

            buttons.forEach(button => {
                button.addEventListener('click', () => {

                    const card = button.closest('.card')
                    const priceSpan = card.querySelector('.info p span')
                    const title = card.querySelector('.info h1').textContent

                    let price = parseFloat(priceSpan.textContent.replace(',', '.'))

                    let quantity = prompt(`Quantas unidades de "${title}" deseja adicionar?`)

                    if (quantity === null) return

                    quantity = parseInt(quantity)

                    if (isNaN(quantity) || quantity <= 0) {
                        alert("Informe uma quantidade válida!")
                        return
                    }

                    let total = (price * quantity).toFixed(2)

                    this.createOrderItem(title, quantity, total)
                })
            })
        }

        this.createOrderItem = (title, quantity, total) => {
            const container = document.querySelector('#orderSummary')

            container.style.display = "flex"

            // Criar a div do pedido
            const div = document.createElement('div')
            div.classList.add('orderItem')

            div.innerHTML = `
                <div>
                    <strong>${quantity}x ${title}</strong><br>
                    Total: R$ <span class="orderPrice" >${total.replace('.', ',')}</span>
                </div>

                <button class="removeOrder">Remover</button>
            `

            div.querySelector('.removeOrder').addEventListener('click', () => {
                div.remove()
                this.checkIfEmpty()
            })
            container.appendChild(div)

            this.createOrder()
        }

        this.createOrder = () => {
            const order = document.querySelector('.confirmOrder')
            order.style.display = "grid";
        }

        this.checkIfEmpty = () => {
            const container = document.querySelector('#orderSummary')
            const order = document.querySelector('.confirmOrder')
            if (container.children.length === 0) {
                container.style.display = "none"
                order.style.display = "none"
            }
        }
    }

    window.addEventListener('DOMContentLoaded', () => {
        const index = new IndexCard()
        index.start()
    })
}

embedGlobalScope()
