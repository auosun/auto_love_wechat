import requests

import card
import config


class WeChatMessagePush(object):
    api = config.wx_api

    def get_token(self):
        data = requests.get(self.api['token']).json()
        # print('get_token success', data)
        return data['access_token']

    @staticmethod
    def construct_message():
        data = {
            "birthDay": card.BirthdayCard()(),
            "loveDay": card.LoveDayCard()(),
            # "rainbow": card.RainBowCard()(),
            "star": card.StarCard()(),
            "salaryDay": card.SalaryCard()()
        }
        data.update(card.WeatherCards()())

        return {
            "touser": config.user_id,
            "template_id": config.template_id,
            "url": "",
            "topcolor": "#FF0000",
            "data": data
        }

    def push_message(self, token, message: dict):
        url = self.api['message'].format(token=token)
        resp = requests.post(url, json=message)
        print(resp.content)

    def run(self):
        token = self.get_token()
        message = self.construct_message()
        self.push_message(token, message)
