from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView


# Create your views here.
def base(request):
    return render(request, 'my_app/base.html')


# class IndexView(View):
#     def get(self, request):
#         return render(request, 'my_app/index.html')

class IndexView(TemplateView):
        template_name = "my_app/index.html"

        def get_context_data(self, **kwargs):
            context =  super().get_context_data(**kwargs)
            context['pass_me'] = "Passed"
            return context

