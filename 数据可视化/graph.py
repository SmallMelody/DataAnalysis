# from pyecharts import Geo,Map
#
# data = [
#     ("海门", 9),("莆田",1),("南京",1),("安徽",10)]
#
# geo = Geo("千人计划", "获得称号信息", title_color="#DC143C",
#           title_pos="center", width=1200,
#           height=600, background_color='#F8F8FF')
# attr, value = geo.cast(data)
# geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#F5FFFA",
#         symbol_size=15, is_visualmap=True)
# geo.render()

from pyecharts import Map
value = [20,20,90,50,20,10,20,20,20,20,80,10,10,50,20,50,20,10,20,70]
attr = ["安徽","福建","北京","广东","广西","黑龙江","河北","河南","湖北","湖南","江苏","江西","山东","浙江","山西","四川",
        "台湾","天津","吉林","陕西"]

map = Map("千人计划学者籍贯分布图", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True,
        visual_text_color='#000')
map.render()