init python:
    def FinishEnterName(launchGame=True):
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        if launchGame:
            renpy.jump_out_of_context("start")

screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.8
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

        else:
            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
            textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

        textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
        textbutton _("Credits") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    #outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]

screen main_menu():

    tag menu
    style_prefix "main_menu"

    add "menu_bg"
    add "menu_art_y"
    add "menu_art_n"

    frame

    use navigation

    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_logo"
    add "menu_art_s"
    add "menu_particles"
    add "menu_art_m"
    add "menu_fade"

    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True
    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0
    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size

screen game_menu(title, scroll=None):

    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        
                        if title == "Credits":
                            yinitial 0
                        else:
                            yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        transclude

                else:
                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

screen about():

    tag menu
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"
        
        window:
            xoffset 35
            has fixed:
                yfit True

            vbox:
                add Transform("mod_assets/DDLCModTemplateLogo.png", size=(200,200)) xalign .5
                null height 5
                label "[config.name!t]" xalign .5
                text _("Version [config.version!t]\n") xalign .5

                if gui.about:
                    text "[gui.about!t]\n"

                text "Made with DDLC Minimal Mod Template, edited by KaylathePianist.\nBased off of bronya_rand's {a=https://github.com/Bronya-Rand/DDLCModTemplate2.0}DDLC Mod Template 2.0{/a}\nCopyright © 2019-" + str(datetime.date.today().year) + " Azariel Del Carmen (bronya_rand). All rights reserved.\n"
                text "Doki Doki Literature Club. Copyright © 2017 Team Salvato. All rights reserved.\n"
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]")

style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#000"
    outlines []
    text_align 0.5
    size gui.label_text_size

style about_text:
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color gui.idle_color
    hover_color gui.hover_color
    hover_underline True

screen save():
    tag menu
    use file_slots(_("Save"))


screen load():
    tag menu
    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)
                #textbutton _("{#auto_page}A") action FilePage("auto")
                #textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    label _("Music Volume")
                    hbox:
                        bar value Preference("music volume")

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

            python:
                has_discord_module = True
                try:
                    RPC
                except NameError:
                    has_discord_module = False

            if not renpy.android and has_discord_module:
                vbox:
                    style_prefix "name"
                    label _("Discord RPC")

                    python:
                        connect_status = _("Disconnected")
                        if not persistent.enable_discord:
                            connect_status = _("Disabled")
                        if RPC.rpc_connected:
                            connect_status = _("Connected")
                    
                    null height 3

                    text "[connect_status]" xalign 0.5

                    python:
                        enable_text = _("Enable")
                        if persistent.enable_discord:
                            enable_text = _("Disable")

                    textbutton enable_text action [ToggleField(persistent, "enable_discord"), 
                        If(persistent.enable_discord, Function(RPC.disconnect), Function(RPC.connect))]:
                            text_style "navigation_button_text"
                    if persistent.enable_discord and not RPC.rpc_connected:
                        textbutton _("Reconnect") action Function(RPC.connect):
                            text_style "navigation_button_text"

            if enable_languages and translations:
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    hbox:
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            ysize 120
                            has vbox

                            for tran in translations:
                                vbox:
                                    for tlid, tlname in tran:
                                        textbutton tlname:
                                            action Language(tlid)

    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style name_label is pref_label
style name_label_text is pref_label_text

style name_text:
    font "gui/font/Halogen.ttf"
    size 24
    color gui.idle_color
    outlines []

style value_text:
    size 18
    color "#000"
    outlines []
    yalign 0.65

screen history():

    tag menu
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):
        
        style_prefix "history"
       
        for h in _history_list:
            
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = set()

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5