from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AddFileForm
from .models import File
from django.views.generic.edit import FormView


class IndexView(View):
    html = 'index.html'
    def get(self, request):
        data = {
            'files': File.objects.all()
        }
        return render(request, self.html, data)


class AddFileView(FormView):
    template_name= 'add_file.html'
    form_class = AddFileForm
    def form_valid(self, form):
        data = form.cleaned_data
        file = File.objects.create(
            name=data['name'],
            parent=data['parent']
        )
        return HttpResponseRedirect(self.request.GET.get('next', '/'))

    