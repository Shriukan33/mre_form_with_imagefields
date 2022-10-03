from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from .models import ModelWithFileField



# This would be in forms.py but for MRE purpose, it's here.
from django import forms

class ModelWithFileFieldForm(forms.ModelForm):
    class Meta:
        model = ModelWithFileField
        fields = ['first_image_title', 'file_field', 'second_file_field']


class MyView(FormView):
    """This view does both new and edit"""
    model = ModelWithFileField
    form_class = ModelWithFileFieldForm
    template_name = 'form_with_files/form.html'
    success_url = '/new'

    def get_context_data(self, **kwargs):
        pk_id = self.kwargs.get('pkid', -1)
        # With "/new" url, we don't initialize the form with an existing record
        if pk_id > 0:
            record = get_object_or_404(self.model, id=pk_id)
            kwargs["form"] = kwargs.get(
                "form",
                self.form_class(instance=record))
        else:
            record = self.model()

        context = super().get_context_data(**kwargs)
        context['record'] = record # Not used in MRE, it's for context

        return context

    def form_valid(self, form: ModelWithFileFieldForm):
        model_instance: ModelWithFileField = form.save(commit=False)
        # Editing a record doesn't override the existing record,
        # but creates another one instead
        model_instance.pk = None
        model_instance.save()

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(self, request, *args, **kwargs)
