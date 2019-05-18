from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("town_merc_1","sargoth_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_2","tihr_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_3","veluca_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_4","suno_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_5","jelkala_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_6","praven_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_7","uxkhal_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_8","reyvadin_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_9","khudan_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_10","tulga_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_11","curaw_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_12","wercheg_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_13","rivacheg_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_14","halmar_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_15","yalen_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_16","dhirim_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_17","ichamur_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_18","narra_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

#Roman Towns
  ("town_1","Roma",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-386.96,49.05),[], 239),                            
  ("town_2","Tibur",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-377.895,55.5249),[], 75),                            
  ("town_3","Tusculum",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-377.103,46.415),[], 68),                         
  ("town_4","Antium",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-390.16,33.9013),[], 170),                         
  ("town_5","Capua",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-350.84,19.04),[], 44),                             
  ("town_6","Nola",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-339.593,9.17724),[], 124),                            
  ("town_7","Neapolis",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-352.48,12.59),[], 184),                        
  ("town_8","Cumae",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-357.02,15.9),[], 110),                           
  ("town_9","Pompeii",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-342.03,-0.700164),[], 202),                         
# Samnite Towns
  ("town_10","Maloenton",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.71,12.07),[], 120),                         
  ("town_11","Ladinod",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-330.08,33.48),[], 171),                         
  ("town_12","Buvaianud",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-343.25,26.72),[], 202), # Nouios Vesulliais as Meddís                     
  ("town_13","Venusia",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-322.56,6.78),[], 226),                         
  ("town_14","Histònion",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-331.81,46.81),[], 163),                         
  ("town_15","Aisernio",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-348.66,31.49),[], 172),                         
  ("town_16","Tullisiom",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-346.11,23.02),[], 232),                         
# Magna Graecia 
  ("town_17","Taras",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-304.64,0.82),[], 1),                         
  ("town_18","Thourioi",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.68,-19.85),[], 116),                         
  ("town_19","Kroton",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-304.46,-28.97),[], 279),                         
  ("town_20","Rhegion",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326.51,-48.6),[], 81),                         
  ("town_21","Lokroi Epizephyrioi",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-311.55,-43.83),[], 232),                         
  ("town_22","Elaía",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-330.4,-14.33),[], 274),
  # Sicily
  ("town_23","Syrákousai",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-338.04,-69.91),[], 256),                         
  ("town_24","Messana",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-334.42,-43.65),[], 152),                         
  ("town_25","Tauroménion",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-334.27,-53.35),[], 251),                         
  ("town_26","Akrágas",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-363.72,-68.06),[], 318),                         
  ("town_27","Herákleia Minōia",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-365.68,-63.74),[], 157),                         
  ("town_28","Morgantína",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-351.92,-59.28),[], 240),
  ("town_29","Gélas",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-351.84,-74.34),[], 304),
# Etruria
  ("town_30","Tarchuna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-404.11,54.147),[], 120),                       
  ("town_31","Fufluna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-416.75, 70.53),[], 270),                        
  ("town_32","Aritim", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-397.32, 85.96),[], 141),                         
  ("town_33","Alalia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-442.35, 44.27),[], 240),                         
  ("town_34","Velzna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-390.489,66.4858),[], 215),                          
  ("town_35","Velathri", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-411.388,83.2772),[], 119),                          
  ("town_36","Phersna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-388.94,78.6913),[], 76),                          
  ("town_37","Pisna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-423.38,87.4619),[], 281),                          
  ("town_38","Halethi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-393.631,55.8655),[], 76),      
# Senones
  ("town_39","Sena", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-361.3,78.07),[], 261),                         
  ("town_40","Pisaurum", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-369.67,89.02),[], 261),                         
  ("town_41","Ravenna", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-378.58,99.67),[], 261),                         
# Ligures
  ("town_42","Genua", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-435.22,105.78),[], 195),                         
  ("town_43","Dertona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-435.873,120.826),[], 105),                         
  ("town_44","Taurasia", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-451.96,128.53),[], 261),                         
# Boii
  ("town_45","Mediolanon", icon_celtic_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-432.147,138.997),[], 81),                         
  ("town_46","Bona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-406.09,102.75),[], 261),                         
  ("town_47","Brixia", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-414.525,143.343),[], 158),                         
  ("town_48","Acerrae", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-423.296,132.954),[], 261),                         
  ("town_49","Verona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-403.187,140.932),[], 261),       
# Poleis_Eleutherai 
  ("town_50","Athenai", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.98,-46.79),[], 140),                         
  ("town_51","Thebai", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-200.19,-36.65),[], 165),                         
  ("town_52","Argos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.8,-63.2),[], 241),                         
  ("town_53","Lakedaimon", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-219.76,-71.96),[], 180),                         
  ("town_54","Gytheion", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.96,-81.88),[], 261),                         
  ("town_55","Messene", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.37,-67.46),[], 261),                         
  ("town_56","Hierápytna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.42,-112.88),[], 195),                         
  ("town_57","Knosós", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.82,-104.58),[], 345),                         
  ("town_58","Rhódos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.59,-69.61),[], 261),                         
  ("town_59","Delphoi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.31,-35.32),[], 184),                         
# Koinon_Hellenon 
  ("town_60","Kórinthos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.38,-43.18),[], 193),                         
  ("town_61","Mégara", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-200.82,-43.54),[], 0),                         
  ("town_62","Elis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.59,-53.94),[], 261),                         
  ("town_63","Megalópolis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.6,-63.55),[], 261),                         
  ("town_64","Tegéa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.81,-63.22),[], 105),        
# Makedonia
  ("town_65","Pella", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.32,28.31),[], 250),                         
  ("town_66","Thessaloníke", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.11,21.7),[], 329),                         
  ("town_67","Édessa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.49,35.75),[], 261),                         
  ("town_68","Díon", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-215.49,14.56),[], 261),                         
  ("town_69","Amphípolis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.5,31.28),[], 4),                         
  ("town_70","Philippoi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.17,38.42),[], 82),                         
  ("town_71","Herakleia Lynkestis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.25,44.92),[], 261),                         
  ("town_72","Chalkis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.83,-36.12),[], 149),                         
  ("town_73","Larissa Kremaste", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.1,-4.88),[], 243),                         
  ("town_74","Phársalos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.72,-10.76),[], 43),                         
  ("town_75","Larissa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.57,0.97),[], 215),                         
# Epeiros
  ("town_76","Ambrakia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.67,-17.65),[], 100),                         
  ("town_77","Kérkyra", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.09,-6.57),[], 261),                         
  ("town_78","Phoinike", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257.53,0.41),[], 204),                         
  ("town_79","Dodona", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.6,-12.66),[], 170),         
  ("town_80","Apollonia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-268.002,11.0111),[], 170),             
  
#Roman Castles 
  ("castle_1","Ostia_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-395.68,42.56),[],179),               
  ("castle_2","Norba_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-373.01,39.95),[],130),               
  ("castle_3","Interamna_Lirenas_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-357.52,26.02),[],127),                
  ("castle_4","Sutrium_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-395.801,52.6532),[],187),                
# Megalle Hellas
  ("castle_5","Skylla",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-325,-40),[],37),                  
# Sicily
  ("castle_6","Euryelos",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-340.09,-68.34),[],233),                
# Etruscan
  ("castle_7","Clevsin",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-392.714,76.5192),[],253),             
  ("castle_8","Caisra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-402.262,48.5534),[],264),            
  ("castle_9","Vatluna",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-414.607,67.9083),[],148),           
# Poleis_Eleutherai
  ("castle_10","Peiraieús",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,  (-196.3,-48.19),[],322),           
  ("castle_11","Trinasos",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,  (-216.01,-79.22),[],339),           
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  #Roman Villages 
  ("village_1", "Gabii",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-379, 50.82),[], 134),               
  ("village_2", "Ostia Portus",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-397.88, 43.22),[], 288),       
  ("village_3", "Praeneste",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-371.27, 50.49),[], 257),            
  ("village_4", "Aricia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-379.38, 43.62),[], 357),               
  ("village_5", "Carseoli",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-376.21, 57.65),[], 184),             
  ("village_6", "Anagnia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-362.98, 49.29),[], 90),         
  ("village_7", "Lanuvium",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-377.76, 40.6),[], 136),           
  ("village_8", "Ardea",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-392.04, 36.69),[], 100),              
  ("village_9", "Astura",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-386.09, 31.33),[], 158),              
  ("village_10", "Circeii",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-378.8, 27.11),[], 359),              
  ("village_11", "Aquinum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-355.36, 30.44),[], 89),              
  ("village_12", "Minturnae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-365.47, 16.04),[], 335),             
  ("village_13", "Cales",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-353.5, 23.66),[], 100),              
  ("village_14", "Fregellae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-363.126,30.5353),[], 212),          
  ("village_15", "Abellinum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.5, 9.56),[], 100),             
  ("village_16", "Suessula",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-341.37, 13.67),[], 100),            
  ("village_17", "Stabiae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-341.07, -2.63),[], 100),            
  ("village_18", "Irna",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-339.3, -5.27),[], 357),        
  ("village_19", "Fundi",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-365.871,24.326),[], 299),         
  ("village_20", "Puteoli",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-355.22, 14.69),[], 343),              
  ("village_21", "Herculaneum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-351.64, 9.54),[], 323),              
  ("village_22", "Satricum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-378.68, 34.83),[], 192),              
  ("village_23", "Volturnum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-361.33, 16.43),[], 344),              
  ("village_24", "Atella",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-353.02, 17.41),[], 192),            
  ("village_25", "Setia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-368.3, 37.39),[], 192),              
  ("village_26", "Lavinium",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-394.78, 39.46),[], 192),              
  ("village_27", "Alba Fucens",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-369.25, 56.1),[], 192),      
  
# Samnite Villages 
  ("village_28", "Lavìdde",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-320.19,9.23),[], 229),               
  ("village_29", "Mélfe",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-323.14,5.98),[], 229),               
  ("village_30", "Akudunniad",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-321.66,11.14),[], 250),               
  ("village_31", "Velecha",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-331.35,-3.62),[], 227),# Abellinum               
  ("village_32", "Aikoulanon",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-327.72,15.81),[], 258),               
  ("village_33", "Kávdio",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337.7,11.2),[], 88),               
  ("village_34", "Saipins",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-340.3,25.9),[], 70),               
  ("village_35", "Ouénafron",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-350.9,28.63),[], 229),               
  ("village_36", "Aufidena",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-350.89,31.81),[], 122),               
  ("village_37", "Cluviae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-334.46,38.4409),[], 65),             
  ("village_38", "Anxanon",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.74,46.78),[], 205),             
  ("village_39", "Fagifulae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-336.13,31.01),[], 277),             
  ("village_40", "Touxion",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-330.49,17.35),[], 229), # Aequum Tuticum              
  ("village_41", "Meflans",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-331.92,15.42),[], 136), # Pagus Meflanuns              
  ("village_42", "Kalena",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-332.27,31.27),[], 229),               
  ("village_43", "Nuvkrinum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.77,3.24),[], 229),               
  ("village_44", "Kaiatinim",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-348.13,21.51),[], 229),  
  
# Magna Graecia 
  ("village_45", "Metapontion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-311.96, -4.32),[], 229),             
  ("village_46", "Herakleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-309.65, -12.64),[], 232),           
  ("village_47", "Kallipolis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-296.76, -1.27),[], 93),               
  ("village_48", "Medma",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-325.59, -32.8),[], 54),               #
  ("village_49", "Kaulonia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-310.14, -39.07),[], 229),               
  ("village_50", "Skylletion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-308.2, -35.32),[], 252),               
  ("village_51", "Petelia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-303.28, -26.45),[], 229),             
  ("village_52", "Hipponion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326.63, -29.76),[], 94),             #
  ("village_53", "Terina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-330.04, -26.24),[], 289),             
  ("village_54", "Metaúros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326.94, -37.82),[], 115),             
  ("village_55", "Satyrion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-300.7, 0.13),[], 115),             
  ("village_56", "Genousía",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-314.58, -2.31),[], 115),             #
  ("village_57", "Tauranía",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-325.58, -35.13),[], 115),            # 
  ("village_58", "Krimisa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-304.34, -23.91),[], 115),     
  
# Syracuse 
  ("village_59", "Leontînoi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-341.71,-66.26),[], 150),           
  ("village_60", "Katána",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337.4,-57.45),[], 241),             #
  ("village_61", "Tyndarís",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-343.97,-40.92),[], 325),           #
  ("village_62", "Naxos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.59,-55.06),[], 119),             #
  ("village_63", "Mylae",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-338.79,-41.26),[], 175),             #
  ("village_64", "Élōros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-338.16,-74.95),[], 239),         #
  ("village_65", "Kamárina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-348.45,-75.5),[], 116),      # 
  ("village_66", "Omphake",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-352.69,-72.56),[], 26),         
  ("village_67", "Mótouka",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-342.24,-75.39),[], 158),               
  ("village_68", "Triokala",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-365.79,-61.28),[], 258),             
  ("village_69", "Mégara Hybláia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337.88,-67.23),[], 258),             #
  ("village_70", "Kentóripa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-342.98,-58.1),[], 258),             
  ("village_71", "Hénna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-355.07,-56.98),[], 258),             
  ("village_72", "Phoinix",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-333.96,-51),[], 258),             #
  ("village_73", "Kaprianon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-362.55,-63.13),[], 170),             
  ("village_74", "Phalarion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-355.82,-71.98),[], 258),           #  
  ("village_75", "Ménainon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-345.04,-70.66),[], 258),             
  ("village_76", "Thapsós",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337.76,-69.02),[], 258),   #
  
# Etruria 
  ("village_77", "Ilva",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-426.52, 61.86),[], 358),         
  ("village_78", "Tlamu",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-411.49, 60.74),[], 325),     
  ("village_79", "Luca",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-421.95, 90.79),[], 165),       
  ("village_80", "Vipsul",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-406.65, 94.95),[], 148),         
  ("village_81", "Curtun",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-394.661,82.9014),[], 258),     
  ("village_82", "Rusla",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-412.053,67.3589),[], 258),           
  ("village_83", "Aurina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-409.575,62.7514),[], 258),       
  ("village_84", "Pyrgi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-403.755,49.6169),[], 107),       
  ("village_85", "Velch",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-407.95,58.2878),[], 258),           
  ("village_86", "Tuter",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-386.904,68.9026),[], 258),       
  ("village_87", "Saina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-404.159,83.2265),[], 119),   
  ("village_88", "Arrantia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-410.918,81.1596),[], 179),       
  ("village_89", "Kersounon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-447.9, 59.89),[], 258),       
  ("village_90", "Nepa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-393.586,52.4873),[], 258),       
  ("village_91", "Hurta",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-390.11,60.9342),[], 258),       
  ("village_92", "Statna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-391.743,61.7318),[], 258),       
  ("village_93", "Arna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-385.129,79.7381),[], 258),       
  ("village_94", "Phlera",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-400.392,55.3648),[], 258),    # Blera   
  ("village_95", "Grauisca",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-405.284,52.7012),[], 258),       
  ("village_96", "Raisne",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-421.332,79.7758),[], 258),       # Vada
  ("village_97", "Birenz",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-407.94, 91.66),[], 258),       
  ("village_98", "Pisturim",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-412.49, 95.95),[], 258),       
  ("village_99", "Kentourinon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-442.93, 63.72),[], 258),       
  ("village_100", "Phikaria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-453.75, 25.05),[], 182),  

# Senones
  ("village_101", "Suasa",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-364.11,75.26),[], 287),             
  ("village_102", "Ostra",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-361.64,74.41),[], 258),             
  ("village_103", "Urvinum Mataurense",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-370.64,83.98),[], 297),             
  ("village_104", "Pitinum Pisaurense",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-374.91,85.9),[], 258),             
  ("village_105", "Sarsina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-380.63,91.6),[], 258),             
  ("village_106", "Faventia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-380.94,96.18),[], 258),             
  ("village_107", "Fanum Fortunae",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-368.27,87.55),[], 258),             
# Ligures
  ("village_108", "Segeste",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-429.22,101),[], 217),             
  ("village_109", "Libarna",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-436.754,112.965),[], 258),             
  ("village_110", "Iria",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-435.047,123.725),[], 258),             
  ("village_111", "Clastidium",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-430.455,124.884),[], 258),             
  ("village_112", "Bodincomagus",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-447.03,130.38),[], 258),             
  ("village_113", "Eporedia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-449.08,136.34),[], 258),             
  ("village_114", "Hasta",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-444.29,122.63),[], 258),             
  ("village_115", "Vercellae",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-442.339,135.349),[], 258),             
  ("village_116", "Alba Ingaunum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-441.64,105.31),[], 258),             
# Boii
  ("village_117", "Modicia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-429.515,140.454),[], 258),             
  ("village_118", "Comum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-433.638,144.147),[], 258),             
  ("village_119", "Bergomum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-422.498,145.174),[], 258),             
  ("village_120", "Placentia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-426.427,130.469),[], 258),             
  ("village_121", "Parma",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-420.497,120.744),[], 258),             
  ("village_122", "Mutina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-409.27,109.03),[], 258),             
  ("village_123", "Minervium",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-418.883,137.318),[], 258),             
  ("village_124", "Voberna",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-410.434,141.538),[], 258),             
  ("village_125", "Mantua",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-407.199,127.989),[], 258),             
  ("village_126", "Spina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-386.75,112.6),[], 258),             
  ("village_127", "Bretina Belounon",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-405.813,140.771),[], 258),             
  ("village_128", "Cremona",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-419.685,130.726),[], 258),   

# Poleis_Eleutherai 
  ("village_129", "Phaleron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.68,-49.68),[], 193),             
  ("village_130", "Thorikos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.71,-52.8),[], 258),             
  ("village_131", "Marathon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.16,-38.49),[], 258),             
  ("village_132", "Acharnaí",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.38,-43.5),[], 258),             
  ("village_133", "Plataiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-199.05,-39.38),[], 258),             
  ("village_134", "Thespiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.49,-37.29),[], 258),             
  ("village_135", "Chairóneia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.42,-35.42),[], 258),             
  ("village_136", "Tanagra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.79,-40.5),[], 258),             
  ("village_137", "Asine",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.08,-63.81),[], 258),             
  ("village_138", "Epidauros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.29,-60.11),[], 258),             
  ("village_139", "Aigina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.7,-57.36),[], 258),             
  ("village_140", "Hermione",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.14,-70.36),[], 258),             
  ("village_141", "Pellana",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.11,-69.31),[], 258),             
  ("village_142", "Amyklai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.24,-74.13),[], 258),             
  ("village_143", "Geronthrai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.95,-75.92),[], 258),             
  ("village_144", "Gerenia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-223.64,-80.88),[], 258),             
  ("village_145", "Epidauros Limera",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.95,-80.32),[], 258),             
  ("village_146", "Helos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.56,-78.19),[], 258),             
  ("village_147", "Tainaron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.29,-92.3),[], 258),             
  ("village_148", "Palaia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.98,-80.1),[], 258),             
  ("village_149", "Methone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-239.3,-81.64),[], 258),             
  ("village_150", "Thouria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-226.78,-70.52),[], 258),             
  ("village_151", "Ampheia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-226.73,-66.71),[], 258),             

  ("village_152", "Praisos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.55,-110.05),[], 258),             
  ("village_153", "Lyktos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.92,-106.49),[], 258),             
  ("village_154", "Chersonasos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.11,-103.04),[], 258),             
  ("village_155", "Heraklion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.37,-103.15),[], 258),             
  ("village_156", "Kydonia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.9,-103.5),[], 258),             
  ("village_157", "Gortyna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.41,-113.79),[], 258),             
  ("village_158", "Eleutherna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.04,-105.33),[], 258),             
  ("village_159", "Kisamos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.99,-104.66),[], 258),             

  ("village_160", "Lindos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.8,-75.8),[], 258),             
  ("village_161", "Ialysos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.75,-68.85),[], 258),             
  ("village_162", "Amphissa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.59,-32.87),[], 258),             
  ("village_163", "Antikyra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.09,-36.43),[], 258),             
  ("village_164", "Amphikleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.76,-32.04),[], 258), 
# Koinon_Hellenon  
  ("village_165", "Lechaion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.31,-41.48),[], 258),             
  ("village_166", "Sikyón",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.81,-41.1),[], 258),             
  ("village_167", "Kleonai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.91,-45.15),[], 258),             
  ("village_168", "Kenchreai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.81,-45.89),[], 258),             
  ("village_169", "Eleusis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.27,-44.25),[], 258),             
  ("village_170", "Pagai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.93,-41.59),[], 258),             
  ("village_171", "Dyme",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-236.97,-44.18),[], 258),             
  ("village_172", "Zakynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.16,-62.22),[], 258),             
  ("village_173", "Krane",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.04,-39.6),[], 258),             
  ("village_174", "Kleitor",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.37,-47.27),[], 258),             
  ("village_175", "Heraia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-232.3,-58.35),[], 258),             
  ("village_176", "Lykosoura",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-228.9,-62.97),[], 258),             
  ("village_177", "Lepreon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.08,-62.56),[], 258),             
  ("village_178", "Mantineia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.33,-61.83),[], 258),             
  ("village_179", "Hysiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.69,-63.95),[], 258),             
  ("village_180", "Orchomenos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.84,-58.82),[], 258),  
# Makedonia  
  ("village_181", "Gortynia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.02,40.2),[], 258),             
  ("village_182", "Berroia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.29,21.21),[], 258),             
  ("village_183", "Methone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.37,19.68),[], 258),             
  ("village_184", "Pydna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.99,17.29),[], 258),             
  ("village_185", "Therme",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.4,17.79),[], 258),             
  ("village_186", "Olynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-197.76,14.54),[], 258),             
  ("village_187", "Akanthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.72,17.47),[], 258),             
  ("village_188", "Europos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-228.162,39.9174),[], 258),             
  ("village_189", "Euboia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.7,33.33),[], 258),             
  ("village_190", "Aigeai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.59,19.3),[], 258),             
  ("village_191", "Arethousa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.42,26.53),[], 258),             
  ("village_192", "Myrkinos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.17,35.35),[], 258),             
  ("village_193", "Neapolis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.84,34.58),[], 258),             
  ("village_194", "Thasos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.32,28.34),[], 258),             
  ("village_195", "Stymbara",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.72,50.91),[], 258),             
  ("village_196", "Lychnidos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257.36,48.86),[], 258),             
  ("village_197", "Gonnoi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.01,4.87),[], 258),             
  ("village_198", "Argoussa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.56,2.44),[], 258),             
  ("village_199", "Atrax",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.7,-0.47),[], 258),             
  ("village_200", "Krannon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.75,-2.83),[], 258),             
  ("village_201", "Skotoussa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.66,-8.08),[], 258),             
  ("village_202", "Kierion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.08,-8.36),[], 258),             
  ("village_203", "Lamia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-219.44,-18),[], 258),             
  ("village_204", "Herakleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-219.89,-22.05),[], 258),             
  ("village_205", "Histiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190.39,-13.91),[], 258),             
  ("village_206", "Eretria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-182.6,-38.77),[], 258),             
  ("village_207", "Amarynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.01,-41.63),[], 258),             
  ("village_208", "Karystos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.98,-44.58),[], 258),             
# Epeiros
  ("village_209", "Leucas",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.23,-27.96),[], 258),             
  ("village_210", "Thyrreion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-242.6,-28.33),[], 258),             
  ("village_211", "Kassope",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.41,-20.02),[], 258),             
  ("village_212", "Orraon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240.33,-15.64),[], 258),             
  ("village_213", "Ephyra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-252.558,-21.5291),[], 258),             
  ("village_214", "Torone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.54,-17.35),[], 258),             
  ("village_215", "Photike",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.78,-12.75),[], 258),             
  ("village_216", "Passaron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.88,-10.47),[], 258),             
  ("village_217", "Onchesmos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-259.04,-2.33),[], 258),             
  ("village_218", "Chalkis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.3,-13.41),[], 258),             
  ("village_219", "Elina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-254.29,-20.48),[], 258),             
  ("village_220", "Bouthroton",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-259.4,-6.03),[], 258),             
  ("village_221", "Omphalion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.22,3.76),[], 258),      
  ("village_222", "Antipatreia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-259.492,11.8277),[], 258),   
  ("village_223", "Amantia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.095,7.38077),[], 258),     
  ("village_224", "Dimalion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.739,12.3994),[], 258),      


  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.4, 102.8),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.8, 33),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.5, 72.0),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.5, -75.2),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.8, 12.5),[], 100),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.37, 65.10),[], -44.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.44, 77.88),[], 4.28),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.87, 87.95),[], 64.5),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.71, 62.13),[], -2.13),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.02, 72.61),[], 21.5),
  ("Bridge_6","{!}6",icon_bridge_b|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.83, 52.24),[], -73.5),
  ("Bridge_7","{!}7",icon_bridge_b|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.79, 76.84),[], -64),
  ("Bridge_8","{!}8",icon_bridge_b|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.05, -6),[], 1.72),
  ("Bridge_9","{!}9",icon_bridge_b|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.95, -9.60),[], -33.76),
  ("Bridge_10","{!}10",icon_bridge_b|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.32, -75.27),[], -44.07),
  ("Bridge_11","{!}11",icon_bridge_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.39, 67.82),[], 81.3),
  ("Bridge_12","{!}12",icon_bridge_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.33, -1.94),[], -35.5),
  ("Bridge_13","{!}13",icon_bridge_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.02, -7),[], -17.7),
  ("Bridge_14","{!}14",icon_bridge_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.36, 75.8),[], 66.6),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-423.31, 136.45),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-219.8, -9.14),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-368.5, 51.4),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  
  # ("delphi","Delphi",icon_parthenon|pf_is_static|pf_always_visible|pf_hide_defenders|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.244,-34.72),[], 90), 
  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
