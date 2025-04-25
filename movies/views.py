from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'movies' : ['I am Thinking of Ending Things', 'The Elephant is Sitting Still', 'Wild Pear Tree', 'A Brighter Summer Day', 'All About Lily Chou-Chou']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})
#app/templates/app/index.html
# movies/templates/movies/index.html