from django.conf import settings  # noqa

from appconf import AppConf


class CashfieldConf(AppConf):

    SETTING_1 = "one"
    SETTING_2 = (
        "two",
    )

    class Meta:
        prefix = "cashfield"
