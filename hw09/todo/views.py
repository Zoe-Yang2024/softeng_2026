from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect

def item_delete(request, item_id):
    item = ToDoItem.objects.get(id=item_id)
    list_id = item.todo_list.id
    item.delete()
    return redirect("list", list_id=list_id)

from .models import ToDoList


def index(request):
    lists = ToDoList.objects.all()
    return render(request, "todo/index.html", {"lists": lists})

from .models import ToDoList, ToDoItem

def detail(request, list_id):
    todo_list = ToDoList.objects.get(id=list_id)

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            ToDoItem.objects.create(
                todo_list=todo_list,
                title=title
            )

    return render(request, "todo/detail.html", {"list": todo_list})

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]
    
    
def list_delete(request, list_id):
    todo_list = ToDoList.objects.get(id=list_id)
    todo_list.delete()
    return redirect("index")

def item_toggle(request, item_id):
    item = ToDoItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect("list", list_id=item.todo_list.id)