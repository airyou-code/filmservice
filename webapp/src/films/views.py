from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
import os
from .models import Film, Year, Age, Country, Ganer, Type, Persons, Group, Comment
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .forms import CommentForm

def search_film(request):
    rqserch = request.GET.get("search","человек")
    vector = SearchVector('name', weight='A') + SearchVector('description', weight='B') + SearchVector('id_film', weight='A')
    query = SearchQuery(rqserch)
    film = Film.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
    print(request.GET.get("search","человек"))
    return render(request, 'film/search.html', {"films":film, "rqserch":rqserch})

def post_comments(request, id):
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
def get_comments(request, pk):
    film = Film.objects.get(id_film=pk)
    comments = film.comments.filter(active=True)
    data = {"comments": comments}
    return render(request, 'main/comments.html', data)

def info(request, pk):
    film = Film.objects.get(id_film=pk)
    persons = film.tg_persons.all()
    # List of active comments for this post
    comments = film.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        user = request.user
        if user.is_anonymous:
            return HttpResponseRedirect(f"/")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.film = film
            new_comment.user = user
            new_comment.save()
            return HttpResponseRedirect(request.path) 
    else:
        comment_form = CommentForm()

    data = { "film": film,
            "persons": persons[:12],
            "comments": comments,
            "comment_form": comment_form,
            }
    a = request
    
    return render(request, 'main/game.html', data)
    pass
