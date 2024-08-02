from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

from .forms import ReviewForm
from  . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def allProdCat(request,c_slug=None):
    global products
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page)
    else:
        products_list=Product.objects.all().filter()
    paginator=Paginator(products_list,6)
    try:
            page=int(request.GET.get('page','1'))
    except:
            page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
            products=paginator.page(paginator.num_pages)

    return  render(request,"category.html",{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):

    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return  render(request,'product.html',{'product':product})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    reviews = item.reviews.all()
    return render(request, 'item_detail.html', {'item': item, 'reviews': reviews})

@login_required
def add_review(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.user = request.user
            review.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'item': item})