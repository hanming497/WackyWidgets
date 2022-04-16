from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from django.http import HttpResponse
from .forms import WidgetsForm

def index(request):
    widgets = Widget.objects.all()
    widgets_form = WidgetsForm()

    return render(request, 'index.html' , {'widgets': widgets , 'widgets_form': widgets_form})

def add_widget(request):
    form = WidgetsForm(request.POST)

    if form.is_valid():
        widget = form.save(commit=False)
        widget.save()

    return redirect('index')

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()

    return redirect('index')