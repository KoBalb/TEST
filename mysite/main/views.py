from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Text
from .forms import UserTextForm
# Create your views here.

def index(request):
    return render(request, "main/index.html")

def index(request):
    if request.method == "POST":
        form = UserTextForm(request.POST)  # Берём данные из формы
        if form.is_valid():  # Проверяем, что данные валидные
            form.save()  # Сохраняем в базу данных
            return redirect("index")  # Обновляем страницу

    else:
        form = UserTextForm()

    texts = Text.objects.all()  # Загружаем все сохранённые тексты

    return render(request, "main/index.html", {"form": form, "texts": texts})