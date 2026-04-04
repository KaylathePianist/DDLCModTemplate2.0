import renpy # type: ignore

"""renpy
init 1 python in DDLCTransforms:
"""

positions = {
    "55": 1140,
    "54": 890,
    "53": 640,
    "52": 390,
    "51": 140,
    
    "44": 1080,
    "43": 786,
    "42": 493,
    "41": 200,
    
    "33": 1040,
    "32": 640,
    "31": 240,
    
    "22": 880, 
    "21": 400,
    
    "11": 640,
}

from renpy import store
from store import focus, tcommon, tinstant, sink, hop, dip, leftin, rightin, hopfocus
transforms = {
    "f": focus,
    "t": tcommon,
    "i": tinstant,
    "s": sink,
    "h": hop,
    "d": dip,
    "l": leftin,
    "r": rightin,
    "hf": hopfocus,
}

# define all positions for a given transform
def make_transforms(_t, pref, positions=positions):
    for pos, x in positions.items():
        name = str(pref+pos)
        trans = _t(x)
        setattr(store, name, trans)

# define all possible positions for all transforms
for pref, trans in transforms.items():
    make_transforms(trans, pref)
