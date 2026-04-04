label start:

    $ _dismiss_pause = config.developer
    $ quick_menu = True
    $ allow_skipping = True
    $ config.allow_skipping = True

    call screen dialog(message="Write a script or write a label and call it in script.rpy", ok_action=MainMenu(confirm=False))
