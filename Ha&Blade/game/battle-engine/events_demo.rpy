label events_demo:
    
    # The Events Demo assumes that you've already read and understood the comments in
    # the Simple Grid Demo, and will not repeat those concepts. Only new things are commented in this
    # demo.

    play music "audio/battle.ogg" fadein 0.5

    
    python:
        battle = Battle(SimpleTurnSchema())

        fieldSprite = BattlefieldSprite('bg woodland simple grid')
        battlefield = GridBattlefield(fieldSprite, origin=(115, 120), gridSize=(8,7), spaceSize=(75, 50), diagonals=False)
        battle.SetBattlefield(battlefield)
        
        treeSprite = BattleSprite('scenery tree', anchor=(0.45, 0.87))
        tree = Scenery('Tree', sprite=treeSprite, blocksPosition=True, blocksLoS=True)
        battle.AddScenery(tree, x=5, y=5)

        treeLineSprite = BattleSprite('scenery front', anchor=(115, 75))
        treeLine = Scenery('Treeline', sprite=treeLineSprite, blocksPosition=False, blocksLoS=False)        
        battle.AddScenery(treeLine, x=0, y=6)
        
        battle.AddFaction('Player', playerFaction=True)
        
        bobSprite = BattleSprite('bob', anchor=(0.5, 0.75), placeMark=(0,-100))
        bob = PlayerFighter("Bob", Speed=8, Move=4, Attack=20, Defence=20, sprite=bobSprite) 
        bob.RegisterSkill(Library.Skills.SwordAttack)
        bob.RegisterSkill(Library.Skills.Skip)
        bob.RegisterSkill(Library.Skills.Move)
        battle.AddFighter(bob, x=1, y=2)
        
        geoffSprite = BattleSprite('geoff', anchor=(0.5, 0.8), placeMark=(0,-100))
        geoff = PlayerFighter("Geoff", Speed=13, Move=5, Attack=7, Defence=10, MP=20, sprite=geoffSprite)
        geoff.RegisterSkill(Library.Skills.SwordAttack)
        geoff.RegisterSkill(Library.Skills.Skip)
        geoff.RegisterSkill(Library.Skills.Move)
        geoff.RegisterSkill(Library.Skills.Fire1)
        geoff.RegisterSkill(Library.Skills.Fire2)
        geoff.RegisterSkill(Library.Skills.Fire3)
        geoff.RegisterSkill(Library.Skills.Water1)
        geoff.RegisterSkill(Library.Skills.Water2)
        geoff.RegisterSkill(Library.Skills.Water3)
        geoff.RegisterSkill(Library.Skills.Earth1)
        geoff.RegisterSkill(Library.Skills.Earth2)
        geoff.RegisterSkill(Library.Skills.Earth3)
        battle.AddFighter(geoff, x=1, y=5)
        
        
        battle.AddFaction('Enemies', playerFaction=False)
        
        banditSprite = BattleSprite('bandit', anchor=(0.5, 0.75), placeMark=(0,-80))
        bandit1 = MovingAIFighter("Bandit 1", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit1.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit1, x=7, y=2)
        bandit2 = MovingAIFighter("Bandit 2", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit2.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit2, x=7, y=3)
        bandit3 = MovingAIFighter("Bandit 3", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit3.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit3, x = 7, y=4)

        
    # Here we add our conditions and results. Because we've dropped back out to
    # Ren'Py code here to do the menu, the lines which deal with the battle engine
    # will need $ signs in front of them.
    
    menu:
        "Select conditions / results:"
        "Kill all enemies to win":
            # To repeat the SimpleWinCondition, we can use a combination of conditions and results.
            # We need a 'FactionDestroyedCondition' to check for when the enemy faction is wiped out:
            $ c = FactionDestroyedCondition('Enemies')
            
            # Now we create a FactionWinsResult to make the player faction win:
            $ r = FactionWinsResult('Player')

            # Next we need to add the relevant result to it. Once a condition is met, all of the results
            # it 'owns' are fired all at once.
            $ c.AddResult(r)
            
            # Lastly, we add the condition to the battle, so that this particular battle will know to fire this particular condition:
            $ battle.AddCondition(c)
            
            # We also have to do the same in reverse, to make sure that the enemy faction wins
            # when the players are wiped out. Much like other things, it can be written a little more concisely:
            $ c2 = FactionDestroyedCondition('Player')
            $ c2.AddResult(FactionWinsResult('Enemies'))
            $ battle.AddCondition(c2)

            # Obviously if this is all you want, it's much quicker and easier to just use the SimpleWinCondition
            # extra. But if you want one faction to win by wiping out the other, but the other faction
            # to win only by reaching a certain square or for a particular fighter to survive for however long,
            # it's useful to be able to define the conditions separately.
            
        "Kill any one bandit to win":
            # To do the 'kill any one bandit' part we could have a condition for killing the first bandit which
            # has a result to win, and another for the second, and another for the third...
            # but this would mean duplicating the result and duplicating code, and if your result isn't a 'win
            # the battle' result but something else, then when player kills the first and then the second
            # bandit, the result would occur a second time.
            
            # Instead, we use the 'AnyCondition', which we add other conditions to, and it fires its attached
            # results as soon as /any/ of the attached conditions are met. After that, it won't fire again, even
            # if other attached conditions are later met.
            $ any = AnyCondition()
            
            # The 'FighterKilledCondition' takes a particular fighter as a parameter and will trigger as soon
            # as that fighter is killed.
            $ any.AddCondition(FighterKilledCondition(bandit1))
            $ any.AddCondition(FighterKilledCondition(bandit2))
            $ any.AddCondition(FighterKilledCondition(bandit3))
            
            # We add results to the AnyCondition just the same as a regular condition:
            $ any.AddResult(FactionWinsResult('Player'))
            
            $ battle.AddCondition(any)
            
            # Again - it's less likely to ever get triggered, but we have to include a condition for
            # the player to lose, as well:
            $ c2 = FactionDestroyedCondition('Player')
            $ c2.AddResult(FactionWinsResult('Enemies'))
            $ battle.AddCondition(c2)
            
        "Kill any one bandit to get a short Ren'Py scene":
            
            # The condition part of this is exactly the same as the last one:
            $ any = AnyCondition()
            $ any.AddCondition(FighterKilledCondition(bandit1))
            $ any.AddCondition(FighterKilledCondition(bandit2))
            $ any.AddCondition(FighterKilledCondition(bandit3))

            # However, this time we're using a 'CallLabelInNewContextResult'. As the name suggests,
            # this calls a [Ren'Py] label in a new context. If the idea of contexts is a bit confusing, just
            # remember this: it will go off and run that Ren'Py scene as normal, and once it hits
            # 'return' (the script for this label is at the bottom of the screen) it will resume your battle
            # exactly where it left off.
            # Remember to put quotes around the label name!
            $ any.AddResult(CallLabelInNewContextResult('event_demo_short_scene'))
            
            $ battle.AddCondition(any)
            
            # Now, we're actually just going to add the SimpleWinCondition here, since - other than the 
            # cut-in Ren'Py scene - we want the win condition to be the same as usual.
            $ battle.AddExtra(SimpleWinCondition())
            
        "Move a fighter into the right-most column for another bandit to appear":
            
            # To check for a player fighter moving into the right-most column, we use the
            # AreaReachedCondition. This condition can have a faction or a fighter specified,
            # and when that fighter enters the defined rectangle of spaces, the condition fires.
            
            # We pass in four numbers - these are the X,Y coordinates of two opposite corners of the area
            # we want to check. In this case we're checking the whole right-hand column, so the X is the
            # same for both corners. The 'faction' parameter tells the condition which faction's fighters
            # to look for - only fighters from this faction will satisfy the condition.
            $ a = AreaReachedCondition(7, 0, 7, 6, faction='Player')
            
            # (We're using the faction option here; if you want the event to only trigger for a particular
            # fighter then replace the word 'faction' with 'fighter' in the call, and instead of passing
            # in the name of a faction, pass a fighter variable instead.)

            # To have the result spawn a new bandit, we can use the PositionalReinforcementsResult result.
            # This result takes a list of reinforcements specified in a tuple of (fighter, x-position, y-position)
            # and when the result is fired, adds those fighters to the battle in the positions specified.
            # First, we need to create a new fighter for our reinforcement guy, and we do this just like we
            # would for a regular battle participant:
            $ bandit4 = MovingAIFighter("Bandit 4", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
            $ bandit4.RegisterSkill(Library.Skills.KnifeAttack, 1)
            
            # Next, we need to put him into a tuple (brackets!) with his new position (the far left of the field):
            $ r = (bandit4, 0, 3)
            
            # Then we can create the PositionalReinforcementsResult using this reinforcement tuple in a list:
            $ a.AddResult(PositionalReinforcementsResult('Enemies', [r]))

            # (Note that we need to specify the faction the reinforcements are for. If you want to have more
            # than one fighter appear as reinforcements, you don't have to add multiple results - you can
            # just put more than one tuple into the list - instead of [r], have [r1, r2, r3, r4] etc. Just make
            # sure that every fighter is given a set of coordinates as well.)
            
            $ battle.AddCondition(a)
            
            $ battle.AddExtra(SimpleWinCondition())
            
        "Kill the top-most bandit and move a fighter into the left-most column to win":
            
            # Here we're dealing with two conditions which have to both be met in order to fire the results...
            # Much like the AnyCondition we saw earlier, there's also an AllCondition which works much the
            # same way, but requires every attached condition to be met instead of just one of them.

            $ all = AllCondition()
            
            $ all.AddCondition(FighterKilledCondition(bandit1))
            $ all.AddCondition(AreaReachedCondition(0,0,0,6, 'Player'))
            
            $ all.AddResult(FactionWinsResult('Player'))
            
            $ battle.AddCondition(all)
            
            # (And again, the inverse to let the bandits win...)
            $ c2 = FactionDestroyedCondition('Player')
            $ c2.AddResult(FactionWinsResult('Enemies'))
            $ battle.AddCondition(c2)
            
        "Survive five turns to win":
            
            # The remaining condition to discuss is the TimedCondition. This fires after the specified number
            # of ticks have passed, but a 'tick' is different in different kinds of battle, so be careful when using
            # this one. It literally depends on the implementation of the Prioritiser and BattleMechanic that are
            # being used for your battle, found in engine-schema.rpy.
            
            # For a turn-based battle like this one, one 'tick' is one whole round - one turn for each faction. So
            # the TimedCondition is easiest to use for turn-based battles, where the number just specifies the
            # number of turns to wait.
            
            # For an active battle, however, all that happens in a tick is that every
            # fighter has their speed added to their priority, and fighters only get to act when their priority
            # reaches 100... so for example, a fighter with speed 10 would get a turn every ten ticks.

            # Since this is a turn-based battle, though, we can just use the number 5 for five turns. Except
            # that actually, we need to specify 6 turns - the event will fire at the very beginning of the
            # 6th turn!
            
            $ timed = TimedCondition(6)
            
            $ timed.AddResult(FactionWinsResult('Player'))
            $ battle.AddCondition(timed)
            
            # We'll also display a message to the player at the beginning of their 5th turn to let them know
            # that they're almost there...
            $ timed2 = TimedCondition(5)
            
            # This time we'll use the 'MessageResult' result, which does what you might expect - shows the
            # player the given message when it's fired:
            $ timed2.AddResult(MessageResult("This is the last turn, you're almost there!"))
            
            $ battle.AddCondition(timed2)
            
            # We /could/ use the SimpleWinCondition here as well, if we didn't mind the objective being
            # "Survive five turns or wipe out the enemy". Instead, though, we'll force the player to wait out
            # the five turns. After all, maybe you want to add reinforcements that appear after three turns!
            # So instead, we just add a win condition for the enemy, so the player can lose.
            $ c2 = FactionDestroyedCondition('Player')
            $ c2.AddResult(FactionWinsResult('Enemies'))
            $ battle.AddCondition(c2)
    python:        
        
        # Note that we're not using the SimpleWinCondition Extra here, because we're defining
        # the win condition differently in the menu options above.
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(GridStatsDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
        



        battle.Start()

        winner = battle.Won
    
    # Back in regular Ren'Py land:
    if (winner == 'Player'):
        #TODO: Play victory music
        "Well Done, You Won!"
    else:
        #TODO: Play failure music
        "Game Over: You Lost."
        
    jump start

    
    
# This is the label that the "Kill any one bandit to see a short Ren'Py scene" result jumps to.
label event_demo_short_scene:
    
    "Geoff" "Wow, a whole bandit, killed, just like that!"
    
    "Bob" "I know, it's amazing, right?"
    
    "Geoff" "And we get a short bit of dialogue, just like that!"
    
    "Bob" "Just remember that if you want to show backgrounds or character sprites, you may have to mess around with layers."
    "Bob" "By default, the battle covers up the regular Ren'Py bgs/sprites layer."
    
    "Geoff" "Once we're finished, we can just go straight back to the battle and pick up where we left off."
    
    # After the scene is over, we need to call 'return' to make sure we return to the battle.
    return
