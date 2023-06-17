from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    if request.method == 'POST':
        new_todo = request.POST.get('new_todo')
        TodoItem.objects.create(title=new_todo)
        
        return redirect('todo_list')
    
    else:
        todos = TodoItem.objects.all()
        return render(request, 'todo/todo_list.html', {'todos': todos})
    
def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.delete()
    
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.completed = True
    todo.save()
    
    return redirect('todo_list')
    
