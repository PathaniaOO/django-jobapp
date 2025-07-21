from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadForm2

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            save_object=form.instance
            return render(request, 'uploadapp/add_image.html', {'form': form, 'saved_object': save_object})
    else:
        form=UploadForm()
    return render(request, 'uploadapp/add_image.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            save_object=form.instance
            return render(request, 'uploadapp/add_file.html', {'form': form, 'saved_object': save_object})
    else:
        form=UploadForm2()
    return render(request, 'uploadapp/add_file.html', {'form': form})