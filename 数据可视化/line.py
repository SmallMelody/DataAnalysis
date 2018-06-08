from pyecharts import Line

attr = ["35-40", "41-45", "46-50", "51-55", "56-60", "61-70"]
v1 = [0, 3, 5, 32, 39, 19]
v2 = [4, 18, 39, 31, 6, 0]
line = Line("部分千人计划年龄与获奖年龄")
line.add("年龄", attr, v1, is_smooth = True,mark_line=["max","average"])
line.add("获奖年龄", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.render()
