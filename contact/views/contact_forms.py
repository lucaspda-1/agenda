from django.shortcuts import render , get_list_or_404,redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def create(request):


    context = {
        
    }

    return render(
        request,
        'contact/create.html',
        context,
    )