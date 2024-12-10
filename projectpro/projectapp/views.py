from django.shortcuts import redirect,render,get_object_or_404
from .models import data
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from.models import data
def apple(request):
    return HttpResponse("hi") 

def color(request):
    return render(request,'home-1.html')
def red(request):
    return render(request,'home-1.html')
def signup_view(request):
    if request.method == 'POST':
        username =  request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username,password=password,email=email)
        return redirect('home')
    return render(request,'signup.html')

def login_view(request):
    if request.method == "POST":  # Fixed case of POST
        username = request.POST.get('username')  # Safely get POST data
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Corrected redirect
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')




def msg(request):
    sedan = data.objects.filter(is_sedan=True)
    hatchback = data.objects.filter(is_hatchback=True)
    premium = data.objects.filter(is_premium=True)
    return render(request, 'home.html', {'sedan': sedan, 'hatchback': hatchback,'premium':premium})



def add_to_cart(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(data, id=product_id)
        cart = request.session.get('cart',{})
        product_id_str = str(product_id)
        if product_id_str in cart:
            cart[product_id_str] += 1
        else:
            cart[product_id_str]=1
        request.session['cart']=cart
        return JsonResponse({'message':'product added to cart','cart':cart})
    
def process_payment(request, product_id):
    # Process payment logic here
    return render(request, 'payment_success.html')


   
def payment_page(request, product_id):
    product = get_object_or_404(data, id=product_id)
    return render(request, 'payment.html', {'product': product})