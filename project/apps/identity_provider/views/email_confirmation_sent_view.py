from django.views import View
from django.shortcuts import render


class EmailConfirmationSentView(View):

    def get(self, request):
        return render(request, 'activation_email_sent.html')
