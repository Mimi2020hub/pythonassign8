from .models import Meeting, MeetingMinutes, Resource, Event

from django.shortcuts import get_object_or_404

from django.shortcuts import render

from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm

# Create your views here.
def index(request):
    return render(request,'pythonclubapp/index.html')


def getresources(request):
    resource_list = Resource.objects.all()
    return render (request, 'pythonclubapp/resources.html', {'resource_list' : resource_list})


def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render (request, 'pythonclubapp/meetings.html',{'meetings_list': meetings_list,})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet': meet,
    }
    return render(request, 'pythonclubapp/meetingdetails.html', context=context)

def newMeeting(request):
    from=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'pythonclubapp/newmeeting.html', {'form':form})

def newMeetingMinutes(request):
    from=MeetingMinutesForm
    if request.method=='POST':
        form=MeetingMinutesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingMinutesForm()
    else:
        form=MeetingMinutesForm()
    return render(request, 'pythonclubapp/newmeetingminutes.html', {'form':form})

def newResource(request):
    from=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'pythonclubapp/newresource.html', {'form':form})

def newEvent(request):
    from=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'pythonclubapp/newevent.html', {'form':form})
