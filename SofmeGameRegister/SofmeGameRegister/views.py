from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from .models import *


class FormView(TemplateView):
    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)