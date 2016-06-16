from django.forms import ModelForm
from .models import Contact

class BaseModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', '%s')
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.help_text
                })
    def clean(self):
        return self.cleaned_data


class ContactForm(BaseModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')
        help_texts = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Type your message here...',
        }
