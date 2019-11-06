from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.18
avatar_scale = 0.12

map_icons = [
  ("player",0,"raw_player", avatar_scale, snd_footstep_grass, 0.35, 0.173, 0),
  ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, 0.35, 0.173, 0),
  ("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.35, 0.173, 0),
  ("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.35, 0.173, 0),
  ("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.35, 0.173, 0),
  ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.35, 0.173, 0),
  ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.35, 0.173, 0),
  ("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.35, 0.173, 0),
  ("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.35, 0.173, 0),
  ("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.35, 0.173, 0),
  ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.35, 0.173, 0),
  ("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.35, 0.173, 0),
  ("town",mcn_no_shadow,"map_town_a", 0.3,0),
  ("town_steppe",mcn_no_shadow,"map_town_steppe_a", 0.3,0),
  ("town_desert",mcn_no_shadow,"map_town_desert_a", 0.3,0),
  ("village_a",mcn_no_shadow,"map_village_a", 0.4, 0),
  ("village_b",mcn_no_shadow,"map_village_b", 0.4, 0),
  ("village_c",mcn_no_shadow,"map_village_c", 0.4, 0),
  ("village_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.4, 0),
  ("village_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.4, 0),
  ("village_burnt_b",mcn_no_shadow,"map_village_burnt_b", 0.4, 0),
  ("village_deserted_b",mcn_no_shadow,"map_village_deserted_b", 0.4, 0),
  ("village_burnt_c",mcn_no_shadow,"map_village_burnt_c", 0.4, 0),
  ("village_deserted_c",mcn_no_shadow,"map_village_deserted_c", 0.4, 0),
  ("village_snow_a",mcn_no_shadow,"map_village_snow_a", 0.4, 0),
  ("village_snow_burnt_a",mcn_no_shadow,"map_village_snow_burnt_a", 0.4, 0),
  ("village_snow_deserted_a",mcn_no_shadow,"map_village_snow_deserted_a", 0.4, 0),


  ("camp",mcn_no_shadow,"camp_tent", 0.13, 0),
  ("ship",mcn_no_shadow,"boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"boat_sail_off", 0.23, 0),

  ("castle_a",mcn_no_shadow,"map_castle_a", 0.3,0),
  ("castle_b",mcn_no_shadow,"map_castle_b", 0.3,0),
  ("castle_c",mcn_no_shadow,"map_castle_c", 0.3,0),
  ("castle_d",mcn_no_shadow,"map_castle_d", 0.3,0),
  ("town_snow",mcn_no_shadow,"map_town_snow_a", 0.3,0),


  ("castle_snow_a",mcn_no_shadow,"map_castle_snow_a", 0.3,0),
  ("castle_snow_b",mcn_no_shadow,"map_castle_snow_b", 0.3,0),
  ("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("training_ground",mcn_no_shadow,"training", 0.35,0),

  ("bridge_a",mcn_no_shadow,"map_river_bridge_a", 1.27,0),
  ("bridge_b",mcn_no_shadow,"map_river_bridge_b", 0.7,0),
  ("bridge_snow_a",mcn_no_shadow,"map_river_bridge_snow_a", 1.27,0),

  ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        (try_end),
        ]),
     ]),

  # Banners
  ("map_flag_a01",0,"map_flag_a01", banner_scale,0),
  ("map_flag_a02",0,"map_flag_a02", banner_scale,0),
  ("map_flag_a03",0,"map_flag_a03", banner_scale,0),
  ("map_flag_a04",0,"map_flag_a04", banner_scale,0),
  ("map_flag_a05",0,"map_flag_a05", banner_scale,0),
  ("map_flag_a06",0,"map_flag_a06", banner_scale,0),
  ("map_flag_a07",0,"map_flag_a07", banner_scale,0),
  ("map_flag_a08",0,"map_flag_a08", banner_scale,0),
  ("map_flag_a09",0,"map_flag_a09", banner_scale,0),
  ("map_flag_a10",0,"map_flag_a10", banner_scale,0),
  ("map_flag_a11",0,"map_flag_a11", banner_scale,0),
  ("map_flag_a12",0,"map_flag_a12", banner_scale,0),
  ("map_flag_a13",0,"map_flag_a13", banner_scale,0),
  ("map_flag_a14",0,"map_flag_a14", banner_scale,0),
  ("map_flag_a15",0,"map_flag_a15", banner_scale,0),
  ("map_flag_a16",0,"map_flag_a16", banner_scale,0),
  ("map_flag_a17",0,"map_flag_a17", banner_scale,0),
  ("map_flag_a18",0,"map_flag_a18", banner_scale,0),
  ("map_flag_a19",0,"map_flag_a19", banner_scale,0),
  ("map_flag_a20",0,"map_flag_a20", banner_scale,0),
  ("map_flag_a21",0,"map_flag_a21", banner_scale,0),

  ("map_flag_b01",0,"map_flag_b01", banner_scale,0),
  ("map_flag_b02",0,"map_flag_b02", banner_scale,0),
  ("map_flag_b03",0,"map_flag_b03", banner_scale,0),
  ("map_flag_b04",0,"map_flag_b04", banner_scale,0),
  ("map_flag_b05",0,"map_flag_b05", banner_scale,0),
  ("map_flag_b06",0,"map_flag_b06", banner_scale,0),
  ("map_flag_b07",0,"map_flag_b07", banner_scale,0),
  ("map_flag_b08",0,"map_flag_b08", banner_scale,0),
  ("map_flag_b09",0,"map_flag_b09", banner_scale,0),
  ("map_flag_b10",0,"map_flag_b10", banner_scale,0),
  ("map_flag_b11",0,"map_flag_b11", banner_scale,0),
  ("map_flag_b12",0,"map_flag_b12", banner_scale,0),
  ("map_flag_b13",0,"map_flag_b13", banner_scale,0),
  ("map_flag_b14",0,"map_flag_b14", banner_scale,0),
  ("map_flag_b15",0,"map_flag_b15", banner_scale,0),
  ("map_flag_b16",0,"map_flag_b16", banner_scale,0),
  ("map_flag_b17",0,"map_flag_b17", banner_scale,0),
  ("map_flag_b18",0,"map_flag_b18", banner_scale,0),
  ("map_flag_b19",0,"map_flag_b19", banner_scale,0),
  ("map_flag_b20",0,"map_flag_b20", banner_scale,0),
  ("map_flag_b21",0,"map_flag_b21", banner_scale,0),  
 
  ("map_flag_c01",0,"map_flag_c01", banner_scale,0),
  ("map_flag_c02",0,"map_flag_c02", banner_scale,0),
  ("map_flag_c03",0,"map_flag_c03", banner_scale,0),
  ("map_flag_c04",0,"map_flag_c04", banner_scale,0),
  ("map_flag_c05",0,"map_flag_c05", banner_scale,0),
  ("map_flag_c06",0,"map_flag_c06", banner_scale,0),
  ("map_flag_c07",0,"map_flag_c07", banner_scale,0),
  ("map_flag_c08",0,"map_flag_c08", banner_scale,0),
  ("map_flag_c09",0,"map_flag_c09", banner_scale,0),
  ("map_flag_c10",0,"map_flag_c10", banner_scale,0),
  ("map_flag_c11",0,"map_flag_c11", banner_scale,0),
  ("map_flag_c12",0,"map_flag_c12", banner_scale,0),
  ("map_flag_c13",0,"map_flag_c13", banner_scale,0),
  ("map_flag_c14",0,"map_flag_c14", banner_scale,0),
  ("map_flag_c15",0,"map_flag_c15", banner_scale,0),
  ("map_flag_c16",0,"map_flag_c16", banner_scale,0), 
  
  ("map_flag_kingdom_a",0,"map_flag_kingdom_a", banner_scale,0),
  ("map_flag_kingdom_b",0,"map_flag_kingdom_b", banner_scale,0),
  ("map_flag_kingdom_c",0,"map_flag_kingdom_c", banner_scale,0),
  ("map_flag_kingdom_d",0,"map_flag_kingdom_d", banner_scale,0),
  ("map_flag_kingdom_e",0,"map_flag_kingdom_e", banner_scale,0),
  ("map_flag_kingdom_f",0,"map_flag_kingdom_f", banner_scale,0),
  ("map_flag_kingdom_g",0,"map_flag_kingdom_g", banner_scale,0),
  ("map_flag_kingdom_h",0,"map_flag_kingdom_h", banner_scale,0),  
  ("map_flag_kingdom_i",0,"map_flag_kingdom_i", banner_scale,0),  
  ("banner_end",0,"map_flag_a01", banner_scale,0),
  ("bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),
  
# RaW Begin  
  ("roman_town_a",0,"roman_town_a", 0.3,0),  
  ("roman_village_a",0,"roman_village_a", 0.4, 0),  
  ("roman_town_b",0,"roman_town_b", 0.5,0),    
  ("castle_besieged", mcn_no_shadow, "castle_a_spike_siege_combined", 0.60, 0),  
  ("celtic_village",0,"celtic_village", 0.4, 0),  
  ("greek_village",0,"greek_village", 0.4, 0),  
  ("greek_village_2",0,"greek_village_2", 0.4, 0),   
  ("greek_city",0,"greek_city", 0.3,0), 
  ("roman_camp_a",mcn_no_shadow,"joub_encampment_icon", 0.3,0),  
  ("parthenon",0,"parthenon", 0.5,0),   
  ("celtic_town_a",0,"celtic_town_a", 0.3,0),    
]
# modmerger_start version=201 type=2
try:
    component_name = "map_icons"
    var_set = { "map_icons" : map_icons }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
