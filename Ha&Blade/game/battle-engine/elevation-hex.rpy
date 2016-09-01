label elevation_hex_demo:

    # The Elevation Hex Grid Demo assumes that you've already read and understood the comments
    # in the Elevation Demo, and will not repeat those concepts. Only new things are commented in 
    # this demo.
    
    play music "audio/battle.ogg" fadein 0.5

    python:
        
        # When using a hex map, we still create a TileMap using the same class as for square grids.
        # Hex battlefields can still be considered to have rectangular areas of spaces, with every
        # other column shifted up by half a space.
        demoTileMap = TileMap("hextest.tm")
        
        # This time we use a hex-shaped select highlight image, which matches the size and shape of our hex tiles.
        # We also set a default rotation amount of 60 degrees, since each facing on a hex tile is 60 degrees around
        # from the previous one.
        battle = Battle(CustomSchema(ActiveSchema, attackResolver=ElementalAttackResolver, uiProvider=TileUIProvider(highlight="tiles/hex-select.png", rotation=60)))
        
        # Instead of the square grid's ElevationGridSprite, we now use ElevationHexGridSprite for the battlefield
        # sprite - as you can imagine, the difference is that this one draws a hex grid instead of a square one.
        fieldSprite = ElevationHexGridSprite(Image('gfx/tile-bg.jpg'), demoTileMap, origin=(362, 441), spaceSize=(75, -40), heightStep=100)
        
        battle.SetBattlefield(HexGridBattlefield(fieldSprite, map=demoTileMap, origin=(362, 441), gridSize=(demoTileMap.XSize, demoTileMap.YSize), spaceSize=(75, -40), heightStep=100))
        
        battle.AddFaction('Player', playerFaction=True)
        
        steve = PlayerFighter("Steve", Speed=99, Move=4, Attack=20, Defence=0, Health=1, sprite=GetClydeHexSprite()) 
        steve.RegisterSkill(Library.Skills.ElevationMove)
        steve.RegisterSkill(Library.Skills.Win)
        
        battle.AddFighter(steve, x=0, y=4)
        
        battle.AddExtra(ActionPanner())
        battle.AddExtra(PanningControls(leftLabel=u'←', rightLabel=u'→', upLabel=u'↑', downLabel=u'↓', distance=250))
        
        battle.Start()
        
    
    jump start