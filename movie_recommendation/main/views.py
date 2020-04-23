import csv
from django.shortcuts import render
from .ContentBasedSystem import give_rec
from .forms import collab,cont
from .Collaborative import recommendation

# Create your views here.

def index(response):
    return render(response, 'main/index.html', {})

def content(response):
    if response.method == "POST":
        data = cont(response.POST)

        if data.is_valid():
            movie_name = data.cleaned_data["movie_name"]
            result = give_rec(movie_name)
            return render(response, 'main/content.html', {"result":result,"form":cont()})
    return render(response, 'main/content.html', {"result":abc(),"form":cont})


def collaborative(response):
    if response.method == "POST":
        data = collab(response.POST)

        if data.is_valid():
            u_id = data.cleaned_data["u_id"]
            no_of_movie = data.cleaned_data["no_of_movie"]
            result = recommendation(u_id,no_of_movie)

            print(result)
            return render(response, 'main/collaborative.html', {"result":result,"form":collab()})
    return render(response, 'main/collaborative.html', {"result":abc(),"form":collab})

def abc():
    return ""