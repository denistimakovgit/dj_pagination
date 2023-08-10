from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

with open("/Users/denistimakov/PycharmProjects/dj_pagination/data-398-2018-08-30.csv", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    stations = []
    for row in reader:
        station = {}
        station['Name'] = row['Name']
        station['Street'] = row['Street']
        station['District'] = row['District']
        stations.append(station)

# Create your  views here.
def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    pagination = Paginator(stations, 10)
    page = pagination.get_page(page_number)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'index.html', context)