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

doc = """
Simple trust game
"""


class Constants(BaseConstants):
    name_in_url = 'AI'
    players_per_group = None
    num_rounds = 10

    endowment = c(10)
    multiplier = 3

    instructions_template = 'AI/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sent_amount = models.CurrencyField(
        choices=currency_range(c(0), Constants.endowment, c(1)),
        doc="""Amount sent by P1""",
        label="コンピュータにいくら送りますか？",
        initial=c(0)
    )