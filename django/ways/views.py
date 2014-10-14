from django.shortcuts import render, get_object_or_404
from ways.models import Way

def ways_index(request):
    context = {
        'ways': Way.objects.all()
    }
    return render(request, 'ways_index.html', context)

def get_all_pics(way):
    vysl = []
    for att in dir(way):
        if str(att).find("pic") != -1 and str(att).find("picd_") == -1:
            pic = getattr(way, att)
            if getattr(way, "picd_{0}".format(att[-1])) and pic:
                vysl.append([pic, getattr(way, "picd_{0}".format(att[-1]))])
            else:
                vysl.append([pic, ""])
    return(vysl)

def view_way(request, slug):   
    context = { 'way': get_object_or_404(Way, slug=slug),
                'pics': get_all_pics(get_object_or_404(Way, slug=slug)),
    }
    return render(request, 'view_way.html', context)