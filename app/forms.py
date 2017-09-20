from django import forms
from material import Row, Fieldset, Layout, Column, Span3
from .models import Post, Father, Mother, Applicant
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'tiny-class'

    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'title_extended', 'text',)


class ApplicantForm(forms.ModelForm):
    name = forms.CharField()
    surname = forms.CharField()
    school = forms.ChoiceField(choices=(('En', 'Engineering'),
                                        ('Ph', 'Philology'), ('L', 'Law'), ('Bu', 'Business Administration')))
    major = forms.CharField()
    gender = forms.ChoiceField(choices=(('F', 'Female'),
                                        ('M', 'Male'), ('O', 'Other')), widget=forms.RadioSelect)
    address = forms.CharField()
    date_of_birth = forms.DateField()
    nationality = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    related = forms.ChoiceField(label="Where you heard about us?",
                                choices=(('Friends', 'Friends'),
                                        ('Relatives', 'Relatives'), ('KTL', 'KTL'),
                                         ('Dostyk', 'Dostyk'), ('Internet', 'Internet'),
                                         ('Other', 'Other')), widget=forms.RadioSelect)
    entry_year = forms.CharField()
    graduation_year = forms.CharField()
    level = forms.ChoiceField(choices=(('BA', 'Bachelor'),
                                        ('MSc', 'Masters'), ('PHD', 'Doctor of Philosophy')))
    student_type = forms.ChoiceField(choices=(('P', 'Preparation'),
                                              ('1', 'Freshman'), ('2', 'Sophomore'),
                                              ('3', 'Junior'), ('4', 'Senior')))
    passport_id = forms.CharField()
    number = forms.CharField()
    unt = forms.ChoiceField(label='UNT', choices=(('125', '125'), ('124', '124'),
                                     ('123', '123'), ('122', '122'),
                                     ('121', '121'), ('120', '120'),
                                     ('119', '119'), ('118', '118'),
                                     ('117', '117'), ('116', '116'),
                                     ('115', '115'), ('114', '114'),
                                     ('113', '113'), ('112', '112'),
                                     ('111', '111'), ('110', '110'),))
    attestat_number = forms.CharField()
    attestat_date = forms.DateField()
    attestat_type = forms.ChoiceField(choices=(('R', 'Regular'),
                                        ('H', 'With Honor'), ('A', 'Altyn Belgi')), widget=forms.RadioSelect)
    payment = forms.ChoiceField(choices=(('GG', 'Grant'),
                                        ('SG', 'SDU Grant'), ('P', 'Paid')), widget=forms.RadioSelect)
    certificate_number = forms.CharField()

    layout = Layout(
        Fieldset('General Information',
                 Row('name', 'surname', 'gender'),
                 Row('school', 'major', ),
                 'address',
                 Row(Span3('date_of_birth'), Span3('nationality'), Span3('phone'), Span3('email')),
                 ),
        Fieldset('Educational Data',
                 Row('level', 'student_type'),
                 'entry_year',
                 'graduation_year',
                 Row('attestat_number', 'attestat_type'),
                 'unt', 'certificate_number',
                 'payment'
                 ),
        Fieldset('Documentation',
                 Row(Column(('passport_id'), ('number')),
                 'related')
                 )
    )

    class Meta:
        model = Applicant
        fields = ('name',
                  'surname', 'school',
                  'major', 'gender',
                  'address', 'date_of_birth',
                  'nationality', 'father',
                  'mother', 'phone',
                  'email', 'related',
                  'entry_year', 'graduation_year',
                  'level', 'student_type',
                  'passport_id', 'number',
                  'unt', 'attestat_number',
                  'attestat_date', 'attestat_type',
                  'payment', 'certificate_number')


class MyApplicantForm(forms.ModelForm):
    name = forms.CharField()
    surname = forms.CharField()
    school = forms.ChoiceField(choices=(('En', 'Engineering'),
                                        ('Ph', 'Philology'), ('L', 'Law'),
                                        ('Bu', 'Business Administration')), widget=forms.RadioSelect)
    major = forms.CharField()
    gender = forms.ChoiceField(choices=(('F', 'Female'),
                                        ('M', 'Male'), ('O', 'Other')))
    address = forms.CharField()
    date_of_birth = forms.DateField()
    nationality = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    related = forms.ChoiceField(label="Where you heard about us?",
                                choices=(('Friends', 'Friends'),
                                        ('Relatives', 'Relatives'), ('KTL', 'KTL'),
                                         ('Dostyk', 'Dostyk'), ('Internet', 'Internet'),
                                         ('Other', 'Other')))
    entry_year = forms.CharField()
    graduation_year = forms.CharField()
    level = forms.ChoiceField(choices=(('BA', 'Bachelor'),
                                        ('MSc', 'Masters'), ('PHD', 'Doctor of Philosophy')))
    student_type = forms.ChoiceField(choices=(('P', 'Preparation'),
                                              ('1', 'Freshman'), ('2', 'Sophomore'),
                                              ('3', 'Junior'), ('4', 'Senior')))
    passport_id = forms.CharField()
    number = forms.CharField()
    unt = forms.ChoiceField(label='UNT', choices=(('125', '125'), ('124', '124'),
                                     ('123', '123'), ('122', '122'),
                                     ('121', '121'), ('120', '120'),
                                     ('119', '119'), ('118', '118'),
                                     ('117', '117'), ('116', '116'),
                                     ('115', '115'), ('114', '114'),
                                     ('113', '113'), ('112', '112'),
                                     ('111', '111'), ('110', '110'),))
    attestat_number = forms.CharField()
    attestat_date = forms.DateField()
    attestat_type = forms.ChoiceField(choices=(('R', 'Regular'),
                                        ('H', 'With Honor'), ('A', 'Altyn Belgi')))
    payment = forms.ChoiceField(choices=(('GG', 'Grant'),
                                        ('SG', 'SDU Grant'), ('P', 'Paid')), widget=forms.RadioSelect)
    certificate_number = forms.CharField()


    layout = Layout(
        Fieldset('Student Information',
                 Row('name', 'surname'),
                 'school', 'major',
                 Row('level', 'student_type'),
                 Row('gender', 'date_of_birth'),
                 'phone', 'email', 'address',
        ),
        Fieldset('Personal Requisites',
                 'passport_id', 'number', 'nationality'
        ),
        Fieldset('Additional Information',
                 Row('entry_year', 'graduation_year'),
                 Row('attestat_number', 'attestat_type','attestat_date'),
                 Row('certificate_number', 'unt'),
                 'payment'
        )

    )

    class Meta:
        model = Applicant
        fields = ('name', #
                  'surname', 'school', ##
                  'major', 'gender', ##
                  'address', 'date_of_birth', ##
                  'nationality', 'father',
                  'mother', 'phone',  #_#
                  'email', 'related',  #_
                  'entry_year', 'graduation_year', ##
                  'level', 'student_type', ##
                  'passport_id', 'number', ##
                  'unt', 'attestat_number', ##
                  'attestat_date', 'attestat_type', ##
                  'payment', 'certificate_number')


class FatherForm(forms.ModelForm):

    name = forms.CharField()
    surname = forms.CharField()
    job = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

    layout = Layout(
        Fieldset("Father",
                 Row('name', 'surname'),
                 Row('job', 'phone', 'email')
        )
    )

    class Meta:
        model = Father
        fields = ('name', 'surname', 'job', 'phone', 'email')

class MotherForm(forms.ModelForm):

    name = forms.CharField()
    surname = forms.CharField()
    job = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

    layout = Layout(
        Fieldset("Mother",
                 Row('name', 'surname'),
                 Row('job', 'phone', 'email')
                 )
    )

    class Meta:
        model = Mother
        fields = ('name', 'surname', 'job', 'phone', 'email')


class MyFatherForm(forms.ModelForm):

    name = forms.CharField()
    surname = forms.CharField()
    job = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

    layout = Layout(
        Fieldset("Father",
                 'name', 'surname',
                 'job', 'phone', 'email'
        )
    )

    class Meta:
        model = Father
        fields = ('name', 'surname', 'job', 'phone', 'email')

class MyMotherForm(forms.ModelForm):

    name = forms.CharField()
    surname = forms.CharField()
    job = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()

    layout = Layout(
        Fieldset("Mother",
                 'name', 'surname',
                 'job', 'phone', 'email'
        )
    )

    class Meta:
        model = Mother
        fields = ('name', 'surname', 'job', 'phone', 'email')