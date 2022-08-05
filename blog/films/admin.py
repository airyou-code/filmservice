from django.contrib import admin
from .models import Film, Year, Age, Country, Ganer, Type, Persons, Group

admin.site.register(Film)
admin.site.register(Persons)
# admin.site.register(Year)
# admin.site.register(Age)
# admin.site.register(Country)
# admin.site.register(Ganer)
# admin.site.register(Type)
admin.site.register(Group)
