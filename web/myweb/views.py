from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
from . import models
import json
# Create your views here.
def index(request):
    path=reverse('myweb_reindex')
    print(path)
    # return HttpResponse('hello word')
    # return HttpResponse('<script>location.href="'+path+'"</script>')
    # return render(request,'index.html',{'path':path})
    # return redirect(path)
    # return redirect('reindex/')
    # return redirect(reverse('myweb_reindex'))
    return render(request,'myweb/index.html')
def reindex(request):
    return HttpResponse('你好世界')
def urlpath(request):
    print(request.path)
    print(request.method)
    print(request.GET.get('id',1))
    data={'name':'京香JuLia','age':26,}
    return HttpResponse(json.dumps(data))