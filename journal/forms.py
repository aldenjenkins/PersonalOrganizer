from django.forms import ModelForm

from journal.models import JournalEntry


class JournalEditForm(ModelForm):
    class Meta:
        model = JournalEntry
        fields = ('text',)

    # def save(self, commit=True):
    #     self.fields['author'] = self.req
    #     return super(JournalEditForm, self).save(commit)
