
init:
    $ demo = NVLCharacter(None, kind=nvl)

    $ _preferences.set_volume("music", 0.7)  
    
    image bg black = "#000"
    

screen start_screen:
    
    modal True
    
    python:
        xSize = int(config.screen_width * 0.9)
        ySize = int(config.screen_height * 0.9)
        
    window:
        background None
        xminimum xSize
        xmaximum xSize
        yminimum ySize
        ymaximum ySize
        
        grid 2 2:
            xalign 0.5
            yalign 0.5
            
            vbox:
                text "Battle Types" xalign 0.5
                button:
                    background None
                    add "shots/active.png"
                    action [Hide("start_screen"), Jump("battle_types")]
                
            vbox:
                text "Features" xalign 0.5
                button:
                    background None
                    add "shots/facing.png"
                    action [Hide("start_screen"), Jump("features")]
            
            vbox:
                text "Screens" xalign 0.5
                button:
                    background None
                    add "shots/equip.png"
                    action [Hide("start_screen"), Jump("screens")]
                
            vbox:
                text "Info" xalign 0.5
                button:
                    background None
                    add "shots/info.png"
                    action [Hide("start_screen"), Jump("info")]
                


screen battle_types:
    
    modal True
    
    python:
        xSize = int(config.screen_width * 0.9)
        ySize = int(config.screen_height * 0.9)
        
    window:
        background None
        xminimum xSize
        xmaximum xSize
        yminimum ySize
        ymaximum ySize
        
        grid 3 3:
            xalign 0.5
            yalign 0.5
            
            vbox:
                text "Active" xalign 0.5
                button:
                    background None
                    add "shots/active.png"
                    action [Hide("battle_types"), Jump("active_demo")]
                
            vbox:
                text "Simple Grid" xalign 0.5
                button:
                    background None
                    add "shots/simple-grid.png"
                    action [Hide("battle_types"), Jump("simple_grid_demo")]
                
            vbox:
                text "Isometric Grid" xalign 0.5
                button:
                    background None
                    add "shots/iso-grid.png"
                    action [Hide("battle_types"), Jump("isometric_grid_demo")]

            vbox:
                text "Path" xalign 0.5
                button:
                    background None
                    add "shots/path.png"
                    action [Hide("battle_types"), Jump("path_demo")]
                
            vbox:
                text "Hex Map" xalign 0.5
                button:
                    background None
                    add "shots/hex.png"
                    action [Hide("battle_types"), Jump("simple_hex_demo")]
                
            vbox:
                text "Elevation Tilemap" xalign 0.5
                button:
                    background None
                    add "shots/elevation.png"
                    action [Hide("battle_types"), Jump("elevation_demo")]
                    
            vbox:
                null
                    
            vbox:
                text "Elevation Hex Tilemap" xalign 0.5
                button:
                    background None
                    add "shots/elevation-hex.png"
                    action [Hide("battle_types"), Jump("elevation_hex_demo")]
                    
            vbox:
                null
                
                
          
screen screens:
    
    modal True
    
    python:
        xSize = int(config.screen_width * 0.9)
        ySize = int(config.screen_height * 0.9)
        
    window:
        background None
        xminimum xSize
        xmaximum xSize
        yminimum ySize
        ymaximum ySize
        
        grid 3 1:
            xalign 0.5
            yalign 0.5
            
            vbox:
                text "Equip Fighters" xalign 0.5
                button:
                    background None
                    add "shots/equip.png"
                    action [Hide("screens"), Jump("equip_demo")]
                
            vbox:
                text "Party Selection" xalign 0.5
                button:
                    background None
                    add "shots/party.png"
                    action [Hide("screens"), Jump("party_screen_demo")]
                
            vbox:
                text "RPG Shop" xalign 0.5
                button:
                    background None
                    add "shots/shop.png"
                    action [Hide("screens"), Jump("shop_screen_demo")]
                    
screen features:
    
    modal True
    
    python:
        xSize = int(config.screen_width * 0.9)
        ySize = int(config.screen_height * 0.9)
        
    window:
        background None
        xminimum xSize
        xmaximum xSize
        yminimum ySize
        ymaximum ySize
        
        grid 3 3:
            xalign 0.5
            yalign 0.5
            
            vbox:
                text "Sprite State and Facing" xalign 0.5
                button:
                    background None
                    add "shots/facing.png"
                    action [Hide("features"), Jump("facing_demo")]
                
            vbox:
                text "Panning/Scrolling" xalign 0.5
                button:
                    background None
                    add "shots/pan.png"
                    action [Hide("features"), Jump("scroll_demo")]
                
            vbox:
                text "Area Scenery" xalign 0.5
                button:
                    background None
                    add "shots/area-scenery.png"
                    action [Hide("features"), Jump("area_scenery")]
        
            vbox:
                text "Experience" xalign 0.5
                button:
                    background None
                    add "shots/experience.png"
                    action [Hide("features"), Jump("xp_demo")]
                
            vbox:
                text "Equipment" xalign 0.5
                button:
                    background None
                    add "shots/equip.png"
                    action [Hide("features"), Jump("equip_demo")]
                
            vbox:
                text "Conditional Events" xalign 0.5
                button:
                    background None
                    add "shots/events.png"
                    action [Hide("features"), Jump("events_demo")]
                
            vbox:
                text "Wargame" xalign 0.5
                button:
                    background None
                    add "shots/wargame.png"
                    action [Hide("features"), Jump("wargame_demo")]
                    
            vbox:
                null
                
            vbox:
                text "Custom Skills" xalign 0.5
                button:
                    background None
                    add "shots/skills.png"
                    action [Hide("features"), Jump("skills_demo")]

# The game starts here.
label start:

    scene bg black
    
    stop music fadeout 1.0
    
    show screen start_screen
    
    pause
    
    jump start
    
    menu:
        "Info":
            jump info
        "Active Demo":
            jump active_demo
        "Path Demo":
            jump path_demo
        "Simple Grid Demo":
            jump simple_grid_demo
        "Isometric Grid Demo":
            jump isometric_grid_demo
        "Sprite/Animation State and Facing Demo":
            jump facing_demo
        "Equipment and Items Demo":
            jump equip_demo
        "Custom Skills Demo":
            jump skills_demo
        "Scrolling/Panning Demo":
            jump scroll_demo
        "Hex Map/Wargame Demo":
            jump hex_grid_demo
        "Area Scenery Demo":
            jump area_scenery
        "Experience Demo":
            jump xp_demo
        "Condition/Result Events Demo":
            jump events_demo
        "Elevation/Tile Map Demo":
            jump elevation_demo
        "Party Selector Screen":
            jump party_screen_demo
        "Shop Screen":
            jump shop_screen_demo
        "Test":
            jump test
            
label battle_types:
    
    show screen battle_types
    
    pause
    
label features:
    
    show screen features
    
    pause
    
label screens:
    
    show screen screens
    
    pause

label info:
    
    nvl clear
    
    demo "{b}Information About the Engine{/b}\n{nw}"
    demo "This is the seventh Alpha release of the battle engine code. To explain to anyone unfamiliar with release terminology, generally speaking:\n- an alpha release is an early release which probably has bugs, doesn't have all the intended features and some things may dramatically change before final release.\n- a beta release is a later release which should be more or less feature-complete and mostly interface-stable (so API calls you were using won't change from one release to another, but still buggy.\n- after that, you get to release candidates, which are expected to be feature-complete and [[relatively] bug-free, ready for final release.{nw}"
    demo "So, don't expect this to function absolutely perfectly, although I've fixed all the bugs I've personally seen. There are definitely some things I want to improve, and some things which require Ren'Py 6.11 minimum to work.{nw}"
    demo "You're welcome to use this version of the engine for your game if you want, but be aware that I may change parameters to methods or ways of doing things, depending on what works best."
    
    nvl clear
    
    demo "All code in this project is copyright (C) Jake Staines. It is released under the {a=http://creativecommons.org/licenses/by-nc/2.0/uk/}Creative Commons Attribution Non-Commercial 2.0 UK{/a} (CC BY-NC) license, meaning that you are free to use it as you wish for non-commercial projects. That is, projects which you are not going to be selling or making any money from.{nw}"
    demo "If you want to use the code in this project in a commercial release, you may ask me for a commercial license; if you do so, please let me know about previous games you've made, and give me an idea of the project you are planning.{nw}"
    demo "Images, music and sounds are not included in this license.{nw}"
    demo "Stan and Boat sprites are copyright (C) {a=http://www.reinerstilesets.de/}Reiner 'Tiles' Prokein{/a} (Reiner has a large number of free 2D game graphics that may be useful for games with battles - particularly fantasy projects.){nw}"
    demo "Party portraits are copyright (C) {a=http://x-ren-x.deviantart.com/}Ren{/a}.{nw}"
    demo "All other graphics copyright (C) Jake Staines."
    demo "With the exception of Reiner Prokein's graphics and the Clyde animations, you do not have permission to use any of the graphics in this release in your own games.{nw}"
    demo "Clyde animations are released under a CC-Attribution license and may be used as a base for character animations in your games under that license."
    
    nvl clear
    
    demo "Sound files were all sourced from {a=http://www.flashkit.com}FlashKit{/a} and have the following authors:{nw}"
    demo "fire - Public D\nfire2 - Public D\nknife - Diode\nsword - Gustavo\nearth - Public D\nearth2 - kayden\nwater - mas27\nwater2 - Public D{nw}"
    demo "Music by Isaac Staines"
    
    jump start
