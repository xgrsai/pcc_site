from django.db import models # модель - в БД це таблиця

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)#1
    date_added = models.DateTimeField(auto_now_add=True)#2
    
    def __str__(self): # для того щоб я міг прочитати, бо без цього виведе <Topic: Topic object (1)> 
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: # внутрішній клас у моделі, який використовується для налаштування її поведінки (як сортувати, як називати модель). З його допомогою можна змінювати порядок сортування записів, задавати назви таблиць у базі даних, визначати, як модель відображатиметься в адміністративній панелі тощо
        verbose_name_plural = 'entries'
        def __str__(self): # в іншому випадку ми виводитимемо не дані а предсталення об'єкта
            """Return a simple string representing the entry."""
            return f"{self.text[:50]}..."
