from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ToDoItemForm, ToDoListForm
from .models import ToDoItem, ToDoList


def index(request):
    lists = ToDoList.objects.all()
    return render(request, "todo/index.html", {"lists": lists})


def list_create(request):
    form = ToDoListForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        todo_list = form.save()
        return redirect(todo_list)
    return render(request, "todo/list_form.html", {"form": form})


def detail(request, list_id):
    todo_list = get_object_or_404(ToDoList, pk=list_id)
    return render(
        request,
        "todo/detail.html",
        {"todo_list": todo_list, "item_form": ToDoItemForm()},
    )


@require_POST
def item_add(request, list_id):
    todo_list = get_object_or_404(ToDoList, pk=list_id)
    form = ToDoItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.todo_list = todo_list
        item.save()
        return redirect(todo_list)
    return render(
        request,
        "todo/detail.html",
        {"todo_list": todo_list, "item_form": form},
        status=400,
    )


@require_POST
def item_toggle(request, item_id):
    item = get_object_or_404(ToDoItem, pk=item_id)
    item.completed = not item.completed
    item.save(update_fields=["completed"])
    return redirect(item.todo_list)


@require_POST
def item_delete(request, item_id):
    item = get_object_or_404(ToDoItem, pk=item_id)
    todo_list = item.todo_list
    item.delete()
    return redirect(todo_list)


@require_POST
def list_delete(request, list_id):
    todo_list = get_object_or_404(ToDoList, pk=list_id)
    todo_list.delete()
    return redirect("todo:index")
