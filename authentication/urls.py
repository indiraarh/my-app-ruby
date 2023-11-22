from django.urls import path
from authentication.views import login

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', include('authentication.urls')),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('logout/', logout, name='logout'),
]