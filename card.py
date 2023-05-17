import datetime
import random

import requests

import config


class MessageCard(object):

    def __init__(self, **kwargs):
        self.context = kwargs

    def get_value(self):
        return self.context.get('value')

    def get_color(self):
        color_str = '0123456789abcdef'
        colors = [color_str[random.randint(0, len(color_str) - 1)] for _ in range(6)]
        return f"#{''.join(colors)}"

    def __call__(self, *args, **kwargs):
        return dict(
            value=self.get_value(),
            color=self.get_color()
        )


class MessageCards(MessageCard):
    card_template = MessageCard

    def get_values(self) -> dict:
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        data = self.get_values()
        return {
            k: self.card_template(value=item)()
            for k, item in data.items()
        }


class WeatherCards(MessageCards):
    def get_values(self) -> dict:
        value = requests.get(config.weather_api)
        weather = value.json()['lives'][0]
        return {
            'weather': weather['weather'],
            'temp': weather['temperature'],
            'humidity': weather['humidity']
        }


class LoveDayCard(MessageCard):

    def get_value(self):
        love_day = (datetime.datetime.now() - config.love_day).days
        return love_day


class BirthdayCard(MessageCard):
    def get_value(self):
        now = datetime.datetime.now()
        now_year = now.year
        birthday = config.birthday.replace(now_year)
        if now > birthday:
            birthday = birthday.replace(year=now_year + 1)

        day = (birthday - now).days
        return day


class RainBowCard(MessageCard):

    def get_value(self):
        content = requests.get('https://tenapi.cn/chp/')
        return content.json()['data']['text']


class SalaryCard(MessageCard):

    def get_value(self):
        now = datetime.datetime.now()
        salary_day = now.replace(day=15)
        if now > now.replace(day=15):
            if now.month == 12:
                salary_day = salary_day.replace(month=1, year=now.year + 1)
            else:
                salary_day = salary_day.replace(month=now.month + 1)

        day = (salary_day - now).days
        return day


class StarCard(MessageCard):

    def get_value(self):
        resp = requests.get(config.star_api)
        content = resp.json()['result']['list']
        content_kv = {item["type"].replace('指数', ''): item["content"].replace('%', '') for item in content}
        self.context['color'] = content_kv.get('幸运颜色')

        # star_str = [f"{item['type'].replace('指数', '')} {item['content']}" for item in content[:-2]]
        # star_str.append(content[-1]['content'])
        # return "\n\r".join(star_str)
        return f"\n综合: {content_kv['综合']} 爱情: {content_kv['爱情']} 工作: {content_kv['工作']} 财运: {content_kv['财运']}" \
               f"\n健康: {content_kv['健康']} 幸运颜色: {content_kv['幸运颜色']} 幸运数字: {content_kv['幸运数字']}" \
               f"\n{content_kv['今日概述']}"

    def get_color(self):
        color = self.context['color']
        if color in config.web_color:
            return config.web_color.get(color)
        else:
            return super(StarCard, self).get_color()


if __name__ == '__main__':
    a = StarCard()()
