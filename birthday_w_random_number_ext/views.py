from .forms import BirthdayWRandomNumberExtForm
from .models import BirthdayWRandomNumberExt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views import generic
import csv


class AddView(generic.edit.CreateView):
    model = BirthdayWRandomNumberExt
    form_class = BirthdayWRandomNumberExtForm
    template_name = 'user/edit.html'
    success_url = reverse_lazy('br_users:index')


class DeleteView(generic.edit.DeleteView):
    model = BirthdayWRandomNumberExt
    form_class = BirthdayWRandomNumberExtForm
    template_name = 'user/delete.html'
    success_url = reverse_lazy('br_users:index')


class DetailView(generic.DetailView):
    model = BirthdayWRandomNumberExt
    template_name = 'user/detail.html'


class EditView(generic.edit.UpdateView):
    model = BirthdayWRandomNumberExt
    form_class = BirthdayWRandomNumberExtForm
    template_name = 'user/edit.html'


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return BirthdayWRandomNumberExt.objects.all()


def csv_view(request):
    '''Generate csv data.

    '''

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="birthday_w_random_number_ext.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for usr in BirthdayWRandomNumberExt.objects.all():
        writer.writerow([usr.username, usr.birthday, usr.is_thirteen(),
                         usr.random_number_field, usr.bizz_fuzz()])

    return response
