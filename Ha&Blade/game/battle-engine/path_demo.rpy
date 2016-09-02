label path_demo:
    
    play music "audio/battle.ogg" fadein 0.5
    
    # The Path Demo assumes that you've already read and understood the comments in
    # the Active Demo, Simple Grid Demo and Iso Grid Demo, and will not repeat those concepts.
    # Only new things are commented in this demo.
    
    python:
        
        battle = Battle(ActiveSchema())

        fieldSprite = BattlefieldSprite('bg woodland path')

        # For a path battle, predictably we use a PathBattlefield... this doesn't have any parameters other than the sprite,
        # we'll add the path separately.
        battlefield = PathBattlefield(fieldSprite)
        
        battle.SetBattlefield(battlefield)
        
        
        # Now we have to create a series of BattlePosition instances, one for each spot on the map.
        # (The example path map has the path drawn on; the spots are numbered in a clockwise spiral from the leftmost one.)
        # Each BattlePosition has two parameters, the X and Y coordinates of the screen position it occupies.

        pos1 = BattlePosition(62, 292)
        pos2 = BattlePosition(196, 271)
        pos3 = BattlePosition(318, 226)
        pos4 = BattlePosition(438, 161)
        pos5 = BattlePosition(571, 191)
        pos6 = BattlePosition(703, 226)
        pos7 = BattlePosition(723, 331)
        pos8 = BattlePosition(683, 436)
        pos9 = BattlePosition(551, 465)
        pos10 = BattlePosition(409, 446)
        pos11 = BattlePosition(278, 361)
        pos12 = BattlePosition(399, 311)
        
        # Now we need to add them to the battlefield...
        
        battlefield.AddPosition(pos1)
        battlefield.AddPosition(pos2)
        battlefield.AddPosition(pos3)
        battlefield.AddPosition(pos4)
        battlefield.AddPosition(pos5)
        battlefield.AddPosition(pos6)
        battlefield.AddPosition(pos7)
        battlefield.AddPosition(pos8)
        battlefield.AddPosition(pos9)
        battlefield.AddPosition(pos10)
        battlefield.AddPosition(pos11)
        battlefield.AddPosition(pos12)

        # Next, we need to add joins between pairs of positions. Each join is two-way, so once you've added a join
        # from pos1 to pos2, you don't have to add one from pos2 to pos1.
        
        battlefield.AddJoin(pos1, pos2)
        battlefield.AddJoin(pos2, pos3)
        battlefield.AddJoin(pos2, pos11)
        battlefield.AddJoin(pos3, pos4)
        battlefield.AddJoin(pos3, pos11)
        battlefield.AddJoin(pos3, pos12)
        battlefield.AddJoin(pos4, pos5)
        battlefield.AddJoin(pos4, pos12)
        battlefield.AddJoin(pos5, pos6)
        battlefield.AddJoin(pos6, pos7)
        battlefield.AddJoin(pos7, pos8)
        battlefield.AddJoin(pos8, pos9)
        battlefield.AddJoin(pos9, pos10)
        battlefield.AddJoin(pos10, pos11)
        battlefield.AddJoin(pos10, pos12)
        battlefield.AddJoin(pos11, pos12)
        
        # (If you want to add a one-way join, you can call the 'AddOneWay' method. So if we were adding a one-way
        # join from pos1 to pos11, we'd write:
        # battlefield.AddOneWay(pos1, pos2)

        
        battle.AddFaction("Player", playerFaction=True)
        
        bobSprite = BattleSprite('bob', anchor=(0.5, 0.75), placeMark=(0,-100))
        bob = PlayerFighter("Bob", Speed=8, Attack=20, Defence=20, Move=1, sprite=bobSprite) 
        bob.RegisterSkill(Library.Skills.SwordAttack)
        bob.RegisterSkill(Library.Skills.Skip)
        bob.RegisterSkill(Library.Skills.PathMove)
        
        # When we add the fighter to a PathBattlefield, we need to supply the 'position' parameter, telling
        # the battlefield which position to place the fighter in:
        battle.AddFighter(bob, position=pos1)
        
        geoffSprite = BattleSprite('geoff', anchor=(0.5, 0.8), placeMark=(0,-100))
        geoff = PlayerFighter("Geoff", Speed=13, Attack=7, Defence=10, Move=1, MP=20, sprite=geoffSprite)
        geoff.RegisterSkill(Library.Skills.SwordAttack)
        geoff.RegisterSkill(Library.Skills.Skip)
        geoff.RegisterSkill(Library.Skills.Fire1)
        geoff.RegisterSkill(Library.Skills.Water1)
        geoff.RegisterSkill(Library.Skills.Earth1)
        geoff.RegisterSkill(Library.Skills.PathMove)
        battle.AddFighter(geoff, position=pos2)
        
        
        battle.AddFaction('Enemies', playerFaction=False)
        
        
        banditSprite = BattleSprite('bandit', anchor=(0.5, 0.75), placeMark=(0,-80))
        
        # Here we're adding an extra parameter to the MovingAIFighter - 'alwaysMove = False'. This tells the
        # AI to only move if it can't do anything more useful, like attacking the player, so it doesn't waste its turns
        # moving when it could attack instead.
        bandit1 = MovingAIFighter("Bandit 1", Library.Skills.PathMove, idealDistance=1, alwaysMove=False, Move=1, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit1.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit1, position=pos6)
        bandit2 = MovingAIFighter("Bandit 2", Library.Skills.PathMove, idealDistance=1, alwaysMove=False, Move=1, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit2.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit2, position=pos7)
        bandit3 = MovingAIFighter("Bandit 3", Library.Skills.PathMove, idealDistance=1, alwaysMove=False, Move=1, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit3.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit3, position=pos8)
        
        
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())

        # Here we add the RPGActionBob extra that we've used before, but this time we add a list of exceptions to it -
        # skills that don't trigger the bob. In this case we don't want the bob when a character moves, only when
        # they perform other actions, so we supply a list containing one item: the MoveSkill class that all move
        # skills descend from.
        battle.AddExtra(RPGActionBob(exceptions=[MoveSkill]))

        # We leave the ActiveDisplay off for now, because I carelessly made the path go underneath it...
        #battle.AddExtra(ActiveDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
        battle.AddExtra(SimpleWinCondition())

        battle.Start()
        
        winner = battle.Won
    
    # Back in regular Ren'Py land:
    if (winner == 'Player'):
        #TODO: Play victory music
        "Well done, you beat the bad guys."
    else:
        #TODO: Play failure music
        "Game Over: You Died."
        
    jump start
