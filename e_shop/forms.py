from django.forms import forms, ModelForm
from django.contrib.auth.models import User

from e_shop.models import Category, Product

class LoginForm(forms.Form):
    class Meta:
        fields = ['username', 'password']
        model = User


class SignupForm(forms.Form):
    class Meta:
        fields = ['username', 'password']
        model = User


class ProductForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Product
        
class CategoryForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Category