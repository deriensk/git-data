from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/deriensk')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
    	userData['login'] = data['login']
        userData['id'] = data['id']
        userData['url'] = data['url']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['created_at'] = data['created_at']
        userData['updated_at'] = data['updated_at']
        userData['following'] = data['following']
    parsedData.append(userData)
    #return HttpResponse(parsedData)
    context = {
    	'data':parsedData
    }
    return render(request, 'profile.html', context)

