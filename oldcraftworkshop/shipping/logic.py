from address.models import Location


def calculate_postage(location_pk, weight, subtotal):
    print("location ", location_pk, " weight ", weight, " subtotal ", subtotal)
    location = Location.objects.filter(pk=location_pk).first()
    if location.isEU:
        if subtotal <= 150:
            return get_boxette_price(location_pk, weight)
        else:
            return get_gpost_price(location.gpostCode, weight)
    else:
        return min(get_gpost_price(location.gpostCode, weight), get_boxette_price(location_pk, weight))


def get_gpost_price(gpostCode, weight):
    return 111


def get_boxette_price(pk, weight):
    return 222
