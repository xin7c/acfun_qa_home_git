# coding=utf8
from django import forms


class AddForm(forms.Form):
    a = forms.CharField(max_length=20, label="Name",
                           widget=forms.TextInput(attrs={"placeholder": "你的名字", "autofocus": "autofocus"}))

    c = forms.EmailField(label="Email",
                         widget=forms.EmailInput(attrs={"placeholder": "请输入合法Email"}))


    # b = forms.IntegerField(max_value=5, label="inputB",
    #                        widget=forms.NumberInput(attrs={"placeholder": "<+=5"}))

    # d = forms.EmailField(label="inputMail",
    #                      widget=forms.EmailInput(attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))
