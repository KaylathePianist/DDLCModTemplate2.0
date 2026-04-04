import renpy  # type: ignore

"""renpy
init -3 python:
"""

persistent = renpy.store.persistent
store = renpy.store

def get_pos(channel: str = "music"):
    """
    Returns the current position of the specified music channel.

    :param channel: The name of the music channel.
    :type channel: str

    :return: The current position of the music channel or 0 if not playing.
    :rtype: int
    """
    pos = renpy.music.get_pos(channel)
    if pos is not None:
        return pos
    return 0

def pause(time=None):
    """
    Pauses the game for a specified amount of time or indefinitely.

    :param time: The time to pause in seconds. If None, pauses indefinitely.
    """
    global _windows_hidden

    if not time:
        _windows_hidden = True
        renpy.ui.saybehavior(afm=" ")
        renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
        _windows_hidden = False
        return
    if time <= 0:
        return
    _windows_hidden = True
    renpy.pause(time)
    _windows_hidden = False

renpy.config.keymap["game_menu"].remove("mouseup_3")
renpy.config.keymap["hide_windows"].append("mouseup_3")
renpy.config.keymap["self_voicing"] = []
renpy.config.keymap["clipboard_voicing"] = []
renpy.config.keymap["toggle_skip"] = []

renpy.music.register_channel("music_poem", mixer="music", tight=True)

if renpy.android:
    renpy.config.keymap["rollback"] = []
    renpy.config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]
    renpy.config.underlay.append(renpy.Keymap(history = ShowMenu("history"))) 