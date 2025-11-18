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
            const container = document.getElementById('orderSummary')

            container.style.display = "flex"

            // Criar a div do pedido
            let div = document.createElement('div')
            div.classList.add('orderItem')

            div.innerHTML = `
                <div>
                    <strong>${quantity}x ${title}</strong><br>
                    Total: R$ ${total.replace('.', ',')}
                </div>

                <button class="removeOrder">Remover</button>
            `

            // Botão remover
            div.querySelector('.removeOrder').addEventListener('click', () => {
                div.remove()
                this.checkIfEmpty()
            })

            container.appendChild(div)
        }

        this.checkIfEmpty = () => {
            const container = document.getElementById('orderSummary')
            if (container.children.length === 0) {
                container.style.display = "none"
            }
        }
    }

    window.addEventListener('DOMContentLoaded', () => {
        const index = new IndexCard()
        index.start()
    })
}

embedGlobalScope()
