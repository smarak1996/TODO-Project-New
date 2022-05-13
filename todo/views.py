from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
#import asana
from core.settings import ASANA_CONFIG
from todo.forms import AddTaskForm
from todo.utils import create_task, get_all_tasks, update_task, delete_task
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


headers = {
    "Asana-Enable": "new_user_task_lists"
}

class TodoApiView(View):
    
    def get(self, request, *args, **kwargs):
        tasks = get_all_tasks()
        return render(request, 'todo/index.html', {'tasks': tasks})
    

    def post(self, request, *args, **kwargs):
        name = self.request.POST['name']
        notes = self.request.POST['notes']
        gid = self.request.POST.get('gid')
        data = {
            "name": name,
            "notes": notes,
            "workspace": ASANA_CONFIG['WORKSPACE'],
            "assignee": ASANA_CONFIG['ASSIGNEE']
        }
        if not gid:
            post_status = create_task(data)
            #print(post_status)
            return HttpResponseRedirect(reverse('todoAPI'))
        put_data = update_task(data, str(gid))
        return HttpResponseRedirect(reverse('todoAPI'))

class TodoApiDeleteView(View):

    def get(self, request, *args, **kwargs):
        gid = kwargs['gid']
        delete_data = delete_task(gid)
        return HttpResponse(delete_data, content_type='application/json', status=200)


@csrf_exempt
def getElement(request):
    tasks = get_all_tasks()
    return JsonResponse(tasks, safe = False)
    # tasks = {
    # "first_name" : "Smarak",
    # "last_name" : "Parida",
    # "email" : "smarak.webkrone@gmail.com",
    # "company" : "Webkrone Technology Pvt Ltd",
    # "product" : "Axtrix",
    # "location" : "Kolkata",
    # "about" : "Webkrone Technology addresses the growing needs of organizations to manage and secure information more effectively and intelligently. We work with clients who do not hide from the future but want to define it, clients with high potential and high ambition, determined to adapt and become enduring winners. The team at Webkrone Technology are well-versed with latest and the most powerful technologies available today for locating, organizing, managing, retrieving, analyzing, protecting, and presenting information."
    # }

    # return JsonResponse(tasks)

@csrf_exempt
def postElement(request):
    name = request.POST.get('name')
    notes = request.POST.get('notes')
    #gid = request.POST.get('gid')
    # print(gid)
    print(name)
    print(notes)

    data = {
        "name": name,
        "notes": notes,
        "workspace": ASANA_CONFIG['WORKSPACE'],
        "assignee": ASANA_CONFIG['ASSIGNEE']
    }
    post_status = create_task(data)
    print(post_status)

    return JsonResponse(post_status)

