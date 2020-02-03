from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries

from . import models


# Create your views here.


# def all_room(request):
#     # page = request.GET.get('page', 1)
#     # page = int(page or 1)
#     # page_size = 10
#     # limit = page * page_size
#     # offset = limit - page_size
#     # all_rooms = rooms_models.Room.objects.all()[offset: limit]
#     # page_count = ceil(rooms_models.Room.objects.count() / page_size)
#     # context = {
#     #     'rooms': all_rooms,
#     #     'page': page,
#     #     'page_count': page_count,
#     #     'page_range': range(1, page_count +1)
#     #
#     # }
#
#     #use pagenator
#     page = request.GET.get('page', 1)
#     page_size = 10
#     all_rooms = rooms_models.Room.objects.all()
#     paginator = Paginator(all_rooms, page_size, orphans=5)
#
#     try:
#         rooms = paginator.page(int(page))
#         context = {
#             'page': rooms
#         }
#         return render(request, 'rooms/home.html', context)
#     except EmptyPage:
#         return redirect('/')


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = 'rooms'


class RoomDetail(DetailView):
    model = models.Room


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        context = {
            'room': room
        }
        return render(request, 'rooms/room_detail.html', context)
    except models.Room.DoesNotExist:
        raise Http404()


def search(request):
    city = request.GET.get('city', 'Anywhere')
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")
    print(s_amenities, s_facilities)

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(request, 'rooms/search.html', {**form, **choices})
