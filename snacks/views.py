from django.views.generic import DetailView, ListView, TemplateView

from .models import Snack


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetail(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
