# # from django import forms
# # from .models import ReviewTable
# # # class Review_form(forms.Form):
# # #     user_name = forms.CharField(max_length=100, label='Your Name:')
# # #     review_text = forms.CharField(
# # #         widget=forms.Textarea,
# # #         label="Review Text:",
# # #         max_length=1000,
# # #         error_messages={
# # #             "required": "You have to fill the blanks",
# # #             "max_length": "It should be below 1001 chars"
# # #         }
# # #     )
# # #     rating = forms.IntegerField(label="Rate:",max_value=5, min_value=1)
# # #     # text = forms.CharField(label="Text", max_length=100)
# # #     # password = forms.CharField(label="Password", widget=forms.PasswordInput)
# # #     # email = forms.EmailField(label="Email")
# # #     # search = forms.CharField(label="Search", widget=forms.TextInput(attrs={'type': 'search'}))
# # #     # tel = forms.CharField(label="Telephone", widget=forms.TextInput(attrs={'type': 'tel'}))
# # #     # url = forms.URLField(label="URL")

# # #     # number = forms.IntegerField(label="Number", min_value=0, max_value=100)
# # #     # range = forms.IntegerField(label="Range", widget=forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100'}))

# # #     # date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type': 'date'}))
# # #     # month = forms.DateField(label="Month", widget=forms.DateInput(attrs={'type': 'month'}))
# # #     # week = forms.DateField(label="Week", widget=forms.DateInput(attrs={'type': 'week'}))
# # #     # time = forms.TimeField(label="Time", widget=forms.TimeInput(attrs={'type': 'time'}))
# # #     # datetime_local = forms.DateTimeField(label="Datetime Local", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

# # #     # checkbox = forms.BooleanField(label="Checkbox", required=False)
# # #     # radio_choice = forms.ChoiceField(
# # #     #     label="Radio",
# # #     #     choices=[('1', 'Option 1'), ('2', 'Option 2')],
# # #     #     widget=forms.RadioSelect
# # #     # )

# # #     # file_upload = forms.FileField(label="File Upload", required=False)

# # #     # image_submit = forms.CharField(
# # #     #     label="Image Submit (simulated)",
# # #     #     required=False,
# # #     #     widget=forms.TextInput(attrs={'type': 'image', 'src': 'https://via.placeholder.com/100'})
# # #     # )

# # #     # color = forms.CharField(label="Color", widget=forms.TextInput(attrs={'type': 'color'}))


# # #     # hidden = forms.CharField(widget=forms.HiddenInput(), initial='12345')


# # class Review_form(forms.ModelForm):
# #     class Meta:
# #         model = ReviewTable
# #         fields = "__all__"