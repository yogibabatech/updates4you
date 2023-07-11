from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.program.scrape import productcomp, flipkartProUp
from .models import Product


def home(request):

    if 'productq' in request.method == "POST":
        print("Search2")

        data = request.POST
        data = data.get('productq')
        if Product.objects.filter(product_name__contains = data).exists():
            product = Product.objects.filter(product_name__contains = data).values()
            return render(request, "post.html", {'data':product})


    elif 'searchq' in request.method == "POST":
        print("Search1")
        data = request.POST
        data = data.get('searchq')
        if Product.objects.filter(product_name__contains = data).exists():
            product = Product.objects.filter(product_name__contains = data).values()
            return render(request, "post.html", {'data':product})

        
    else:
        return render(request, "index.html")


def search(request):
    if request.method == 'POST':
        if 'productq' in request.POST:
            minprice = 500
            maxprice = 1500
            data = request.POST
            data = data.get('productq')
            if Product.objects.filter(product_name__contains = data).exists():
                product = Product.objects.filter(product_name__contains = data).values()
                return render(request, "post.html", {'data':product, 'query':data, 'minprice':minprice, 'maxprice':maxprice})
            
            else:
                productcomp(data)
                product = Product.objects.order_by('-created_at').values()[0:10]
                return render(request, "post.html", {'data':product, 'query':data, 'minprice':minprice, 'maxprice':maxprice})


        elif 'sort' in request.POST:
            data = request.POST
            data1 = data.get('sort')
            data2 = data.get('query')
            minprice = 500
            maxprice = 1500

            if data1 == "borated":
                product = Product.objects.filter(product_name__contains = data2).order_by('overall_ratings').values()
                return render(request, "post.html", {'data':product, 'query':data2, 'minprice':minprice, 'maxprice':maxprice})
            elif data1 == "brated":
                product = Product.objects.filter(product_name__contains = data2).order_by('-ratings').values()
                return render(request, "post.html", {'data':product, 'query':data2, 'minprice':minprice, 'maxprice':maxprice})
            elif data1 == "mreview":
                product = Product.objects.filter(product_name__contains = data2).order_by('reviews').values()
                return render(request, "post.html", {'data':product, 'query':data2, 'minprice':minprice, 'maxprice':maxprice})

        elif "min-input" in request.POST:
            print("Filtering Process Command")
            data = request.POST
            data2 = data.get('query')
            minprice = int(data.get('min-input'))
            maxprice = int(data.get('max-input'))
            ratinginput = data.get("ratingFilter")
            print(type(ratinginput))
            if ratinginput == None:
                ratinginput = 0
    
            reviewinput = data.get("reviewFilter")
            if reviewinput == None:
                reviewinput = 0
            product = Product.objects.filter(product_name__contains = data2).filter(price__gte = minprice).filter(price__lte=maxprice).filter(reviews__gte=reviewinput).filter(ratings__gte=ratinginput).values()
            return render(request, "post.html", {'data':product, 'query':data2, 'minprice':minprice, 'maxprice':maxprice, 'ratingvalue':ratinginput, 'reviewvalue':reviewinput})

    else:
         return render(request, "index.html")

    
def singleproduct(request, id):
    prod = Product.objects.filter(id = id).values()
    prod = prod[0]
    scrollprod = Product.objects.all().order_by('?')[0:4]
    return render(request, 'singleproduct.html', {'prod':prod, 'scroll':scrollprod})


def updateProduct(request, id):
    prod = Product.objects.get(id = id)
    link = prod.link
    flipkartProUp(link, id)
    scrollprod = Product.objects.all().order_by('?')[0:4]
    prod = Product.objects.get(id = id)
    return render(request, 'singleproduct.html', {'prod':prod, 'scroll':scrollprod})


def product(request):
    data2 = ""
    minprice = 500
    maxprice = 5000
    prod = Product.objects.all()[0:50]
    return render(request, "post.html", {'data':prod, 'query':data2, 'minprice':minprice})


def about (request):
    return render(request, 'about.html')