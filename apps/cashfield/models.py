from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from django.db.models import Sum, Avg, Max, Min ## in attesa di passare a pandas

from datetime import timedelta

from moneyed import Money
import moneyed
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator


class Container(TimeStampedModel):
    """Container model

    TimeStampedModel defines fields:
    created
    modified
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='container',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=200,
    )

    currency = models.CharField(
        _('currency'),
        max_length=5,
        choices=settings.CURRENCY_CHOICES
    )

    def __str__(self):
        return self.name

    @property
    def last_balance(self):
        try:
            return self.balance.latest('time')
        except:
            return Money(0, self.currency)

class Channel(TimeStampedModel):
    """Channel model

    TimeStampedModel defines fields:
    created
    modified
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='channel',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=50,
        blank=True,
        null=True
    )

    source = models.ForeignKey(
        Container,
        verbose_name=_('source'),
        related_name='source',
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Container,
        verbose_name=_('destination'),
        related_name='destination',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '[' + str(self.source) + '] -> [' + str(self.destination) + ']'

    @property
    def total_in(self):
        return Money(self.transfer.aggregate(Sum('start_value'))['start_value__sum'], self.source.currency)

    @property
    def total_out(self):
        return Money(self.transfer.aggregate(Sum('end_value'))['end_value__sum'], self.destination.currency)

class Transfer(TimeStampedModel):
    """Transfer model

    TimeStampedModel defines fields:
    created
    modified
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='transfer',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=50,
        blank=True,
        null=True
    )

    channel = models.ForeignKey(
        Channel,
        verbose_name=_('channel'),
        related_name='transfer',
        on_delete=models.CASCADE
    )

    start_time = models.DateTimeField(
        blank=True,
        null=True
    )

    end_time = models.DateTimeField(
        blank=True,
        null=True
    )

    start_value = MoneyField(
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        default=10,
        default_currency='EUR'
    )

    end_value = MoneyField(
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        default=10,
        default_currency='EUR'
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '[' + str(self.channel) + '] @ [' + str(self.start_time) + ']'

    @property
    def ratio_in(self):
        try:
            return ( self.start_value.amount / self.end_value.amount )
        except:
            return 1

    @property
    def ratio_out(self):
        try:
            return ( self.end_value.amount / self.start_value.amount )
        except:
            return 1

    @property
    def transfer_time(self):
        try:
            return ( self.end_time - self.start_time )
        except:
            return timedelta(days=365)

class Balance(TimeStampedModel):
    """Balance model

    TimeStampedModel defines fields:
    created
    modified
    """

    container = models.ForeignKey(
        Container,
        verbose_name=_('container'),
        related_name='balance',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True
    )

    amount = MoneyField(
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        default=10,
        default_currency='EUR'
    )

    def __str__(self):
        return str(self.container) + '@' + str(self.time)


class Combo(TimeStampedModel):
    """Combo model

    TimeStampedModel defines fields:
    created
    modified
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='combo',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=50,
        blank=True,
        null=True
    )

    closed = models.BooleanField(
        _('closed'),
        default=False
    )

    transfers = models.ManyToManyField(Transfer)
