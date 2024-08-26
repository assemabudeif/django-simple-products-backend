from django.shortcuts import render, redirect
from django.views import View

from e_shop.forms import CategoryForm, ProductForm
from e_shop.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def home(request):
    if request.session.get('username'):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        print(context)
        return render(request, 'e_shop/home.html', context=context)
    else:
         return redirect('e_login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.all()
        users.filter(username=username, password=password)
        if users:
            request.session['username'] = username
            return redirect(home)
        else:
            return render(request, 'e_shop/login.html', {'error': 'Invalid username or password'})

    return render(request, 'e_shop/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.all()
        t_user = users.filter(username=username)
        if t_user:
            return render(request, 'e_shop/signup.html', {'error': 'Username already exists'})

        user = Users(username=username, password=password)
        user.save()
        return redirect('e_login')

    return render(request, 'e_shop/signup.html')

def logout(request):
    # request.session.clear()
    auth_logout(request)
    return redirect('login')

class LoginView(View):
    form = AuthenticationForm()

    def get(self, request):
        return render(request, 'e_shop/login.html', {'form': self.form})


    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            request.session['username'] = username
            return redirect(home)
        except Exception as e:
            return render(request, 'e_shop/login.html', {'error': str(e), 'form': self.form})


class SignUpView(View):
    form = UserCreationForm()

    def get(self, request):
        return render(request, 'e_shop/signup.html', {'form': self.form})


    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, password=password)
            if user:
                user.save()
                return redirect('login')

        except Exception as e:
            return render(request, 'e_shop/signup.html', {'error': str(e)})


def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        products = ProductForm(request.POST, request.FILES)
        products.save()
        return redirect(home)
    context = {}
    context['form'] = form
    return render(request, 'e_shop/addproduct.html', context=context)



def delete_product(request, id):
    products = Product.objects.filter(id=id)
    if products:
        products.delete()
    else:
        return render(request, 'e_shop/home.html', {'error': 'Product not found'})


    return redirect(home)

def update_product(request, id):
    product = Product.objects.filter(id=id).first()
    form = ProductForm()

    form.fields['name'].initial = product.name
    form.fields['price'].initial = product.price
    form.fields['description'].initial = product.description
    form.fields['image'].initial = product.image

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect(home)

    context = {}
    context['form'] = form
    return render(request, 'e_shop/update.html', context=context)

def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect(home)
        else:
            return render(request, 'e_shop/addcategory.html', {'error': 'Invalid data'})
    context = {}
    context['form'] = form
    return render(request, 'e_shop/addcategory.html', context=context)
