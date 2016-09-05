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

    scene bg sakuza with dissolve

    "樱花开了，只有忍耐，才能看到鲜血洗去一地落英……"

    what "你想成为一个守卫秩序的战士吗，合？或者更愿意在这混乱的做一个不稳定的魔法师？"
    menu:
        "苟利战士生死以":
            python:
                Ujob = False
                Uattack = Uattack + 10
                Udefence += 10
        "岂因魔法避趋之":
            python:
                Ujob = True
                Uspecial = Uspecial + 20
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
    "？？？的剑尖划过，穿过几片飘落的花瓣。你急忙举起武器格挡。"
    what "接受了我的挑战，那就拿出你的本事来吧。"
    ha "什么设定？这就真打了？……"
    
    "进入战斗"
    python:
        battle = Battle(ActiveSchema())
        fieldSprite = BattlefieldSprite('bg sakuza')
        battlefield = SimpleBattlefield(fieldSprite)
        battle.SetBattlefield(battlefield)
        
        battle.AddFaction("Player", playerFaction=True)
        if Ujob==False:
            haSprite = BattleSprite('bob', anchor=(0.5, 0.75), placeMark=(0,-100))
            ha1 = PlayerFighter(u"虫忍合", Speed=Uspeed*Ubuff, Attack=Uspeed*Ubuff, Defence=Udefence*Ubuff, HP=Uhp, sprite=haSprite) 
            ha1.RegisterSkill(Library.Skills.SwordAttack)
            ha1.RegisterSkill(Library.Skills.Skip)
            battle.AddFighter(ha1)
        if Ujob:
            haSprite = BattleSprite('geoff', anchor=(0.5, 0.8), placeMark=(0,-100))
            ha1 = PlayerFighter("虫忍合", Speed=Uspeed*Ubuff, Attack=Uspeed*Ubuff, Defence=Udefence*Ubuff, MP=Uspecial*Ubuff, sprite=haSprite)
            ha1.RegisterSkill(Library.Skills.SwordAttack)
            ha1.RegisterSkill(Library.Skills.Skip)
            ha1.RegisterSkill(Library.Skills.Fire1)
            ha1.RegisterSkill(Library.Skills.Water1)
            battle.AddFighter(ha1)

        battle.AddFaction('Enemies', playerFaction=False)
        whatSprite = BattleSprite('bandit', anchor=(0.5, 0.75), placeMark=(0,-100))
        what1 = SimpleAIFighter("???", Speed=5, Attack=65535, Defence=65535, sprite=whatSprite)
        what1.RegisterSkill(Library.Skills.KnifeAttack,16)
        battle.AddFighter(what1)        
        
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(ActiveDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
        battle.AddExtra(RPGActionBob())
        battle.AddExtra(SimpleWinCondition())

        battle.Start()

        winner = battle.Won
    
    if (winner == 'Player'):
        #TODO: Play victory music
        what "可以你很强。"
        $ Ubuff+=2.0
   
    if entryFlag:
        jump dead2
    "被击败了……"
    what "不错，看你骨骼清奇，是个可造之才。半个月后开学，尽早收拾启程吧。"
    ha "蛤？这就入学考？"

label wakeup:
#    scene bg bedroom
#    with dissolve
    "午后醒来，恍若隔世。"
    #笑
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
                "虫忍合得到了\"鸡骨杖\"，MP+10"
            else:
                python:
                    Uattack += 5
                "虫忍合得到了\"鸡骨剑\"，Attack+10"
        "去吃尸米":
            jump dead3

label firstdayInSchool:
    
    scene bg sakuza with fade
    
    "花期将尽，但大部分樱花仍开在枝头。你想起中学时的努力奋斗，此刻站在这方圆千米内的最高学府中，不禁怅然。"
    
    jade "你好，你是虫忍合吗？"
    ha "是的。学姐你是？"
    jade "我的名字？我是{color=#ff6666}长穹玉华{/color}，就是你所在的游泳部的部长。很高兴见到你。"
    
    "{color=#cc99cc}诶，我进的是男子游泳部吧{/color}"
    
    ha "蛤？学姐你难道是……"
    
    menu:
        "ふたなり":
            jump deadfuta
        "Lesbian":
            jade "呵呵。"
            #如果二周目，好感降低10
        "可爱的蓝孩子":
            #笑
            jade "你真有趣，难道要我掀起裙子验明正身吗？"
            #如果二周目，好感+10
        "死宅腐女":
            jade "算你说对了"
    #叹息
    jade "我们部里都是些腐女，茂鹏教练早就不高兴了。现在终于有一个真的男生，他写的《提乾社经》终于能派上用场了。"
    ha "什么经？"
    #笑
    jade "呃(⊙o⊙)…别的事情都收拾好了吧？来，我带你去我们部的活动场地——是我们学校唯一的泳池喔。"
    
label firstToPool:
    scene bg shower with fade
    ha "部长，我们这更衣室好小啊。为什么还有一个浴缸？"
    #笑
    jade "这就是我们的泳池啊！"
    ha "蛤？……我可以换部吗？"
    #不悦
    menu:
        "田径部":
            call firstAthletic
        "放学回家部":
            jump deadHoming
        "电竞部":
            jump deadGaming
        "不换":
            #笑
            jade "你做的好，就该这样。"
    jade "我知道我们部设施不好，但是你想想，田径部也只有一台跑步机，科技部也就一只电烙铁，舞部和偶研部还要在天台跳舞抢地盘，音乐部到第八集就弄不出什么好曲子，应援团在全世界Rank100的一个也没有，考古部除了读古文就是打尻鼓，手工研究部都要上课偷偷做作品，电竞部甚至要到校外开展活动。我们部有一个可以放松身心的浴缸，不是很好吗？"

label firstClassroom:
    scene bg classroom with fade
    #笑
    jade "要好好学习喔！"
    return

label firstAthletic:
    scene bg pg with fade
    #不悦
    jade "喏，这就是田径部的活动场地。要是你真想换的话，我就直接把你的名字从游泳部换到这里了。"
    ha "没有田赛项目？"
    jade "准确地说，只有径赛中的跑步项目。"
    ha "部长是谁？我要和他谈谈。为什么只有一台跑步机？"
    jade "田径部的部长也是我。"
    ha "那我还是不换部了……"
    #笑
    jade "这就对了。"





























