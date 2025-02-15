from django.shortcuts import render

from .models import Topic

def index(request): # request як http запит
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request): 
    """Show all topics."""
    topics = Topic.objects.order_by('date_added') # запит до бази даних, запитуючи об'єкти Topic, відсортовані за атрибутом date_added
    context = {'topics': topics} # django y render() просить словник
    return render(request, 'learning_logs/topics.html', context) # context як словник тому django просить словник
