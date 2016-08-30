label facing_demo:
    
    play music "audio/battle.ogg" fadein 0.5
    
    # The Facing Demo assumes that you've already read and understood the comments in
    # the Active, Simple Grid and Isometric Demos, and will not repeat those concepts. Only new things
    # are commented in this demo.
    
    # Here, we'll demonstrate facings - that is, discrete recognised directions that Fighters can be facing,
    # moving, etc. In the GridBattlefield, the facings 'N', 'S', 'E' and 'W' are set up by default for the compass
    # bearings; 'N' is towards positive-infinity in the Y axis, 'E' is towards positive-infinity in the X axis,
    # and so on.
    
    
    python:
        
        schema = CustomSchema(SimpleTurnSchema, attackResolver=ElementalAttackResolver)
        
        battle = Battle(schema)
        
        fieldSprite = BattlefieldSprite('bg woodland iso grid')
        
        # If you plan to set diagonals = True and want to use facings, you may want to also pass the following parameter,
        # which contains eight-way facing information:
        # facings={'N' :(-22.5, 22.5),'NE' :(22.5, 67.5),'E' :(67.5, 112.5),'SE' :(112.5, 157.5),'S' :(157.5, 202.5),'SW' :(202.5, 247.5),'W' :(247.5, 292.5),'NW' :(292.5, 337.5)}
        battlefield = GridBattlefield(fieldSprite, origin=(362, 441), gridSize=(6,5), spaceSize=(75, -38), diagonals=False, isometric=True)

        battle.SetBattlefield(battlefield)
        
        treeSprite = BattleSprite('scenery tree', anchor=(0.57, 0.85))
        tree = Scenery('Tree', sprite=treeSprite, blocksPosition=True, blocksLoS=True)
        battle.AddScenery(tree, x=2, y=0)

        # One alternative when drawing scenery onto the battlefield is to pass the 'transparent=True' parameter.
        # This tells the engine to draw the scenery such that you can see fighters through it. This arguably looks
        # better, but means the scenery gets drawn two times rather than one, so uses more resources.
        solidTreeSprite = BattleSprite('scenery tree solid', anchor=(0.57, 0.85))
        tree2 = Scenery('Tree 2', sprite=solidTreeSprite, transparent=True, blocksPosition=True, blocksLoS=True)
        battle.AddScenery(tree2, x=1, y=2)

        #treeLineSprite = BattleSprite('scenery front', anchor=(115, 75))
        #treeLine = Scenery('Treeline', sprite=treeLineSprite, blocksPosition=False, blocksLoS=False)        
        #battle.AddScenery(treeLine, x=0, y=0)
        
        battle.AddFaction('Team Clyde', playerFaction=True)
        
        clydeSprite = BattleSprite('clyde n', anchor=(0.5, 0.8), placeMark=(0,-80))

        # Here we add some extra states to Clyde's sprite for the different directions he can be facing.
        # The first parameter ('default' below) describes the state we want to change the sprite for.
        #   - the 'default' state will be used when there's no other state sprites defined for a direction. 
        # The second parameter is the name of the sprite we're using. This could also be a Displayable,
        #    if you prefer.
        # The last parameter - facing - is the facing for which to display this sprite.
        #  If we missed off the facing parameter, this sprite would be used in the specified state
        #  regardless of the facing of the character, if no facing-specific sprite was defined.
        clydeSprite.AddStateSprite('default', 'clyde e', facing='E')
        clydeSprite.AddStateSprite('default', 'clyde s', facing='S')
        clydeSprite.AddStateSprite('default', 'clyde w', facing='W')
        clydeSprite.AddStateSprite('default', 'clyde n', facing='N')

        # Here we add some more sprite states, for when Clyde is moving - we have a short walking animation
        # so it doesn't look like he's just sliding around the battlefield.
        clydeSprite.AddStateSprite('moving', 'clyde walk e', facing='E')
        clydeSprite.AddStateSprite('moving', 'clyde walk s', facing='S')
        clydeSprite.AddStateSprite('moving', 'clyde walk w', facing='W')
        clydeSprite.AddStateSprite('moving', 'clyde walk n', facing='N')
        
        
        # A good trick to understand for action animations is sprite state transitions. When the fighter performs
        # certain actions its sprite is set into different states, and each state has a facing. So when a fighter
        # starts facing E and starts moving S, there's a transition from "default"/E to "moving"/S. If the fighter
        # moves S only one square and then starts moving W, then there's a transition from "moving"/S to "moving"/E.
        
        # If you insert a state transition graphic - or animation - into the fighter's sprite, you can have the
        # engine show that graphic or play that animation for a period of time between those states. This could be
        # a turning-to-face animation for movement, but it's particularly useful for things like 'melee'. The 'melee'
        # state only actually lasts as long as it takes to calculate and action the damage from the attack, which often
        # means your attacking animation may not stay on-screen long enough to be seen properly... and worse still, the
        # player may see the bouncing red damage numbers before your fighter's animated sword has actually hit his
        # target! If you instead play the animation as an "acting" -> "melee" state transition this ensures that the
        # attack animation plays out in full before the damage is calculated and displayed.
        
        # To define a state transition graphic or animation, you use the AddStateTransition method.
        # The first two parameters are the 'from' and 'to' states, and the third is the image/animation to use for
        # this transition. The fourth parameter is the number of seconds to play that animation for - in this case
        # 0.8 (4/5ths) of a second.
        # There are optional 'fromFacing' and 'toFacing' params, meaning you can specify precisely which facing-to-
        # facing transitions your animation plays for. In this case we've omitted the fromFacing, so the first state
        # transition animation here will play when the fighter sprite moves from "acting" *with any facing* to
        # "melee" specifically facing N. 
        clydeSprite.AddStateTransition('acting', 'melee', 'clyde melee pre n', 0.8, toFacing='N')
        clydeSprite.AddStateTransition('acting', 'melee', 'clyde melee pre e', 0.8, toFacing='E')
        clydeSprite.AddStateTransition('acting', 'melee', 'clyde melee pre s', 0.8, toFacing='S')
        clydeSprite.AddStateTransition('acting', 'melee', 'clyde melee pre w', 0.8, toFacing='W')
        
        # Lastly we add a static 'just attacked' pose to the melee state itself, so the fighter holds the pose
        # until the damage calculation and display has finished.
        clydeSprite.AddStateSprite('melee', 'clyde melee n', facing='N')
        clydeSprite.AddStateSprite('melee', 'clyde melee e', facing='E')
        clydeSprite.AddStateSprite('melee', 'clyde melee s', facing='S')
        clydeSprite.AddStateSprite('melee', 'clyde melee w', facing='W')
        

        # Now, for future use in these demos we'll actually use the GetClydeSprite() method defined in
        # directional_sprites.rpy, and writing a method to get a particular sprite when you need it is
        # probably a better practice than going through all the definition over and over again each time
        # you use it... but it's done here anyway for illustrative purposes.
        
        
        clyde = PlayerFighter("Clyde", Speed=8, Move=4, Attack=20, Defence=0, Health=1, sprite=clydeSprite) 
        clyde.RegisterSkill(Library.Skills.SwordAttack)
        clyde.RegisterSkill(Library.Skills.Skip)
        clyde.RegisterSkill(Library.Skills.Move)
        
        # When adding Clyde to the battlefield, we can also specify his facing.
        # If we don't do this, he'll just get the default facing for this battlefield (in this case, 'N').
        battle.AddFighter(clyde, x=4, y=3, facing='E')
        
        # Since this is just a demo of sprites and facing, we'll have Clyde paired off against another player-controlled
        # Fighter with the same sprite.
        battle.AddFaction('Team Kevin', playerFaction=True)

        # Since the sprite contains some Fighter-specific information - such as which state to draw in - we
        # can't just re-use the same instance of Battlesprite, or Kevin will be animated the same as Clyde
        # half the time. So we call the 'Copy' method to make a copy of clydeSprite for Kevin.
        
        # We didn't need to do this for previous examples, such as the bandits, because those sprites didn't
        # have state so it didn't really matter if more than one Fighter was using them, because they'd display
        # correctly anyway - there was only one thing they /could/ display.
        kevinSprite = clydeSprite.Copy()
        
        kevin = PlayerFighter("Kevin", Speed=8, Move=4, Attack=20, Defence=0, Health=1, sprite=kevinSprite) 
        kevin.RegisterSkill(Library.Skills.SwordAttack)
        kevin.RegisterSkill(Library.Skills.Skip)
        kevin.RegisterSkill(Library.Skills.Move)
        
        battle.AddFighter(kevin, x=3, y=3, facing='W')

        battle.AddExtra(RPGDamage())
        battle.AddExtra(RPGDeath())
        battle.AddExtra(SimpleWinCondition())
        
        battle.Start()

        winner = battle.Won
    
    # Back in regular Ren'Py land:
    "%(winner)s won!"        
    jump start
