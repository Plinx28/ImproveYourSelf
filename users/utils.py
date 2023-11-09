from django.forms import DateInput

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

class MyDateInput(DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'

