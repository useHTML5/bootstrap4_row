from django import forms
from . import models


class NewRowForm(forms.ModelForm):
    create_columns = forms.IntegerField(required=False, min_value=0, max_value=16, )

    class Meta:
        model = models.Bootstrap4Row
        fields = 'create_columns', 'column_classes', 'row_classes', 'container_classes',
