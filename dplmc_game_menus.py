## Diplomacy Battle Contiuation Disable for use with
## Prebattle Orders & Deployment by Caba'drin
## v0.91
## 14 Dec 2011

from header_operations import *

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)


def modmerge_game_menus(orig_game_menus):
	find_i = list_find_first_match_i( orig_game_menus, "dplmc_preferences" )
	codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOption("dplmc_disable_battle_continuation").GetConditionBlock()
	codeblock.InsertBefore(0, [(eq,0,1)])
	codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOption("dplmc_enable_battle_continuation").GetConditionBlock()
	codeblock.InsertBefore(0, [(eq,0,1)])	
