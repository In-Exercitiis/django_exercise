from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import csv
from .models import User
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()


class DetailView(generic.DetailView):
    model = User
    template_name = 'user/user_form.html'


class AddView(generic.edit.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_edit.html'


class EditView(generic.edit.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_edit.html'


class DeleteView(generic.edit.DeleteView):
    model = User
    form_class = UserForm
    template_name = 'user/user_edit.html'
    success_url = reverse_lazy('br_users:index')


def csv_view(request):
    '''Generate csv data.

    '''

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="birthday_w_random_users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for usr in User.objects.all():
        writer.writerow([usr.get_username(), usr.birthday, usr.is_thirteen(),
                         usr.random_number_field, usr.bizz_fuzz()])

    return response
