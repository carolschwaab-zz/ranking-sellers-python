from operator import itemgetter

class SellersRancking:
    def best_seller(self, sellers):
        seller_first = [max(sellers, key=itemgetter('value'))['name']] if sellers else []

        return seller_first

    def rancking_list(self, sellers):

        sellers.sort(key=lambda elem: elem['value'], reverse=True)

        return [seller['name'] for seller in sellers]

    def best_seller_store(self, sellers, store):

        return self.best_seller([seller for seller in sellers if seller['store'] == store])

    def sales_goals(self, sellers):

        return [sellers['name'] for sellers in (sorted(sellers, key=itemgetter('value'))) if sellers['value'] < 500]


