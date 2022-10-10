from django.shortcuts import render

#librarys importings methods
import requests

import json

import pandas as pd

import googlemaps 
#import googlemaps
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def reviews(request):
    r = requests.get('https://api.reviewsmaker.com/gmb/?placeid=ChIJO-2Z8A5kUjoRgXokgqGaBEs')
    data = r.json()
    #print(data)
    with open('./media/json/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    # Opening JSON file
    with open('./media/json/data.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    #print(type(json_object))
    data = json.load(open('./media/json/data.json'))
    #pd.DataFrame(data["reviews"])
    df = pd.DataFrame(data["reviews"])
    df.to_csv('./media/csv/data.csv', encoding='utf-8', index=False)
    return HttpResponse("Hello, world!")

def gmaps(request):
    gmaps = googlemaps.Client(key='INSERT_KEY_HERE')

    place_name = 'Desss applying technology, 12th Street, C-Sector, Anna Nagar West Extension, Chennai, Tamil Nadu, India'
    places_result = gmaps.places(place_name)
    place_id = places_result['results'][0]['place_id']
    #place_id
    place = gmaps.place(place_id = place_id)
    reviews = [] #empty list which will hold dictionaries of reviews
    for i in range(len(place['result']['reviews'])):
        author = place['result']['reviews'][i]['author_name']
        text = place['result']['reviews'][i]['text']
        rating = place['result']['reviews'][i]['rating']
        time = place['result']['reviews'][i]['relative_time_description']
    
        reviews.append({'author': author,
                        'rating':rating,
                        'text':text,
                        'time':time
                        })
    
    df = pd.DataFrame(reviews)
    #df
    df.to_csv('./media/csv/desss_reviews.csv', index=False)
    return HttpResponse("Hello, world!")