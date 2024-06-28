from decimal import Decimal
from django.conf import settings
from .models import Mancuerna

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, mancuerna, quantity=1, update_quantity=False):
        mancuerna_id = str(mancuerna.id)
        if mancuerna_id not in self.cart:
            self.cart[mancuerna_id] = {'quantity': 0, 'price': str(mancuerna.precio)}
        if update_quantity:
            self.cart[mancuerna_id]['quantity'] = quantity
        else:
            self.cart[mancuerna_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, mancuerna):
        mancuerna_id = str(mancuerna.id)
        if mancuerna_id in self.cart:
            del self.cart[mancuerna_id]
            self.save()

    def __iter__(self):
        mancuerna_ids = self.cart.keys()
        mancuernas = Mancuerna.objects.filter(id__in=mancuerna_ids)
        for mancuerna in mancuernas:
            self.cart[str(mancuerna.id)]['mancuerna'] = mancuerna

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True