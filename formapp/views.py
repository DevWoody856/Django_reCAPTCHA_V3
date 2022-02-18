from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import CreateForm
import requests
from django_06 import settings
from django.contrib import messages


def home(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():

            ''' Start validation '''
            recaptcha_response = request.POST.get('recaptcha_v3_func')
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            print(result)

            if result['success']:
                return HttpResponse('Success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    form = CreateForm()
    return render(request, "formapp/func_view.html", {'form':form, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})


class ContactFormView(FormView):
    template_name = 'formapp/class_view.html'
    form_class = CreateForm
    success_url = '/contact2/'
    extra_context = {
        'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY
    }

    def form_valid(self, form):
        ''' Start validation '''
        recaptcha_response = self.request.POST.get('recaptcha_v3_class')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        print(result)

        if result['success']:
            return HttpResponse('Success!')

        else:
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')

        form = CreateForm()
        return super().form_valid(form)