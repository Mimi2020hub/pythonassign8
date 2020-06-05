from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields = '__all__'_''

class MeetingMinutesForm(forms.ModelForm):
    class Meta:
        model=MeetingMinutes
        fields = '__all__'_''

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields = '__all__'_''

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields = '__all__'_''
