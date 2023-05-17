import datetime

app_id = ""
app_secret = ""
template_id = ""
user_id = ""

wx_api = {
    'token': f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}",
    "message": "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={token}"
}

love_day = datetime.datetime(year=1970, month=1, day=1, hour=1, minute=1)

birthday = datetime.datetime(year=1970, month=1, day=1)

salary_day = 15

city = "320104"  # 秦淮区
amap_key = ""
weather_api = f"https://restapi.amap.com/v3/weather/weatherInfo?key={amap_key}&city={city}"

star_key = ""
astro = "virgo"
star_api = f"https://apis.tianapi.com/star/index?key={star_key}&astro={astro}"

wx_template = """
今日天气: {{weather.DATA}} 
当前温度: {{temp.DATA}} 
空气湿度: {{humidity.DATA}} 
今天是我们的第 {{loveDay.DATA}} 天 
距离你的生日还有 {{birthDay.DATA}} 天 
距离发工资还有 {{salaryDay.DATA}} 天
星座运势: {{star.DATA}}
{{rainbow.DATA}}
"""

web_color = {
    "黑色": "#000000",
    "白色": "#FFFFFF",
    "红色": "#FF0000",
    "酸橙": "#00FF00",
    "蓝色": "#0000FF",
    "黄色": "#FFFF00",
    "青色": "#00FFFF",
    "水色": "#00FFFF",
    "洋红色": "#FF00FF",
    "紫红色": "#FF00FF",
    "银": "#C0C0C0",
    "灰色": "#808080",
    "栗色": "#800000",
    "橄榄": "#808000",
    "绿色": "#008000",
    "紫色": "#800080",
    "蓝绿色": "#008080",
    "海军": "#000080",
    "金色": "#FFD700",
    "橙色": "#FFA500"
}
