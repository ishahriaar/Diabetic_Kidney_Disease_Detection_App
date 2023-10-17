from django.shortcuts import render
from .forms import EDUserInputForm, DKDInputForm
from .ed_train_model import machine_learning_fnc
from .dkd_train_model import dkd_machine_learning_fnc


def home_page_view(request, *args, **kwargs):
    return render(request, 'thesis_work/home.html')


def ed_user_input_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = EDUserInputForm(request.POST)
        if form.is_valid():
            user_input_data = form.cleaned_data
            # predicted_result = {}
            predicted_result = machine_learning_fnc(user_input_data)
            return render(request, 'thesis_work/ed.html', {"predicted_result": predicted_result})
    else:
        form = EDUserInputForm()
    return render(request, 'thesis_work/ed_input.html', {"form": form})


def dkd_user_input_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = DKDInputForm(request.POST)
        if form.is_valid():
            user_input_data = form.cleaned_data
            # predicted_result = {}
            predicted_result = dkd_machine_learning_fnc(user_input_data)
            return render(request, 'thesis_work/dkd.html', {"predicted_result": predicted_result})
    else:
        form = DKDInputForm()
    return render(request, 'thesis_work/dkd_input.html', {"form": form})
