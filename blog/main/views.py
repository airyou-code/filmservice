from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
import os
from films.models import Film, Year, Age, Country, Ganer, Type, Persons, Group, Comment
from django.contrib.auth.models import User
from films.forms import CommentForm

from main.models import backImg

import fake_useragent
import requests
from bs4 import BeautifulSoup

def index(request):
    group = Group.objects.get(name="main_films")
    films = group.films.filter(tg_type=Type.objects.get(name="movie").id)
    img = backImg.objects.all()
    series = []
    series.extend(Film.objects.filter(tg_type=Type.objects.get(name="tv-series").id))
    series.extend(Film.objects.filter(tg_type=Type.objects.get(name="animated-series").id))
    newFilm = []
    firstPoster = []
    for i in range(len(img)):
        if i == 0:
            firstPoster.append(img[i])
            firstPoster.append(Film.objects.get(id_film=f"{img[i].name}"))
        else:
            new = []
            new.append(img[i])
            new.append(Film.objects.get(id_film=f"{img[i].name}"))
            newFilm.append(new)
    
    user = User.objects.all()
    print(user[1])
    # print(os.path.abspath(os.curdir))
    return render(request, 'main/index.html', { "films": films,
                                                "series": series,
                                                "imgs": img,
                                                "postrs": newFilm,
                                                "first": firstPoster})
    # return render(request, 'main/game.html', {"game": game[0]})
    pass

def post_detail(request, id):
    film = Film.objects.filter(id=id)
    # List of active comments for this post
    comments = film.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = film
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    # return render(request,'blog/post/detail.html',
    #              {'post': film,
    #               'comments': comments,
    #               'comment_form': comment_form})

def info(request, pk):
    film = Film.objects.get(id_film=pk)
    persons = film.tg_persons.all()
    # List of active comments for this post
    comments = film.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.film = film
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, 'main/game.html', {  "film": film,
                                                "persons": persons[:12],
                                                "comments": comments,
                                                "comment_form": comment_form,
                                             })
    pass


def pars_film(request):
    # films = ['1282688', '4400203', '558393', '1219909', '572032', '1322324', '1115098', '1309570', '4368595',
    #          '590286', '4291715', '468373', '1355142', '4308624', '1100425', '1009513', '655800', '685246', '4312383']
    films = ['4312383']
    
    for i in films:
        pars(i)

    return HttpResponseRedirect(f"/")



def pars(idkino):
    try:
        Film.objects.get(id_film=f"{idkino}")
        return
    except:
        film_info = KinoSearch(idkino)
        if film_info == "none":
            return

        name = film_info['name']
        id_film = film_info['id']
        try:
            url_img = film_info['poster']['url']
        except:
            url_img = "none"

        try:
            yearProd = film_info['year']
        except:
            yearProd = "none"

        try:
            type_f = Type.objects.get(name=film_info['type'])
        except:
            type_f = Type.objects.create(name=film_info['type'])

        try:
            year_tg = Year.objects.get(name=f"{yearProd}")
        except:
            year_tg = Year.objects.create(name=f"{yearProd}")


        country = ""
        country_tg = []
        for i in film_info['countries']:
            try:
                country_tg.append(Country.objects.get(name=f"{i['name']}"))
            except:
                country_tg.append(Country.objects.create(name=f"{i['name']}"))
            country = country + i['name'] + ","

        genre = ""
        genre_tg = []
        for i in film_info['genres']:
            try:
                genre_tg.append(Ganer.objects.get(name=f"{i['name']}"))
            except:
                genre_tg.append(Ganer.objects.create(name=f"{i['name']}"))
            genre = genre + i['name'] + ", "

        try:
            Budget = f"{film_info['budget']['currency']}{film_info['budget']['value']}"
        except:
            Budget = "none"

        try:
            Fees = f"{film_info['fees']['world']['currency']}{film_info['fees']['world']['value']}"
        except:
            Fees = "none"
        
        try:
            premiere = film_info['premiere']['world'][:10]
        except:
            premiere = "none"

        try:    
            description = film_info['description']
            if description == None:
                description = "none"
        except:
            description = "none"

        try:    
            rating = film_info['rating']['kp']
        except:
            rating = "none"

        age_tg = []
        try:
            age = f"{film_info['ageRating']}+"

            try:
                age_tg.append(Age.objects.get(name=age))
            except:
                age_tg.append(Age.objects.create(name=age))
        except:
            age = "none"
        
        if age == "None+":
            age = "none"


        try:
            angl_name = film_info["alternativeName"]
        except:
            angl_name = "none"
            pass

        if angl_name == None:
            angl_name = "none"


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


        film.tg_year.add(year_tg.id)
        try:
            film.tg_age.add(age_tg[0].id)
        except:
            pass
        for i in genre_tg:
            film.tg_genre.add(i.id)
        for i in country_tg:
            film.tg_country.add(i.id)
        
        pers = person(film_info)
        if pers != None:
            for i in pers:
                film.tg_persons.add(i.id)

        film.tg_type.add(type_f.id)


        return
        pass


def person(json_film):
    try:
        json_persons = json_film["persons"]
        if json_persons == None:
            return None
    except:
        return None
    persons = []
    for i in json_persons:
        try:
            p = Persons.objects.get(id_persons=f"{i['id']}")
        except:
            try:
                id_persons = f"{i['id']}"
            except:
                id_persons = "none"

            try:
                name = i['name']
            except:
                name = "none"

            try:
                enName = i['enName']
                if enName == None:
                    enName = "none"
            except:
                enName = "none"

            try:
                description = i['description']
                print(description)
                if description == None:
                    description = "none"
            except:
                description = "none"

            try:
                enProfession = i['enProfession']
                if enProfession == None:
                    enProfession = "none"
            except:
                enProfession = "none"

            try:
                photo = i['photo']
                if photo == None:
                    continue
                    photo = "none"
            except:
                continue
                photo = "none"

            p = Persons.objects.create(
                id_persons=id_persons,
                name=name,
                enName=enName,
                description=description,
                enProfession=enProfession,
                photo=photo
            )
            persons.append(p)

    return persons

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
