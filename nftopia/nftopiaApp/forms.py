from dataclasses import field
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Post
from django.forms import ModelForm, TextInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo']
        # widgets = {
        #     'nickname': forms.TextInput(attrs={
        #         'class': 'input-nickname', 
        #         'placeholder': '이메일 입력'}),
        # }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        #self.fields['nickname'].widget.attrs = {
        #    'class': 'input-nickname',
        #    'placeholder': '이메일 입력',
        #    'style': 'margin-left: auto, margin-right: auto'
        #}

        self.fields['photo'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "사진 선택",
            'id': 'imagefile',
            # 'style': 'color:black;' # 알아서 색 맞춰 수정하기
        }