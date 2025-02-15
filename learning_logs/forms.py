from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta: # внутрішній клас у моделі (тут у формі), який використовується для налаштування її поведінки (як сортувати, як назвати). З його допомогою можна змінювати порядок сортування записів, задавати назви таблиць у базі даних, визначати, як модель відображатиметься в адміністративній панелі тощо
        model = Topic # цей параметр вказує, що форма TopicForm пов'язана з моделлю Topic. Коли ми створюємо або оновлюємо запис у базі даних через форму, Django використовуватиме цю модель для роботи з даними.
        fields = ['text'] # які саме поля з моделі Topic повинні бути включені у форму. У цьому випадку лише поле text.
        labels = {'text': ''} # це підпис перед полем вводу. Його нам не треба тому забрав (бо типу ця мітка типу допомагає зоорієнтуватися за який атрибут відповідає ця мітка)