from otree.api import Currency as c, currency_range

from ._builtin import Page


class Demographics(Page):
    form_model = 'player'
    form_fields = ['personality4', 'personality9', 'personality2', 'personality7', 'personality5', 'personality1', 'personality6', 'personality3', 'personality10', 'personality8']

class matching(Page):
    after_all_players_arrive = 'set_payoffs'

page_sequence = [Demographics, matching]
