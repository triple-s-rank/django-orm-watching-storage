from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    serialized_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_long(),
        } for visit in this_passcard_visits
    ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }

    return render(request, 'passcard_info.html', context)
