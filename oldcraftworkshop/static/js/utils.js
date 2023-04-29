
var CART_KEY = "cart3"
var base_url = 'http://localhost:8000/'


function is_in_cart(carti, slug) {
    return slug in carti
}

function increment_basket_counter(){
    element = document.querySelector(".basket-value")    
    old_value = parseInt(element.innerHTML)
    element.innerHTML = old_value + 1
}

function decrement_basket_counter(){
    element = document.querySelector(".basket-value")    
    old_value = parseInt(element.innerHTML)
    element.innerHTML = old_value - 1
}




function init_catalog_listeners(){
    document.querySelectorAll(".add_from_catalog").forEach(element => element.addEventListener("click", () => {
        const max = element.getAttribute('data-max')
        const price = element.getAttribute('data-price')
        const slug = element.getAttribute('data-slug')
        const title = document.querySelector(`#${slug}`).innerHTML
        add_to_cart(slug, price, 1, max, title)   
    }))
    document.querySelector(".modal-added-item").addEventListener("click", ()=> document.querySelector(".modal-added-item").classList.add("hiden"))
}


function init_card_listeners(){
    document.querySelectorAll(".add_from_card").forEach(element => {
        element.addEventListener("click", ()=>{
            const max = element.getAttribute('data-max')
            const price = element.getAttribute("data-price")
            const slug = element.getAttribute('data-slug')
            const quantity = parseInt(document.querySelector(".count-current__value").value)
            const title = document.querySelector(".title").innerHTML
            add_to_cart(slug, price, Number(quantity), max, title)
        })        
    })
}


function showAdds(){
    if (sessionStorage.getItem("addsShowed") == 'true'){

    } else {
        document.querySelector(".modal-added-item").classList.remove("hiden")
        sessionStorage.setItem("addsShowed", true)
    }
}





function Get_cart_len() {
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))
    return cart3?Object.keys(JSON.parse(localStorage.getItem(CART_KEY))).length:0
}

function added_to_cart_notification(text, description){
    if (a = document.querySelector(".modal-added-item")) {
        a.classList.remove("hiden")    
        document.querySelector(".status-text").innerHTML = text
        document.querySelector(".status-desc").innerHTML = description
    } else { console.log("мы не в каталоге")}
}

function render_basket_value(value){
    document.querySelector(".basket-value").innerHTML = value
}

function render_empty_cart() {
        document.querySelector(".basket").classList.add("hiden")
        document.querySelector("#empty-basket-label").classList.remove("hiden")
}


function delete_from_cart(product_slug) {
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))
    if (cart3) {
        delete cart3[product_slug]
        const element_for_deleting = document.querySelector(`#${product_slug}`)                
        element_for_deleting.setAttribute("id", "")
        element_for_deleting.classList.add("hiden")
    
        const price = document.querySelector(`#${product_slug}-subtotal`)
        setTimeout(function(){
            element_for_deleting.remove()
        }, 250)

        render_total_cost(-1 * parseFloat(price.innerHTML), true)
        if (!(cart3) || (Object.keys(cart3).length === 0 && cart3.constructor === Object))  {        
            setTimeout(function(){render_empty_cart()},250)
        }
    }
    localStorage.setItem(CART_KEY, JSON.stringify(cart3))
    decrement_basket_counter()
}





function add_to_cart(product_slug, price, quantity, max, product_title){
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))
    if (cart3 == null){
        cart3 = {}
    }
    if (product_slug in cart3) {

        if (cart3[product_slug]["quantity"] + quantity > max){
            cart3[product_slug]["quantity"] = max
            added_to_cart_notification(product_title, "The maximum available quantity has been added to the cart")
        } else if (cart3[product_slug]["quantity"] + quantity < 1) {
            cart3[product_slug]["quantity"] = 1
        } else {
            cart3[product_slug]["quantity"] += quantity
            added_to_cart_notification(product_title, "Item added to cart")
        }

    } else {
        if (quantity > 0) {
            cart3[product_slug] = {}
            cart3[product_slug]["quantity"] = quantity
            cart3[product_slug]["price"] = price
            added_to_cart_notification(product_title)
            increment_basket_counter()


        }
    }
    localStorage.setItem(CART_KEY, JSON.stringify(cart3))
}




function render_total_cost(value, update_mode){
    const element = document.querySelector(".total")
    const new_value = value + (update_mode?parseFloat(element.innerHTML):0) 
    element.innerHTML = new_value.toFixed(2)
}



function renderCart(){
    cart = JSON.parse(localStorage.getItem(CART_KEY))
    const basket_body = document.querySelector(".basket-body");
    const template = document.querySelector('#basketrow');
    var total_cost = 0
    if (!(cart) || (Object.keys(cart).length === 0 && cart.constructor === Object))  {
        render_empty_cart()
    } else {
        for (slug in cart) {            
            const clone = template.content.cloneNode(true);
            const row = clone.querySelector(".basket-item")
            row.setAttribute("id", slug)
            const del_button = clone.querySelector(".del-btn")
            del_button.setAttribute("data-slug", slug)
            const temp = slug
            const title = clone.querySelector(".basket-item__name")
            title.setAttribute("id", `${slug}-title`)
            const quantity = clone.querySelector(".count-current__value")
            quantity.value = cart[slug]['quantity']
            quantity.setAttribute("data-slug", slug)
            quantity.setAttribute("id", `${slug}-quantity`)
            const image = clone.querySelector("img")
            image.setAttribute("id", `${slug}-img`)
            const price = clone.querySelector(".subtotal")
            price.setAttribute("id", `${slug}-subtotal`)
            
            fetch(`${base_url}api/v1/product/${slug}/`)
                .then(response => response.json())
                .then(data => {
                    const temp_slug = data.slug
                    const title = document.querySelector(`#${temp_slug}-title`)
                    title.textContent = data.title
                    document.querySelector(`#${temp_slug}-img`).setAttribute('src', data.titlePhoto.image)  
                    const quantity_input = document.querySelector(`#${temp_slug}-quantity`)
                    quantity_input.setAttribute("data-max", data.availableQuantity)
                    quantity_input.setAttribute("data-price", data.price)
                    if (quantity_input.value > data.availableQuantity)    {
                        quantity_input.value = data.availableQuantity
                    }
                    const price = document.querySelector(`#${temp_slug}-subtotal`)
                    const sub_sum = data.price * quantity_input.value
                    price.textContent = sub_sum.toFixed(2)
                    render_total_cost(sub_sum, true)
                    if (data.availableQuantity == 0) {
                        delete_from_cart(temp_slug)
                    }
                })
            basket_body.appendChild(clone)
        }

        document.querySelectorAll(".del-btn")
            .forEach(x => x.addEventListener("click", () => {        
                delete_from_cart(x.getAttribute("data-slug"))

            }))        
        render_total_cost(total_cost, false)
    }

    console.log(document.querySelectorAll(".add-from-basket"))
    // добавляем ивент-лисенеры
    document.querySelectorAll(".add-from-basket").forEach(button => {
        button.addEventListener("click" , function() {
            const type = button.getAttribute('data-type');
            const input = button.closest('.count-current').querySelector("input");        
            const max = input.getAttribute('data-max');            
            const price = input.getAttribute('data-price')
            const slug =  input.getAttribute('data-slug')
            const value = parseInt(input.value);
            var new_val = 0
            var quantity
            if (type == 'plus'){
                  new_val = Math.min(value + 1, parseInt(max))
                  input.value = new_val
                  quantity = 1
            }

            if (type == 'minus'){
                  new_val = Math.min(Math.max(1, value - 1))
                  input.value = new_val
                  quantity = -1
            }
            if (new_val != value) {
                  const sub_sum = document.querySelector(`#${slug}-subtotal`)                                             
                  sub_sum.innerHTML = (parseFloat(sub_sum.innerHTML) + quantity *  parseFloat(price)).toFixed(2)
                  render_total_cost(quantity * parseFloat(price), true)
            }
            add_to_cart(slug, price, quantity, parseInt(max), "product_title")
        
        })
    })
}


function calculateShippingCost(){
    if (localStorage.getItem("chosen-location") && localStorage.getItem("weight"))  {
        const location = JSON.parse(localStorage.getItem(localStorage.getItem("chosen-location")))        
        const weight = localStorage.getItem("weight")
        console.log("calculate shipping cost: ", location.gpostCode, weight)
        fetch(`${base_url}api/v1/shippingCost/`, {
            
            headers: {
                'X-CSRFToken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
                "Content-Type": "application/json",
            },
            
            body: JSON.stringify({
                weight: weight,
                gpostCode: location.gpostCode
            }),
            method:"POST",
        })      
            .then(response =>  {
                if (response.ok) {
                    return response.json()
                }

            }) 
            .then(data =>{
                localStorage.setItem("shippingCost", data.shippingCost)
                document.getElementById("shippingCost").value = data.shippingCost
                const subtotal = parseFloat(localStorage.getItem("subtotal"))
                const shippingCost = parseFloat(data.shippingCost)
                document.getElementById("totalCost").value = subtotal + shippingCost
            })
    }



}



function  render_empty_checkout(){

        document.querySelector(".checkout").classList.add("hiden")
        document.querySelector(".").classList.add("hiden")

}
//инициализируем чекаут

function initCheckout(){
    const loc = document.getElementById("location-filter")
    const slctr = document.getElementById("location-selector")
    const cart = localStorage.getItem(CART_KEY)
    if (!(cart) || (Object.keys(cart).length === 0 && cart.constructor === Object))  {
        render_empty_checkout()
    } else {


        
        

        fetch(`${base_url}api/v1/location/`)
            .then(response => {
                if (response.ok) {
                    return response.json()
                }            
            })
            .then(data => {
                console.log(data)
                const locationsWrapper = document.getElementById("loc-list")
                loc_option_template = document.getElementById("loc-template")
                data.forEach((loc) => {
                    const clone = loc_option_template.content.cloneNode(true)
                    const option = clone.querySelector(".option")
                    option.textContent = loc.title
                    locationsWrapper.appendChild(clone)
                    localStorage.setItem(loc.title, JSON.stringify(loc))                
                    console.log(loc.synonims)
                    option.addEventListener("click", (event)=> {            
                        localStorage.setItem("chosen-location", event.target.textContent)
                        loc.value = event.target.textContent
                        slctr.classList.add("hide-option")
                        slctr.classList.remove("show-option")
                        calculateShippingCost()
                        console.log("click")
                    })
                })
            })

                
        if (localStorage.getItem("chosen-location")){ 
            loc.value = localStorage.getItem("chosen-location")
            calculateShippingCost()
        }

        const cart = {cart: localStorage.getItem(CART_KEY)}

        fetch(`${base_url}api/v1/cartWeight/`, {
            
            headers: {
                'X-CSRFToken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
                "Content-Type": "application/json",
            },
            
            body: JSON.stringify(cart),
            method:"POST",
        })      
            .then(response =>  {
                if (response.ok) {
                    return response.json()
                }

            })        
            .then(data => {
                localStorage.setItem("weight", data.weight)
                localStorage.setItem("subtotal", data.subtotal)
                console.log(data.weight)
                document.getElementById("weight").value = data.weight
                document.getElementById("subtotal").value = data.subtotal

        })



        




        slctr.classList.add("hide-option")






    const filt = (event) => {
            slctr.classList.add("show-option")
            document.querySelectorAll(".option").forEach(option => {

            var matched = option.innerHTML.toLowerCase().includes(event.target.value.toLowerCase())
            const synonims = JSON.parse(localStorage.getItem(option.innerHTML)).synonims.map(s => s.toLowerCase())
            synonims.forEach(synonim => {
                matched = matched || synonim.includes(event.target.value.toLowerCase())
            })

            if (matched){
                option.classList.remove("hide-option")
                option.classList.add("show-option")
            } else {
                option.classList.add("hide-option")
                option.classList.remove("show-option")
            }
        })
    }

        loc.addEventListener("focus", ()=> slctr.classList.add("show-option"), )
        loc.addEventListener("blur", ()=> {
            console.log("lost-focus")

            setTimeout(()=> {
                console.log(loc.value)
                if (localStorage.getItem("chosen-location")){
                    loc.value = localStorage.getItem("chosen-location")
                }

                slctr.classList.add("hide-option")
                slctr.classList.remove("show-option")},
                200)
        })

        loc.addEventListener("input", filt)

    }
}




