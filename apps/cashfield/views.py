from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django.core.exceptions import PermissionDenied

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Container, Channel, Transfer, Balance, Combo
from .forms import ContainerForm, ChannelForm, TransferForm
from .utils import ContainerStats, ChannelStats

# per serializzare - serve per i grafici
import json


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    """
    """

    template_name = 'cashfield/home.html'

# Container


@method_decorator(login_required, name='dispatch')
class ContainerListView(ListView):
    template_name = 'cashfield/list/container.html'
    model = Container
    context_object_name = 'container'


@method_decorator(login_required, name='dispatch')
class ContainerAddView(CreateView):
    template_name = 'cashfield/add/container.html'
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('cashfield:container_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContainerAddView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ContainerDetailView(DetailView):
    """
    """

    template_name = 'cashfield/detail/container.html'
    model = Container
    context_object_name = 'container'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ContainerDetailView, self).get_context_data(**kwargs) # get the default context data
        context['stats'] = ContainerStats(self.object)
        return context

@method_decorator(login_required, name='dispatch')
class ContainerUpdateView(UpdateView):
    """
    """

    template_name = 'cashfield/update/container.html'
    model = Container
    form_class = ContainerForm
    success_url = reverse_lazy('cashfield:container_list')
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        obj = super(ContainerUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ContainerDeleteView(DeleteView):
    """
    """

    template_name = 'cashfield/delete/container.html'
    model = Container
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cashfield:container_list')

    def get_object(self, *args, **kwargs):
        obj = super(ContainerDeleteView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ContainerHomeView(TemplateView):
    """
    """

    def get(self, request):
        return redirect('cashfield:container_list')

# /Container

# Channel


@method_decorator(login_required, name='dispatch')
class ChannelListView(ListView):
    template_name = 'cashfield/list/channel.html'
    model = Channel
    context_object_name = 'channel'


@method_decorator(login_required, name='dispatch')
class ChannelAddView(CreateView):
    template_name = 'cashfield/add/channel.html'
    model = Channel
    form_class = ChannelForm
    success_url = reverse_lazy('cashfield:channel_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ChannelAddView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ChannelDetailView(DetailView):
    """
    """

    template_name = 'cashfield/detail/channel.html'
    model = Channel
    context_object_name = 'channel'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ChannelDetailView, self).get_context_data(**kwargs) # get the default context data
        context['stats'] = ChannelStats(self.object)
        return context


@method_decorator(login_required, name='dispatch')
class ChannelUpdateView(UpdateView):
    """
    """

    template_name = 'cashfield/update/channel.html'
    model = Channel
    form_class = ChannelForm
    success_url = reverse_lazy('cashfield:channel_list')
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        obj = super(ChannelUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ChannelDeleteView(DeleteView):
    """
    """

    template_name = 'cashfield/delete/channel.html'
    model = Channel
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cashfield:channel_list')

    def get_object(self, *args, **kwargs):
        obj = super(ChannelDeleteView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ChannelHomeView(TemplateView):
    """
    """

    def get(self, request):
        return redirect('cashfield:channel_list')

# /Channel

# Transfer


@method_decorator(login_required, name='dispatch')
class TransferListView(ListView):
    template_name = 'cashfield/list/transfer.html'
    model = Transfer
    context_object_name = 'transfer'


@method_decorator(login_required, name='dispatch')
class TransferAddView(CreateView):
    """
    """

    template_name = 'cashfield/add/transfer.html'
    model = Transfer
    form_class = TransferForm
    success_url = reverse_lazy('cashfield:transfer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransferAddView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TransferDetailView(DetailView):
    """
    """

    template_name = 'cashfield/detail/transfer.html'
    model = Transfer
    context_object_name = 'transfer'
    pk_url_kwarg = 'id'


@method_decorator(login_required, name='dispatch')
class TransferUpdateView(UpdateView):
    """
    """

    template_name = 'cashfield/update/transfer.html'
    model = Transfer
    form_class = TransferForm
    success_url = reverse_lazy('cashfield:transfer_list')
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        obj = super(TransferUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class TransferDeleteView(DeleteView):
    """
    """

    template_name = 'cashfield/delete/transfer.html'
    model = Transfer
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cashfield:transfer_list')

    def get_object(self, *args, **kwargs):
        obj = super(TransferDeleteView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class TransferHomeView(TemplateView):
    """
    """

    def get(self, request):
        return redirect('cashfield:transfer_list')

# /Transfer

# Balance
# /Balance

# Combo


@method_decorator(login_required, name='dispatch')
class ComboListView(ListView):
    template_name = 'cashfield/list/combo.html'
    model = Combo
    context_object_name = 'combo'


@method_decorator(login_required, name='dispatch')
class ComboAddView(CreateView):
    """
    """

    template_name = 'cashfield/add/combo.html'
    model = Combo
    form_class = TransferForm
    success_url = reverse_lazy('cashfield:combo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ComboAddView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ComboDetailView(DetailView):
    """
    """

    template_name = 'cashfield/detail/combo.html'
    model = Combo
    context_object_name = 'combo'
    pk_url_kwarg = 'id'


@method_decorator(login_required, name='dispatch')
class ComboUpdateView(UpdateView):
    """
    """

    template_name = 'cashfield/update/combo.html'
    model = Combo
    form_class = TransferForm
    success_url = reverse_lazy('cashfield:combo_list')
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        obj = super(ComboUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ComboDeleteView(DeleteView):
    """
    """

    template_name = 'cashfield/delete/combo.html'
    model = Combo
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cashfield:combo_list')

    def get_object(self, *args, **kwargs):
        obj = super(ComboDeleteView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ComboHomeView(TemplateView):
    """
    """

    def get(self, request):
        return redirect('cashfield:combo_list')

# /Combo

# Chart

@method_decorator(login_required, name='dispatch')
class ChartHomeView(TemplateView):
    """
    """

    template_name = 'cashfield/chart/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChartHomeView, self).get_context_data(**kwargs)

        containers = Container.objects.all().filter(user=self.request.user)
        IN = []
        OUT = []
        TEXT = []
        BALANCE = []
        for c in containers:
            IN.append(str(ContainerStats(c).total_in.amount))
            OUT.append(str(ContainerStats(c).total_out.amount))
            TEXT.append(c.name + '<br>' + str(ContainerStats(c).current_balance))
            BALANCE.append(str(10 + abs(ContainerStats(c).current_balance.amount)))
        context['IN'] = json.dumps(IN)
        context['OUT'] = json.dumps(OUT)
        context['TEXT'] = json.dumps(TEXT)
        context['BALANCE'] = json.dumps(BALANCE)
        return context

# /Chart
