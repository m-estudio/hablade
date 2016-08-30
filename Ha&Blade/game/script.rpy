# 您可以在此编写游戏的脚本。

# 下方的image命令可用于定义一个图像。
# 例：image eileen happy = "eileen_happy.png"

image bg sakuza = "sakuza.jpg"
#image bg bedroom = "bedroom.jpg"
#image bg WC = "wc.jpg"

# 下方的define命令可定义游戏中出现的角色名称与对应文本颜色。
# 译注：define还可以定义很多功能，具体请参阅官方文档。
define ha = Character(u'虫忍合', color="#66ccff")
define what = Character(u'？？？',color="#ff66cc")
define mom = Character(u'母上',color="#fafafa")
define jade = Character(u'玉华',color="#990066")
# 引用游戏OP视频，在进入程序主菜单显示前自动播放。
# 此处也可以使用图片代替。
# label splashscreen:
    # $ renpy.movie_cutscene('data/op.avi')
    # return
init python:
    Uattack = 0
    Uspecial = 0
    Udefence = 0
    Uhp = 0
    Ujob = False
    Ubuff = 1.0

label start:
# 下面的参数用于设定是否允许用户通过点击或快进功能跳过转场特效。
    $ _skipping = True

# 是否允许用户通过点击或快进跳过暂停时间。
# 暂停时间是通过pause命令实现的，具体请参阅官方文档。
    $ _dismiss_pause = True


    scene bg sakuza

    "樱花开了，只有忍耐，才能看到鲜血洗去一地落英……"

    what "你想成为一个守卫秩序的战士吗，合？或者更愿意在这混乱的做一个不稳定的魔法师？"
    menu:
        "苟利战士生死以":
            python:
                Ujob = False
                Uattack = Uattack + 10
        "岂因魔法避趋之":
            python:
                Ujob = True
                Uattack = Uattack + 5
                Uspecial = Uspecial + 5
        "我选择汪峰导师":
            jump dead1
    
    what "想不到你是这样的虫忍合。入学考马上就开始了，你准备的如何"
    $entryFlag = False
    menu:
        "不怎么样":
            python:
                Ubuff = Ubuff + 0.01
        "还行，估计能不挂":
            python:
                Ubuff = Ubuff
        "其实学校已经内定了，我将以第一名入校":
            python:
                entryFlag = True
    if entryFlag:
        what "你好强啊。"
    what "其实我没准备好……不如我们先来打一架吧！"
    ha "一言不合？……啊……啊啊……不要啊……"
    "？？？的剑尖划过，穿过几片飘落的花瓣。合急忙举起武器格挡。"
    what "接受了我的挑战，那就拿出你的本事来吧。"
    ha "什么设定？这就真打了？……"
    "进入战斗"
#战斗
    if entryFlag:
        jump dead2
    what "不错，看你骨骼清奇，是个可造之才。半个月后开学，尽早收拾启程吧。"
    ha "蛤？这就入学考？"
label wakeup:
#    scene bg bedroom
#    with dissolve
    "午后醒来，恍若隔世。"
    mom "虫忍合，好孩子！你真的真的真的考上了夏威夷州立高级中学俄亥俄州立大学分部的音乃木阪和常盘台女子中学的男子高中游泳部！今晚想吃什么，妈妈什么也不会给你做的。"
    ha "真是亲妈……话说我什么时候考的这鬼畜高中？"
    mom "就是半个月前你考的那个华莱士高校啊。录取通知书刚刚发到。"
    ha "这明显是两个学校吧……还有，我到底吃什么啊？"
    mom "我刚订了华莱士炸鸡。你就吃剩下的末吧。"
    menu:
        "自己订便当":
            jump biandang
        "吃末":
            if Ujob:
                python:
                    Uspecial += 10
            else:
                python:
                    Uattack += 5
        "去吃尸米":
            jump dead3
    return 
