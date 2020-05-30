from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop.forms import ReviewForm, SignupForm, SigninForm
from shop.models import Product, Category,Featured_Ads,count_down_ads,Main_Category,site_settings,order
from shop.serializer import ProductSerializer
from django.db.models import Sum
from shop.gladePay import *


def home(request):
    # if request.META['HTTP_HOST'] != "ecommerce.hem.xyz.np":
    #     return redirect("http://ecommerce.hem.xyz.np")
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    new = Product.objects.filter(active=True).last()
    featued_first = Featured_Ads.objects.first()
    featued_last = Featured_Ads.objects.last()
    ctdown = count_down_ads.objects.last()
    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()
    context = {"products": products, 
                    "categories": categories,
                    "new":new,
                    "featued_first":featued_first,
                    "featued_last":featued_last,
                    "ctdown":ctdown,
                    "shops":shops,
                    "cart_products_sum":cart_products_sum,
                    "cart_products":cart_products,
                    "site_data":site_data}
    return render(request, "shop/index.html", context)


def product_view(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()

    context = {
        "products":products,
        "categories":categories,
        "shops":shops,
        "cart_products_sum":cart_products_sum,
        "cart_products":cart_products,
        "site_data":site_data
    }
    return render(request,"shop/shop.html",context)



def search(request):
    q = request.GET["q"]
    products = Product.objects.filter(active=True, name__icontains=q)
    categories = Category.objects.filter(active=True)
    context = {"products": products,
               "categories": categories,
               "title": q + " - search"}
    return render(request, "shop/list.html", context)


def categories(request, slug):
    cat = Category.objects.get(slug=slug)
    products = Product.objects.filter(active=True, category=cat)
    categories = Category.objects.filter(active=True)
    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()
    context = {"products":products, 
        "categories":categories,
        "cat":cat,
        "shops":shops,
        "cart_products_sum":cart_products_sum,
        "cart_products":cart_products,
        "site_data":site_data}
    return render(request, "shop/shop.html", context)


def detail(request, slug):
    product = Product.objects.get(active=True, slug=slug)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Review saved")
        else:
            messages.error(request, "Invalid form")
    else:
        form = ReviewForm()


    categories = Category.objects.filter(active=True)
    products = Product.objects.filter(active=True)
    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()

    context = {"product" : product,
               "categories":categories,
               "slug":slug,
               "products":products,
                "shops":shops,
                "cart_products_sum":cart_products_sum,
                "cart_products":cart_products,
                "site_data":site_data}

    return render(request, "shop/detail.html", context)


def signup(request):
    if request.method == "POST":
        User.objects.create(username=request.POST['username'],
                            email=request.POST['email'],
                            password=make_password(request.POST['password']))
        messages.success(request, "User saved")
        return redirect("shop:signin")

    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()

    context = {"shops":shops,
            "cart_products_sum":cart_products_sum,
            "cart_products":cart_products,
            "site_data":site_data}    
    
    return render(request, "shop/login-register.html",context)


def signin(request):
    if request.method=="POST":
      
        # username = req.POST["username"]
        # password = req.POST["password"]
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,  password=password)
        email = authenticate(request,email=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("shop:account")
        if email:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("shop:account")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    shops = Main_Category.objects.all()
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    site_data = site_settings.objects.first()

    context = {"shops":shops,
            "cart_products_sum":cart_products_sum,
            "cart_products":cart_products,
            "site_data":site_data}    
    return render(request, "shop/login-register.html", context)


def signout(request):
    logout(request)
    return redirect("shop:signin")


def cart(request, slug):
    """
        data = {"items" : ["slug1", "slug2"],
                "price" : 12342,
                "count" : 5
                }
        request.session["data"] = data
        """
    product = Product.objects.get(slug=slug)
    inital = {"items":[],"price":0.0,"count":0}
    session = request.session.get("data", inital)
    if slug in session["items"]:
        messages.error(request, "Already added to cart")
    else:
        session["items"].append(slug)
        session["price"] += float(product.price)
        session["count"] += 1
        request.session["data"] = session
        messages.success(request, "Added successfully")
    return redirect("shop:detail", slug)


def mycart(request):
    sess = request.session.get("data", {"items":[]})
    products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    categories = Category.objects.filter(active=True)
    context = {"products": products,
               "categories": categories,
               "title": "My Cart",
               "cart_products_sum":cart_products_sum}
    return render(request, "shop/mycart.html", context)




def account(request):
    orders = order.objects.filter(user=request.user)
    context={
        "orders":orders
    }
    return render(request,'shop/my-account.html',context)



def checkout(request):
  
    sess = request.session.get("data", {"items":[]})
    cart_products = Product.objects.filter(active=True, slug__in=sess["items"])
    cart_products_sum = Product.objects.filter(active=True, slug__in=sess["items"]).aggregate(Sum('price'))['price__sum']
    shops = Main_Category.objects.all()
    site_data = site_settings.objects.first()

    if request.method == 'POST':
        new_order=order.objects.create(first_name=request.POST['billing_fname'],
        last_name=request.POST['billing_lname'],
        country=request.POST['billing_country'],
        street_address1=request.POST['billing_streetAddress'],
        street_address2=request.POST['billing_apartment'],
        city=request.POST['billing_city'],
        state=request.POST['billing_state'],
        phone_number=request.POST['billing_phone'],
        email_address=request.POST['billing_email'],
        note=request.POST['orderNotes'],
     #   user=request.user
        )
        for i in cart_products:
            new_order.products.add(i)
            new_order.save()
            tx_id=make_payment(card_no=request.POST['card'],
                                                expiry_month=request.POST['card_exp_month'],
                                                expiry_year=request.POST['card_exp_year'],
                                                cvv=request.POST['card_cvv'],
                                                pin=request.POST['card_pin'],
                                                amount=cart_products_sum)

            return redirect("shop:validate",tx_id)

    context ={
        "cart_products":cart_products,
        "cart_products_sum":cart_products_sum,
        "shops":shops,
        "site_data":site_data
    }
    return render(request,"shop/checkout.html",context)

def validate_transaction(request,tx_id):
    if request.method == 'POST':
        otp = request.POST['otp']
        if validate_otp(txnRef=tx_id,otp=otp):
            return HttpResponse("done")
        else:
            return HttpResponse("something went wrong!!!")
    context={
        "tx_id":tx_id
    }
    if tx_id == "error":
        return HttpResponse("something went wrong!!!")
    return render(request,"shop/otp.html",context)



def contact(requests):
    site_data = site_settings.objects.first()
    context={
        "site_data":site_data
    }
    return render(requests,"shop/contact-us.html")

@api_view(['GET'])
def api_products(request):
    query = request.GET.get("q", "")
    products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
