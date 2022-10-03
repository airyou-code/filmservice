from django.contrib import admin
from .models import Film, Year, Age, Country, Ganer, Type, Persons, Group, Comment


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id','id_film', 'name' ]
    search_fields = ['id_film', 'name']
    list_filter = ['tg_genre']

admin.site.register(Film, FilmAdmin)
admin.site.register(Persons)
admin.site.register(Comment)
# admin.site.register(Year)
# admin.site.register(Age)
# admin.site.register(Country)
# admin.site.register(Ganer)
# admin.site.register(Type)
admin.site.register(Group)
