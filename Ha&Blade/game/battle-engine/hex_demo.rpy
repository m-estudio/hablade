label hex_grid_demo:
    
    # The Hex Grid Demo assumes that you've already read and understood the comments in
    # the Grid Demo, and will not repeat those concepts. Only new things are commented in this
    # demo.

    nvl clear
    
    demo "There are two hex grid demos included.{nw}"
    
    demo "The first hex demo is a simple demonstration of setting up a hexagonal map, onto which you can place fighters in the same way as the grid demo - there are simply six facings from each square, which is also demonstrated. From this demo, you can create normal battles over a hexagonal grid.{nw}"
    
    demo "The second hex demo is the wargame demo, which seeks to emulate the kind of behaviour seen in card-counter (also known as 'chit') wargames/boardgames, and as such is more complex. The 'WargameSchema' and 'WargameSkill' which govern this type of game can also be used with square grids, but it's more common to see hex grids in this kind of boardgame."
    
    menu:
        
        "Which hex grid demo do you want to see?"
        
        "Simple Demo with Directional Sprite":
            jump simple_hex_demo
            
        "Wargame Demo":
            jump wargame_demo

label simple_hex_demo:

    
    # The Hex Grid Demo assumes that you've already read and understood the comments in
    # the Grid Demo, and will not repeat those concepts. Only new things are commented in this
    # demo.

    play music "audio/battle.ogg" fadein 0.5

    $ _preferences.battle_automatic_skill = True
    
    python:
        battle = Battle(ActiveSchema())
        fieldSprite = BattlefieldSprite('bg hex ocean')
        
        # This time, we're using the HexGridBattlefield instead of the GridBattlefield.
        # This is mostly the same as the GridBattlefield, but with fewer parameters - we only
        # allow hexes to be set at one angle presently (since the entire point of hexagons is to
        # allow uniform movement in most directions) - with horizontal top and bottom sides.
        # The parameters are the same as those for GridBattlefield, but the 'offsets' and
        # 'diagonals' parameters are missing as they are no longer relevant.
        # The 'spacesize' parameter measures from the left-most point of one hex column to the
        # left-most point of the next hex column - 3/4ths the total distance between opposite
        # hex corners.

        battlefield = HexGridBattlefield(fieldSprite, origin=(126, 473), gridSize=(9,6), spaceSize=(67, -78))
        battle.SetBattlefield(battlefield)
        
        battle.AddFaction('Player', playerFaction=True)
        
        boatSprite = BattleSprite('boat n', anchor=(0.5, 0.55), placeMark=(0,-40))
        
        # Here we add different versions of the sprite for different situations, with the 'AddStateSprite' method.
        #
        # The first parameter is the 'state' the fighter should be in to show this particular image; 'default' is - as
        # you may expect - the default, but you can also specify states like 'moving' or 'acting' or 'melee'.
        # The second parameter is the image itself - here we're just using the predefined images for the boat
        # facing in different directions.
        # Lastly, we specify the facing that this sprite should be used for. In grids, every fighter has a 'facing', which
        # is generally the direction they last moved or acted in. For a hex grid there are six facings:
        #   N, NE, SE, S, SW, NW
        # - these correspond to the (rough) compass bearings of the different hex directions; 'N' is both up and the
        # default facing, so we only have to define facing sprites for the other five directions.
        boatSprite.AddStateSprite('default', 'boat ne', facing='NE')
        boatSprite.AddStateSprite('default', 'boat nw', facing='NW')
        boatSprite.AddStateSprite('default', 'boat s', facing='S')
        boatSprite.AddStateSprite('default', 'boat se', facing='SE')
        boatSprite.AddStateSprite('default', 'boat sw', facing='SW')

        boat = PlayerFighter("Boat", Speed=99, Move=6, Attack=20, Defence=0, Health=1, sprite=boatSprite)

        boat.RegisterSkill(Library.Skills.PathMove)
        
        # Because there's no actual combat in this demo and only one fighter, we'll give it the 'Win' skill to allow
        # the user to finish the demo and get back to the main menu. Ordinarily you'd add more fighters in 
        # more factions and define win conditions, just like any other battle.
        boat.RegisterSkill(Library.Skills.Win)
        
        # We still add fighters to the hex grid using regular X/Y coordinates; essentially the hex grid is like
        # a grid of rectangles where every other column is shifted upward half a space.
        battle.AddFighter(boat, x=2, y=3)

        battle.Start()

    jump start
    
label wargame_demo:
    
    play music "audio/battle.ogg" fadein 0.5

    
    python:
        
        # To run a wargame battle, simply use the 'WargameSchema' - this will set up pretty much everything
        # for you.
        battle = Battle(WargameSchema())
        fieldSprite = BattlefieldSprite('bg hex grid')
        
        battlefield = HexGridBattlefield(fieldSprite, origin=(126, 473), gridSize=(9,6), spaceSize=(67, -78))
        
        battle.SetBattlefield(battlefield)

        
        battle.AddFaction('Red', playerFaction=True)

        # It's also required that you give each fighter three stats - 'Move', 'Attack' and 'Defence'.
        # Because we're using the same fighters in more than one place, there are a few simple
        # set-up-a-fighter methods used here. Scroll down to see how 'getKnight' and 'getSwordsman'
        # and so on are defined - it's just after the battle code itself.
        
        # Using fighter-creation methods like this is handy if you aren't using exactly the same party
        # of fighters throughout a series of battles, like if you're making a wargame which doesn't include
        # character experience or levelling up, so it doesn't matter if each fighter is a fresh and new fighter
        # for every battle.
        
        # If you're planning on having experience and levelling in your game, on the other hand, you should
        # just create your fighters once - just after the 'start' label - and keep the same ones throughout the
        # game. Of course, you can still use quick-set-up methods like these for the random-encounter
        # monsters who are always the same!
        
        battle.AddFighter(getKnight('red'), x=3, y=2)
        battle.AddFighter(getKnight('red'), x=3, y=3)
        battle.AddFighter(getSwordsman('red'), x=3, y=1)
        battle.AddFighter(getHalberdier('red'), x=3, y=4)
        battle.AddFighter(getArcher('red'), x=2, y=2)
        battle.AddFighter(getArcher('red'), x=2, y=3)

        battle.AddFaction('Blue', playerFaction=True)

        battle.AddFighter(getKnight('blue'), x = 5, y=2)
        battle.AddFighter(getKnight('blue'), x = 5, y=3)
        battle.AddFighter(getSwordsman('blue'), x=5, y=4)
        battle.AddFighter(getHalberdier('blue'), x=5, y=1)
        battle.AddFighter(getArcher('blue'), x=6, y=2)
        battle.AddFighter(getArcher('blue'), x=6, y=3)
        
        
        battle.AddExtra(RPGDeath())
        battle.AddExtra(SimpleWinCondition())
        



        battle.Start()

        winner = battle.Won
    
    # Back in regular Ren'Py land:
    "%(winner)s Won."
        
    jump start

    
init python:

    
    def getKnight(colour):
        s = BattleSprite(colour + ' counter knight')

        k = PlayerFighter("Knight", Move=3, Attack=3, Defence=1, sprite=s) 
        
        return k

    def getArcher(colour):
        s = BattleSprite(colour + ' counter archer')

        a = PlayerFighter("Archer", Move=1, Attack=2, Defence=0, sprite=s) 
        a.RegisterSkill(AttackSkill(range=2))
        
        return a

    def getHalberdier(colour):
        s = BattleSprite(colour + ' counter halberdier')

        h = PlayerFighter("Halberdier", Move=1, Attack=1, Defence=3, sprite=s) 
        
        return h
        
    def getCannon(colour):
        s = BattleSprite(colour + ' counter cannon')

        c = PlayerFighter("Cannon", Move=0, Attack=4, Defence=0, sprite=s) 
        
        return c
        
    def getSwordsman(colour):
        s = BattleSprite(colour + ' counter swordsman')

        sw = PlayerFighter("Swordsman", Move=1, Attack=2, Defence=2, sprite=s) 
        
        return sw
        



        
