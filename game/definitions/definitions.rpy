define config.developer = True
default enable_languages = False

default last_reported_status_data = {}
default persistent.enable_discord = not renpy.android

define config.allow_underfull_grids = True
define config.gestures = { "n" : 'game_menu', "s" : "hide_windows", "e" : 'toggle_skip', "w" : "history" }

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer
default persistent.playername = ""
default player = persistent.playername
default persistent.first_load = False
default persistent.first_run = False
default persistent.has_chosen_language = False

define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default currentpos = 0

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"