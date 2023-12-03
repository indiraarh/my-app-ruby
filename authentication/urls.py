from django.urls import path
from authentication.views import login, create_product_flutter, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('logout/', logout, name='logout'),
]