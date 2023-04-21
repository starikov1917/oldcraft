

var CART_KEY = "cart3"


function is_in_cart(carti, slug) {
    return slug in carti
}

function increment_basket_counter(){
    basket =  $(".basket-value")
    old_value = parseInt(basket.text())

    render_basket_value(old_value + 1)
}

function decrement_basket_counter(){
    basket =  $(".basket-value")
    old_value = parseInt(basket.text())
    render_basket_value(old_value - 1)
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
        element_for_deleting = $("#" + product_slug)
        element_for_deleting.attr("id", "")
        element_for_deleting.addClass("hiden")
        var price = $('#' + product_slug + "-subtotal")
        render_total_cost(-1 * parseFloat(price[0].textContent), true)
        if (!(cart3) || (Object.keys(cart3).length === 0 && cart3.constructor === Object))  {
            $(".basket").addClass("hiden")
            $("#empty-basket-label").removeClass("hiden")

        }
        setTimeout(function(){
            element_for_deleting.remove()
        }, 250)
    }
    localStorage.setItem(CART_KEY, JSON.stringify(cart3))
    decrement_basket_counter()
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
            increment_basket_counter()


        }
    }

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
        console.log("сколько прибавить",value)
        temp_value = parseFloat($(".total").text()) + value
        $(".total").text(temp_value.toFixed(2))

    } else {
        $(".total").text(value.toFixed(2))
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
        for (slug in cart) {



            var clone = template.content.cloneNode(true);
            var row = clone.querySelectorAll(".basket-item")
            row[0].setAttribute("id", slug)
            var del_button = clone.querySelectorAll(".del-btn")
            del_button[0].setAttribute("data-slug", slug)
            var title = clone.querySelectorAll(".basket-item__name")
            title[0].setAttribute("id", slug)
            var quantity = clone.querySelectorAll(".count-current__value")
            quantity[0].value = cart[slug]['quantity']
            quantity[0].setAttribute("data-slug", slug)

            quantity[0].setAttribute("id", slug)

            var image = clone.querySelectorAll("img")
            image[0].setAttribute("id", slug + "-img")

            var price = clone.querySelectorAll(".subtotal")
            price[0].setAttribute("id", slug + "-subtotal")





            $.ajax({
            url: 'http://localhost:8000/api/v1/product/' + slug + "/",
            type: 'get',
            success: function(response){

                var title = $("#" + response.slug + " .basket-item__name")
                console.log(response)
                title[0].textContent = response.title



                var image = $("#" + response.slug + "-img")

                var price = $('#' + response.slug + "-subtotal")


                // тут запросить по АПИ настоящее изображение
                //image.attr("src", response.titlePhoto)

                var quantity_input = $("#" + response.slug + " .count-current__value")
                quantity_input[0].setAttribute("data-max", response.availableQuantity)
                quantity_input[0].setAttribute("data-price", response.price)



                if (quantity_input[0].value > response.availableQuantity)    {
                    quantity_input[0].value = response.availableQuantity
                }

                sub_sum = response.price * quantity_input[0].value
                price[0].textContent = sub_sum.toFixed(2)
                render_total_cost(sub_sum, true)

                if (response.availableQuantity == 0) {
                    var temp_row = $(".basket-item #" + response.slug)
                    delete_from_cart(response.slug)
                }





            }
            })

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

      if (new_val != value) {
            var sub_sum = $("#"+ slug + '-subtotal')
            sub_sum[0].textContent = (parseFloat(sub_sum[0].textContent) + quantity *  parseFloat(price)).toFixed(2)
            render_total_cost(quantity * parseFloat(price), true)

      }
      add_to_cart(slug, price, quantity, parseInt(max), "product_title")

})





