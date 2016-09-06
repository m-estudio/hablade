# 您可以在此编写游戏的脚本。

# 下方的image命令可用于定义一个图像。
# 例：image eileen happy = "eileen_happy.png"

image bg sakuza = "images/sakuza.jpg"
#image bg bedroom = "images/bedroom.jpg"
#image bg WC = "images/wc.jpg"
#image bg shower = "images/shower.jpg"
#image bg pg = "images/pg.jpg"
#image bg homeRoad = "images/homeRoad.jpg"
#image bg comroom = "images/comroom.jpg"
#image bg classroom = "images/classroom.jpg"

# 下方的define命令可定义游戏中出现的角色名称与对应文本颜色。
# 译注：define还可以定义很多功能，具体请参阅官方文档。
define ha = Character(u'虫忍合', color="#66ccff")
define what = Character(u'？？？',color="#ff6666")
define mom = Character(u'母上',color="#fafafa")
define jade = Character(u'玉华',color="#ff6666")
define jianhua = Character(u'建嬅',color="#7fffd4")
# 引用游戏OP视频，在进入程序主菜单显示前自动播放。
# 此处也可以使用图片代替。
# label splashscreen:
    # $ renpy.movie_cutscene('data/op.avi')
    # return
init python:
    Uattack = 10
    Uspecial = 10
    Udefence = 10
    Uhp = 50
    Ujob = False
    Ubuff = 1.0
    Uspeed = 11

label start:
# 下面的参数用于设定是否允许用户通过点击或快进功能跳过转场特效。
    $ _skipping = True

# 是否允许用户通过点击或快进跳过暂停时间。
# 暂停时间是通过pause命令实现的，具体请参阅官方文档。
    $ _dismiss_pause = True

    jump chap0
    
    return





























