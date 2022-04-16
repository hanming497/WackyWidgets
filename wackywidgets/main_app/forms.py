from django.forms import ModelForm
from .models import Widget

class WidgetsForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']