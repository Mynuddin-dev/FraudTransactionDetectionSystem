from django.forms import ModelForm, forms 
from .models import AllFile, Transaction



class FilesForm(ModelForm):

    class Meta:
        model = AllFile
        fields = '__all__'

class TransactionForm(ModelForm):

  class Meta:
    model = Transaction
    fields = ("__all__")
  