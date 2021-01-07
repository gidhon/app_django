from promotions.models import Promotion

def latest(request):
    query = Promotion.objects.all().order_by('-created')[0]
    return {'latest': query}
