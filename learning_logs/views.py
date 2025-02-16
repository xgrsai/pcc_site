from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request): # request як http запит (типу URL адреса в браузері)
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request): 
    """Show all topics."""
    topics = Topic.objects.order_by('date_added') # запит до бази даних, запитуючи об'єкти Topic, відсортовані за атрибутом date_added
    context = {'topics': topics} # django y render() просить словник
    return render(request, 'learning_logs/topics.html', context) # context як словник тому django просить словник

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') # мінус означає від найновіших до старіших
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context) # потім дані з context можна використовувати у шаблоні 

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST) # аргумент передає значення полів форми
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context) # потім дані з context можна використовувати у шаблоні 

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # commit=false не записує об'єкт в базу даних
            new_entry.topic = topic # зберегти запис на тему яку ми витягли з БД (на початку функції)
            new_entry.save() # тут воно вже зберігає з правильно темою
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context) # потім дані з context можна використовувати у шаблоні 

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id) # отримання запису по id
    topic = entry.topic # до якої теми належить запис

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry) # означає, що форма буде заповнена даними з конкретного entry, який ми передали як instance
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST) # бере існуючий запис і дані який надіслав користуввач (типу змінив текст)
        if form.is_valid():
            form.save() # типу запис до бд
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context) # потім дані з context можна використовувати у шаблоні (хтмл)