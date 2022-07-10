from django.shortcuts import redirect, render
from file.forms import DocumentForm


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {
        'form': form
    })
