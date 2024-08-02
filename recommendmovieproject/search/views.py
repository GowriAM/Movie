from django.shortcuts import render
from book.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'search.html', {'message': 'Please enter a search term.'})
    else:
        products=Product.objects.all().filter(Q(name__contains=query) |  Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})

# def SearchResult(request):
#     products=None
#     Query=None
#     if 'q' in request.GET:
#         query=request.GET.get('q')
#         products=Product.objects.all().filter(Q(name__contains=query) |  Q(description__contains=query))
#         return render(request,'search.html',{'query':query,'products':products})
