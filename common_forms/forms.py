#coding=utf8
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField(max_value=5, label="inputA",
                           widget=forms.NumberInput(attrs={'placeholder': "<+=5"}))
    b = forms.IntegerField(max_value=5, label="inputB",
                           widget=forms.NumberInput(attrs={'placeholder': "<+=5"}))
    c = forms.EmailField(label="inputMail",
                         widget=forms.EmailInput(attrs={'placeholder': "请输入合法Email"}))

    # d = forms.EmailField(label="inputMail",
    #                      widget=forms.EmailInput(attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))