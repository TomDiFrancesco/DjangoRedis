from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from iacademy.views import Index, CertificateCreateView, CertificateDetailView, CertificateListView, CertificateCheckView, \
    CertificateCheckDetailView
from iacademy.forms import LoginForm, PasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='iacademy/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='iacademy/logout.html'), name='logout'),
    path('', Index.as_view(), name='index'),
    path('certificate-create/', CertificateCreateView.as_view(), name='certificate-create'),
    path('certificate-detail/<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
    path('certificate-list/', CertificateListView.as_view(), name='certificate-list'),
    path('certificate-check/', CertificateCheckView.as_view(), name='certificate-check'),
    path('certificate-check-detail/', CertificateCheckDetailView.as_view(), name='certificate-check-detail'),
]