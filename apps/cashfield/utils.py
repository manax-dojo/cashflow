from django.db.models import Sum, Avg, Max, Min ## in attesa di passare a pandas

from moneyed import Money

from .models import Container, Channel, Transfer

class ChannelStats():
    """
    """

    def __init__(self, channel):
        self.channel = channel
        transfers = Transfer.objects.all().filter(channel=channel)
        total_in = transfers.aggregate(Sum('start_value'))
        total_out = transfers.aggregate(Sum('end_value'))
        avg_in = transfers.aggregate(Avg('start_value'))
        avg_out = transfers.aggregate(Avg('end_value'))
        max_in = transfers.aggregate(Max('start_value'))
        max_out = transfers.aggregate(Max('end_value'))
        min_in = transfers.aggregate(Min('start_value'))
        min_out = transfers.aggregate(Min('end_value'))
        self.transfers = transfers
        self.total_in = Money(total_in['start_value__sum'], self.channel.source.currency)
        self.total_out = Money(total_out['end_value__sum'], self.channel.destination.currency)
        self.total_ratio = total_out['end_value__sum'] / total_in['start_value__sum']
        self.avg_in = Money(avg_in['start_value__avg'], self.channel.source.currency)
        self.avg_out = Money(avg_out['end_value__avg'], self.channel.destination.currency)
        self.avg_ratio = avg_out['end_value__avg'] / avg_in['start_value__avg']
        self.max_in = Money(max_in['start_value__max'], self.channel.source.currency)
        self.max_out = Money(max_out['end_value__max'], self.channel.destination.currency)
        self.max_ratio = max_out['end_value__max'] / max_in['start_value__max']
        self.min_in = Money(min_in['start_value__min'], self.channel.source.currency)
        self.min_out = Money(min_out['end_value__min'], self.channel.destination.currency)
        self.min_ratio = min_out['end_value__min'] / min_in['start_value__min']

class ContainerStats():
    """
    """

    def __init__(self, container):
        """
        """
        self.container = container
        self.ch_in = Channel.objects.all().filter(destination=container)
        self.ch_out = Channel.objects.all().filter(source=container)

        total_in = Money(0, self.container.currency)
        for c in self.ch_in:
#            self.ch_in.c.total_out = ChannelStats(c).total_out
#            total_in = total_in + ChannelStats(c).total_out
            total_in = total_in + c.total_out

            

        self.total_in = total_in

        total_out = Money(0, self.container.currency)
        for c in self.ch_out:
#            total_out = total_out + ChannelStats(c).total_in
            total_out = total_out + c.total_in

        self.total_out = total_out

        self.net_flow = self.total_in - self.total_out

        try:
            last_balance_time = self.container.last_balance.time

            current_balance = self.container.last_balance.amount

            #for c in ch_in:
            #    print(c) ## DEBUG
            #    t_in = Transfer.objects.all().filter(channel=c).filter(end_time__gt=self.container.last_balance.time)
            #    plus = t_in.aggregate(Sum('end_value'))
            #    print(plus) ## DEBUG
            #    if plus['end_value__sum']:
            #        current_balance.amount = current_balance.amount + plus['end_value__sum']
            #    print(current_balance, current_balance.amount) ## DEBUG


            #for c in ch_out:
            #    print(c) ## DEBUG
            #    t_out = Transfer.objects.all().filter(channel=c).filter(end_time__gt=self.container.last_balance.time)
            #    minus = t_out.aggregate(Sum('start_value'))
            #    print(plus) ## DEBUG
            #    if minus['start_value__sum']:
            #        current_balance.amount = current_balance.amount - minus['start_value__sum']
            #    print(current_balance, current_balance.amount) ## DEBUG

            self.current_balance = current_balance

        except:
            self.current_balance = self.net_flow
