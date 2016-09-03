label dead1:

    what"职业这么重要的事情，怎么能不慎重？"
    "选职业？"
    "虫忍合狗带了"
    "Dead Ending."

    return
label dead2:
    
    what "哼。果然走后门进来的就没什么好货。去死吧。"
    ha "你说什么？……啊……"
    "手臂好凉啊。"
    "腿好凉啊。"
    "杀头，至痛也。然花生米与豆腐干同嚼，有火腿滋味。"
    "虫忍合狗带了"
    "Dead Ending."

    return
label biandang:
    "半小时后……"
    "你要的便当到了，领一下。"
    "虫忍合狗带了"
    "Dead Ending."

    return
label dead3:
    scene bg WC
    ha "不小心吃太多了……噎到了……"
    "虫忍合狗带了"
    "Dead Ending."

    return
label deadfuta:
    "玉华掏出了一个带着马赛克的长棍，面色阴沉地捅死了你。"
    "虽然我不喜欢法式长棍，但我喜欢法式长吻。"
    "虫忍合狗带了"
    "Dead Ending."
    return
label deadHoming:
    scene bg homeRoad with fade
    what "去死吧！"
    ha "是你？！！"
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
            ha1 = PlayerFighter("虫忍合", Speed=Uspeed*Ubuff, Attack=Uspeed*Ubuff, Defence=Udefence*Ubuff, MP=Uspecial*Ubuff, sprite=geoffSprite)
            ha1.RegisterSkill(Library.Skills.SwordAttack)
            ha1.RegisterSkill(Library.Skills.Skip)
            ha1.RegisterSkill(Library.Skills.Fire1)
            ha1.RegisterSkill(Library.Skills.Water1)
            ha1.RegisterSkill(Library.Skills.Earth1)
            battle.AddFighter(ha1)

        battle.AddFaction('Enemies', playerFaction=False)
        whatSprite = BattleSprite('bandit', anchor=(0.5, 0.75), placeMark=(0,-100))
        what1 = SimpleAIFighter("???", Speed=10, Attack=65535, Defence=65535, sprite=whatSprite)
        what1.RegisterSkill(Library.Skills.KnifeAttack,16)
        battle.AddFighter(what1)        
        
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(ActiveDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
        battle.AddExtra(RPGActionBob())
        battle.AddExtra(SimpleWinCondition())

        battle.Start()
    "虫忍合狗带了"
    "但你死前闻到了???身上的香水味。似乎和玉华用的是同一款。"
    "Dead Ending."
    return
label deadGaming:
    scene bg comroom
    "三天后，电竞部开展了第一次线下交流赛。"
    "经过10个小时的奋战，你终于电死了对手。"
    ha "我们赢了！赢啦！啊……心好痛！"
    "由于长时间承受电击，你猝死了。"
    "虫忍合狗带了"
    "Dead Ending."
    return