# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from . import models

# # Create your views here.
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)

#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")

from django.views.generic import ListView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models

# 반복을 피하고 싶다.
# ListView : A page representing a list of objects
class HomeView(ListView):

    """ HomeView Definition """

    # Room을 리스트로 나타내고 싶습니다.
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()
