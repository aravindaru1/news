import json
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
import re

#eenadu

def fetch_news_data(request):
    if request.method == 'DELETE':
        request.session.pop('news_data', None)
        return HttpResponse(status=204)
    
    # Constructing dynamic URL based on current date
    today = datetime.now().strftime('%d/%m/%Y')
    data_url = f"https://epaper.eenadu.net/Home/GetAllpages?editionid=1&editiondate={today}&IsMag=0"

    if 'news_data' not in request.session:
        response = requests.get(data_url)
        if response.status_code == 200:
            data = response.json()
            request.session['news_data'] = data
        else:
            return HttpResponse(status=500)
    else:
        data = request.session['news_data']
    
    return JsonResponse(data, safe=False)

def index(request):
    return render(request, 'epaper/display.html')



#v6

# URL of the page you want to fetch
webpage_url = 'https://epaper.v6velugu.com/3883220/Telangana-Main/24-06-2024#page/1/1'

# Function to extract the number from the webpage dynamically
def extract_number_from_webpage():
    try:
        response = requests.get(webpage_url)
        if response.status_code == 200:
            html_content = response.text
            # Regular expression pattern to find the number
            pattern = r"https://epaper\.v6velugu\.com/r/(\d+)"
            match = re.search(pattern, html_content)
            if match:
                number = match.group(1)
                return number
            else:
                print("No matching number found")
        else:
            print(f"Failed to fetch URL: {webpage_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while fetching URL: {webpage_url}. Error: {str(e)}")
    
    return None

def scrape_and_display(request):
    return render(request, 'epaper/display.html')

def fetch_scraped_data(request):
    # Extract the number from the webpage
    if request.method == 'DELETE':
        request.session.pop('news_data2', None)
        return HttpResponse(status=204)
    
    number = extract_number_from_webpage()
    if not number:
        return JsonResponse({'error': 'Failed to fetch number from webpage'}, status=500)
    
    # Construct the URL with the extracted number
    url = f'https://epaper.v6velugu.com/pagemeta/get/{number}/1-50'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            return JsonResponse(json_data)
        else:
            return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': f'Failed to fetch data: {str(e)}'}, status=500)
