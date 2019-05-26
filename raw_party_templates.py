from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

party_templates = [

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### RAW AoR TEMPLATES ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

("campanian_reinforcements_a", "{!}campanian_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_campanian_leves,5,10),(trp_sp_campanian_ensiferi,10,20)]),
("campanian_reinforcements_b", "{!}campanian_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_campanian_pedites,5,10),(trp_sp_campanian_sagittarius,2,8),(trp_sp_campanian_cavalry,5,10)]),
("campanian_reinforcements_c", "{!}campanian_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_campanian_elite_cavalry,2,8),(trp_sp_campanian_pedites_extraordinarius,5,10)]),
("campanian_officers_template", "{!}kingdom_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_campanian_centurio,1,2)]),

("legio_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_legio_1_hastatus,5,10),(trp_sp_legio_1_hastatus_2,5,10),(trp_sp_roman_veles,2,8)]),
("legio_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_legio_1_princeps,5,10),(trp_sp_legio_1_princeps_2,5,10),(trp_sp_roman_sagittarius,2,8)]),
("legio_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_roman_eques,2,8),(trp_sp_roman_eques_2,2,8),(trp_sp_legio_1_triarius,2,8)]),
("legio_1_officers_template", "{!}legio_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_roman_centurio,1,2),(trp_sp_roman_vexillarius_legio_1,1,2)]),

("legio_2_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_legio_2_hastatus,5,10),(trp_sp_legio_2_hastatus_2,5,10),(trp_sp_roman_veles,2,8)]),
("legio_2_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_legio_2_princeps,5,10),(trp_sp_legio_2_princeps_2,5,10),(trp_sp_roman_sagittarius,2,8)]),
("legio_2_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_roman_eques,2,8),(trp_sp_roman_eques_2,2,8),(trp_sp_legio_2_triarius,2,8)]),
("legio_2_officers_template", "{!}legio_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_roman_centurio,1,2),(trp_sp_roman_vexillarius_legio_2,1,2)]),

("legio_3_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_legio_3_hastatus,5,10),(trp_sp_legio_3_hastatus_2,5,10),(trp_sp_roman_veles,2,8)]),
("legio_3_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_legio_3_princeps,5,10),(trp_sp_legio_3_princeps_2,5,10),(trp_sp_roman_sagittarius,2,8)]),
("legio_3_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_roman_eques,2,8),(trp_sp_roman_eques_2,2,8),(trp_sp_legio_3_triarius,2,8)]),
("legio_3_officers_template", "{!}legio_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_roman_centurio,1,2),(trp_sp_roman_vexillarius_legio_3,1,2)]),

("legio_4_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_legio_4_hastatus,5,10),(trp_sp_legio_4_hastatus_2,5,10),(trp_sp_roman_veles,2,8)]),
("legio_4_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_legio_4_princeps,5,10),(trp_sp_legio_4_princeps_2,5,10),(trp_sp_roman_sagittarius,2,8)]),
("legio_4_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_roman_eques,2,8),(trp_sp_roman_eques_2,2,8),(trp_sp_legio_4_triarius,2,8)]),
("legio_4_officers_template", "{!}legio_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_roman_centurio,1,2),(trp_sp_roman_vexillarius_legio_4,1,2)]),

### Greek Army Reinforcements
# Athenians
("athens_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_athenian_hoplite_levy,5,10),(trp_sp_athenian_marine,5,10),(trp_sp_greek_peltast,2,8)]),
("athens_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_athenian_hoplite,5,10),(trp_sp_greek_toxotes,2,8)]),
("athens_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_athenian_hoplite_elite,5,10),(trp_sp_athenaikos_hippakontistes,5,10)]),

# Boeotians
("thebes_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_boeotian_citizen_hoplite,10,20),(trp_sp_boeotian_skirmisher,2,8)]),
("thebes_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_boeotian_hoplite,5,10),(trp_sp_boeotian_skirmisher,2,8)]),
("thebes_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_boeotian_horseman,5,10),(trp_sp_boeotian_elite_hoplite,2,8)]),
("thebes_officers", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_boeotian_officer,1,2)]),

# Spartans
("sparta_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_ekdromos,5,10),(trp_sp_perioikos_skirmisher,2,8),(trp_sp_perioikos_hoplite,5,10)]),
("sparta_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_hoplite,5,10),(trp_sp_skiritan_machairophoros,2,8),(trp_sp_spartan_amyklai_hoplite,1,4),(trp_sp_spartan_geronthrai_hoplite,1,4)]),
("sparta_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_horseman,2,8),(trp_sp_spartan_elite_hoplite,2,8)]),
("sparta_officers", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_officer,1,2)]),

("pellana_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_skirmisher,2,8),(trp_sp_skiritan_machairophoros,10,20)]),
("pellana_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_hoplite,10,20)]),
("pellana_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_horseman,5,10)]),

("amyklai_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_skirmisher,2,8),(trp_sp_spartan_ekdromos,10,20)]),
("amyklai_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_amyklai_hoplite,10,20)]),
("amyklai_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_horseman,5,10)]),

("geronthrai_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_skirmisher,2,8),(trp_sp_spartan_ekdromos,10,20)]),
("geronthrai_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_geronthrai_hoplite,10,20)]),
("geronthrai_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_elite_hoplite,5,10)]),

("sparta_reinforcements_d", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_ekdromos,10,20),(trp_sp_perioikos_skirmisher,5,8)]),
("sparta_reinforcements_e", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_hoplite,5,10),(trp_sp_perioikos_hoplite,5,10)]),
("sparta_reinforcements_f", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_horseman,2,8),(trp_sp_spartan_elite_hoplite,2,8)]),

# Cretans
("crete_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_cretan_levy_hoplite,10,20),(trp_sp_cretan_akontistes,2,8)]),
("crete_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_cretan_hoplite,10,15),(trp_sp_cretan_toxotes,2,8)]),
("crete_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_cretan_hoplite_elite,5,10),(trp_sp_cretan_toxotes,2,8)]),

# Corinthians
("corinth_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_corinthian_levy_hoplite,10,20),(trp_sp_greek_peltast,2,8)]),
("corinth_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_corinthian_hoplite,10,15),(trp_sp_greek_toxotes,2,8)]),
("corinth_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_corinthian_hoplite_elite,5,10),(trp_sp_greek_hippeus,2,8),(trp_sp_greek_sphendonetes,2,8)]),

# Sykels
("sykel_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_sykeloi_hoplites,5,10),(trp_sp_syracusan_toxotes,2,8)]),

### Thessalian Reinforcements
("thessalian_reinforcements_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_hoplite_levy,5,10),(trp_sp_thessalian_akontistes,2,8),(trp_sp_thessalian_hippeis,2,8)]),
("thessalian_reinforcements_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_hoplite,5,10),(trp_sp_thessalian_hippeis,2,8),(trp_sp_thessalian_toxotes,2,8)]),
("thessalian_reinforcements_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_xystophoros,2,8),(trp_sp_thessalian_hoplite_elite,2,8)]),
("thessalian_officers", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_lochagos,1,2),(trp_sp_thessalian_semaphoros,1,2)]),

# ("thracian_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_sarissaphoros,5,10),(trp_sp_makedonian_deuteros,5,10),(trp_sp_makedonian_pezhetairos,5,10),(trp_sp_makedonian_toxotes,2,8)]),
("thracian_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_hypaspist,5,10),(trp_sp_makedonian_agema_hypaspist,2,8),(trp_sp_makedonian_basilikos_agema_hypaspist,1,5),(trp_sp_thraikos_peltastes,2,8),(trp_sp_makedonian_hippeis,2,8)]),
# ("thracian_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_argyraspides,5,10),(trp_sp_makedonian_hetairoi,2,8)]),

("agrianian_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_hypaspist,5,10),(trp_sp_makedonian_agema_hypaspist,2,8),(trp_sp_makedonian_basilikos_agema_hypaspist,1,5),(trp_sp_thraikos_peltastes,2,8),(trp_sp_makedonian_hippeis,2,8)]),

### Illyrian Reinforcements
("illyrian_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_illyrian_paraktios,10,20),(trp_sp_illyrian_peltast,2,8)]),
("illyrian_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_illyrian_doryphoros,10,15),(trp_sp_illyrian_toxotes,2,8)]),
("illyrian_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_illyrian_hoplite,5,10),(trp_sp_illyrian_hippakontistes,2,8)]),
("illyrian_officers", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_illyrian_lochagos,1,2)]),

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### RAW CUSTOM ARMIES ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

########## Rome
("kingdom_1_lord_reinforcements", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_campanian_elite_cavalry,1,4),(trp_sp_roman_eques_2,1,4),(trp_sp_roman_princeps,5,10),(trp_sp_roman_princeps_2,5,10),(trp_sp_roman_triarius,1,4),(trp_sp_roman_veles,2,8)]),

("legio_1_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_1_hastatus,5,10),(trp_sp_legio_1_hastatus_2,5,10),(trp_sp_roman_eques_2,1,4),(trp_sp_roman_veles,2,8)]),
("legio_1_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_1_princeps,5,10),(trp_sp_legio_1_princeps,5,10),(trp_sp_roman_veles,2,8),(trp_sp_roman_eques,1,4)]),
("legio_1_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_roman_sagittarius,2,8),(trp_sp_legio_1_hastatus,5,10),(trp_sp_legio_1_hastatus_2,5,10),(trp_sp_legio_1_triarius,2,8)]),

("legio_2_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_2_hastatus,5,10),(trp_sp_legio_2_hastatus_2,5,10),(trp_sp_roman_eques_2,1,4),(trp_sp_roman_veles,2,8)]),
("legio_2_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_2_princeps,5,10),(trp_sp_legio_2_princeps,5,10),(trp_sp_roman_veles,2,8),(trp_sp_roman_eques,1,4)]),
("legio_2_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_roman_sagittarius,2,8),(trp_sp_legio_2_hastatus,5,10),(trp_sp_legio_2_hastatus_2,5,10),(trp_sp_legio_2_triarius,2,8)]),

("legio_3_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_3_hastatus,5,10),(trp_sp_legio_3_hastatus_2,5,10),(trp_sp_roman_eques_2,1,4),(trp_sp_roman_veles,2,8)]),
("legio_3_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_3_princeps,5,10),(trp_sp_legio_3_princeps,5,10),(trp_sp_roman_veles,2,8),(trp_sp_roman_eques,1,4)]),
("legio_3_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_roman_sagittarius,2,8),(trp_sp_legio_3_hastatus,5,10),(trp_sp_legio_3_hastatus_2,5,10),(trp_sp_legio_3_triarius,2,8)]),

("legio_4_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_4_hastatus,5,10),(trp_sp_legio_4_hastatus_2,5,10),(trp_sp_roman_eques_2,1,4),(trp_sp_roman_veles,2,8)]),
("legio_4_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_legio_4_princeps,5,10),(trp_sp_legio_4_princeps,5,10),(trp_sp_roman_veles,2,8),(trp_sp_roman_eques,1,4)]),
("legio_4_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_roman_sagittarius,2,8),(trp_sp_legio_4_hastatus,5,10),(trp_sp_legio_4_hastatus_2,5,10),(trp_sp_legio_4_triarius,2,8)]),

("campanian_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_campanian_ensiferi,10,20),(trp_sp_campanian_leves,2,8),(trp_sp_campanian_elite_cavalry,2,8)]),
("campanian_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_campanian_pedites,5,10),(trp_sp_campanian_pedites_extraordinarius,5,10),(trp_sp_campanian_sagittarius,2,8),(trp_sp_campanian_cavalry,1,4)]),	

########## Samnites
("samnite_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_samnite_linteati,5,10),(trp_sp_samnite_pedites,5,10),(trp_sp_samnite_pedites_2,5,10),(trp_sp_samnite_ensiferi,2,8),(trp_sp_samnite_eques_2,1,4)]),

("generic_samnite_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_samnite_hastatus,2,8),(trp_sp_samnite_hastatus_2,5,10),(trp_sp_samnite_hastatus_3,2,8),(trp_sp_samnite_ensiferi,2,8),(trp_sp_samnite_eques_2,1,4)]),
("generic_samnite_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_samnite_pedites,5,10),(trp_sp_samnite_pedites_2,5,10),(trp_sp_samnite_sagittarius,2,8),(trp_sp_samnite_eques,1,4)]),
("generic_samnite_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_samnite_linteati,2,8),(trp_sp_samnite_hastatus_2,5,10),(trp_sp_samnite_hastatus_3,2,8),(trp_sp_samnite_ensiferi,2,8),(trp_sp_samnite_eques,1,4)]),

########## Tarentines
("tarantine_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_ekdromos,5,10),(trp_sp_spartan_hoplite,5,10),(trp_sp_spartan_elite_hoplite,2,8),(trp_sp_tarentine_hippakontistes,5,10),(trp_sp_tarentine_horseman,2,8),]),
("tarantine_king_officers", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_officer,1,2),(trp_sp_tarentine_semaphoros,1,2),(trp_sp_tarentine_hipparchos,1,2),]),

("tarantine_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_levy_hoplite,5,10),(trp_sp_tarentine_hoplite,5,10),(trp_sp_tarentine_horseman,2,8),(trp_sp_tarentine_hippakontistes,5,10),(trp_sp_tarentine_peltast,2,8)]),
("tarantine_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_hoplite,5,10),(trp_sp_tarentine_elite_hoplite,5,10),(trp_sp_tarentine_hippakontistes,5,10),(trp_sp_tarentine_sphendonetes,2,8)]),
("tarantine_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_levy_hoplite,5,10),(trp_sp_tarentine_hoplite,5,10),(trp_sp_tarentine_leukaspides,2,8),(trp_sp_tarentine_hippakontistes,5,10),(trp_sp_tarentine_toxotes,2,8)]),

########## Syracusans
("syracusan_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_sykeloi_hoplites,2,8),(trp_sp_syracusan_hoplite_elite,2,8),(trp_sp_syracusan_horseman,2,8),(trp_sp_cretan_toxotes_syracuse,2,8),(trp_sp_etruscan_hoplites,2,8),(trp_sp_celtic_kladioviros,2,8)]),

("syracusan_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_hoplite_levy,5,10),(trp_sp_syracusan_hippakontistes,5,10),(trp_sp_syracusan_peltast,2,8),(trp_sp_syracusan_hoplite,5,10)]),
("syracusan_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_hoplite,5,10),(trp_sp_syracusan_toxotes,2,8),(trp_sp_syracusan_horseman,2,8),(trp_sp_syracusan_hoplite_levy,5,10)]),
("syracusan_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_hoplite_elite,2,8),(trp_sp_syracusan_toxotes,2,8),(trp_sp_syracusan_hoplite,5,10),(trp_sp_syracusan_hoplite_levy,5,10)]),

("sykel_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_sykeloi_hoplites,10,20),(trp_sp_syracusan_hippakontistes,2,8),(trp_sp_syracusan_peltast,2,8)]),

("etruscan_mercenary_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_hoplites,10,20),(trp_sp_etruscan_cutlis,2,8),(trp_sp_etruscan_uphale_vipa,2,8)]),

############ Etruscans
("etruscan_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_huzrna,5,10),(trp_sp_etruscan_athumic,2,8),(trp_sp_etruscan_ultna_athumic,1,4),(trp_sp_etruscan_satna,2,8),(trp_sp_etruscan_uphale_vipa,2,8),(trp_sp_etruscan_eprial_luvcatru,1,4)]),

("etruscan_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_venzile,5,10),(trp_sp_etruscan_veiane,5,10),(trp_sp_etruscan_uphale_vipa,2,8),(trp_sp_etruscan_satna,2,8),(trp_sp_etruscan_eprial_luvcatru,1,4)]),
("etruscan_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_axunana,5,10),(trp_sp_etruscan_huzrna,5,10),(trp_sp_etruscan_sauturine,2,8),(trp_sp_etruscan_cutlis,2,8)]),
("etruscan_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_venzile,5,10),(trp_sp_etruscan_athumic,2,8),(trp_sp_etruscan_uphale_vipa,2,8),(trp_sp_etruscan_luvcatru,1,4)]),

########## Celts
("generic_celt_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_celtic_solduros,1,4),(trp_sp_celtic_ambaktos,5,10),(trp_sp_celtic_argos,1,4),(trp_sp_celtic_gaisatos,2,8),(trp_sp_celtic_rigeporedos,5,10)]),

("generic_celt_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_celtic_kingetos,5,10),(trp_sp_celtic_gaisatos,2,8),(trp_sp_celtic_argos,1,4),(trp_sp_celtic_ambaktos,2,8),(trp_sp_celtic_eporedos,2,8)] ),
("generic_celt_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_celtic_batoros,5,10),(trp_sp_celtic_saitoros,2,8),(trp_sp_celtic_kladioviros,2,8),(trp_sp_celtic_solduros,2,8),(trp_sp_celtic_gaisaredos,2,8)]),
("generic_celt_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_celtic_kingetos,5,10),(trp_sp_celtic_gaisatos,2,8),(trp_sp_celtic_ambaktos,2,8),(trp_sp_celtic_rigeporedos,2,8),(trp_sp_celtic_argos,1,4)] ),

########## Greece
("athenai_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_athenian_hoplite,5,10),(trp_sp_athenian_marine,2,8),(trp_sp_athenaikos_hippakontistes,5,10),(trp_sp_athenian_hoplite_elite,5,10)]),
("kretai_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_cretan_hoplite,10,15),(trp_sp_cretan_akontistes,2,8),(trp_sp_cretan_toxotes,5,10)]),
("korinthioi_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_corinthian_hoplite,10,20),(trp_sp_greek_peltast,2,8),(trp_sp_greek_hippakontistes,2,8)]),

("generic_greek_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_greek_hippeus,2,8),(trp_sp_greek_ekdromos,5,10),(trp_sp_greek_hoplites,5,10),(trp_sp_greek_sphendonetes,2,8)]),
("generic_greek_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_greek_hoplitai_haploi,5,10),(trp_sp_greek_peltast,5,10),(trp_sp_greek_hoplites_epilektoi,2,8),(trp_sp_greek_hippakontistes,2,8)] ),
("generic_greek_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_greek_hoplitai_haploi,5,10),(trp_sp_greek_hoplites,5,10),(trp_sp_greek_toxotes,2,8),(trp_sp_greek_hippeus,2,8)] ),

("spartan_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_perioikos_horseman,2,8),(trp_sp_spartan_ekdromos,5,10),(trp_sp_spartan_hoplite,5,10),(trp_sp_perioikos_skirmisher,2,8)]),
("spartan_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_ekdromos,5,10),(trp_sp_spartan_hoplite,5,10),(trp_sp_spartan_elite_hoplite,2,8),(trp_sp_perioikos_horseman,2,8)] ),
("spartan_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_spartan_ekdromos,5,10),(trp_sp_spartan_elite_hoplite,5,10),(trp_sp_perioikos_skirmisher,2,8),(trp_sp_perioikos_horseman,2,8)] ),

########## Macedon
("mak_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_basilikos_agema_hypaspist,2,8),(trp_sp_makedonian_hypaspist,5,10),(trp_sp_makedonian_agema_hypaspist,2,8),(trp_sp_agrianos_pelekephoros,2,8),(trp_sp_makedonian_hetairoi,5,10)]),

 ("generic_thessalian_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_hoplite_levy,5,10),(trp_sp_thessalian_akontistes,2,8),(trp_sp_thessalian_xystophoros,2,8),(trp_sp_thessalian_hoplite,5,10)] ),
 ("generic_thessalian_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_hoplite,5,10),(trp_sp_thessalian_toxotes,2,8),(trp_sp_thessalian_hoplite_elite,2,8),(trp_sp_thessalian_hippeis,2,8)] ),
 ("generic_thessalian_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_thessalian_hoplite_levy,2,8),(trp_sp_thessalian_akontistes,2,8),(trp_sp_thessalian_hoplite,5,10),(trp_sp_thessalian_hoplite_elite,2,8)] ),

("generic_thraikan_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_symmachos_hoplites,5,10),(trp_sp_thraikos_peltastes,2,8),(trp_sp_makedonian_hippeis,2,8)]),
("generic_agrianian_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_symmachos_hoplites,5,10),(trp_sp_agrianos_pelekephoros,2,8),(trp_sp_makedonian_hippeis,2,8)]),

 ("generic_mak_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_sarissaphoros,5,10),(trp_sp_makedonian_akontistes,2,8),(trp_sp_makedonian_hetairoi,2,8),(trp_sp_makedonian_deuteros,5,10),(trp_sp_makedonian_pezhetairos,2,8)] ),
 ("generic_mak_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_hypaspist,5,10),(trp_sp_makedonian_toxotes,2,8),(trp_sp_makedonian_agema_hypaspist,5,10),(trp_sp_makedonian_basilikos_agema_hypaspist,1,4)] ),
 ("generic_mak_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_argyraspides,5,10),(trp_sp_makedonian_akontistes,2,8),(trp_sp_makedonian_hippeis,2,8),(trp_sp_makedonian_agema_argyraspides,1,4)] ),

############ Epirotes
("epirote_king_army", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_chalkaspides,2,8),(trp_sp_epeiros_pezhetairos,5,10),(trp_sp_epeiros_xystophoros,2,8),(trp_sp_agrianos_pelekephoros,2,8)]), 

("epirote_army_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_sarissaphoros,5,10),(trp_sp_epeiros_deuteros,5,10),(trp_sp_epeiros_pezhetairos,2,8),(trp_sp_epeiros_hippeus,2,8),(trp_sp_epeiros_akontistes,2,8)]),
("epirote_army_b", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_pheraspides,5,10),(trp_sp_epeiros_politai_hoplitai,5,10),(trp_sp_epeiros_toxotes,2,8),(trp_sp_epeiros_xystophoros,2,8),]),
("epirote_army_c", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_chalkaspides,2,8),(trp_sp_epeiros_deuteros,5,10),(trp_sp_epeiros_pezhetairos,2,8),(trp_sp_epeiros_akontistes,2,8)]),

("illyrian_auxiliary_a", "{!}special_reinforcements", 0, 0, fac_commoners, 0, [(trp_sp_illyrian_paraktios,28,10),(trp_sp_illyrian_hoplite,5,15),(trp_sp_epeiros_hippeus,2,8),(trp_sp_epeiros_akontistes,2,8)]),



]