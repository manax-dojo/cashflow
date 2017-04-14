from django.db.models import Sum, Avg, Max, Min ## in attesa di passare a pandas

from .models import Container, Channel, Transfer

class ChannelStats():
    """
    """

    def __init__(self, channel):
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
        self.total_in = total_in['start_value__sum']
        self.total_out = total_out['end_value__sum']
        self.avg_in = avg_in['start_value__avg']
        self.avg_out = avg_out['end_value__avg']
        self.max_in = max_in['start_value__max']
        self.max_out = max_out['end_value__max']
        self.min_in = min_in['start_value__min']
        self.min_out = min_out['end_value__min']
