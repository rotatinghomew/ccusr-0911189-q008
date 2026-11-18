def spent(offers, orders, budget):
    catalog = {offer['id']:offer for offer in offers}
    total = 0
    booked = set()
    for order in orders:
        item = catalog[order['offer']]
        key = item['network'],item['window'],item['slot']
        if key in booked:
            raise ValueError('已购安排占用同一时段')
        booked.add(key)
        total += order['paid']
    return {'spent':total,'remaining':budget-total}
