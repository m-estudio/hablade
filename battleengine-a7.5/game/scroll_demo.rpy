label scroll_demo:
    
    play music "audio/battle.ogg" fadein 0.5
    
    
    # The Scrolling Demo assumes that you've already read and understood the comments in
    # the Facing Demo, and will not repeat those concepts. Only new things
    # are commented in this demo.

    # Mostly we're demonstrating the new Extras for panning which can be found right near the bottom of the script, 
    # but we also take the opportunity to introduce the methods to add or remove spaces from your grid. 
    
    python:
        
        battle = Battle(ActiveSchema())

        # Here we're using an image with larger dimensions than our screen size - it's 1600x1000 pixels.
        fieldSprite = BattlefieldSprite('bg rocky valley')
        
        battlefield = GridBattlefield(fieldSprite, origin=(393, 969), gridSize=(18,4), spaceSize=(75, -38), diagonals=False, isometric=True)

        battle.SetBattlefield(battlefield)
        
        # Now we'll perform some surgery on the grid - the methods 'AddRect' and 'RemoveRect' can be used to add or remove extra
        # grid areas which fighters can be positioned in.
        # Bear in mind that line-of-sight cannot pass through areas where the grid doesn't extend. So only use RemoveRect if you
        # want the removed area to block LoS as well as movement. The battlefield literally doesn't exist there!
        
        # Note: These operations can only be performed after the call to SetBattlefield.
        
        # AddRect takes two parameters - each is a tuple of grid (X, Y) coordinates. Here we're adding an extra bit of grid in the
        # rectangle between (3, 4) in one corner and (12, 5) in the other - a 10-wide, 2-tall rectangle.
        battlefield.AddRect((3, 4), (12, 5))
        
        # RemoveRect takes a similar pair of parameters, so here we're removing part of that rectangle we just added -
        # a 2x1 chunk out of one corner.
        battlefield.RemoveRect((11, 5), (12, 5))
        
        # There's also 'AddSpace' and 'RemoveSpace', which just take a single (X, Y) tuple parameter.
        battlefield.RemoveSpace((3, 5))
        
        battlefield.AddRect((15, 4), (16, 4))
        battlefield.AddSpace((16, 5))
        battlefield.AddRect((6, -2), (9, -1))
        battlefield.RemoveSpace((6, -2))
        battlefield.RemoveRect((4, 1), (8, 3))
        battlefield.AddSpace((4, 3))
        battlefield.RemoveRect((14, 0), (17, 1))
        battlefield.RemoveSpace((13, 0))
        battlefield.RemoveSpace((17, 2))
        battlefield.AddRect((15, 4), (16, 5))
        battlefield.RemoveSpace((15, 5))
        battlefield.RemoveRect((0, 0), (2, 0))
        battlefield.RemoveSpace((13, 3))
        
        rocks1Sprite = BattleSprite('scenery rocks 1', anchor=(0.41, 0.61))
        rocks1 = Scenery('Rocks1', sprite=rocks1Sprite, blocksPosition=True, blocksLoS=True, transparent=True)
        # We actually removed the space we want to stick this in as part of a big rect removal earlier, so we'll add one in just to stick the scenery in.
        battlefield.AddSpace((6, 2))
        battle.AddScenery(rocks1, x=6, y=2)
        
        rocks2Sprite = BattleSprite('scenery rocks 2', anchor=(0.155, 0.52))
        rocks2 = Scenery('Rocks2', sprite=rocks2Sprite, blocksPosition=True, blocksLoS=True, transparent=True)
        battle.AddScenery(rocks2, x=10, y=0)
        
        battle.AddFaction('Player', playerFaction=True)

        # Just for fun, we'll add an animated walking sprite.        
        stanSprite = BattleSprite('stan n', anchor=(0.5, 0.8), placeMark=(0,-80))
        stanSprite.AddStateSprite('default', 'stan ne', facing='E')
        stanSprite.AddStateSprite('default', 'stan se', facing='S')
        stanSprite.AddStateSprite('default', 'stan sw', facing='W')
        stanSprite.AddStateSprite('default', 'stan nw', facing='N')
        stanSprite.AddStateSprite('moving', 'stan run ne', facing='E')
        stanSprite.AddStateSprite('moving', 'stan run se', facing='S')
        stanSprite.AddStateSprite('moving', 'stan run sw', facing='W')
        stanSprite.AddStateSprite('moving', 'stan run nw', facing='N')
        stan = PlayerFighter("Stan", Speed=99, Move=6, Attack=20, Defence=0, Health=1, sprite=stanSprite) 
        stan.RegisterSkill(Library.Skills.SwordAttack)
        stan.RegisterSkill(Library.Skills.Skip)
        
        # (We're using PathMove because it ends his turn, giving him a new Move allowance immediately.
        # After all, we're just demonstrating the scrolling here.)
        stan.RegisterSkill(Library.Skills.PathMove)
        
        battle.AddFighter(stan, x=0, y=2, facing='E')

        # The 'PanningControls' extra is probably the most important one - it adds buttons on-screen to pan the view around.
        # The 'leftLabel', 'rightLabel' and so on parameters allow you to override the default text in the directional buttons.
        # The 'distance' parameter tells the controls Extra how far to pan the view in each direction when you click the button.
        battle.AddExtra(PanningControls(leftLabel=u'←', rightLabel=u'→', upLabel=u'↑', downLabel=u'↓', distance=250))
        
        # The 'ActionPanner' extra will automatically pan the view to centre on any action - so if an enemy moves, or attacks
        # one of your guys, the camera will centre on it (as best it can) so you can see it happen! 
        battle.AddExtra(ActionPanner())
        
        # Here we set the default values of the camera. If the camera X and Y are set to 0, then the camera starts looking at the 
        # top-left corner of the battlefield. The values we set here move the camera right (for positive X) or down (positive Y) across
        # the battlefield.
        battle.CameraX = 0
        battle.CameraY = 600
        
        # These values set the limits of the camera, so that the user (or ActionPanner, or any other mechanism) cannot pan any
        # further than you allow.
        # Each setting takes a tuple of two values, as seen below - the first value is the minimum allowed value for the camera in
        # that axis, the second is the maximum. Setting the second parameter lower than the first will result in weird behaviour.
        # Generally, you probably want the first value to be 0 (the left/top of the battlefield) and the second value to be the width/height
        # of the battlefield graphic minus the width/height of the screen.
        battle.CameraXLimit=(0, 1600 - 800)
        battle.CameraYLimit=(0, 1000 - 600)
        
        
        
        
        # Just to make sure that the battle can be exited, we'll have a win-condition of reaching
        # the end of the cavern.
        winCondition = AreaReachedCondition(16, 1, 17, 5, faction='Player')
        winCondition.AddResult(FactionWinsResult('Player'))
        battle.AddCondition(winCondition)
        
        battle.Announce("Reach the end of the cavern!")
        battle.Start()
        
        winner = battle.Won
    
    # Back in regular Ren'Py land:
    "Well done, you reached the end of the cavern."
        
    jump start
