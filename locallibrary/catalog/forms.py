import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from catalog.models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #check if date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in the past '))

        #check if a date is in the allowed range (+4 from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        #Returning of the clean data.
        return data
       
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_text = { 'due_back': _('Enter a date between now and 4 weeks (default 3).')} 
