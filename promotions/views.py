from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from promotions.models import Promotion, Image

def promotions(request):
    query = Promotion.objects.all()
    t = 'promotions/promotions.html'
    c1 = {'promotions': query}
    c2 = RequestContext(request)
    return render_to_response(t, c1, c2)

def promotion(request, slug):
    query = get_object_or_404(Promotion, slug=slug)
    t = 'promotions/promotion.html'
    c1 = {'promotion': query}
    c2 = RequestContext(request)
    return render_to_response(t, c1, c2)