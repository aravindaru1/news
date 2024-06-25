from django.urls import path
from .views import fetch_news_data, index,scrape_and_display, fetch_scraped_data

urlpatterns = [
    path('fetch_news/', fetch_news_data, name='fetch_news'),
    path('', index, name='index'),
    path('', scrape_and_display, name='scrape_and_display'),
    path('fetch_scraped_data', fetch_scraped_data, name='fetch_scraped_data'),
]
