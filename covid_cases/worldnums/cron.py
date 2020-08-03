from .models import Country
from covid import Covid

covid = Covid()

def update_data():
    for country in covid.list_countries():
        print(country)
        obj = Country.objects.get(num=country['id'])
        obj.name = country['name']
        obj.save()

def make_data():
    for country in covid.list_countries():
        print(country)
        c = Country(name=country['name'], num=country['id'])

        c.save()
