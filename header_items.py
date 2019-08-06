###################################################
# header items.py
# This file contains declarations for items
# DO NOT EDIT THIS FILE!
###################################################



from header_common import *
from header_item_modifiers import *

#item flags
itp_type_horse           = 0x0000000000000001
itp_type_one_handed_wpn  = 0x0000000000000002
itp_type_two_handed_wpn  = 0x0000000000000003
itp_type_polearm         = 0x0000000000000004
itp_type_arrows          = 0x0000000000000005
itp_type_bolts           = 0x0000000000000006
itp_type_shield          = 0x0000000000000007
itp_type_bow             = 0x0000000000000008
itp_type_crossbow        = 0x0000000000000009
itp_type_thrown          = 0x000000000000000a
itp_type_goods           = 0x000000000000000b
itp_type_head_armor      = 0x000000000000000c
itp_type_body_armor      = 0x000000000000000d
itp_type_foot_armor      = 0x000000000000000e
itp_type_hand_armor      = 0x000000000000000f
itp_type_pistol          = 0x0000000000000010
itp_type_musket          = 0x0000000000000011
itp_type_bullets         = 0x0000000000000012
itp_type_animal          = 0x0000000000000013
itp_type_book            = 0x0000000000000014

##itp_attach_left_item     = 0x000000100
##itp_attach_left_hand     = 0x000000200
##itp_attach_forearm       = 0x000000300
##itp_attach_armature      = 0x000000f00

itp_force_attach_left_hand      = 0x0000000000000100
itp_force_attach_right_hand     = 0x0000000000000200
itp_force_attach_left_forearm   = 0x0000000000000300
itp_attach_armature             = 0x0000000000000f00
itp_attachment_mask             = 0x0000000000000f00

itp_unique               = 0x0000000000001000
itp_always_loot          = 0x0000000000002000
##itp_melee                = 0x000002000
itp_no_parry             = 0x0000000000004000
##itp_spear                = 0x000008000 #obsolete
itp_default_ammo         = 0x0000000000008000
itp_merchandise          = 0x0000000000010000
itp_wooden_attack        = 0x0000000000020000
itp_wooden_parry         = 0x0000000000040000
itp_food                 = 0x0000000000080000
#itp_bow                  = 0x0000000000000010
#itp_shield               = 0x0000000000000020
#itp_javelin              = 0x0000000000000040
#itp_crossbow             = 0x0000000000000080

itp_cant_reload_on_horseback = 0x0000000000100000
itp_two_handed               = 0x0000000000200000
itp_primary                  = 0x0000000000400000 # for weapons
itp_replaces_helm            = 0x0000000000400000 # for armor, allows body armor items which include helmet
itp_secondary                = 0x0000000000800000 # for weapons
itp_replaces_shoes           = 0x0000000000800000 # for armor, allows body armor items which include boots
itp_covers_legs              = 0x0000000001000000
itp_doesnt_cover_hair        = 0x0000000001000000
itp_can_penetrate_shield     = 0x0000000001000000
itp_consumable               = 0x0000000002000000
itp_bonus_against_shield     = 0x0000000004000000
itp_penalty_with_shield      = 0x0000000008000000
itp_cant_use_on_horseback    = 0x0000000010000000
itp_civilian                 = 0x0000000020000000
itp_next_item_as_melee       = 0x0000000020000000
itp_fit_to_head              = 0x0000000040000000
itp_offset_lance             = 0x0000000040000000
itp_covers_head              = 0x0000000080000000
itp_couchable                = 0x0000000080000000
itp_crush_through            = 0x0000000100000000
#itp_knock_back               = 0x0000000200000000 being used?
itp_remove_item_on_use       = 0x0000000400000000
itp_unbalanced               = 0x0000000800000000

itp_covers_beard             = 0x0000001000000000    #remove beard mesh
itp_no_pick_up_from_ground   = 0x0000002000000000
itp_can_knock_down           = 0x0000004000000000
itp_covers_hair              = 0x0000008000000000    #remove hair mesh for armors only

itp_force_show_body          = 0x0000010000000000 # forces showing body (works on body armor items)
itp_force_show_left_hand     = 0x0000020000000000 # forces showing left hand (works on hand armor items)
itp_force_show_right_hand    = 0x0000040000000000 # forces showing right hand (works on hand armor items)
itp_covers_hair_partially    = 0x0000080000000000

itp_extra_penetration        = 0x0000100000000000
itp_has_bayonet              = 0x0000200000000000
itp_cant_reload_while_moving = 0x0000400000000000
itp_ignore_gravity           = 0x0000800000000000
itp_ignore_friction          = 0x0001000000000000
itp_is_pike                  = 0x0002000000000000
itp_offset_musket            = 0x0004000000000000
itp_no_blur                  = 0x0008000000000000

itp_cant_reload_while_moving_mounted = 0x0010000000000000
itp_has_upper_stab           = 0x0020000000000000
itp_disable_agent_sounds     = 0x0040000000000000 #disable agent related sounds, but not voices. useful for animals
itp_kill_info_mask           = 0x0700000000000000
itp_kill_info_bits           = 56 # 0x0700000000000000


#equipment slots
ek_item_0 = 0
ek_item_1 = 1
ek_item_2 = 2
ek_item_3 = 3
ek_head   = 4
ek_body   = 5
ek_foot   = 6
ek_gloves = 7
ek_horse  = 8
ek_food   = 9

##diplomacy start+
dplmc_ek_alt_item_a = 10
dplmc_ek_alt_item_b = 11
dplmc_ek_alt_item_c = 12
dplmc_ek_alt_item_d = 13

dplmc_ek_alt_items_begin = dplmc_ek_alt_item_a
dplmc_ek_alt_items_end   = dplmc_ek_alt_item_d + 1
##diplomacy end+

max_inventory_items = 96
num_equipment_kinds = ek_food + 1
num_weapon_proficiencies = 7

#damage types:
cut    = 0
pierce = 1
blunt  = 2



#ibf_head_armor_bits      = 0
#ibf_body_armor_bits      = 8
#ibf_leg_armor_bits       = 16
#ibf_weight_bits          = 24
#ibf_difficulty_bits      = 32
#ibf_hitpoints_bits       = 40
#iwf_swing_damage_bits       = 50
#iwf_swing_damage_type_bits  = 58
#iwf_thrust_damage_bits      = 60
#iwf_thrust_damage_type_bits = 68
#iwf_weapon_length_bits      = 70
#iwf_speed_rating_bits       = 80
#iwf_shoot_speed_bits        = 90
#iwf_max_ammo_bits           = 100 # use this for shield endurance too?
#iwf_abundance_bits          = 110
#iwf_accuracy_bits           = 16  #reuse leg_armor for accuracy  
#iwf_damage_type_bits = 8

#ibf_armor_mask           = 0xff
#ibf_damage_mask          = 0x3ff
#ibf_10bit_mask           = 0x3ff
#ibf_hitpoints_mask       = 0xffff

ibf_2bit_mask  = 0x0003
ibf_8bit_mask  = 0x00ff
ibf_10bit_mask = 0x03ff
ibf_12bit_mask = 0x0fff
ibf_16bit_mask = 0xffff

ibf_armor_mask           = ibf_8bit_mask
ibf_damage_mask          = ibf_10bit_mask
ibf_damage_type_mask     = ibf_2bit_mask
ibf_hitpoints_mask       = ibf_16bit_mask

# PREVIOUS MASKS:

#                 1 1 1
#                 2 1 0 9 8 8 7 6 5 4 4 3 2 1
#                 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0

# head_armor : 0x000000000000000000000000000000ff
# body_armor : 0x0000000000000000000000000000ff00
# leg_armor  : 0x00000000000000000000000000ff0000
# weight     : 0x000000000000000000000000ff000000
# difficulty : 0x0000000000000000000000ff00000000
# hit_points : 0x000000000000000000ffff0000000000
# swing_dmg  : 0x000000000000000003fc000000000000
# swing_type : 0x00000000000000000c00000000000000
# thrust_dmg : 0x000000000000000ff000000000000000
# thrust_type: 0x00000000000000300000000000000000
# length     : 0x000000000000ffc00000000000000000
# speed      : 0x0000000000ff00000000000000000000
# shoot_speed: 0x0000000ffc0000000000000000000000
# max_ammo   : 0x00000ff0000000000000000000000000
# abundance  : 0x003fc000000000000000000000000000

# IMPROVED MASKS:

#                 1 1 1 1 1
#                 3 2 2 1 0 9 8 8 7 6 5 4 4 3 2 1
#                 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0

# head_armor : 0x0000000000000000000000000000000000ff
# body_armor : 0x00000000000000000000000000000000ff00
# leg_armor  : 0x000000000000000000000000000000ff0000
# weight     : 0x00000000000000000000000000ffff000000
# difficulty : 0x000000000000000000000000ff0000000000
# hit_points : 0x00000000000000000000ffff000000000000
# swing_comb : 0x00000000000000000fff0000000000000000
# thrust_comb: 0x00000000000000fff0000000000000000000
# length     : 0x00000000000fff0000000000000000000000
# speed      : 0x000000000ff0000000000000000000000000
# shoot_speed: 0x000000fff000000000000000000000000000
# max_ammo   : 0x00ffff000000000000000000000000000000
# abundance  : 0xff0000000000000000000000000000000000

ibf_head_armor_bits      = 0
ibf_body_armor_bits      = 8
ibf_leg_armor_bits       = 16
ibf_weight_bits          = 24
ibf_difficulty_bits      = 40
ibf_hitpoints_bits       = 48
iwf_swing_damage_bits    = 64
iwf_thrust_damage_bits   = 76
iwf_weapon_length_bits   = 88
iwf_speed_rating_bits    = 100
iwf_shoot_speed_bits     = 108
iwf_max_ammo_bits        = 120
iwf_abundance_bits       = 136

iwf_damage_type_bits = 8


def weight(x):
  a = int(100.0 * x + 0.5)
  a = ibf_16bit_mask & a
  return (((bignum | a) & ibf_16bit_mask) << ibf_weight_bits)
  
def get_weight(y):
  a = (y >> ibf_weight_bits) & ibf_16bit_mask
  return a / 100.0

def head_armor(x):
  return (((bignum | x) & ibf_armor_mask) << ibf_head_armor_bits)

def get_head_armor(y):
  return (y >> ibf_head_armor_bits) & ibf_armor_mask

def body_armor(x):
  return (((bignum | x) & ibf_armor_mask) << ibf_body_armor_bits)

def get_body_armor(y):
  return (y >> ibf_body_armor_bits) & ibf_armor_mask

def leg_armor(x):
  return (((bignum | x) & ibf_armor_mask) << ibf_leg_armor_bits)

def get_leg_armor(y):
  return (y >> ibf_leg_armor_bits) & ibf_armor_mask

def difficulty(x):
  return (((bignum | x) & ibf_armor_mask) << ibf_difficulty_bits)

def get_difficulty(y):
  return (y >> ibf_difficulty_bits) & ibf_armor_mask

def hit_points(x):
  return (((bignum | x) & ibf_hitpoints_mask) << ibf_hitpoints_bits)

def get_hit_points(y):
  return (y >> ibf_hitpoints_bits) & ibf_hitpoints_mask

def spd_rtng(x):
  return (((bignum | x) & ibf_armor_mask) << iwf_speed_rating_bits)

def get_speed_rating(y):
  return (y >> iwf_speed_rating_bits) & ibf_armor_mask

def shoot_speed(x):
  return (((bignum | x) & ibf_12bit_mask) << iwf_shoot_speed_bits)

def get_missile_speed(y):
  return (y >> iwf_shoot_speed_bits) & ibf_12bit_mask

def weapon_length(x):
  return (((bignum | x) & ibf_12bit_mask) << iwf_weapon_length_bits)

def horse_scale(x):
  return weapon_length(x)

def shield_width(x):
  return weapon_length(x)
 
def shield_height(x):
  return shoot_speed(x)
 
def get_weapon_length(y):
  return ((y >> iwf_weapon_length_bits) & ibf_12bit_mask)

def max_ammo(x):
  return (((bignum | x) & ibf_16bit_mask) << iwf_max_ammo_bits)

def get_max_ammo(y):
  return (y >> iwf_max_ammo_bits) & ibf_16bit_mask

def swing_damage(damage,damage_type):
  x = ((damage_type << iwf_damage_type_bits) | (damage & ibf_armor_mask))
  return (((bignum | x) & ibf_damage_mask) << iwf_swing_damage_bits)

def get_swing_damage(y):
  return (y >> iwf_swing_damage_bits) & ibf_damage_mask

def thrust_damage(damage,damage_type):
  x = ((damage_type << iwf_damage_type_bits) | (damage & ibf_armor_mask))
  return (((bignum | x) & ibf_damage_mask) << iwf_thrust_damage_bits)

def get_thrust_damage(y):
  return (y >> iwf_thrust_damage_bits) & ibf_damage_mask

def horse_speed(x):
  return shoot_speed(x)

def horse_maneuver(x):
  return spd_rtng(x)

def horse_charge(x):
  return thrust_damage(x, blunt)

def food_quality(x):
  return head_armor(x)

def abundance(x):
  return (((bignum | x) & ibf_armor_mask) << iwf_abundance_bits)

def get_abundance(y):
  abnd = (y >> iwf_abundance_bits) & ibf_armor_mask
  if (abnd == 0):
    abnd = 100
  return abnd

def accuracy(x):
  return leg_armor(x)

def custom_kill_info(x): # you have to add ico_custom_x (where x is a number between 1 and 7) mesh in order to display it correctly.
  return (((bignum | x) & (itp_kill_info_mask >> itp_kill_info_bits)) << itp_kill_info_bits)

# Item capabilities:
itcf_thrust_onehanded                                = 0x0000000000000001
itcf_overswing_onehanded                             = 0x0000000000000002	
itcf_slashright_onehanded                            = 0x0000000000000004
itcf_slashleft_onehanded                             = 0x0000000000000008

itcf_thrust_twohanded                                = 0x0000000000000010
itcf_overswing_twohanded                             = 0x0000000000000020
itcf_slashright_twohanded                            = 0x0000000000000040
itcf_slashleft_twohanded                             = 0x0000000000000080

itcf_thrust_polearm                                  = 0x0000000000000100
itcf_overswing_polearm                               = 0x0000000000000200
itcf_slashright_polearm                              = 0x0000000000000400
itcf_slashleft_polearm                               = 0x0000000000000800

itcf_shoot_bow                                       = 0x0000000000001000
itcf_shoot_javelin                                   = 0x0000000000002000
itcf_shoot_crossbow                                  = 0x0000000000004000

itcf_throw_stone                                     = 0x0000000000010000
itcf_throw_knife                                     = 0x0000000000020000
itcf_throw_axe                                       = 0x0000000000030000
itcf_throw_javelin                                   = 0x0000000000040000
itcf_shoot_pistol                                    = 0x0000000000070000
itcf_shoot_musket                                    = 0x0000000000080000
itcf_shoot_mask                                      = 0x00000000000ff000

itcf_horseback_thrust_onehanded                      = 0x0000000000100000
itcf_horseback_overswing_right_onehanded             = 0x0000000000200000
itcf_horseback_overswing_left_onehanded              = 0x0000000000400000
itcf_horseback_slashright_onehanded                  = 0x0000000000800000
itcf_horseback_slashleft_onehanded                   = 0x0000000001000000
itcf_thrust_onehanded_lance                          = 0x0000000004000000
itcf_thrust_onehanded_lance_horseback                = 0x0000000008000000

itcf_carry_mask                                      = 0x00000007f0000000
itcf_carry_sword_left_hip                            = 0x0000000010000000
itcf_carry_axe_left_hip                              = 0x0000000020000000
itcf_carry_dagger_front_left                         = 0x0000000030000000
itcf_carry_dagger_front_right                        = 0x0000000040000000
itcf_carry_quiver_front_right                        = 0x0000000050000000
itcf_carry_quiver_back_right                         = 0x0000000060000000
itcf_carry_quiver_right_vertical                     = 0x0000000070000000
itcf_carry_quiver_back                               = 0x0000000080000000
itcf_carry_revolver_right                            = 0x0000000090000000
itcf_carry_pistol_front_left                         = 0x00000000a0000000
itcf_carry_bowcase_left                              = 0x00000000b0000000
itcf_carry_mace_left_hip                             = 0x00000000c0000000

itcf_carry_axe_back                                  = 0x0000000100000000
itcf_carry_sword_back                                = 0x0000000110000000
itcf_carry_kite_shield                               = 0x0000000120000000
itcf_carry_round_shield                              = 0x0000000130000000
itcf_carry_buckler_left                              = 0x0000000140000000
itcf_carry_crossbow_back                             = 0x0000000150000000
itcf_carry_bow_back                                  = 0x0000000160000000
itcf_carry_spear                                     = 0x0000000170000000
itcf_carry_board_shield                              = 0x0000000180000000

itcf_carry_katana                                    = 0x0000000210000000
itcf_carry_wakizashi                                 = 0x0000000220000000


itcf_show_holster_when_drawn                         = 0x0000000800000000

itcf_reload_pistol                                   = 0x0000007000000000
itcf_reload_musket                                   = 0x0000008000000000
itcf_reload_mask                                     = 0x000000f000000000

itcf_parry_forward_onehanded                         = 0x0000010000000000
itcf_parry_up_onehanded                              = 0x0000020000000000
itcf_parry_right_onehanded                           = 0x0000040000000000
itcf_parry_left_onehanded                            = 0x0000080000000000

itcf_parry_forward_twohanded                         = 0x0000100000000000
itcf_parry_up_twohanded                              = 0x0000200000000000
itcf_parry_right_twohanded                           = 0x0000400000000000
itcf_parry_left_twohanded                            = 0x0000800000000000

itcf_parry_forward_polearm                           = 0x0001000000000000
itcf_parry_up_polearm                                = 0x0002000000000000
itcf_parry_right_polearm                             = 0x0004000000000000
itcf_parry_left_polearm                              = 0x0008000000000000

itcf_horseback_slash_polearm                         = 0x0010000000000000
itcf_overswing_spear                                 = 0x0020000000000000	# Twohanded
itcf_overswing_musket                                = 0x0040000000000000	# Onehanded used for spears
itcf_thrust_musket                                   = 0x0080000000000000		# Onehanded used for sarissa and xyston

itcf_force_64_bits                                   = 0x8000000000000000

#combined capabilities
itc_cleaver = itcf_force_64_bits | (itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded |
                                    itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded)
itc_dagger  = itc_cleaver | itcf_thrust_onehanded

itc_parry_onehanded = itcf_force_64_bits | itcf_parry_forward_onehanded| itcf_parry_up_onehanded | itcf_parry_right_onehanded |itcf_parry_left_onehanded
itc_longsword = itc_dagger | itc_parry_onehanded
itc_scimitar  = itc_cleaver | itc_parry_onehanded

itc_parry_two_handed = itcf_force_64_bits | itcf_parry_forward_twohanded | itcf_parry_up_twohanded | itcf_parry_right_twohanded | itcf_parry_left_twohanded
itc_cut_two_handed = itcf_force_64_bits | (itcf_slashright_twohanded | itcf_slashleft_twohanded | itcf_overswing_twohanded | 
                                           itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded)
itc_greatsword = itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_two_handed |itcf_thrust_onehanded_lance
itc_nodachi    = itc_cut_two_handed | itc_parry_two_handed

itc_bastardsword = itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_two_handed |itc_dagger
itc_morningstar = itc_cut_two_handed |  itc_parry_two_handed |itc_cleaver
it_rhomphaia =  itc_cleaver | itc_nodachi

itc_parry_polearm = itcf_parry_forward_polearm | itcf_parry_up_polearm | itcf_parry_right_polearm | itcf_parry_left_polearm
itc_poleaxe    = itcf_overswing_polearm |itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm
itc_staff      = itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_overswing_musket |itcf_thrust_polearm
itc_spear      = itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm | itcf_overswing_musket
itc_cutting_spear = itcf_thrust_musket|itcf_overswing_spear
itc_pike       = itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm
itc_guandao    = itc_parry_polearm|itcf_overswing_polearm|itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm
itc_standard = itcf_parry_up_twohanded | itcf_parry_forward_twohanded | itcf_slashright_polearm | itcf_slashleft_twohanded | itcf_thrust_onehanded_lance_horseback
itc_greatlance = itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback| itcf_thrust_polearm
itc_musket_melee = itcf_overswing_musket|itcf_thrust_musket|itcf_slashright_twohanded|itcf_slashleft_twohanded
itc_rg_spear_back = itc_parry_polearm | itcf_thrust_onehanded_lance_horseback | itcf_thrust_onehanded_lance | itcf_horseback_thrust_onehanded   #overhead atack with spear back
#itc_rg_spear_down      = itc_parry_polearm |itcf_thrust_onehanded |itcf_overswing_musket |itcf_thrust_onehanded_lance_horseback |itcf_thrust_polearm
itc_rg_spear_down      = itcf_thrust_onehanded |itcf_thrust_onehanded_lance_horseback |itcf_thrust_polearm
itc_rg_spear_up      = itcf_overswing_musket |itcf_thrust_polearm | itcf_horseback_thrust_onehanded   
itc_rg_spear      = itcf_thrust_onehanded |itcf_overswing_musket |itcf_thrust_onehanded_lance_horseback |itcf_thrust_polearm
itc_xyston   =  itcf_thrust_onehanded_lance_horseback|itcf_thrust_musket|itcf_thrust_onehanded_lance
itc_sword_up      = itcf_overswing_musket | itcf_thrust_onehanded | itcf_horseback_thrust_onehanded | itcf_slashright_onehanded | itcf_slashleft_onehanded | itc_parry_onehanded   

#EXtra Mesh IDs
ixmesh_inventory   = 0x1000000000000000
ixmesh_flying_ammo = 0x2000000000000000
ixmesh_carry       = 0x3000000000000000

