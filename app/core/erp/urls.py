from django.urls import path
from core.erp.views import miprimeravista,misegundavista    
app_name='erp'

urlpatterns = [
    path('uno/',miprimeravista,name='vista1'),
    path('dos/',misegundavista,name='vista2')
    
    
]
    
    
    

