image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

label splashscreen:

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        if not persistent.has_chosen_language and translations:
            if _preferences.language is None:
                call choose_language

        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated in anyway with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: https://ddlc.moe or on Steam."
        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                $ persistent.first_run = True

        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white

    $ config.allow_skipping = False
    show white
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "(Splash Message)" with Dissolve(0.5, alpha=True)
    $ pause(1.5)
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ pause(0.5)
    $ config.allow_skipping = True
    return

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    if not persistent.first_load and not config.developer:
        $ persistent.first_load = True
        call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return