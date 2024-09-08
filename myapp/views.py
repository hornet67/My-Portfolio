from django.shortcuts import render
from django.http import HttpResponse,Http404
from .forms import ContactForm
from .models import *

# Create your views here.

def home(request):
        datas = Portfolio.objects.all()
        docs = Document.objects.all()
       
        context = {
                'datas' : datas,
                'docs'   : docs,
               
        }

        if request.method == 'POST':
              form = ContactForm(request.POST or None)
              if form.is_valid():
                    form.save()
              return render(request,'index.html')

        return render (request,'index.html', context)




def download_pdf(request, doc_id):
    try:
        document = Document.objects.get(id=doc_id)
        pdf_file = document.pdf_file
        
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{document.title}.pdf"'
        
        return response
    except Document.DoesNotExist:
        raise Http404("Document not found")


def index(request):
        data = Portfolio.objects.all()
        for d in data:
                print(d)
        context = {
                data: 'data'
        }
        return render(request, 'dt.html', context)
