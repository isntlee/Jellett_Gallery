from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    """ Creates here the initial logic/equations"""
    """that dictate the later checkout transactions """

    bag_items = []
    total = 0
    delivery = 0
    grand_total = 0
    product_count = 0
    delivery_percentage = 10
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.offer
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

            if request.user.is_authenticated:
                delivery = 0
            else:
                delivery = (total/delivery_percentage)

            grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
