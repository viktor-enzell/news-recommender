from django.shortcuts import render


def index(request):
    data_to_populate_template = {'message': 'Stuff to populate template with'}
    return render(request, 'index.html', data_to_populate_template)
