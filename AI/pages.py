from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants, Player
import random

class Send(Page):

    form_model = 'player'
    form_fields = ['sent_amount']

    timeout_seconds = 180

    @staticmethod
    def  before_next_page(player: Player):
            num = random.randrange(1, 101)
            if 91 <= num <= 100:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.1 + player.sent_amount
            elif 81 <= num <= 90:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.2 + player.sent_amount
            elif 71 <= num <= 80:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.3 + player.sent_amount
            elif 61 <= num <= 70:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.4 + player.sent_amount
            elif 51 <= num <= 60:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.5 + player.sent_amount
            elif 41 <= num <= 50:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.6 + player.sent_amount
            elif 31 <= num <= 40:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.7 + player.sent_amount
            elif 21 <= num <= 30:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.8 + player.sent_amount
            elif 11 <= num <= 20:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 0.9 + player.sent_amount
            elif 1 <= num <= 10:
                sent_back_amount = (player.sent_amount * Constants.multiplier - player.sent_amount) * 1.0 + player.sent_amount
            player.payoff = Constants.endowment - player.sent_amount + sent_back_amount

            # if 91 <= num <= 100:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.1 + self.sent_amount
            # elif 81 <= num <= 90:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.2 + self.sent_amount
            # elif 71 <= num <= 80:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.3 + self.sent_amount
            # elif 61 <= num <= 70:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.4 + self.sent_amount
            # elif 51 <= num <= 60:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.5 + self.sent_amount
            # elif 41 <= num <= 50:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.6 + self.sent_amount
            # elif 31 <= num <= 40:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.7 + self.sent_amount
            # elif 21 <= num <= 30:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.8 + self.sent_amount
            # elif 11 <= num <= 20:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 0.9 + self.sent_amount
            # elif 1 <= num <= 10:
            #     sent_back_amount = (self.sent_amount * Constants.multiplier - self.sent_amount) * 1.0 + self.sent_amount
            # self.payoff = Constants.endowment - self.sent_amount + sent_back_amount


class Results(Page):
    timeout_seconds = 180
    def vars_for_template(player: Player):
        return dict(sent_back_amount = player.payoff + player.sent_amount - Constants.endowment)

page_sequence = [Send, Results]