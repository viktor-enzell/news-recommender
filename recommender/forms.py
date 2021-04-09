from django import forms


class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        initial_user = kwargs.get('initial_user')
        if initial_user is not None:
            kwargs.pop('initial_user')
        super(UserForm, self).__init__(*args, **kwargs)
        if initial_user is not None:
            self.fields['user'].initial = initial_user

    USERS = (('User 1', 'User 1'), ('User 2', 'User 2'),)

    user = forms.ChoiceField(
        choices=USERS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
