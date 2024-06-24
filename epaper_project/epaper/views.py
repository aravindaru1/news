# views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def scrape_and_display(request):
    return render(request, 'epaper/display.html')

def fetch_scraped_data(request):
    url = 'https://epaper.v6velugu.com/pagemeta/get/3883615/1-50'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return JsonResponse(json_data)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
