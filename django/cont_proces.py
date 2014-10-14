from relic.models import Relic

def extra_context(request):
    extras = {}
    extras["ALL_RELICS"] = Relic.objects.all().order_by("-title")

    return(extras)
