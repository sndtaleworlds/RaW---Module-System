from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "the_free_city_states_of_greece.ogg", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),

  ("ambushed_by_neutral", "ambushed_by_neutral.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("ambushed_by_khergit", "ambushed_by_khergit.ogg", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_nord",    "ambushed_by_nord.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_rhodok",  "ambushed_by_rhodok.ogg", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_swadian", "ambushed_by_swadian.ogg", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_vaegir",  "ambushed_by_vaegir.ogg", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_sarranid", "middle_eastern_action.ogg", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  
  ("arena_1", "arena_1.ogg", mtf_sit_arena, 0),
#  ("arena_2", "arena_2.ogg", mtf_looping|mtf_sit_arena, 0),
  ("armorer", "armorer.ogg", mtf_sit_travel, 0),
  ("bandit_fight", "bandit_fight.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),

  ("calm_night_1", "calm_night_2.ogg", mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeat.ogg",mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("defeated_by_neutral_2", "defeat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("defeated_by_neutral_3", "defeat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

  ("fight_1", "a_land_besieged.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_2", "east_meets_east.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_3", "final_battle.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_as_khergit", "the_celts_are_coming.ogg", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_4", "lineadvance.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),  
  ("fight_as_nord", "glory_to_the_gods.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_as_rhodok", "highlander_charge.ogg", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_as_swadian", "they_came_they_saw_they.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_module_track, mtf_culture_all),
  ("fight_as_vaegir", "glory_to_the_gods.ogg", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_while_mounted_1", "victoris.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_while_mounted_2", "fight_while_mounted_2.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_3", "warband_action.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  ("infiltration_khergit", "infiltration_khergit.ogg", mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_all),

  ("killed_by_khergit", "killed_by_khergit.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
#  ("killed_by_neutral", "killed_by_neutral.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed, 0),
#  ("killed_by_nord", "killed_by_nord.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed, 0),
#  ("killed_by_rhodok", "killed_by_rhodok.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, 0),
  ("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
#  ("killed_by_vaegir", "killed_by_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed, 0),
  
  ("lords_hall_khergit", "druids_call.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_nord", "the_free_city_states_of_greece.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_swadian", "breeze_from_the_mediterranean_sea.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_rhodok", "civitates_aegaeo.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_vaegir", "winds_of_the_free.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("mounted_snow_terrain_calm", "calm_night_2.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
  ("outdoor_beautiful_land", "wrath_of_zeus.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern|mtf_module_track),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("seige_neutral", "honor_bound.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track),
  ("enter_the_juggernaut", "enter_the_juggernaut.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("siege_attempt", "siege_attempt.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "they_came_they_saw_they.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  ("tavern_1", "tavern_1.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "tavern_2.ogg", mtf_sit_tavern|mtf_sit_feast, 0),

  ("town_neutral", "the_steppes.ogg", mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_module_track),
  ("town_khergit", "druids_call.ogg", mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("town_nord", "civitates_aegaeo.ogg", mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("town_rhodok", "highlands.ogg", mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("town_swadian", "civitates_aegaeo.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("town_vaegir", "breeze_from_the_mediterranean_sea.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),

  ("travel_khergit", "a_celts_pride.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("travel_neutral", "winds_of_the_free.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_module_track),
  ("travel_nord",    "breeze_from_the_mediterranean_sea.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("travel_rhodok",  "highlands.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("travel_swadian", "glory_of_rome.ogg", mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("travel_vaegir",  "breeze_from_the_mediterranean_sea.ogg",  mtf_culture_2|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),
  ("travel_sarranid",  "middle_eastern_travel.ogg",  mtf_culture_6|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all|mtf_module_track),

  ("uncertain_homestead", "winds_of_the_free.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("hearth_and_brotherhood", "breeze_from_the_mediterranean_sea.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "tragic_village.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_evil.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_evil.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_evil.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("victorious_swadian", "victorious_evil.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_evil.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_evil.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),



  
]
