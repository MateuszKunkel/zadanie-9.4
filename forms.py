from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class RecordsForm(FlaskForm):
    recordauto = StringField("Autor", validators=[DataRequired()])
    recordname = StringField("Tytuł", validators=[DataRequired()])
    recordtext = TextAreaField("Opis", validators=[DataRequired()])
    recordstar = IntegerField(
        "Ile dajesz gwiazdek", validators=[NumberRange(min=1, max=5), DataRequired()]
    )
