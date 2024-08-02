from django.shortcuts import render,redirect,get_object_or_404
from book.models import Product
from . models import Rate,RateMovie
from django.core.exceptions import ObjectDoesNotExist


def _rate_id(request):
    rate=request.session.session_key
    if not rate:
        rate=request.session.create()
    return rate
def add_rate(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        rate=Rate.objects.get(rate_id=_rate_id(request))
    except Rate.DoesNotExist:
        rate=Rate.objects.create(
            rate_id=_rate_id(request)
        )
        rate.save()
    try:
        rate_movie=RateMovie.objects.get(product=product,rate=rate)
        if rate_movie.quantity < rate_movie.product.stock:
            rate_movie.quantity +=1
        rate_movie.save()
    except RateMovie.DoesNotExist:
        rate_movie=RateMovie.objects.create(
            product=product,
            quantity=1,
            rate=rate
        )
        rate_movie.save()
    return redirect('rate:rate_detail')
def rate_detail(request,total=0,counter=0,rate_movies=None):
    try:
        rate=Rate.objects.get(rate_id=_rate_id(request))
        rate_movies=RateMovie.objects.filter(rate=rate,active=True)
        for rate_movie in rate_movies:
            # total+=(rate_movie.product.price * cart_item.quantity)
            counter +=rate_movie.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'rate.html',dict(rate_movies=rate_movies,total=total,counter = counter))

def rate_remove(request,product_id):
    rate=Rate.objects.get(rate_id=_rate_id(request))
    product=get_object_or_404(Product,id=product_id)
    rate_movie=RateMovie.objects.get(product=product,cart=cart)
    if rate_movie.quantity>1:
        rate_movie.quantity -=1
        rate_movie.save()
    else:
        rate_movie.delete()
    return  redirect('rate:rate_detail')
# def full_remove(request,product_id):
#     cart=Cart.objects.get(cart_id=_cart_id(request))
#     product=get_object_or_404(Product,id=product_id)
#     cart_item=CartItem.objects.get(product=product,cart=cart)
#     cart_item.delete()
#     return  redirect('cartapp:cart_detail')


# def make_payment(request):
#     cart = Cart.objects.get(cart_id=_cart_id(request))
#     product = get_object_or_404(Product, id=product_id)
#     cart_item = CartItem.objects.get(product=product, cart=cart)
#     cart_item.save()
#     return redirect('cartapp:cart_detail')
