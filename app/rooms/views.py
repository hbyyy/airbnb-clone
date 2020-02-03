from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import models
from rooms import models as rooms_models

from math import ceil
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

