from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from products.models import Basket, Product
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistartionView(CreateView, SuccessMessageMixin):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем!Вы зарегистрированы!'

    def get_context_data(self, **kwargs):
        context = super(UserRegistartionView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        total_sum = 0
        for basket in context['baskets']:
            total_sum += basket.sum()
        context['total_sum'] = total_sum
        return context
