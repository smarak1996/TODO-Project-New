import asana
from pprint import pprint as p
from django.shortcuts import resolve_url

from django.urls.base import reverse

ACCESS_TOKEN = "1/1200852251571420:5aa33400c5eb23f759052becfb896093"
CLIENT_ID = "1200852290101635"
WORKSPACE = "1200852178821700"
ASSIGNEE = "1200852251571420"
headers = {
    "Asana-Enable": "new_user_task_lists"
}


def create_task(payload):
    client = asana.Client.access_token(ACCESS_TOKEN)
    post_task = client.post('/tasks', payload, headers=headers)
    return post_task

def get_all_tasks():
    client = asana.Client.access_token(ACCESS_TOKEN)
    gen_data = client.get("/tasks", {"opt_fields": ["name", "notes"], "assignee": ASSIGNEE, "workspace": WORKSPACE, "limit": "50"})
    return gen_data

def update_task(payload, gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.put(f"/tasks/{gid}", payload, opt_pretty=True, headers=headers)
    return result

def delete_task(gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.delete(f'/tasks/{gid}', {'gid': gid}, opt_pretty=True, headers=headers)
    return result
