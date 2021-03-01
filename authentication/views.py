from twitteruser.forms import TwitterUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Signup view
class SignUpView(generic.CreateView):
    form_class = TwitterUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
