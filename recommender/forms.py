from django import forms


class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        initial_user = kwargs.pop('initial_user', None)
        available_users = kwargs.pop('available_users', None)
        super(UserForm, self).__init__(*args, **kwargs)
        if initial_user is not None:
            self.fields['user'].initial = initial_user
        if available_users is not None:
            self.fields['user'].choices = available_users

    user = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-select',
            'onchange': 'this.form.submit()'
        })
    )


class SearchForm(forms.Form):
    search_bar = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Search for news...'
        })
    )
