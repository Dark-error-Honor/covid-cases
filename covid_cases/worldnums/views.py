from covid import Covid
from django.shortcuts import render
from worldnums.models import Country
from .cron import make_data, update_data


def home_view(request):

    covid = Covid()
    confirmed = covid.get_total_confirmed_cases
    active = covid.get_total_active_cases
    deaths = covid.get_total_deaths
    recovered = covid.get_total_recovered

    query = Country.objects.all()

    context = {
        'queryset': query,
        'confirmed': confirmed,
        'active': active,
        'deaths': deaths,
        'recovered': recovered
    }

    return render(request, 'home/home.html', context)

def lookup_view(request, name):
    covid = Covid()

    obj = Country.objects.get(name__iexact=name.lower())
    print(obj)

    country = covid.get_status_by_country_id(obj.num)
    confirmed = country['confirmed']
    active = country['active']
    deaths = country['deaths']
    recovered = country['recovered']

    query = Country.objects.all()

    context = {
        'queryset': query,
        'obj': obj,
        'confirmed': confirmed,
        'active': active,
        'deaths': deaths,
        'recovered': recovered
               }

    return render(request, 'home/lookup.html', context)
