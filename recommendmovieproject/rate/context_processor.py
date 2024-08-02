from .models import RateMovie, rate, Rate
from  . views import _rate_id
def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            rate=Rate.objects.filter(rate_id=_rate_id(request))
            rat_movies=RateMovie.objects.all().filter(rate=rate[:1])
            for rate_item in rat_movies:
                item_count += rate_item.quantity
        except Rate.DoesNotExist:
            item_count=0
    return  dict(item_count=item_count)
