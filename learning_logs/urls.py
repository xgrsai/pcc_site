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
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]