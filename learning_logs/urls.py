"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'learning_logs' # Змінна app_name допомагає Django відрізнити цей файл urls.py від файлів з такою ж назвою в інших додатках проекту
urlpatterns = [
    # Home page
    path('', views.index, name='index'), # тут при пустому url основна сторінка learning_logs в основному urls ||| name='index': Дає маршруту унікальне ім’я. Це дозволяє звертатися до цього URL за іменем (наприклад, у шаблонах за допомогою тегу {% url 'learning_logs:index' %}) замість того, щоб жорстко прописувати URL-адресу.
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'), # можна без похилої риски головне щоб після нічого зайвого не було
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'), # другий аргумент звертається яку сторінку відображати
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'), # третій аргумент дозоляє зручноо посилатися на цей шлях в інших частинах проекту (зверхку написано -_-)
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # <int:topic_id> - щоб знати куди записуємо
]