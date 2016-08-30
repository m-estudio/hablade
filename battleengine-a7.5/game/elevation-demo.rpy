label elevation_demo:
    
    play music "audio/battle.ogg" fadein 0.5

    python:
        # The ElevationGridSprite class is used to easily construct a tile-based map with elevation data.
        # But to construct the ElevationGridSprite class, we first need to set up a TileMap.
        
        # The TileMap contains the data for the map itself - which tileset to use, which tiles are
        # in which positions on the map, and what their heights are.
        
        demoTileMap = TileMap("test.tm")
        
        # Here we're referring to the test.tm file which is in the game directory - obviously you can load in
        # any file you choose, but it has to conform to a particular format. You can find more information about
        # the tileset and tilemap formats in the elevation.rpy file.
        # A good way to get started editing tileset/map files would be to play around modifying the test.tm
        # and test.ts files in this demo.
        
        # We're using the ElevationUIProvider defined above, of course - and an ActiveSchema since this demo
        # is going to be just one character moving around freely. We're using the same trick as the boat hex demo
        # - an Active schema coupled with a very high speed stat means that the character's next turn arrives 
        # immediatly that he finishes his previous one.
        
        battle = Battle(CustomSchema(ActiveSchema, attackResolver=ElementalAttackResolver, uiProvider=TileUIProvider(highlight="gfx/iso-select.png")))
        
        # The ElevationGridSprite displayable draws the tiles out in the correct positions and at the correct
        # heights.
        # The first parameter is an image to use as a background for the entire screen - the isometric tiles will
        # often not cover the entire screen, so we need to display something behind them.
        # The second parameter is the TileMap instance we defined previously, 
        # Then similarly to the GridBattlefield, we're defining an origin, spaceSize and offset parameter.
        # Lastly, heightStep defines how tall in pixels 1.0 height is. This should ideally line up with the
        # height of an average character sprite.
        
        fieldSprite = ElevationGridSprite(Image('gfx/tile-bg.jpg'), demoTileMap, origin=(362, 441), spaceSize=(50, -25), heightStep=100)
        
        # We can then set the GridBattlefield up with similar values, and get the gridSize values from the TileMap.
        battle.SetBattlefield(GridBattlefield(fieldSprite, map=demoTileMap, origin=(362, 441), gridSize=(demoTileMap.XSize, demoTileMap.YSize), spaceSize=(50, -25), diagonals=False, heightStep=100, isometric=True))
        
        battle.AddFaction('Player', playerFaction=True)
        
        steve = PlayerFighter("Steve", Speed=99, Move=4, Attack=20, Defence=0, Health=1, sprite=GetClydeSprite()) 
        steve.RegisterSkill(Library.Skills.ElevationMove)
        steve.RegisterSkill(Library.Skills.Win)
        
        battle.AddFighter(steve, x=0, y=4)

        battle.AddExtra(ActionPanner())
        battle.AddExtra(PanningControls(leftLabel=u'←', rightLabel=u'→', upLabel=u'↑', downLabel=u'↓', distance=250))
        
        battle.Start()
        
    jump start