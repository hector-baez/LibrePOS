from babel.numbers import list_currencies
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

from librepos.utils.datetime import get_all_timezones
from librepos.utils.enums import DateFormatEnum


class SystemSettingsForm(FlaskForm):
    timezone = SelectField(
        "Timezone",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )
    currency = SelectField(
        "Currency",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )
    date_format = SelectField(
        "Date Format",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )
    time_format = SelectField(
        "Time Format",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )
    language = SelectField(
        "Language",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )
    locale = SelectField(
        "Locale",
        coerce=str,
        validators=[DataRequired()],
        render_kw={"placeholder": " "},
    )

    def __init__(self, **kwargs):
        super(SystemSettingsForm, self).__init__(**kwargs)
        all_currencies = list_currencies()
        self.timezone.choices = get_all_timezones()
        self.currency.choices = [
            (currency, currency) for currency in sorted(all_currencies)
        ]
        self.date_format.choices = [(i.value, i.name) for i in DateFormatEnum]
        self.time_format.choices = [
            ("%I:%M %p", "12-Hour (AM/PM)"),
            ("%H:%M", "24-Hour"),
        ]
        self.language.choices = [("en", "English"), ("es", "Spanish")]

        # Fixed locale choices implementation
        available_locales = [
            ("en_US", "English (United States)"),
            ("en_GB", "English (United Kingdom)"),
            ("es_ES", "Spanish (Spain)"),
            ("es_MX", "Spanish (Mexico)"),
        ]
        self.locale.choices = sorted(available_locales, key=lambda x: x[1])
