from django import forms
from django.utils.safestring import mark_safe

#
# class HorizontalRadioRenderer(forms.RadioSelect):
#     def render(self):
#         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class EDUserInputForm(forms.Form):
    GENDER_CHOICES = (
        (int(1), 'Male'),
        (int(0), 'Female'),
    )
    BINARY_CHOICES = (
        (int(1), 'Yes'),
        (int(0), 'No'),
    )
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender',widget=forms.Select)
    polyuria = forms.ChoiceField(choices=BINARY_CHOICES, label='Polyuria',widget=forms.Select)
    polydipsia = forms.ChoiceField(choices=BINARY_CHOICES, label='Polydipsia',widget=forms.Select)
    sudden_weight_loss = forms.ChoiceField(choices=BINARY_CHOICES, label='Sudden Weight Loss',widget=forms.Select)
    # weakness = forms.ChoiceField(choices=BINARY_CHOICES, label='Weakness',widget=forms.RadioSelect)
    polyphagia = forms.ChoiceField(choices=BINARY_CHOICES, label='Polyphagia',widget=forms.Select)
    genital_thrush = forms.ChoiceField(choices=BINARY_CHOICES, label='Genital Thrush',widget=forms.Select)
    visual_blurring = forms.ChoiceField(choices=BINARY_CHOICES, label='Visual Blurring',widget=forms.Select)
    itching = forms.ChoiceField(choices=BINARY_CHOICES, label='Itching',widget=forms.Select)
    irritability = forms.ChoiceField(choices=BINARY_CHOICES, label='Irritability',widget=forms.Select)
    delayed_healing = forms.ChoiceField(choices=BINARY_CHOICES, label='Delayed Healing',widget=forms.Select)
    partial_paresis = forms.ChoiceField(choices=BINARY_CHOICES, label='Partial Paresis',widget=forms.Select)
    muscle_stiffness = forms.ChoiceField(choices=BINARY_CHOICES, label='Muscle Stiffness',widget=forms.Select)
    alopecia = forms.ChoiceField(choices=BINARY_CHOICES, label='Alopecia',widget=forms.Select)
    # obesity = forms.ChoiceField(choices=BINARY_CHOICES, label='Obesity',widget=forms.RadioSelect)


class DKDInputForm(forms.Form):
    AL_CHOICES = (
        (int(0), "0"),
        (int(1), "1"),
        (int(2), "2"),
        (int(3), "3"),
        (int(4), "4"),
        (int(5), "5"),
    )
    AL_CHOICES2 = (
        (int(0), "0"),
        (int(1), "1"),
        (int(2), "2"),
        (int(3), "3"),
        (int(4), "4"),

    )
    RBC_CHOICES = (
        (int(1), 'Normal'),
        (int(0), 'Abnormal'),
    )

    PCC_CHOICES = (
        (int(1), 'Present'),
        (int(0), 'Not Present'),
    )
    DBINARY_CHOICE = (
        (int(1), 'Yes'),
        (int(0), 'No'),
    )

    GOOD_CHOICE = (
        (int(0), 'Good'),
        (int(1), 'Poor'),
    )

    age = forms.IntegerField(label='Age')
    bp = forms.IntegerField(label='Blood Pressure (Diastolic) ',)
    sg = forms.ChoiceField(choices=AL_CHOICES2, label='Specific Gravity')
    al = forms.ChoiceField(choices=AL_CHOICES, label='Albumin',widget=forms.RadioSelect)
    # rbc = forms.ChoiceField(choices=RBC_CHOICES, label='Red Blood Cells')
    # pcc = forms.ChoiceField(choices=PCC_CHOICES, label='Pus Cell Clumps')
    su = forms.ChoiceField(choices=AL_CHOICES, label='Sugar', widget=forms.RadioSelect)
    bgr = forms.FloatField(label='BGR')
    sc = forms.FloatField(label='Serum Creatinine',widget=forms.NumberInput(attrs={'placeholder': 'Adult Men, 0.74 to 1.35 mg/dL || Adult Women, 0.59 to 1.04 mg/dL'}))
    hemo = forms.FloatField(label='Hemoglobin',widget=forms.NumberInput(attrs={'placeholder': 'Men, 13.5 to 17.5 gm/dL || Women, 12.0 to 15.5 gm/dL'}))
    pcv = forms.IntegerField(label='pcv', widget=forms.NumberInput(attrs={'placeholder': '10 to 12'}))
    wbcc = forms.IntegerField(label='White Blood Cells Count',widget=forms.NumberInput(attrs={'placeholder': '4,500 to 11,000 μ/L'}))
    rbcc = forms.FloatField(label='RBCC', widget=forms.NumberInput(attrs={'placeholder': 'not set yet'}))
    htn = forms.ChoiceField(choices=DBINARY_CHOICE, label='Hypertension',widget=forms.RadioSelect)
    dm = forms.ChoiceField(choices=DBINARY_CHOICE, label='Diabetes',widget=forms.RadioSelect)
    cad = forms.ChoiceField(choices=DBINARY_CHOICE, label='Coronary Artery Disease',widget=forms.RadioSelect)
    appet = forms.ChoiceField(choices=GOOD_CHOICE, label='Appetite',widget=forms.RadioSelect)
    pe = forms.ChoiceField(choices=DBINARY_CHOICE, label='Pedal Enema',widget=forms.RadioSelect)
    # ane = forms.ChoiceField(choices=DBINARY_CHOICE, label='Anemia',widget=forms.RadioSelect)
