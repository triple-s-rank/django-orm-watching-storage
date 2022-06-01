from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.get(passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
        'entered_at': visit.entered_at,
        'duration': visit.format_duration(),
        'is_strange': visit.is_long(),
         } for visit in visits_by_passcard
    ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
