# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView


class ThanksPage(TemplateView):
    template_name = 'thanks.html'