from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task", min_length=2)
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10, initial=5)
    desc = forms.CharField(label="Details", widget=forms.Textarea)

    def clean(self):
        #WRONG: super(NewTaskForm, self.clean())
        super(NewTaskForm, self).clean()

        t = self.cleaned_data['task']
        p = self.cleaned_data['priority']

        if p >5 and len(t) < 10:
            self.errors['task'] = self.error_class([
                'Minimum 10 chars needed when priorty > 5'
            ])
        return self.cleaned_data


class TaskNameForm(forms.Form):
    task = forms.CharField(label="Task", min_length=2)


from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"