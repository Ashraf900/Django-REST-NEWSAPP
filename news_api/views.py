from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')




# Create your views here.

def home(request):
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2022-06-20&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    context = {
        'articles':articles
    }

   
    return render(request, 'news_api/home.html',context)