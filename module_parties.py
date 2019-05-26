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
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(78.7, 147.69),[(trp_player,1,0)]),
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
  ("town_1","Roma",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.01,168.09),[], 225),                            
  ("town_2","Tibur",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.16,173.06),[], 121),                            
  ("town_3","Tusculum",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.12,162.36),[], 53),                         
  ("town_4","Antium",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.45,145.72),[], 170),                         
  ("town_5","Capua",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.61,126.1),[], 58),                             
  ("town_6","Nola",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.48,118.38),[], 109),                            
  ("town_7","Neapolis",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.03,115.48),[], 177),                        
  ("town_8","Cumae",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.5,118.21),[], 102),                           
  ("town_9","Pompeii",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.57,111.26),[], 202),                         
# Samnite Towns
  ("town_10","Maloenton",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.88,128.46),[], 145),                         
  ("town_11","Ladinod",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.54,160.17),[], 242),                         
  ("town_12","Buvaianud",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.37,145.51),[], 210), # Nouios Vesulliais as Meddís                     
  ("town_13","Venusia",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.09,121.31),[], 218),                         
  ("town_14","Histònion",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.19,176.1),[], 163),                         
  ("town_15","Aisernio",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.85,151.98),[], 172),                         
  ("town_16","Tullisiom",  icon_roman_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.75,132.09),[], 166),                         
# Magna Graecia 
  ("town_17","Taras",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.07,98.21),[], 158),                         
  ("town_18","Thourioi",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.28,55.95),[], 106),                         
  ("town_19","Kroton",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.98,27.62),[], 68),                         
  ("town_20","Rhegion",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.27,-21.54),[], 81),                         
  ("town_21","Lokroi Epizephyrioi",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.26,-15.66),[], 68),                         
  ("town_22","Elaía",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.45,81.61),[], 355),
  # Sicily
  ("town_23","Syrákousai",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.57,-69.05),[], 256),                         
  ("town_24","Messana",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.74,-13.24),[], 245),                         
  ("town_25","Tauroménion",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.34,-34.33),[], 251),                         
  ("town_26","Akrágas",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.25,-59.36),[], 163),                         
  ("town_27","Herákleia Minoia",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.96,-55.88),[], 91),                         
  ("town_28","Morgantína",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.29,-45.72),[], 160),
  ("town_29","Gélas",  icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.58,-70.75),[], 324),
# Etruria
  ("town_30","Tarchuna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.07, 188.61),[], 120),                       
  ("town_31","Fufluna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.95, 225.38),[], 254),                        
  ("town_32","Aritim", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.7, 239.97),[], 138),                         
  ("town_33","Alalia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.92, 181.49),[], 240),                         
  ("town_34","Velzna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.37, 205.23),[], 302),                          
  ("town_35","Velathri", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.49, 237.29),[], 119),                          
  ("town_36","Phersna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.44, 226.52),[], 110),                          
  ("town_37","Pisna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.41, 263.83),[], 315),                          
  ("town_38","Halethi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.63, 187.79),[], 121),      
# Senones
  ("town_39","Sena", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.02,257.11),[], 160),                         
  ("town_40","Pisaurum", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.18,265.47),[], 157),                         
  ("town_41","Ravenna", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.15,286.32),[], 162),                         
# Ligures
  ("town_42","Genua", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.51,298.93),[], 178),                         
  ("town_43","Dertona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.35,317.95),[], 71),                         
  ("town_44","Taurasia", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.68,325.22),[], 249),                         
# Boii
  ("town_45","Mediolanon", icon_celtic_town_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.39,353.41),[], 182),                         
  ("town_46","Bona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.26,293.47),[], 271),                         
  ("town_47","Brixia", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.11,359.47),[], 155),                         
  ("town_48","Acerrae", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.4,331.94),[], 161),                         
  ("town_49","Verona", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.71,353.09),[], 192),       
# Poleis_Eleutherai 
  ("town_50","Athenai", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(337.13,-25.38),[], 58),                         
  ("town_51","Thebai", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(322.74,-6.12),[], 165),                         
  ("town_52","Argos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(302.87,-43.29),[], 254),                         
  ("town_53","Lakedaimon", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(294.99,-70.9),[], 195),                         
  ("town_54","Gytheion", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300.17,-85.04),[], 46),                         
  ("town_55","Messene", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(278.15,-64.82),[], 261),                         
  ("town_56","Hierápytna", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(397.95,-171.03),[], 235),                         
  ("town_57","Knosós", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(386.45,-158.66),[], 360),                         
  ("town_58","Rhódos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(466.68,-110.13),[], 322),                         
  ("town_59","Delphoi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(295.36,-0.46),[], 132),                         
# Koinon_Hellenon 
  ("town_60","Kórinthos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(308.42,-29.32),[], 276),                         
  ("town_61","Mégara", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325.73,-22.89),[], 34),                         
  ("town_62","Elis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(269.86,-32.5),[], 84),                         
  ("town_63","Megalópolis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(286.46,-51.29),[], 220),                         
  ("town_64","Tegéa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(294.19,-50.8),[], 57),        
# Makedonia
  ("town_65","Pella", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(299.86,111.63),[], 142),                         
  ("town_66","Thessaloníke", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(312.71,103.81),[], 13),                         
  ("town_67","Édessa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(282.22,115.34),[], 9),                         
  ("town_68","Díon", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(299.04,78.39),[], 287),                         
  ("town_69","Amphípolis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(340.92,112.95),[], 20),                         
  ("town_70","Philippoi", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(354.47,124.39),[], 243),                         
  ("town_71","Herakleia Lynkestis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(262.49,122.46),[], 248),                         
  ("town_72","Chalkis", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(333.53,-0.64),[], 241),                         
  ("town_73","Larissa Kremaste", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(311.85,23.87),[], 73),                         
  ("town_74","Phársalos", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(290.25,38.54),[], 27),                         
  ("town_75","Larissa", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(296.86,56.4),[], 207),                         
# Epeiros
  ("town_76","Ambrakia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(251.53,29.7),[], 33),                         
  ("town_77","Kérkyra", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(216.25,54.99),[], 67),                         
  ("town_78","Phoinike", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222.74,65.03),[], 166),                         
  ("town_79","Dodona", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(247.04,47.57),[], 133),         
  ("town_80","Apollonia", icon_greek_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(204.74,109.08),[], 145),             
  
#Roman Castles 
  ("castle_1","Ostia_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.46,161.82),[],179),               
  ("castle_2","Norba_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.4,152.4),[],130),               
  ("castle_3","Interamna_Lirenas_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.69,144.42),[],128),                
  ("castle_4","Sutrium_Castra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.42,184.17),[],211),                
# Megalle Hellas
  ("castle_5","Skylla",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.17,-12.84),[],141),                  
# Sicily
  ("castle_6","Euryelos",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.12,-66.86),[],277),                
# Etruscan
  ("castle_7","Clevsin",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.7, 224.61),[],245),             
  ("castle_8","Caisra",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.24, 171.45),[],221),            
  ("castle_9","Vatluna",icon_roman_camp_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.38, 219.25),[],225),           
# Poleis_Eleutherai
  ("castle_10","Peiraieús",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,  (335.19,-25.96),[],354),           
  ("castle_11","Trinasos",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,  (302.59,-83.84),[],64),           
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  #Roman Villages 
  ("village_1", "Gabii",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.43,166.01),[], 134),               
  ("village_2", "Ostia Portus",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.58,159.96),[], 121),       
  ("village_3", "Praeneste",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.41,163.53),[], 106),            
  ("village_4", "Aricia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.72,159.14),[], 194),               
  ("village_5", "Carseoli",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.41,174.12),[], 104),             
  ("village_6", "Anagnia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.59,159.16),[], 84),         
  ("village_7", "Lanuvium",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.28,155.67),[], 136),           
  ("village_8", "Ardea",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.57,152.49),[], 100),              
  ("village_9", "Astura",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.91,142.89),[], 158),              
  ("village_10", "Circeii",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.04,133.59),[], 359),              
  ("village_11", "Aquinum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.65,145.96),[], 66),              
  ("village_12", "Minturnae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.92,133.87),[], 335),             
  ("village_13", "Cales",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.47,132.58),[], 100),              
  ("village_14", "Fregellae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.53,151.21),[], 212),          
  ("village_15", "Abella",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.68,119.9),[], 100),             
  ("village_16", "Suessula",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.02,120.85),[], 62),            
  ("village_17", "Stabiae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.64,108.51),[], 100),            
  ("village_18", "Irna",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.81,103.77),[], 271),        
  ("village_19", "Fundi",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.31,137.89),[], 299),         
  ("village_20", "Puteoli",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.2,113.91),[], 343),              
  ("village_21", "Herculaneum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.29,113.39),[], 140),              
  ("village_22", "Satricum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.44,146.69),[], 116),              
  ("village_23", "Volturnum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.57,125),[], 223),              
  ("village_24", "Atella",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.07,122.1),[], 192),            
  ("village_25", "Setia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.26,148.08),[], 188),              
  ("village_26", "Lavinium",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.52,156.01),[], 192),              
  ("village_27", "Alba Fucens",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.23,172.29),[], 136),      
  
# Samnite Villages 
  ("village_28", "Lavìdde",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.58,125.44),[], 206),               
  ("village_29", "Mélfe",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.09,123.27),[], 229),               
  ("village_30", "Akudunniad",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.39,125.89),[], 250),               
  ("village_31", "Velecha",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.69,116.99),[], 53),# Abellinum               
  ("village_32", "Aikoulanon",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.33,122.32),[], 88),               
  ("village_33", "Kávdio",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.63,124.08),[], 357),               
  ("village_34", "Saipins",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.82,141.39),[], 70),               
  ("village_35", "Ouénafron",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.89,148.72),[], 239),               
  ("village_36", "Aufidena",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.29,156.1),[], 161),               
  ("village_37", "Cliternia",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.73,163.89),[], 65),             
  ("village_38", "Anxanon",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.64,184.31),[], 216),             
  ("village_39", "Fagifulae",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.39,154.27),[], 29),             
  ("village_40", "Touxion",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.69,126.99),[], 110), # Aequum Tuticum              
  ("village_41", "Meflans",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.43,130.72),[], 136), # Pagus Meflanuns              
  ("village_42", "Kalena",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.26,154.81),[], 229),               
  ("village_43", "Nuvkrinum",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.31,108.24),[], 66),               
  ("village_44", "Kaiatinim",  icon_roman_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.33,131.35),[], 229),  
  
# Magna Graecia 
  ("village_45", "Metapontion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.03,96.87),[], 229),             
  ("village_46", "Herakleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.36,84.32),[], 232),           
  ("village_47", "Kallipolis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.15,76.61),[], 93),               
  ("village_48", "Medma",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.64,-0.88),[], 110),               #
  ("village_49", "Kaulonia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.95,-2.87),[], 229),               
  ("village_50", "Skylletion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.21,15.26),[], 245),               
  ("village_51", "Petelia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.13,107.22),[], 229),             
  ("village_52", "Hipponion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.79,9.78),[], 94),             #
  ("village_53", "Terina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.49,21.77),[], 183),             
  ("village_54", "Metaúros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.86,-4.79),[], 244),             
  ("village_55", "Satyrion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.84,92.41),[], 330),             
  ("village_56", "Genousía",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118.12,103.28),[], 214),             #
  ("village_57", "Tauranía",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.61,-7.98),[], 115),            # 
  ("village_58", "Krimisa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.51,42.77),[], 84),     
  
# Syracuse 
  ("village_59", "Leontînoi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.6,-57.83),[], 222),           
  ("village_60", "Katána",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.4,-50),[], 241),             #
  ("village_61", "Tyndarís",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.63,-18.45),[], 202),           #
  ("village_62", "Naxos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.6,-36.23),[], 164),             #
  ("village_63", "Mylae",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.41,-13.43),[], 175),             #
  ("village_64", "Éloros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.43,-85.32),[], 239),         #
  ("village_65", "Kamárina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.55,-77.48),[], 116),      # 
  ("village_66", "Omphake",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.54,-67.78),[], 194),         
  ("village_67", "Mótouka",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.42,-82.29),[], 158),               
  ("village_68", "Triokala",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.75,-48.57),[], 148),             
  ("village_69", "Mégara Hybláia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.41,-63.4),[], 110),             #
  ("village_70", "Kentóripa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.91,-43.5),[], 219),             
  ("village_71", "Hénna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.74,-40.69),[], 268),             
  ("village_72", "Phoinix",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.81,-22.56),[], 258),             #
  ("village_73", "Kaprianon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.32,-53.96),[], 8),             
  ("village_74", "Phalarion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.36,-67.81),[], 186),           #  
  ("village_75", "Ménainon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.45,-73.35),[], 258),             
  ("village_76", "Thapsós",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.36,-67.18),[], 258),   #
  
# Etruria 
  ("village_77", "Ilva",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.61, 218.18),[], 351),         
  ("village_78", "Tlamu",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.38, 201.3),[], 320),     
  ("village_79", "Luca",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.75, 267.76),[], 165),       
  ("village_80", "Vipsul",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.85, 266.57),[], 307),         
  ("village_81", "Curtun",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.32, 234.48),[], 45),     
  ("village_82", "Rusla",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.51, 216.86),[], 11),           
  ("village_83", "Aurina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.54, 204.78),[], 175),       
  ("village_84", "Pyrgi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.34, 172.73),[], 308),       
  ("village_85", "Velch",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.63, 195.7),[], 118),           
  ("village_86", "Tuter",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.59, 196.62),[], 214),       
  ("village_87", "Saina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.9, 230.71),[], 128),   
  ("village_88", "Arrantia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.06, 231.55),[], 179),       
  ("village_89", "Kersounon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.17, 212.9),[], 198),       
  ("village_90", "Nepet",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.03, 184.14),[], 237),       
  ("village_91", "Hurta",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.41, 195.37),[], 164),       
  ("village_92", "Statna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.35, 198.91),[], 114),       
  ("village_93", "Arna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.91, 227.47),[], 172),       
  ("village_94", "Phlera",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.7, 188.21),[], 140),    # Blera   
  ("village_95", "Grauisca",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.7, 186.75),[], 255),       
  ("village_96", "Raisne",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.52, 245.52),[], 259),       # Vada
  ("village_97", "Birenz",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.99, 265.03),[], 233),       
  ("village_98", "Pisturim",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.77, 271.84),[], 207),       
  ("village_99", "Kentourinon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.73, 227.29),[], 88),       
  ("village_100", "Phikaria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.66, 149.28),[], 299),  

# Senones
  ("village_101", "Suasa",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.63,256.69),[], 287),             
  ("village_102", "Ostra",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.01,251.41),[], 258),             
  ("village_103", "Urvinum Mataurense",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.59,255.48),[], 279),             
  ("village_104", "Pitinum Pisaurense",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.64,263.35),[], 13),             
  ("village_105", "Sarsina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.91,270.99),[], 270),             
  ("village_106", "Faventia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.51,282.83),[], 279),             
  ("village_107", "Fanum Fortunae",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.71,262.23),[], 161),             
# Ligures
  ("village_108", "Segeste",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.92,289.56),[], 267),             
  ("village_109", "Libarna",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.78,304.52),[], 237),             
  ("village_110", "Iria",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.01,320.22),[], 52),             
  ("village_111", "Clastidium",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.54,325.95),[], 48),             
  ("village_112", "Bodincomagus",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.88,330.5),[], 258),             
  ("village_113", "Eporedia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.48,344.77),[], 215),             
  ("village_114", "Hasta",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.68,326.28),[], 28),             
  ("village_115", "Vercellae",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.52,343.2),[], 190),             
  ("village_116", "Alba Ingaunum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.36,284.77),[], 28),             
# Boii
  ("village_117", "Modicia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.5,357.12),[], 155),             
  ("village_118", "Comum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.36,367.7),[], 200),             
  ("village_119", "Bergomum",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.62,366.24),[], 170),             
  ("village_120", "Placentia",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.2,329.24),[], 306),             
  ("village_121", "Parma",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.39,311.58),[], 346),             
  ("village_122", "Mutina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.63,302.58),[], 325),             
  ("village_123", "Minervium",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85,347.86),[], 223),             
  ("village_124", "Voberna",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.12,363.73),[], 27),             
  ("village_125", "Mantua",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.21,339.86),[], 258),             
  ("village_126", "Spina",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.41,299.84),[], 155),             
  ("village_127", "Bretina Belounon",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.81,361.84),[], 193),             
  ("village_128", "Cremona",  icon_celtic_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.13,328.59),[], 227),   

# Poleis_Eleutherai 
  ("village_129", "Phaleron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(336.51,-27.55),[], 122),             
  ("village_130", "Thorikos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(344.08,-33.88),[], 90),             
  ("village_131", "Marathon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(343.92,-16.32),[], 36),             
  ("village_132", "Acharnaí",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(336.17,-20.02),[], 260),             
  ("village_133", "Plataiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(320.09,-12),[], 305),             
  ("village_134", "Thespiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(312.29,-5.65),[], 281),             
  ("village_135", "Chairóneia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(308.69,0.42),[], 258),             
  ("village_136", "Tanagra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(330.91,-7.64),[], 55),             
  ("village_137", "Asine",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(309.65,-47.94),[], 21),             
  ("village_138", "Epidauros",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(318.44,-39.49),[], 127),             
  ("village_139", "Aigina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(327.92,-35.14),[], 73),             
  ("village_140", "Hermione",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(321.56,-56.35),[], 57),             
  ("village_141", "Pellana",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(291.84,-65.31),[], 237),             
  ("village_142", "Amyklai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(297.93,-74.27),[], 131),             
  ("village_143", "Geronthrai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(305.89,-78.6),[], 110),             
  ("village_144", "Gerenia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(287.72,-76.48),[], 14),             
  ("village_145", "Epidauros Limera",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(314.73,-89.6),[], 50),             
  ("village_146", "Helos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(301.76,-81.87),[], 63),             
  ("village_147", "Tainaron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(297.33,-103.05),[], 1),             
  ("village_148", "Palaia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(309.5,-84.13),[], 70),             
  ("village_149", "Methone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.46,-83.72),[], 332),             
  ("village_150", "Thouria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(284.64,-68.88),[], 67),             
  ("village_151", "Ampheia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(283.57,-61.23),[], 83),             

  ("village_152", "Praisos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(410.89,-165.6),[], 67),             
  ("village_153", "Lyktos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(387.34,-168.06),[], 121),             
  ("village_154", "Chersonasos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(391.78,-158.65),[], 149),             
  ("village_155", "Heraklion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(383.66,-156.88),[], 233),             
  ("village_156", "Kydonia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(346.08,-146.61),[], 196),             
  ("village_157", "Gortyna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(374.03,-167.84),[], 154),             
  ("village_158", "Eleutherna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(364.67,-155.58),[], 30),             
  ("village_159", "Kisamos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(339.57,-147.24),[], 308),             

  ("village_160", "Lindos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(462.69,-126.72),[], 55),             
  ("village_161", "Ialysos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(463.42,-110.26),[], 176),             
  ("village_162", "Amphissa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(292,2.31),[], 258),             
  ("village_163", "Antikyra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(302.14,-3.88),[], 306),             
  ("village_164", "Amphikleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(298.16,7.37),[], 340), 
# Koinon_Hellenon  
  ("village_165", "Lechaion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.59,-27.64),[], 143),             
  ("village_166", "Sikyón",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(303.75,-23.59),[], 248),             
  ("village_167", "Kleonai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(305.09,-29.88),[], 312),             
  ("village_168", "Kenchreai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(313.5,-28.97),[], 71),             
  ("village_169", "Eleusis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(330.28,-20.21),[], 25),             
  ("village_170", "Pagai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(319.08,-19.4),[], 252),             
  ("village_171", "Dyme",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(268.13,-17.1),[], 155),             
  ("village_172", "Zakynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(247.54,-35.1),[], 291),             
  ("village_173", "Krane",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(231.71,-14.27),[], 208),             
  ("village_174", "Kleitor",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(282.33,-29.02),[], 59),             
  ("village_175", "Heraia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280.38,-42.92),[], 65),             
  ("village_176", "Lykosoura",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(282.37,-53.05),[], 275),             
  ("village_177", "Lepreon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(271.85,-52.48),[], 133),             
  ("village_178", "Mantineia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(293.91,-44.11),[], 184),             
  ("village_179", "Hysiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300.95,-49.75),[], 215),             
  ("village_180", "Orchomenos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(292.27,-38.8),[], 132),  
# Makedonia  
  ("village_181", "Gortynia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(298.14,126.98),[], 227),             
  ("village_182", "Berroia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(286.78,100.74),[], 270),             
  ("village_183", "Methone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300.06,96.57),[], 73),             
  ("village_184", "Pydna",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(301.34,92.89),[], 150),             
  ("village_185", "Therme",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(313.88,99.93),[], 258),             
  ("village_186", "Olynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(324.9,88.6),[], 41),             
  ("village_187", "Akanthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(340.99,93.21),[], 84),             
  ("village_188", "Europos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(288.13,120.18),[], 122),             
  ("village_189", "Euboia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(286.67,113.83),[], 258),             
  ("village_190", "Aigeai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(291.96,97.21),[], 323),             
  ("village_191", "Arethousa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(334.24,106.12),[], 330),             
  ("village_192", "Myrkinos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(340.8,116.77),[], 170),             
  ("village_193", "Neapolis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(358.82,120.6),[], 27),             
  ("village_194", "Thasos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(369.63,117.64),[], 21),             
  ("village_195", "Stymbara",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(263.17,132.15),[], 239),             
  ("village_196", "Arnisa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(273.23,109.09),[], 221),             
  ("village_197", "Gonnoi",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(299.24,65.69),[], 151),             
  ("village_198", "Argoussa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(291.19,58.22),[], 311),             
  ("village_199", "Atrax",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(282.46,50.67),[], 246),             
  ("village_200", "Krannon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(287.96,48.27),[], 111),             
  ("village_201", "Skotoussa",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(297.66,42.73),[], 94),             
  ("village_202", "Kierion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(285.7,42.93),[], 269),             
  ("village_203", "Lamia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(295.04,22.27),[], 145),             
  ("village_204", "Herakleia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(294.88,15.21),[], 292),             
  ("village_205", "Histiai",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317.13,24.5),[], 244),             
  ("village_206", "Eretria",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(338.9,-3.78),[], 258),             
  ("village_207", "Amarynthos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(345.17,-3.66),[], 10),             
  ("village_208", "Karystos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(357.9,-23.35),[], 36),             
# Epeiros
  ("village_209", "Leucas",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(241.03,17.16),[], 189),             
  ("village_210", "Thyrreion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(248.87,19.31),[], 35),             
  ("village_211", "Kassope",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(242.17,30.14),[], 310),             
  ("village_212", "Orraon",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(252.18,33.21),[], 141),             
  ("village_213", "Ephyra",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.69,31.05),[], 258),             
  ("village_214", "Torone",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(225.91,48.97),[], 258),             
  ("village_215", "Photike",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230.34,47.16),[], 250),             
  ("village_216", "Passaron",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(245.07,58.57),[], 174),             
  ("village_217", "Onchesmos",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(219.57,63.95),[], 332),             
  ("village_218", "Chalkis",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(252.9,50.86),[], 153),             
  ("village_219", "Elina",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(235.59,35.37),[], 326),             
  ("village_220", "Bouthroton",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(220.77,58.92),[], 313),             
  ("village_221", "Omphalion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(232.28,68.59),[], 116),      
  ("village_222", "Antipatreia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(221.63,107.72),[], 101),   
  ("village_223", "Amantia",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(210.15,93.03),[], 43),     
  ("village_224", "Dimalion",  icon_greek_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.8,110.53),[], 17),      


  
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

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(70, 150),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(300, 50),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(265, -25),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-65, 250),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-69, 320),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(215, 125),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(23, 213),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(150, 95),[(trp_looter,15,0)]),
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
