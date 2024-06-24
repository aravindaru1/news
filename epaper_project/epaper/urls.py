from django.urls import path
from .views import scrape_and_display, fetch_scraped_data

urlpatterns = [
    path('', scrape_and_display, name='scrape_and_display'),
    path('fetch_scraped_data', fetch_scraped_data, name='fetch_scraped_data'),
]
