from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

from . models import iaMarks,Students,Subjects,ClassStudents
from. forms import TopicForm

# from . models import Students
# Create your views here.
def index(request):
    return render(request,'index.html')

def internals(request):
    return render(request,'internals.html')

# @login_required
# def chooseSem(request):
#     return render(request,'chooseSem.html')

@login_required
def iamarks(request,topic_id):
    topicss = iaMarks.objects.filter(sub_code=topic_id)
    context = {'topicss':topicss}
    return render(request,'iamarks.html',context)

@login_required
def newEntry(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        newtopics = form.save(commit=False)
        newtopics.owner = request.user
        newtopics.save()
        return HttpResponseRedirect(reverse('app:subjects'  ))
    context = {'form':form}
    return render(request,'newEntry.html',context)


@login_required
def subjects(request):
    topicss = Subjects.objects.filter(owner=request.user).order_by('SEM')
    context = {'topicss':topicss}
    return render(request,'subjects.html',context)






def newEntry1(request,topic_id):
    try:
        topicss = Subjects.objects.get(subcode=topic_id)
    except Subjects.DoesNotExist:
        raise Http404('topic does not exists')
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        newtopics = form.save(commit=False)
        newtopics.owner = request.user
        newtopics.topic = topicss
        form.sub_code = Subjects.objects.get(subcode=topic_id)
        newtopics.save()
        return HttpResponseRedirect(reverse('app:subjects'))
    context = {'topicss':topicss,'form':form}
    return render(request,'newentry1.html',context)