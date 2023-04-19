from .settings import CART_SESSION_ID


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get[CART_SESSION_ID]
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item["total_price"] = item["price"] * item['quantity']
            yield item


    def __len__(self):
        return self.cart.__len__()



    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': product.price}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def get_total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
