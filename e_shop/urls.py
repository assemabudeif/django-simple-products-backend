from django.urls import path
from .views import home, addProduct, login, signup, update_product, delete_product, logout, LoginView, SignUpView, addCategory
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', home, name='home'),
    path('addproduct', addProduct, name='addproduct'),
    path('category/add', addCategory, name='addCategory'),
    # path('login', login, name='login'),
    path('login', view=LoginView.as_view(), name='login'),
    path('signup', view=SignUpView.as_view(), name='signup'),
    path('update/<int:id>', update_product, name='update'),
    path('delete/<int:id>', delete_product, name='delete'),
    path('logout', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
