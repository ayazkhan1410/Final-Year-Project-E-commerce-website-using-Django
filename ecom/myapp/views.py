from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
   
    # taking mobile phones category  and its company brand
    mobile_brand = get_object_or_404(Category, category='Mobile Phones')
    company_brand = Company.objects.filter(category=mobile_brand)
    
    # taking tablet category and its company brand
    tablet_brand = get_object_or_404(Category, category='Tablet')
    tab_brand = Company.objects.filter(category=tablet_brand)
    
 
        
    
    # trending_items = Product.objects.filter(is_trending=True)
    
    paginator = Paginator(product, 6)  # Assuming 6 items per page

    try:
        product1 = paginator.get_page(paginator)
    except PageNotAnInteger:
        product1 = paginator.get_page(1)
    except EmptyPage:
        product1 = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'product': product,
        'product1':product1,
        'company_brand': company_brand,
        'tab_brand': tab_brand
    }
    
    return render(request, "home.html", context)

def search_results(request):
    return render(request, 'search_results.html')

def about_us(request):
    return render(request, 'about_us.html')

def checkout_cart(request):
    return render(request, 'checkout_cart.html')

def checkout_complete(request):
    return render(request,'checkout_complete.html')

def checkout_info(request):
    return render(request, 'checkout_info.html')

def checkout_payment(request):
    return render(request, 'checkout_payment.html')

def contact_us(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
        
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       contact = contact.create(name=name, email=email, subject=subject, message=message)
       contact.save()
       
       messages.info(request, 'Your message has been sent successfully')
       return redirect('contact_us')
       
    return render(request, 'contact_us.html')

def faq(request):
    return render(request, 'faq.html')

def my_account(request):
    return render(request, 'my_account.html')

def product_detail(request, slug):
    
    product = Product.objects.get(slug = slug)
    product_description = ProductDescription.objects.filter(product=product)
    product1 = Product.objects.filter(is_trending=True)
    product_img = ProductDescription.objects.filter(product=product)
    
    paginator = Paginator(product1, 6)  # Assuming 6 items per page

    try:
        product1 = paginator.get_page(paginator)
    except PageNotAnInteger:
        product1 = paginator.get_page(1)
    except EmptyPage:
        product1 = paginator.page(paginator.num_pages)
        
    context = {
        'product': product,
        'product1': product1,
        'product_description': product_description,
        'product_img': product_img,
    }
    return render(request, 'product_detail.html', context)

def product(request):
    return render(request, 'product.html')

def order_tracking(request):
    return render(request, 'order_tracking.html')

def login_page(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
