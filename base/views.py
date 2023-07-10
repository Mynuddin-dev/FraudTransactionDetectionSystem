from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import FilesForm
# Create your views here.

from pathlib import Path
import os
from .Predict_Transaction import check


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)

        print("post print")
        # check whether it's valid:
        if form.is_valid():
            print('is valid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            file_name = form.cleaned_data['file_name']
            print('File name is: ', file_name)
            form.save()

            base_dir = Path(__file__).resolve().parent.parent

            file_path = os.path.join(
                base_dir, "{}/{}/{}".format("media", "media", file_name))

            print(file_path)
            result = check(file_path)
            return result

        else:
            print(form.errors.as_data())  # here you print errors to terminal

    else:
        form = FilesForm

    context = {
        'form': form
    }

    return render(request, "index.html", context)


@login_required(login_url='login')
def transaction(request):

    form = forms.TransactionForm
    context = {
        'form': form,
    }

    return render(request, 'transaction.html', context)
