from django.urls import path
from portfolio import views as portfolio_views 

urlpatterns = [
path('portfolio/', portfolio_views.portfolio, name="portfolio"),  #<==========
]
