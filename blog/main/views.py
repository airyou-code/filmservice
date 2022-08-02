from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
import os
from films.models import Film
from main.models import backImg

import fake_useragent
import requests
from bs4 import BeautifulSoup

def index(request):
    game = Film.objects.all()
    img = backImg.objects.all()
    newFilm = []
    for i in range(len(img)):
        new = []
        new.append(img[i])
        new.append(Film.objects.get(id_film=f"{img[i].name}"))
        newFilm.append(new)
        
    # print(os.path.abspath(os.curdir))
    return render(request, 'main/index.html', {"game": game, "imgs": img, "films": newFilm})
    # return render(request, 'main/game.html', {"game": game[0]})
    pass

def info(request, pk):
    film = Film.objects.get(id_film=pk)
    return render(request, 'main/game.html', {"film": film})
    pass

def pars(request,idkino):
    film_info = KinoSearch(idkino)
    if film_info == "none":
        return HttpResponseRedirect(f"/")
    name = film_info['name']
    id_film = film_info['id']
    url_img = film_info['poster']['url']
    yearProd = film_info['year']
    country = ""
    for i in film_info['countries']:
        country = country + i['name'] + ","

    genre = ""
    for i in film_info['genres']:
        genre = genre + i['name'] + ", "

    try:
        Budget = f"{film_info['budget']['currency']}{film_info['budget']['value']}"
    except:
        Budget = "none"

    Fees = f"{film_info['fees']['world']['currency']}{film_info['fees']['world']['value']}"
    premiere = film_info['premiere']['world'][:10]
    description = film_info['description']
    rating = film_info['rating']['kp']
    try:
        age = f"{film_info['ageRating']}+"
    except:
        age = "none"
        
    if age == "None+":
        age = "none"


    try:
        angl_name = film_info["alternativeName"]
    except:
        angl_name = "none"
        pass

    film = Film.objects.create(
        name=name,
        id_film=id_film,
        url_img=url_img,
        yearProd=yearProd,
        country=country,
        genre=genre,
        Budget=Budget,
        Fees=Fees,
        premiere=premiere,
        description=description,
        rating=rating,
        Age=age,
        angl_name=angl_name
        )
    return HttpResponseRedirect(f"/")
    pass

def KinoSearch(id="none"):
    if id != "none":
        token = "A8TW6DY-4VB4155-HBGC57E-20VK33J"

        session = requests.Session()
        url = " https://api.kinopoisk.dev/movie"
        params = {
            'token' : token,
            'search' : f'{id}',
            'field' : 'id',
        }
        index = requests.get(url=url, params=params)
        return index.json()
    return "none"
    # index = requests.get(url=url, params=params)
    # print(index.text)



    # game = Games.objects.all()
    # session = requests.Session()
    # user = fake_useragent.UserAgent().random
    # header = {
    #     'user-agent': user
    # }
    # link = "https://www.kinopoisk.ru/lists/movies/popular-films/?page=1"
    # index = session.get(link, headers=header).text
    # soup = BeautifulSoup(index.text, 'lxml')
    # all_piece = soup.find_all("div", class_="styles_root__ti07r")
    # print(all_piece[0])
    # pass
