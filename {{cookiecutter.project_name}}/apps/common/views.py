from django.views.generic import TemplateView


class VueHomeView(TemplateView):
    template_name = 'index.html'
