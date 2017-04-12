from django.conf import settings  # noqa

from appconf import AppConf


class ManaxThemeAlphaConf(AppConf):

    SETTING_1 = "one"
    SETTING_2 = (
        "two",
    )

    class Meta:
        prefix = "manax_theme_alpha"
