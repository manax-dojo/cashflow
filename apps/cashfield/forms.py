from django import forms
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


from .models import Container, Channel, Transfer, Balance

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ('name', 'currency', )

    helper = FormHelper()
    #helper.form_class = 'form-horizontal'

    helper.layout = Layout(
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('name', 'source', 'destination')
        #exclude = ('id', 'created', 'modified', 'owner')

    helper = FormHelper()
    #helper.form_class = 'form-horizontal'

    helper.layout = Layout(
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('name', 'channel', 'start_time', 'end_time', 'start_value', 'end_value',)

    helper = FormHelper()
    #helper.form_class = 'form-horizontal'

    helper.layout = Layout(
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

class BalanceForm(forms.ModelForm):  
    class Meta:  
        model = Balance  
        fields = ('amount', 'container')  
  
    helper = FormHelper()  
     
    helper.layout = Layout( 
        #Field('container', type="hidden", required=False), 
        FormActions( 
            Submit('save_changes', 'Save changes', css_class="btn-primary"), 
        ) ,
        #HTML("<button data-dismiss='modal' class='btn btn-default' type='button'><i class='fa fa-times'></i>{% trans 'Cancel' %}</button>")
    )     
