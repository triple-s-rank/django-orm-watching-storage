from datetime import timedelta

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    return str(timedelta(seconds=duration))


def storage_information_view(request):

    open_visits = Visit.objects.filter(leaved_at__isnull=True)

    serialized_visits = [
        {'who_entered': visit.passcard,
         'entered_at': visit.entered_at,
         'is_strange': visit.is_long(),
         'duration': format_duration(visit.get_duration())} for visit in open_visits
    ]
    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
