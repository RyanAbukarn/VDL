from django.shortcuts import render

from CAN_reader.filter import OrderFilter
from CAN_reader.models import Parser


def home(request):
    parsers = Parser.objects.all()
    myFilter = OrderFilter(request.GET, queryset=parsers)
    parsers = myFilter.qs

    context = {'parsers': parsers, 'myFilter': myFilter}
    return render(request, 'home.html', context)
