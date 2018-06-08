# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 15:59
# @Author  : Spytensor
# @File    : move.py
# @Email   : zhuchaojie@buaa.edu.cn

from pyecharts import GeoLines, Style
style = Style(
    title_top="#DC143C",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#FFFFFF"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#DC143C",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#DC143C'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#FFA500",
)
geo_cities_coords = {
    "东京":[139.7319925000,35.7090259000],
    "南昌大学":[115.9373470000,28.6835290000],
    "伊利诺伊州立大学":[-88.9946702000,40.5122833000],
    #"北京":[116.3252350000,40.0003040000],
    "巴黎第七大学":[2.3817936000,48.8293187000],
    "华北电力大学":[116.3036974567,40.0884828800],
    "McMaster大学":[-79.9192254000,43.2608790000],
    "华东师范大学":[121.4064049360,31.2284858690],
    "加州大学伯克利分校":[-122.2585399000,37.8718992000],
    "纽约大学":[-73.9964609000,40.7295134000],
    "波士顿塔夫兹大学":[-71.1190232000,42.4074843000],
    "中山大学":[113.2988830000,23.0965384000],
    "欧道明大学":[-76.3067777000,36.8856104000],
    "加州理工学院":[-118.125269,34.137657600],
    "德州大学":[-97.7340567000,30.284918500],
    "俄亥俄州立大学":[-83.0309143000,40.0141905],
    "蒙特利尔大学":[-73.613759200,45.5056156],
    "厦门大学":[118.0978550000,24.43734840],
    "加州大学":[-117.2340135,32.88006040],
    "佛蒙特州大学":[-73.1964637,44.47785280],
    "爱因斯坦医学院":[-73.84439380,40.85214510],
    "加州大学圣巴巴拉分校":[-119.8489470,34.4139629],
    "纽约州立大学布法罗分校":[-78.78896970,43.00080930],
    "纽约州立大学布法罗分":[-78.7889697,43.00080930],
    "纽约州立大学石溪分校":[-73.1233889,40.9123761],
    "巴塞尔大学":[7.5826000,47.560253500],
    "天主教大学":[-76.998692,38.9368811],
    "美国":[-77.0368707000,38.9071923000],
    "瑞士":[4474468000,46.9479739],
    "法国":[2.3522219,48.8566140],
    "加拿大":[-75.6971931,45.42152960]
}

data_beijing = [
    ["美国","南昌"],
    ["法国","北京"],
    ["加拿大","北京"],
    ["美国","上海"],
    ["美国","北京"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国","广州"],
    ["美国",'厦门'],
    ["美国","厦门"],
    ["美国","厦门"],
    ["美国","厦门"],
    ["美国","厦门"],
    ["美国","厦门"],
    ["美国","厦门"],
    ["瑞士","厦门"],
    ["美国","厦门"],

]
geolines = GeoLines("千人计划学者院校迁移图(部分展示)", **style.init_style)
geolines.add("学籍迁移", data_beijing, maptype="world",**style_geo,geo_cities_coords=geo_cities_coords)
geolines.render()

