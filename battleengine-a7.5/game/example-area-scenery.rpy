label area_scenery:
   
    # The Area Scenery Demo assumes that you've already read and understood the comments
    # in the Facing Demo, and will not repeat those concepts. Only new things are
    # commented in this demo.

    nvl clear
    
    demo "The simple scenery found in other demos has one big drawback - it only occupies a single space. If you want to represent larger, multi-square scenery, it can be difficult to position it such that fighter sprites are always drawn on the correct side of it.{nw}"
    demo "Because the scenery is drawn as if it is entirely in the square it's anchored to, fighters standing 'behind' that square but still 'in front' of the scenery - for example, if you have a long wall extending backwards many squares - may be drawn on the wrong side of it, which looks weird at best!{nw}"
    demo "Additionally, it's a hassle to have to add an extra bit of 'blank' scenery for every extra square your big scenery piece takes up. These problems are solved by the AreaScenery class.{nw}"
    demo "You can choose to see the following demo with or without using the AreaScenery - the gameplay is the same, but graphically and code-wise the AreaScenery looks better."
    
    # The simple scenery presented in the previous grid demos has one big drawback - if you
    # need to represent a larger, multi-square piece of scenery, it can be difficult to position it
    # such that fighter sprites are always drawn on the correct side of it.
    # Take for example a wall three squares long, on an isometric grid. If you place the scenery
    # by the point lowest down the screen, then fighters standing behind that front square but
    # in front of other parts of it - for example, directly in front of the last part of the wall - will
    # actually get drawn behind it, because they are behind that front anchor point. If you place
    # the anchor point on that furthest square, then fighters standing behind the nearest part
    # the wall will erroneously get drawn in front of it, and so on.
    
    # Obviously multi-square scenery is an important part of your average tactical battle game,
    # and it's a hassle to have to place a long succession of single-square wall pieces, and this
    # can still lead to problems. The solution to this is Area Scenery - you define the sprite
    # used and also the area it occupies extending from that anchor square, and the engine
    # works out how to draw fighters or other bits of scenery in front of or behind it.
    
label area_scenery_menu:
    
    menu: 
        "Which version of this battle do you want to see?"
        
        "The (broken) multiple-single-square scenery pieces version.":
            $ useAreaScenery = False
            "Notice that as the fighter moves to the square next to the middle rocks square, on the same side as the tree, the rocks are drawn incorrectly over the fighter's head."
        "The (solution to the above problem) AreaScenery version.":
            $ useAreaScenery = True
        " Back to Main Demo Menu":
            jump start
    
    python:
        
        battle = Battle(ActiveSchema())
        
        battlefield = GridBattlefield(BattlefieldSprite('bg woodland iso grid'), origin=(362, 441), gridSize=(6,5), spaceSize=(75, -38), diagonals=False, isometric=True)

        battle.SetBattlefield(battlefield)
        
        
        treeSprite = BattleSprite('scenery tree', anchor=(0.57, 0.85))
        tree = Scenery('Tree', sprite=treeSprite, blocksPosition=True, blocksLoS=False)
        battle.AddScenery(tree, x=2, y=0)

        if (useAreaScenery == False):

            # First we'll do the 'old' way of doing things, where the scenery doesn't draw properly and it's a hassle to set up.
            # First, we add the actual scenery with its relevant properties...
            
            blockSprite = BattleSprite('scenery rocks', anchor=(0.225, 0.835))
            block = Scenery('Block', sprite=blockSprite, blocksPosition=True, blocksLoS=True)
            battle.AddScenery(block, x=1, y=3)

            # Next we'll add a couple more bits of scenery to block off the other two squares so we
            # can't walk through them... We use an image of 'None' in our sprite to make sure 
            # it doesn't draw anything.
            
            emptySprite = BattleSprite(None)
            
            block2 = Scenery('Block2', sprite=emptySprite, blocksPosition=True, blocksLoS=True)
            battle.AddScenery(block2, x=2, y=3)
            block3 = Scenery('Block3', sprite=emptySprite, blocksPosition=True, blocksLoS=True)
            battle.AddScenery(block3, x=3, y=3)
            
            
        else:
            # Here we're defining a block piece of scenery - this may be a wall or a fence or a small hut or
            # something, although for the purposes of the demo it's a row of rocks.
            
            blockSprite = BattleSprite('scenery rocks', anchor=(0.225, 0.835))
            
            # To create the scenery, we use an 'AreaScenery' class, which is exactly like the 'Scenery' class, 
            # except it has an added 'area' parameter.
    
            # This area is the full dimensions of the scenery piece. It must occupy a rectangle of spaces, and if you
            # want to block off non-rectangular spaces you will need to divide the blocks into a collection of rectangles
            # and single spaces and have a Scenery or AreaScenery item for each. In this case, however, our concrete
            # block is 3 spaces wide in X, and 1 space wide in Y, so we're happy with a rectangle.
            
            # Again, the blocksPosition and blocksLoS parameters apply to the entire rectangle - if you want parts of
            # your scenery to have different properties, you will have to split it into several Scenery or AreaScenery parts. 
            
            block = AreaScenery('Block', area=(3, 1), sprite=blockSprite, blocksPosition=True, blocksLoS=True)
    
            # When you add an AreaScenery to a battlefield, be aware that you are anchoring the 'bottom-left' corner of
            # the area to this square - the area you defined will extend out in the positive-X and positive-Y directions.
            # (This will be to the right and up respectively in the 'normal' isometric setup.)
            
            battle.AddScenery(block, x=1, y=3)

        # As a tip - if you do want to have a block of scenery which has differing properties - for example, a wall 
        # with windows, so you can see through some squares of it but not others - you will need to construct more
        # than one Scenery/AreaScenery instance to do so. However, it's probably better if you don't just have each
        # separate Scenery/AreaScenery item only extending so far as you want those properties to extend, because
        # this will introduce the 'pass-through' draw-order problem, where (for example) you might see the
        # extended arm of a fighter passing 'through' a bit of your wall because he's up against the join between one
        # Scenery and the next.

        # Instead, it's probably better to define one large AreaScenery over the whole area which has the least-limiting
        # properties, and then add the small islands of more-restrictive scenery where you want those properties to
        # exist. So for example, if you had a wall running from (1,2) to (5, 2) but there's a window at (3,2) which you 
        # want fighters to be able to see through, then you could define a single AreaScenery stretching from (1, 2) to
        # (5,2) which has blocksPosition=True (cannot walk through) but blocksLoS=False (can see through) - then
        # add two other AreaScenery instances from (1, 2) to (2, 2) and from (4, 2) to (5, 2) with the blocksLoS = True
        # to prevent people seeing through the wall everywhere except for the window. You can set the main wall
        # sprite on the biggest AreaScenery, and then give the other two smaller blocking ones a blank sprite so they
        # don't actually draw. Like this, the draw-order is worked out for the big sprite correctly, and you don't see
        # any draw bugs, but you can still see through only that one square of the wall.

        
        
        battle.AddFaction('Player', playerFaction=True)
        
        clydeSprite = BattleSprite('clyde n', anchor=(0.5, 0.8), placeMark=(0,-80))
        clydeSprite.AddStateSprite('default', 'clyde e', facing='E')
        clydeSprite.AddStateSprite('default', 'clyde s', facing='S')
        clydeSprite.AddStateSprite('default', 'clyde w', facing='W')
        clydeSprite.AddStateSprite('default', 'clyde n', facing='N')
        clydeSprite.AddStateSprite('moving', 'clyde walk e', facing='E')
        clydeSprite.AddStateSprite('moving', 'clyde walk s', facing='S')
        clydeSprite.AddStateSprite('moving', 'clyde walk w', facing='W')
        clydeSprite.AddStateSprite('moving', 'clyde walk n', facing='N')
        
        clyde = PlayerFighter("Clyde", Speed=99, Move=99, Attack=20, Defence=0, Health=1, sprite=clydeSprite) 
        clyde.RegisterSkill(Library.Skills.Move)
        clyde.RegisterSkill(Library.Skills.Win)
        battle.AddFighter(clyde, x=0, y=4, facing='E')

        battle.Start()
        
    jump area_scenery_menu
