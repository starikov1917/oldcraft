

var CART_KEY = "cart3"


function is_in_cart(carti, slug) {
    return slug in carti
}


$(document).on("click" , ".add_from_catalog", function() {
    var max = $(this).attr('data-max')

    var price = $(this).attr('data-price')
    var slug =  $(this).attr('data-slug')


    var title = $("#" + slug).text()


    add_to_cart(slug, price, 1, max, title)

})



$(document).on("click" , ".add_from_card", function() {
    var max = $(this).attr('data-max')
    var price = $(this).attr('data-price')
    var slug =  $(this).attr('data-slug')
    var quantity = $(".count-current__value").val()
    var title = $(".title ").text()
    console.log(title)
    add_to_cart(slug, price, Number(quantity), max, title)
})







function Get_cart_len() {
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))

    return cart3?Object.keys(JSON.parse(localStorage.getItem(CART_KEY))).length:0
}

function added_to_cart_notification(text, description){
    $(".modal-added-item").removeClass("hiden")
    $(".status-text").text(text)
    $(".status-desc").text(description)
}

function render_basket_value(value){
    $(".basket-value").text(value)
}

function render_empty_cart() {
        body = $(".basket")
        body.replaceWith("<p>Your cart is empty</p>")
}


function delete_from_cart(product_slug) {
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))
    if (cart3) {
        delete cart3[product_slug]
        $("#" + product_id).remove()
    }
    localStorage.setItem(CART_KEY, JSON.stringify(cart3))
    //render_empty_cart()
}





function add_to_cart(product_id, price, quantity, max, product_title){
    cart3 = JSON.parse(localStorage.getItem(CART_KEY))
    if (cart3 == null){
        cart3 = {}
    }
    if (is_in_cart(cart3, product_id))  {
        if (cart3[product_id]["quantity"] + quantity > max){
            cart3[product_id]["quantity"] = max
            added_to_cart_notification(product_title, "The maximum available quantity has been added to the cart")
        } else if (cart3[product_id]["quantity"] + quantity < 1) {

        }else{
            cart3[product_id]["quantity"] += quantity
            added_to_cart_notification(product_title, "Item added to cart")
        }

        } else {
        if (quantity > 0) {
            cart3[product_id] = {}
            cart3[product_id]["quantity"] = quantity
            cart3[product_id]["price"] = price
            added_to_cart_notification(product_title)
        }
    }
    render_basket_value(Object.keys(cart3).length)

    localStorage.setItem(CART_KEY, JSON.stringify(cart3))
}



function get_product_by_slug(slug){
    if (slug == "tunic2") {
    return {"slug": "tunic2",
            "title": "Туника тестовая 2",
            "availableQuantity": 456,
            "titlePhoto": "https://oldcraftworkshop.com/upload/iblock/65c/hrqvw8ai34dca4yovn9xylcbq4uwmrbu.jpg",
            "price": 152.00,}

    } else if (slug == "legwraps1") {
    return {"slug": "legwraps1",
            "title": "Обмотки на ноги 1",
            "availableQuantity": 2,
            "titlePhoto": "https://oldcraftworkshop.com/upload/iblock/65c/hrqvw8ai34dca4yovn9xylcbq4uwmrbu.jpg",
            "price": 49,

    }
    } else if (slug == "tunic3"){

    return {"slug": "tunic3",
            "title": "Туника 3",
            "availableQuantity": 3,
            "titlePhoto": "https://oldcraftworkshop.com/upload/iblock/65c/hrqvw8ai34dca4yovn9xylcbq4uwmrbu.jpg",
            "price": 123,

    }
    }
}

function render_total_cost(value, update_mode){
    if (update_mode) {

    } else {
        $(".basket-summ").text("€" + value)
    }
}


function renderCart(){
    cart = JSON.parse(localStorage.getItem(CART_KEY))
    var basket_body = document.querySelector(".basket-body");
    var template = document.querySelector('#basketrow');
    var total_cost = 0
    if (!(cart) || (Object.keys(cart).length === 0 && cart.constructor === Object))  {
        render_empty_cart()
    } else {
        for (product_id in cart) {
            var product = get_product_by_slug(product_id)
            console.log(cart[product_id])
            total_cost += product.price * cart[product_id]["quantity"]
            var clone = template.content.cloneNode(true);

            var row = clone.querySelectorAll(".basket-item")
            row[0].setAttribute("id", product_id)


            var title = clone.querySelectorAll(".basket-item__name")
            title[0].textContent = product.title

            var quantity = clone.querySelectorAll(".count-current__value")
            quantity[0].value = cart[product_id]['quantity']
            quantity[0].setAttribute("data-slug", product_id)
            quantity[0].setAttribute("data-price", product.price)
            quantity[0].setAttribute("data-max", product.availableQuantity)

            var photo = clone.querySelectorAll(".basket-item__preview img")
            photo[0].setAttribute("src", product.titlePhoto)


            var price = clone.querySelectorAll(".basket-item__summ")
            console.log(price[0])
            price[0].textContent = "€" + product.price

            var del_button = clone.querySelectorAll(".del-btn")
            del_button[0].setAttribute("data-slug", product_id)
            basket_body.appendChild(clone)
        }

        render_total_cost(total_cost, false)
    }

}




$(document).on("click" , ".del-btn", function() {
    delete_from_cart($(this).attr("data-slug"))
})



$(document).on("click" , ".add-from-basket", function(element) {
  var type = $(this).attr('data-type');
  var input = $(this).closest('.count-current').find('input');
  var min = input.attr('data-min');
  var max = input.attr('data-max');

  var price = input.attr('data-price')
  var slug =  input.attr('data-slug')
  var value = parseInt(input.val());
  var new_val = 0
  var quantity
  if (type == 'plus'){
        new_val = Math.min(value + 1, parseInt(max))
        input.val(new_val)
        quantity = 1
  }
  if (type == 'minus'){
        new_val = Math.min(Math.max(1, value - 1))
        input.val(new_val)
        quantity = -1
  }

  if (new_val != value) {location.reload()}
  add_to_cart(slug, price, quantity, parseInt(max), "product_title")
  console.log("кликнул тут", slug)


})






