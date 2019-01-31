from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from .forms import PostForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Запись создана!'))
            form.clean()
            return redirect('index')
        else:
            messages.success(request, ('Не удалось создать запись!'))
    all_items = List.objects.all
    form = ListForm()
    return render(request, 'index.html', {'form': form, 'all_items': all_items})


def check(request, list_id):
    item = List.objects.get(pk = list_id)
    if item.completed:
        item.completed = False
    else:
        item.completed = True
    item.save()

    return redirect('index')


def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()

    messages.success(request, ('Запись успешно удалена!'))
    return redirect('index')

def edit(request, list_id):
        item = List.objects.get(pk = list_id)
        return render(request, 'edit_page.html', {'item': item})


def delete_chacked_items(request):
    items = List.objects.filter( completed= True)
    if items:
        for item in items:
            item.delete()
        messages.success(request, ('Записи успешно удалены!'))
    else:
        messages.success(request, ('Нет выделенных записей!'))
    return redirect('index')


def post_new(request, list_id):
    if request.method == "POST":
        form = request.POST

        item = List.objects.get(pk = list_id)
        if form['item']:
            item.item = form['item']
        item.completed = form['completed']
        item.save()
        return redirect('index')
    else:
        return redirect('edit')


