from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
@login_required

def index(request):
    all_items = List.objects.all
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to list!'))
            return render(request, 'index.html', {'all_items': all_items})

        else:
            messages.error(request,('Item is not valid!'))
            all_items = List.objects.all
            return render(request, 'index.html', {'all_items': all_items})
    else:
        return render(request, 'index.html', {'all_items': all_items})
def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request,('Item has been deleted!'))
    return redirect('index')

def cross_off(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!'))
            return redirect('index')
    else:
        item = List.objects.get(pk= list_id)
        return render(request, 'index.html', {'item': item})