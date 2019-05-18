## Diplomacy Horse Speed Merger for inclusion With
## Prebattle Orders & Deployment by Caba'drin
## v0.91
## 14 Dec 2011

from header_common import *
#from header_items import *
from header_operations import *
from module_constants import *
from header_skills import *
#from header_mission_templates import *

mt_list = [
"lead_charge",
"village_attack_bandits",
"village_raid",
"besiege_inner_battle_castle",
"besiege_inner_battle_town_center",
"castle_attack_walls_defenders_sally",
"castle_attack_walls_belfry",
"castle_attack_walls_ladder",
"quick_battle_battle",
]

dplmc_horse_speed = (
  1, 0, 0, [(eq, "$g_dplmc_horse_speed", 0)],
  [
  (try_for_agents, ":agent_no"),
    (agent_is_alive, ":agent_no"),
    (agent_is_human, ":agent_no"),
    (agent_get_horse, ":horse_agent", ":agent_no"),
    (try_begin),
      (ge, ":horse_agent", 0),
      (store_agent_hit_points, ":horse_hp",":horse_agent"),
      (store_sub, ":lost_hp", 100, ":horse_hp"),
      (try_begin),
        (le, ":lost_hp", 15),
        (val_div, ":lost_hp", 2),
        (store_add, ":speed_factor", 100, ":lost_hp"),
      (else_try),
        (val_mul, ":lost_hp", 2),
        (val_div, ":lost_hp", 3),
        (store_sub, ":speed_factor", 115, ":lost_hp"),
      (try_end),
      (agent_get_troop_id, ":agent_troop", ":agent_no"),
      (store_skill_level, ":skl_level", skl_riding, ":agent_troop"),
      (store_mul, ":speed_multi", ":skl_level", 2),
      (val_add, ":speed_multi", 100),
      (val_mul, ":speed_factor", ":speed_multi"),
      (val_div, ":speed_factor", 100),
      (agent_set_horse_speed_factor, ":agent_no", ":speed_factor"),
    (try_end),
  (try_end),
  ])
	
from util_common import *

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "mission_templates"
		orig_mission_templates = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)


def modmerge_mission_templates(orig_mission_templates):
	for i in mt_list:
		find_i = list_find_first_match_i( orig_mission_templates, i )
		if not find_i == None:
			orig_mission_templates[find_i][5].append(dplmc_horse_speed)
