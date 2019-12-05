from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed.
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,5,20),(trp_peasant_woman,0,8)]),

("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

# Ryan BEGIN
("looters","Eleutheroi",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,4,200)]),
# Ryan END
("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,20,120)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
("steppe_bandits","Sikel Rebels",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sp_sykeloi_hoplites,12,80)]),
("desert_bandits","Cretan Pirates",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sp_cretan_toxotes,10,30),(trp_sp_cretan_akontistes,10,30),(trp_sp_cretan_levy_hoplite,15,40),(trp_sp_cretan_hoplite,10,20),(trp_sp_cretan_hoplite_elite,5,10)]),
# RaW
("taiga_bandits","Apulian Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sp_apulian_eques,4,40),(trp_sp_apulian_ensifer,8,80)]),
("forest_bandits","Thracian Raiders",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_sp_thracian_warrior,4,30),(trp_sp_thraikos_peltastes,4,30),(trp_sp_thracian_falxman,2,20),(trp_sp_thracian_noble_falxman,1,10)]),
("sea_raiders","Illyrian Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,20,80),(trp_illyrian_toxotes,5,20),(trp_illyrian_akontistes,5,30),(trp_illyrian_hoplite,5,30)]),
("mountain_bandits","Transalpine Gauls",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_sp_celtic_atectos,10,60),(trp_sp_celtic_batoros,10,60),(trp_sp_celtic_gaisatos,5,20),(trp_sp_celtic_saitoros,4,30)]),

("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),

("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1)]),
("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,12,55)]),
("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,12,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1)]),
("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[]),

("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),

("reinforcements","Reinforcements",icon_axeman|pf_show_faction,0,fac_commoners,soldier_personality,[]),

# Reinforcements
# each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised

("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_roman_hastatus,5,10),(trp_sp_roman_hastatus_2,5,10),(trp_sp_roman_veles,2,8)]),
("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_roman_princeps,5,10),(trp_sp_roman_princeps_2,5,10),(trp_sp_roman_sagittarius,2,8)]),
("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_roman_eques,5,10),(trp_sp_roman_eques_2,2,8),(trp_sp_roman_triarius,2,8)]),
("kingdom_1_officers_template", "{!}kingdom_1_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_roman_centurio,1,2),(trp_sp_roman_vexillarius,1,2)]),

("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_greek_hoplitai_haploi,5,10),(trp_sp_greek_ekdromos,5,10),(trp_sp_greek_peltast,2,8)]),
("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_greek_hoplites,5,10),(trp_sp_greek_hoplites_epilektoi,5,10),(trp_sp_greek_toxotes,2,8)]),
("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_greek_hippakontistes,2,8),(trp_sp_greek_hippeus,5,10),(trp_sp_greek_sphendonetes,2,8)]),
("kingdom_2_officers_template", "{!}kingdom_2_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_greek_lochagos,1,2),(trp_sp_greek_semaphoros,1,2)]),

("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_celtic_atectos,5,10),(trp_sp_celtic_batoros,5,10),(trp_sp_celtic_gaisatos,5,10)]),
("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_celtic_kladioviros,2,8),(trp_sp_celtic_kingetos,2,8),(trp_sp_celtic_saitoros,2,8),(trp_sp_celtic_togiatos,2,8),(trp_sp_celtic_eporedos,2,8)]),
("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_celtic_rigeporedos,2,8),(trp_sp_celtic_solduros,5,10),(trp_sp_celtic_ambaktos,5,10),(trp_sp_celtic_argos,2,8),(trp_sp_celtic_talmori,2,8)]),
("kingdom_3_officers_template", "{!}kingdom_3_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_celtic_arios,1,2)]),

("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_sarissaphoros,5,10),(trp_sp_makedonian_deuteros,5,10),(trp_sp_makedonian_pezhetairos,5,10),(trp_sp_makedonian_toxotes,2,8)]),
("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_hypaspist,5,10),(trp_sp_makedonian_agema_hypaspist,2,8),(trp_sp_makedonian_basilikos_agema_hypaspist,1,5),(trp_sp_makedonian_akontistes,2,8),(trp_sp_makedonian_hippeis,2,8)]),
("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_argyraspides,5,10),(trp_sp_makedonian_hetairoi,2,8)]),
("kingdom_4_officers_template", "{!}kingdom_4_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_makedonian_lochagos,1,2),(trp_sp_makedonian_semaphoros,1,2)]),

("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_samnite_hastatus,5,10),(trp_sp_samnite_hastatus_2,5,10),(trp_sp_samnite_hastatus_3,2,8),(trp_sp_samnite_ensiferi,2,8)]),
("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_samnite_pedites,5,10),(trp_sp_samnite_pedites_2,5,10),(trp_sp_samnite_sagittarius,2,8)]),
("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_samnite_eques,5,10),(trp_sp_samnite_eques_2,2,8),(trp_sp_samnite_linteati,2,8)]),
("kingdom_5_officers_template", "{!}kingdom_5_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_samnite_verehia_minor,1,2),(trp_sp_samnite_verehia_maior,1,2),(trp_sp_samnite_vexillarius,1,2)]),

("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_levy_hoplite,5,10),(trp_sp_tarentine_hoplite,5,10),(trp_sp_tarentine_peltast,2,8)]),
("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_elite_hoplite,5,10),(trp_sp_tarentine_sphendonetes,2,8),(trp_sp_tarentine_toxotes,2,8),(trp_sp_tarentine_hippakontistes,5,10)]),
("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_horseman,5,10),(trp_sp_tarentine_leukaspides,2,8)]),
("kingdom_6_officers_template", "{!}kingdom_6_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_tarentine_hipparchos,1,2),(trp_sp_tarentine_semaphoros,1,2),(trp_sp_tarentine_lochagos,1,2)]),

("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_hoplite_levy,5,10),(trp_sp_syracusan_peltast,2,8),(trp_sp_syracusan_hippakontistes,2,8)]),
("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_hoplite,5,10),(trp_sp_syracusan_toxotes,2,8)]),
("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_horseman,2,8),(trp_sp_syracusan_hoplite_elite,5,10)]),
("kingdom_7_officers_template", "{!}kingdom_7_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_syracusan_semaphoros,1,2),(trp_sp_syracusan_lochagos,1,2)]),

("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_sarissaphoros,5,10),(trp_sp_epeiros_deuteros,5,10),(trp_sp_epeiros_pezhetairos,2,8),(trp_sp_epeiros_akontistes,2,8)]),
("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_pheraspides,5,10),(trp_sp_epeiros_politai_hoplitai,5,10),(trp_sp_epeiros_toxotes,2,8),(trp_sp_epeiros_hippeus,5,10)]),
("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_chalkaspides,2,8),(trp_sp_epeiros_xystophoros,2,8)]),
("kingdom_8_officers_template", "{!}kingdom_8_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_epeiros_lochagos,1,2),(trp_sp_epeiros_semaphoros,1,2)]),

("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_veiane,5,10),(trp_sp_etruscan_venzile,2,8),(trp_sp_etruscan_axunana,2,8),(trp_sp_etruscan_uphale_vipa,2,8)]),
("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_etera,5,10),(trp_sp_etruscan_huzrna,2,8),(trp_sp_etruscan_luvcatru,1,4),(trp_sp_etruscan_cutlis,2,8),(trp_sp_etruscan_sauturine,2,8)]),
("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_athumic,2,8),(trp_sp_etruscan_ultna_athumic,1,5),(trp_sp_etruscan_eprial_luvcatru,1,4),(trp_sp_etruscan_satna,2,8)]),
("kingdom_9_officers_template", "{!}kingdom_9_officers_template", 0, 0, fac_commoners, 0, [(trp_sp_etruscan_velthinei,1,2)]),

#####################################
("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,25)]),
("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),

("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,25)]),

("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

##diplomacy begin
("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
##diplomacy end
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
