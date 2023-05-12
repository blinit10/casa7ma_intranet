from django.shortcuts import render

from tvs.models import Slide, Room


# Create your views here.
def serve_room(request, room_id):
    context = {}
    context['room'] = Room.objects.get(pk=int(room_id))
    context['slides'] = context['room'].slides.all()
    return render(request, 'tvs/index.html', context=context)