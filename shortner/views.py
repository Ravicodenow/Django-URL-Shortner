from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Url
import uuid # this_is_for_unique_id
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('htttp://'+ url_details.link)
