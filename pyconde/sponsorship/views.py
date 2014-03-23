from django.views import generic as generic_views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from pyconde.sponsorship import forms
from pyconde.sponsorship.tasks import send_job_offer


class JobOffer(generic_views.FormView):
    template_name = 'sponsorship/send_job_offer.html'
    form_class = forms.JobOfferForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('sponsorship.add_joboffer'):
            messages.error(request, _('You do not have permission to send job offers.'))
            return HttpResponseRedirect(self.get_success_url())
        return super(JobOffer, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        offer = form.save()
        send_job_offer.delay(offer.id)
        messages.success(self.request, _('Job offer sent'))
        return HttpResponseRedirect('/')