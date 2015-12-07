from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import logging

logger = logging.getLogger(__name__)

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
