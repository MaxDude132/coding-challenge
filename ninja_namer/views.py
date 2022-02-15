from django.shortcuts import render
from django.http import JsonResponse

from .naming_processes import MainNamingProcess

# Create your views here.
def get_name(request):
    initial_words = request.GET.get("x")
    main_naming_process = MainNamingProcess(initial_words)

    response = {
        "name": main_naming_process.get_full_name()
    }

    return JsonResponse(response)