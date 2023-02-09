from django.views.generic import View, CreateView, DetailView, ListView, TemplateView
from .models import Certificate
from .forms import CertificateCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from .utils import get_transaction_by_hash, send_transaction
from django.shortcuts import render, get_object_or_404



class Index(TemplateView):
    template_name = 'iacademy/index.html'


class CertificateListView(ListView):
    template_name = 'iacademy/certificate_list.html'
    model = Certificate
    context_object_name = 'certificate'

    def get_queryset(self):
        queryset = {
            'all': Certificate.objects.order_by('-date_of_creation', 'name'),
        }
        return queryset


class CertificateCreateView(CreateView):
    template_name = 'iacademy/certificate_create.html'
    form_class = CertificateCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CertificateDetailView(DetailView):
    template_name = 'iacademy/certificate_detail.html'
    model = Certificate


class CertificateCheckView(View):
    def get(self, request):
        return render(request, 'iacademy/certificate_check.html')

    def post(self, request):
        transaction_hash = request.POST.get('hash', None)
        transaction = get_transaction_by_hash(transaction_hash)
        request.session['hash'] = transaction_hash
        request.session['transaction'] = transaction
        return HttpResponseRedirect('/certificate-check-detail/')



######

class CertificateCheckDetailView(View):
    def get(self, request):
        transaction = request.session.get('transaction')
        transaction_hash = request.session.get('hash')
        certificate = Certificate.objects.get(transaction_id=transaction_hash)
        context = {
            'transaction': transaction,
            'object': certificate,
        }
        return render(request, 'iacademy/certificate_check_detail.html', context)