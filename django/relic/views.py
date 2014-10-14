from django.shortcuts import render, get_object_or_404
from relic.models import Relic

def relics_index(request):
    context = {
        'relics': Relic.objects.all()
    }
    return render(request, 'relics_index.html', context)

def get_all_pics(relic):
    vysl = []
    for att in dir(relic):
        if str(att).find("pic") != -1 and str(att).find("picd_") == -1 and len(att) != 3:
            pic = getattr(relic, att)
            if getattr(relic, "picd_{0}".format(att[-1])) and pic and pic != "":
                vysl.append([pic, getattr(relic, "picd_{0}".format(att[-1]))])
            elif  pic != "":
                vysl.append([pic, ""])
    return(vysl)

def get_day_and_month(relic):
    a = relic.posted
    mes = ""
    if a.month == 1: mes = "Leden"
    elif a.month == 2: mes = "Únor"
    elif a.month == 3: mes = "Březen"
    elif a.month == 4: mes = "Duben"
    elif a.month == 5: mes = "Květen"
    elif a.month == 6: mes = "Červen"
    elif a.month == 7: mes = "Červenec"
    elif a.month == 8: mes = "Srpen"
    elif a.month == 9: mes = "Září"
    elif a.month == 10: mes = "Říjen"
    elif a.month == 11: mes = "Listopad"
    elif a.month == 12: mes = "Prosinec"
    else: mes = "nic"

    return(a.day, mes)

def view_relic(request, slug):
    
    context = { 'relic': get_object_or_404(Relic, slug=slug),
                'pics': get_all_pics(get_object_or_404(Relic, slug=slug)),
                'dam': get_day_and_month(get_object_or_404(Relic, slug=slug)),
               }
    return render(request, 'view_relic.html', context)
