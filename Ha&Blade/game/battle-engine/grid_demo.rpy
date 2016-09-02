label simple_grid_demo:
    
    # The Simple Grid Demo assumes that you've already read and understood the comments in
    # the Active Demo, and will not repeat those concepts. Only new things are commented in this
    # demo.

    play music "audio/battle.ogg" fadein 0.5

    
    python:
        battle = Battle(SimpleTurnSchema())
        fieldSprite = BattlefieldSprite('bg woodland simple grid')
        
        # This time, we're using the GridBattlefield instead of the SimpleBattlefield. This requires
        # a bit more setup, because we not only need to set the sprite, but also the size and shape of 
        # the grid, and any scenery that may block movement, or that fighters might stand behind.
        # The first parameter, as before, is the sprite to use for the BG.
        # The second parameter - origin - is the screen position (left-right, up-down) of the (0,0) grid square.
        # - (In our example here, it's the top-left square in the grid)
        # The third parameter - gridSize - is the size of the grid (width, height) in terms of grid spaces.
        # - (This is how far right and how far down the engine will consider each successive space to be.
        #    So if you want to start at the bottom-left square and work up, you'll need a negative height.)
        # The fourth parameter - spaceSize - is the on-screen size (width, height) of a single grid space.
        # The fifth parameter - diagonals - tells the grid whether or not to allow diagonal movement.
        battlefield = GridBattlefield(fieldSprite, origin=(115, 120), gridSize=(8, 7), spaceSize=(75, 50), diagonals=False)
        
        battle.SetBattlefield(battlefield)
        
        
        # Another new thing is that on the grid, we can have bits of scenery which can block line-of-sight
        # and movement.
        # First we'll add a tree...
        treeSprite = BattleSprite('scenery tree', anchor=(0.45, 0.87))
        
        # The first parameter to create a piece of Scenery is its name, much like a Fighter.
        # Next the sprite, and the third parameter tells the engine whether to block Movement and LoS
        # for the position we stick it in with the blocksPosition and blocksLoS flags
        tree = Scenery('Tree', sprite=treeSprite, blocksPosition=True, blocksLoS=True)
        
        # We add scenery much like a fighter. Since this is a grid battlefield, we'll also need to give it
        # and x and a y to tell the engine which space to stick it in.
        battle.AddScenery(tree, x=5, y=5)


        # Next we'll add a tree-line to the bottom of the screen.
        # It's not specific to a single space, and it doesn't block, so it doesn't matter much where we
        # put it... so we'll stick it in the bottom-left grid position and adjust its position using
        # anchor.
        # (Of course, since this is going to be in front of every fighter, we could just use an overlay layer
        # something... but this is for the sake of an example.)
        treeLineSprite = BattleSprite('scenery front', anchor=(115, 75))
        treeLine = Scenery('Treeline', sprite=treeLineSprite, blocksPosition=False, blocksLoS=False)        
        battle.AddScenery(treeLine, x=0, y=6)
        
        battle.AddFaction('Player', playerFaction=True)
        
        bobSprite = BattleSprite('bob', anchor=(0.5, 0.75), placeMark=(0,-75))
        
        bob = PlayerFighter("Bob", Speed=8, Move=4, Attack=20, Defence=20, sprite=bobSprite) 
        bob.RegisterSkill(Library.Skills.SwordAttack)
        bob.RegisterSkill(Library.Skills.Skip)
        
        # Since we're on a grid now, we'll also need to give each of our fighters a movement skill... this
        # uses the 'Move' stat we gave the fighter.
        bob.RegisterSkill(Library.Skills.Move)
        
        # Setting up a fighter is pretty much the same as for any other battle, but when we call AddFighter
        # on a GridBattlefield, we need to also tell the battle where he's standing. So we'll pass in extra 'x' and
        # 'y' parameters to denote which grid square he's standing in.
        # Remember that like most things in programming, the first space is '0', and the maximum one in
        # our 8-wide grid is '7'.
        battle.AddFighter(bob, x=1, y=2)
        
        geoffSprite = BattleSprite('geoff', anchor=(0.5, 0.8), placeMark=(0,-85))
        geoff = PlayerFighter("Geoff", Speed=13, Move=5, Attack=7, Defence=10, MP=20, sprite=geoffSprite)
        geoff.RegisterSkill(Library.Skills.SwordAttack)
        geoff.RegisterSkill(Library.Skills.Skip)
        geoff.RegisterSkill(Library.Skills.Move)
        # We're giving Geoff a larger complement of spells this time...
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
        
        # Of course, our enemy fighters can also move... so we'll need to use a new Enemy class which
        # is capable of movement. MovingAIFighter will provide simple movement AI on top of
        # the skill-selection SimpleAIFighter gives you.
        # However, MovingAIFighter also needs more parameters to set it up:
        # The first parameter is the name, as before.
        # The second parameter is the skill by which the AI moves. Here we're using the same skill as we gave
        # our player fighters.
        # The third parameter is the distance that the fighter prefers to be from the enemy.
        # - these are all melee fighters, so they prefer to be up as close as possible - one square from the player.
        bandit1 = MovingAIFighter("Bandit 1", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit1.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit1, x=7, y=2)
        bandit2 = MovingAIFighter("Bandit 2", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit2.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit2, x=7, y=3)
        bandit3 = MovingAIFighter("Bandit 3", Library.Skills.Move, idealDistance=1, Move=4, Speed=10, Attack=10, Defence=8, sprite=banditSprite)
        bandit3.RegisterSkill(Library.Skills.KnifeAttack, 1)
        battle.AddFighter(bandit3, x = 7, y=4)
        
        
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(GridStatsDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
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


label isometric_grid_demo:
    
    play music "audio/battle.ogg" fadein 0.5
    
    
    # The Isometric Grid Demo assumes that you've already read and understood the comments in
    # the Active Demo and Simple Grid Demo, and will not repeat those concepts. Only new things
    # are commented in this demo.
    
    # Using an isometric grid is very similar to the simple grid shown before... the difference is only in the
    # setup of the GridBattlefield. However, we'll introduce another couple of things at the same time.
    
    
    python:
        
        # Here we're using a CustomSchema instead of one of the built-in ones. To create a CustomSchema, 
        # the first parameter is the existing schema to base it on, after which any named parameters (one of
        # 'attackResolver', 'mechanic', 'layers' or 'uiProvider') override one facet of that schema.
        # In this case, we're using the same SimpleTurnSchema as the previous example, but this time we're
        # replacing the attackResolver with the ElementalAttackResolver, which will cause the element attributes
        # of particular attacks or Fighters to make some attacks extra-effective or ineffective against some targets.
        schema = CustomSchema(SimpleTurnSchema, attackResolver=ElementalAttackResolver, uiProvider=AlternateUIProvider)
        
        battle = Battle(schema)
        
        fieldSprite = BattlefieldSprite('bg woodland iso grid')
        
        # Firstly, this time we're making our (0,0) square - the 'origin' parameter - the bottom-most square of the isometric grid.
        # This means that the 'height' in the 'spaceSize' parameter has to be negative (-50 in this case) so that the grid
        # moves up the screen rather than down it.
        
        # (To find the spaceSize for an already-drawn iso grid, you can open your paint program and drag a rectangle from one grid
        # (square corner to the next along a single side of the grid - the size of that rectangle is the size you need to enter for your
        # squaresize. If you drew the grid yourself and have a graphic for a single grid square, then (for an isometric grid) simply
        # divide the width and height by two each  - because of the way each successive square is lined up half-a-square further than
        # the last in each direction.
        # In this case I started out with a 150x76 graphic for my square, so my squareSize is (75, 38).)
        
        # The next new thing is the 'isometric' parameter - this treats the grid as an isometric one, with the spaceSize as above.
        # Setting these two parameters correctly is all you need to do to create an isometric grid.
        
        battlefield = GridBattlefield(fieldSprite, origin=(362, 441), gridSize=(6,5), spaceSize=(75, -38), diagonals=False, isometric=True)

        battle.SetBattlefield(battlefield)
        
        
        treeSprite = BattleSprite('scenery tree', anchor=(0.57, 0.85))
        tree = Scenery('Tree', sprite=treeSprite, blocksPosition=True, blocksLoS=False)
        battle.AddScenery(tree, x=2, y=0)
        
        battle.AddFaction('Player', playerFaction=True)
        
        # For the purposes of this demo we're using some animated directional sprites that are put together by methods in the
        # directional-sprites.rpy file. See the facing-demo.rpy file (features => sprite state and facing) to see how these
        # are put together.
        
        steve = PlayerFighter("Steve", Speed=8, Move=4, Attack=20, Defence=20, sprite=GetKnightSprite())
        steve.RegisterSkill(Library.Skills.SwordAttack)
        steve.RegisterSkill(Library.Skills.Skip)
        steve.RegisterSkill(Library.Skills.Move)
        battle.AddFighter(steve, x=0, y=4)
        
        # Because the enemies are off to the east, we set both fighter's facing to E before the battle starts.
        # This can only be done after you've added the fighter to the battle, though.
        steve.Facing = "E"
        
        larry = PlayerFighter("Laurence", Speed=13, Move=5, Attack=7, Defence=10, MP=30, sprite=GetMageSprite())
        larry.RegisterSkill(Library.Skills.SwordAttack)
        larry.RegisterSkill(Library.Skills.Skip)
        larry.RegisterSkill(Library.Skills.Move)
        larry.RegisterSkill(Library.Skills.Fire1)
        larry.RegisterSkill(Library.Skills.Fire2)
        larry.RegisterSkill(Library.Skills.Fire3)
        larry.RegisterSkill(Library.Skills.Water1)
        larry.RegisterSkill(Library.Skills.Water2)
        larry.RegisterSkill(Library.Skills.Water3)
        larry.RegisterSkill(Library.Skills.Earth1)
        larry.RegisterSkill(Library.Skills.Earth2)
        larry.RegisterSkill(Library.Skills.Earth3)
        battle.AddFighter(larry, x=0, y=0)
        larry.Facing = "E"
        
        
        battle.AddFaction('Enemies', playerFaction=False)
        
        # This time, we'll have some elementals as enemies. These creatures are aligned with the three magic
        # elements that Geoff uses, so each one will be particularly vulnerable to one kind of magic and
        # particularly strong against another kind.
        
        fireSprite = BattleSprite('fire elemental', anchor=(0.5, 0.8), placeMark=(0,-80))
        
        # We're adding an extra parameter here when we create the enemy Fighter: 'attributes'.
        # It's a list of textual attributes we're attaching to the fighter. In this case we're giving him the 'fire'
        # attribute, and our damage system knows that when an attack with the 'water' attribute hits a
        # target with the 'fire' attribute, it should damage it more (and when an earth attack hits a fire target,
        # it damages it less).
        # If we wanted to add more attributes at the same time, we'd just separate them with commas, e.g.
        # attributes=['fire', 'magic', 'undead']
        fireElemental = MovingAIFighter("Fire Elemental", Library.Skills.Move, attributes=['fire'], idealDistance=3, Move=4, Speed=15, Attack=15, Defence=12, Health=300, sprite=fireSprite)
        fireElemental.RegisterSkill(Library.Skills.KnifeAttack, 1)
        fireElemental.RegisterSkill(Library.Skills.Fireball, 3)

        battle.AddFighter(fireElemental, x=5, y=0)

        
        earthSprite = BattleSprite('earth elemental', anchor=(0.5, 0.8), placeMark=(0,-80))
        earthElemental = MovingAIFighter("Earth Elemental", Library.Skills.Move, attributes=['earth'], idealDistance=3, Move=4, Speed=15, Attack=15, Defence=12, Health=300, sprite=earthSprite)
        earthElemental.RegisterSkill(Library.Skills.KnifeAttack, 1)
        earthElemental.RegisterSkill(Library.Skills.Tremor, 3)

        battle.AddFighter(earthElemental, x=5, y=2)

        waterSprite = BattleSprite('water elemental', anchor=(0.5, 0.8), placeMark=(0,-80))
        waterElemental = MovingAIFighter("Water Elemental", Library.Skills.Move, attributes=['water'], idealDistance=3, Move=4, Speed=15, Attack=15, Defence=12, Health=300, sprite=waterSprite)
        waterElemental.RegisterSkill(Library.Skills.KnifeAttack, 1)
        waterElemental.RegisterSkill(Library.Skills.Aqua, 3)

        battle.AddFighter(waterElemental, x=5, y=4)
        
        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(GridStatsDisplay("Player", {"HP": "Health", "Move": "Move", "MP":"MP"}))
        battle.AddExtra(SimpleWinCondition())
        
        battle.AddExtra(CurrentFighterPointer(Image('gfx/pointer.png'), (0, -90)))

        
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
