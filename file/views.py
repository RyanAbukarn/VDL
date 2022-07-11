from file.models import Document

from django.shortcuts import redirect, render
from file.forms import DocumentForm


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_ = Document(name=request.FILES['file'].name,
                            description=request.POST['description'])
            new_.save()
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {
        'form': form
    })


def documents(request):
    documents = Document.objects.all()
    return render(request, 'documents.html', {'documents': documents})


def show(request, pk):
    document = Document.objects.get(id=pk)
    return render(request, 'show.html', {'document': document})
