from django.shortcuts import render,redirect

from django.views.generic import *

from django.shortcuts import get_object_or_404

from user_task.forms import *

from user_task.models import *

from django.db.models import Q

from django.urls import *

# Create your views here.

class AddTaskView(View):
    
    def get(self,request):
        
        form = TaskForm()
        
        return render (request,"task_add.html",{"form":form})
    
    def post(self,request):
        
        form = TaskForm(request.POST)
        
        if form.is_valid():
            
            print(form.cleaned_data)
            
            task = form.save(commit=False)
            
            task.user = request.user
            
            task.save()
            
        return render(request,"task_add.html",{"task":task})
    
# view data

class TaskView(View):
    
    def get(self,request):
        
        task = Task.objects.filter(user = request.user)
        
        return render(request,"task_list.html",{"task":task})
    
# update data

class TaskUpdateView(UpdateView):
    
    model = Task
    
    form_class = TaskForm
    
    template_name = "task_update.html"
    
    success_url = reverse_lazy("home")
    
    def get_queryset(self):
        
        return Task.objects.filter(user=self.request.user)
    

# dalete data

class TaskDelete(View):
    
    def get(self,request,**kwargs):
        
        id = kwargs.get("pk")
        
        task = get_object_or_404(Task , id = id,user = request.user)
        
        task.delete()
        
        return redirect("home")
    
class TaskCompleteView(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        task = get_object_or_404(Task, id=id, user=request.user)

        # Toggle completion status
        task.is_complete = True
        
        task.save()

        return redirect("home")
    
# filter data

class SearchView(View):
    
    teplate_name = "task_search.html"
    
    def get(self,request):
        
        query = request.GET.get("q")
        
        task = Task.objects.filter(user = request.user)
        
        if query:
            
            task = task.filter(Q(priority__icontains = query))
            
            return render(request,self.teplate_name,{"task":task})
