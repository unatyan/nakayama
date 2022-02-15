from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'survey_A'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    personality4 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='人に気をつかう、やさしい人間だと思う。',
        widget=widgets.RadioSelect, 
    )
    personality9 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='新しいことが好きで、変わった考えをもつと思う。',
        widget=widgets.RadioSelect, 
    )
    personality2 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='ひかえめで、おとなしいと思う。',
        widget=widgets.RadioSelect, 
    )
    personality7 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='心配性で、うろたえやすいと思う。',
        widget=widgets.RadioSelect, 
    )
    personality5 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='しっかりしていて、自分に厳しいと思う。',
        widget=widgets.RadioSelect, 
    )
    personality1 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='活発で、外向的だと思う。',
        widget=widgets.RadioSelect, 
    )
    personality6 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='だらしなく、うっかりしていると思う。',
        widget=widgets.RadioSelect, 
    )
    personality3 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='他人に不満をもち、もめごとを起こしやすいと思う。',
        widget=widgets.RadioSelect, 
    )
    personality10 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='発想力に欠けた、平凡な人間だと思う。',
        widget=widgets.RadioSelect, 
    )
    personality8 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        label='冷静で、気分が安定していると思う。',
        widget=widgets.RadioSelect, 
    )