import string

from module_info import *

from process_common import *
from process_operations import *

dword      = 0x8000000000000000
dword_mask = 0xffffffffffffffff

density_bits      = 32
fkf_density_mask  = 0xFFFF #16K

#terain condition flags
fkf_plain             = 0x00000004
fkf_steppe            = 0x00000008
fkf_snow              = 0x00000010
fkf_desert            = 0x00000020
fkf_plain_forest      = 0x00000400
fkf_steppe_forest     = 0x00000800
fkf_snow_forest       = 0x00001000
fkf_desert_forest     = 0x00002000
fkf_terrain_mask      = 0x0000ffff

fkf_realtime_ligting  = 0x00010000 #deprecated
fkf_point_up          = 0x00020000 #uses auto-generated point-up(quad) geometry for the flora kind
fkf_align_with_ground = 0x00040000 #align the flora object with the ground normal
fkf_grass             = 0x00080000 #is grass
fkf_on_green_ground   = 0x00100000 #populate this flora on green ground
fkf_rock              = 0x00200000 #is rock 
fkf_tree              = 0x00400000 #is tree -> note that if you set this parameter, you should pass additional alternative tree definitions
fkf_snowy             = 0x00800000
fkf_guarantee         = 0x01000000

fkf_speedtree         = 0x02000000  #NOT FUNCTIONAL: we have removed speedtree support on M&B Warband

fkf_has_colony_props  = 0x04000000  # if fkf_has_colony_props -> then you can define colony_radius and colony_treshold of the flora kind


def density(g):
  if (g > fkf_density_mask):
    g = fkf_density_mask
  return ((dword | g) << density_bits)


fauna_kinds = [
  ("grass",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_plain|density(800),[["grass_a","0"],["grass_b","0"],["grass_yellow_a","0"]]),
  ("grass_b",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_plain_forest|density(500),[["grass_forest_a","0"],["grass_forest_b","0"]]),
  ("grass_steppe",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_steppe|fkf_steppe_forest|density(400),[["grass_yellow_a","0"],["grass_yellow_b","0"],["grass_yellow_c","0"]]),

  ("flowers_yellow",fkf_align_with_ground|fkf_on_green_ground|fkf_plain|density(120),[["flowers_yellow","0"],["flowers_yellow_b","0"]]),
  ("flowers_white",fkf_align_with_ground|fkf_on_green_ground|fkf_plain|density(120),[["flowers_white","0"],["flowers_white_b","0"]]),  
  ("grass_flower",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_steppe|fkf_steppe_forest|density(20),[["grass_flower_a","0"],["grass_flower_b","0"]]),
  
  ("fern",fkf_grass|fkf_plain_forest|fkf_align_with_ground|density(150),[["fern_a","0"],["fern_b","0"]]),
  # ("fern",fkf_grass|fkf_plain_forest|fkf_align_with_ground|density(20),[["forest_bush_a","0"]]), 
  ("champi_rouge",fkf_plain_forest|fkf_align_with_ground|density(100),[["champi_rouge","0"],["champi_rouge_2","0"],["champi_rouge_3","0"]]),
  ("champi_marron",fkf_plain_forest|fkf_align_with_ground|density(100),[["champi_marron","0"],["champi_marron_2","0"]]),
  
  ("grass_bush",fkf_grass|fkf_align_with_ground|fkf_plain|fkf_steppe|fkf_steppe_forest|density(10),[["grass_bush_a","0"],["grass_bush_b","0"]]),  

  ("basak",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(30),[["basak","0"]]),
  ("common_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(20),[["common_plant","0"]]), 
  ("big_bush",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(150),[["big_bush","0"]]),
  ("buddy_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(30),[["buddy_plant","0"],["buddy_plant_b","0"],["buddy_plant_c","0"]]),  
  
  ("bush_dead",fkf_align_with_ground|fkf_plain|fkf_steppe|fkf_steppe_forest|density(10),[["bush_dead_a","0"],["bush_dead_b","0"],["bush_dead_c","0"]]),

  ("thorn_a",fkf_align_with_ground|fkf_plain_forest|density(50),[["thorn_a","0"],["thorn_b","0"],["thorn_c","0"],["thorn_d","0"]]),



  


  ("wheat",fkf_steppe|fkf_steppe_forest|density(15),[["wheat_a","0"],["wheat_b","0"],["wheat_c","0"],["wheat_d","0"]]),
  
 ("rock_group",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(15),[["rock_group_a","bo_rock_group_a"],["rock_group_b","bo_rock_group_b"],["rock_group_c","bo_rock_group_c"]]),  
 ("rock",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(15),[["rock_a","bo_rock_a"],["rock_b","bo_rock_b"]]),  
 ("rock_large",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(10),[["rock_c","bo_rock_c"],["rock_e","bo_rock_e"],["rock_k","bo_rock_k"]]),  

 ("tree_stump",fkf_align_with_ground|fkf_plain_forest|fkf_realtime_ligting|fkf_rock|density(15),[["tree_stump_a","bo_tree_stump_a"],["tree_stump_b","bo_tree_stump_b"],["tree_stump_c","bo_tree_stump_c"]]),  

 
  ("cypress",fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["cypress_a","bo_cypress_a",("0","0")],["cypress_b","bo_cypress_b",("0","0")],["cypress_c","bo_cypress_c",("0","0")]]),
  ("olive_tree",fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["oliva_tree_a","bo_oliva_tree_a",("0","0")],["oliva_tree_b","bo_oliva_tree_b",("0","0")],["oliva_tree_c","bo_oliva_tree_c",("0","0")],["oliva_tree_d","bo_oliva_tree_d",("0","0")],["oliva_tree_e","bo_oliva_tree_e",("0","0")]]),
  ("acacia",fkf_plain|fkf_steppe_forest|fkf_tree|density(4),[["acacia_a","bo_acacia_a",("0","0")],["acacia_savana_a","bo_acacia_savana_a",("0","0")]]),
  ("xenoargh_tree_1",fkf_plain_forest|fkf_steppe_forest|fkf_tree|density(4),[["xenoargh_tree_1","bo_xenoargh_tree_1",("0","0")],["xenoargh_tree_1_b","bo_xenoargh_tree_1",("0","0")],["xenoargh_tree_1_c","bo_xenoargh_tree_1",("0","0")]]),
  ("xenoargh_tree_2",fkf_plain_forest|fkf_steppe_forest|fkf_tree|density(4),[["xenoargh_tree_2","bo_xenoargh_tree_2",("0","0")],["xenoargh_tree_2_b","bo_xenoargh_tree_2",("0","0")],["xenoargh_tree_2_c","bo_xenoargh_tree_2",("0","0")]]),
  ("xenoargh_tree_3",fkf_plain_forest|fkf_steppe_forest|fkf_tree|density(4),[["xenoargh_tree_3","bo_xenoargh_tree_3",("0","0")],["xenoargh_tree_3_b","bo_xenoargh_tree_3",("0","0")],["xenoargh_tree_3_c","bo_xenoargh_tree_3",("0","0")]]),
  ("xenoargh_tree_4",fkf_plain_forest|fkf_steppe_forest|fkf_tree|density(4),[["xenoargh_tree_4","bo_xenoargh_tree_4",("0","0")],["xenoargh_tree_4_b","bo_xenoargh_tree_4",("0","0")],["xenoargh_tree_4_c","bo_xenoargh_tree_4",("0","0")]]),
  
  ("pine",fkf_tree|density(4),[["pine_1_a","bo_pine_1_a",("0","0")],["pine_1_a","bo_pine_1_a",("0","0")],["pine_1_b","bo_pine_1_b",("0","0")],["pine_2_a","bo_pine_2_a",("0","0")],["pine_3_a","bo_pine_3_a",("0","0")]]),
  ("snowy_pine",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["snowy_pine_2","bo_snowy_pine_2",("0","0")]]),
  ("tree_snowy",fkf_snow|fkf_snow_forest|fkf_tree|density(5),[["tree_snowy_a","bo_tree_snowy_a",("0","0")],["tree_snowy_b","bo_tree_snowy_b",("0","0")]]),
  ("rock_snowy",fkf_snow|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["rock_snowy_a","bo_rock_snowy_a"],["rock_snowy_b","bo_rock_snowy_b"],["rock_snowy_c","bo_rock_snowy_c"],]),


  ("dead_tree",fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["dead_tree_a","bo_dead_tree_a",("0","0")],["dead_tree_b","bo_dead_tree_b",("0","0")],["dead_tree_c","bo_dead_tree_c",("0","0")],["dead_tree_d","bo_dead_tree_d",("0","0")]]),
  ("fir",fkf_tree|density(4),[["fir","bo_fir",("0","0")],["fir_2","bo_fir_2",("0","0")]]),  
  ("tree_f",fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["tree_f_1","bo_tree_f_1",("0","0")],["tree_f_2","bo_tree_f_2",("0","0")],["tree_f_3","bo_tree_f_3",("0","0")]]),
  ("tree_8",fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_8_a","bo_tree_8_a",("0","0")),("tree_8_b","bo_tree_8_b",("0","0")),("tree_8_c","bo_tree_8_c",("0","0"))]),
  ("tree_15",fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["tree_15_a","bo_tree_15_a",("0","0")],["tree_15_b","bo_tree_15_b",("0","0")],["tree_15_c","bo_tree_15_c",("0","0")],["tree_15_d","bo_tree_15_d",("0","0")],["tree_15_e","bo_tree_15_e",("0","0")]]),
  ("tree_16",fkf_tree|density(4),[["tree_16_a","bo_tree_16_a",("0","0")],["tree_16_b","bo_tree_16_b",("0","0")]]),  
  
  # ("tree_4",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_4_a","bo_tree_4_a",("0","0")),("tree_4_b","bo_tree_4_b",("0","0"))]),
  # ("tree_5",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_5_a","bo_tree_5_a",("0","0")),("tree_5_b","bo_tree_5_b",("0","0")),("tree_5_c","bo_tree_5_c",("0","0")),("tree_5_d","bo_tree_5_d",("0","0"))]),
  # ("tree_6",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_6_a","bo_tree_6_a",("0","0")),("tree_6_b","bo_tree_6_b",("0","0")),("tree_6_c","bo_tree_6_c",("0","0")),("tree_6_d","bo_tree_6_d",("0","0"))]),
  # ("tree_7",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_7_a","bo_tree_7_a",("0","0")),("tree_7_b","bo_tree_7_b",("0","0")),("tree_7_c","bo_tree_7_c",("0","0"))]),


  # ("tree_9",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_9_a","bo_tree_9_a",("0","0")),("tree_9_b","bo_tree_9_a",("0","0")),("tree_9_c","bo_tree_9_a",("0","0"))]),
  # ("tree_10",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_10_a","bo_tree_10_a",("0","0")),("tree_10_b","bo_tree_10_a",("0","0")),("tree_10_c","bo_tree_10_a",("0","0"))]),
  # ("tree_11",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_11_a","bo_tree_11_a",("0","0")),("tree_11_b","bo_tree_11_a",("0","0")),("tree_11_c","bo_tree_11_a",("0","0"))]),
  # ("tree_12",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_12_a","bo_tree_12_a",("0","0")),("tree_12_b","bo_tree_12_b",("0","0")),("tree_12_c","bo_tree_12_c",("0","0"))]),
  # ("tree_14",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_14_a","bo_tree_14_a",("0","0")),("tree_14_b","bo_tree_14_b",("0","0")),("tree_14_c","bo_tree_14_c",("0","0"))]),

  # ("tree_16",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_16_a","bo_tree_16_a",("0","0")),("tree_16_b","bo_tree_16_b",("0","0"))]),

  # ("tree_17",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_17_a","bo_tree_17_a",("0","0")),("tree_17_b","bo_tree_17_b",("0","0")),("tree_17_c","bo_tree_17_c",("0","0")),("tree_17_d","bo_tree_17_d",("0","0"))]),

  # ("palm",fkf_desert_forest|fkf_tree|density(4),[("palm_a","bo_palm_a",("0","0"))]),

  # ("tree_new_1",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_a01","bo_tree_a01",("0","0")),("tree_a02","bo_tree_a01",("0","0"))]),
  # ("bush_new_1",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["bush_a01","0"],["bush_a02","0"]]),
  # ("bush_new_2",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["bush_new_a","0"]]),
  # ("bush_new_3",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["bush_new_b","0"]]),
  # ("bush_new_4",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["bush_new_c","0"]]),

  # ("dry_bush",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["dry_bush","0"]]),
  # ("dry_leaves",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(70),[["dry_leaves","0"]]),

  # ("tree_new_2",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_b01","bo_tree_b01",("0","0")),("tree_b02","bo_tree_b02",("0","0"))]),
  # ("tree_new_3",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_c01","bo_tree_c01",("0","0")),("tree_c02","bo_tree_c02",("0","0"))]),

  # ("tree_plane",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_18_a","bo_tree_18_a",("0","0")),("tree_18_b","bo_tree_18_b",("0","0"))]),
  # ("tree_19",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tree_19_a","bo_tree_19_a",("0","0"))]),
  # ("beech",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(3),[("tree_20_a","bo_tree_20_a",("0","0")),("tree_20_b","bo_tree_20_b",("0","0"))]),

  # ("tall_tree",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[("tall_tree_a","bo_tall_tree_a",("0","0"))]),

  # ("tree_e",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["tree_e_1","bo_tree_e_1",("0","0")],["tree_e_2","bo_tree_e_2",("0","0")],["tree_e_3","bo_tree_e_3",("0","0")]]),

  ("grape_vineyard",density(0),[("grape_vineyard","bo_grape_vineyard")]),
  ("grape_vineyard_stake",density(0),[("grape_vineyard_stake","bo_grape_vineyard_stake")]),  
  

  
  ("valleyRock_rounded",fkf_rock|density(5),[["valleyRock_rounded_1","bo_valleyRock_rounded_1"],["valleyRock_rounded_2","bo_valleyRock_rounded_2"],["valleyRock_rounded_3","bo_valleyRock_rounded_3"],["valleyRock_rounded_4","bo_valleyRock_rounded_4"]]),
  ("valleyRock_flat",fkf_rock|density(5),[["valleyRock_flat_1","bo_valleyRock_flat_1"],["valleyRock_flat_2","bo_valleyRock_flat_2"],["valleyRock_flat_3","bo_valleyRock_flat_3"],["valleyRock_flat_4","bo_valleyRock_flat_4"],["valleyRock_flat_5","bo_valleyRock_flat_5"],["valleyRock_flat_6","bo_valleyRock_flat_6"]]),
  ("valleyRock_flatRounded_small",fkf_rock|density(5),[["valleyRock_flatRounded_small_1","bo_valleyRock_flatRounded_small_1"],["valleyRock_flatRounded_small_2","bo_valleyRock_flatRounded_small_2"],["valleyRock_flatRounded_small_3","bo_valleyRock_flatRounded_small_3"]]),
  ("valleyRock_flatRounded_big",fkf_rock|density(5),[["valleyRock_flatRounded_big_1","bo_valleyRock_flatRounded_big_1"],["valleyRock_flatRounded_big_2","bo_valleyRock_flatRounded_big_2"]]),
]


def save_fauna_kinds():
  file = open(export_dir + "/data/flora_kinds.txt","w")
  file.write("%d\n"%len(fauna_kinds))
  for fauna_kind in fauna_kinds:
    meshes_list = fauna_kind[2]
    file.write("%s %d %d\n"%(fauna_kind[0], (dword_mask & fauna_kind[1]), len(meshes_list)))
    for m in meshes_list:
      file.write(" %s "%(m[0]))
      if (len(m) > 1):
        file.write(" %s\n"%(m[1]))
      else:
        file.write(" 0\n")
      if ( fauna_kind[1] & (fkf_tree|fkf_speedtree) ):  #if this fails make sure that you have entered the alternative tree definition (NOT FUNCTIONAL in Warband)
        speedtree_alternative = m[2]
        file.write(" %s %s\n"%(speedtree_alternative[0], speedtree_alternative[1]))
    if ( fauna_kind[1] & fkf_has_colony_props ):
      file.write(" %s %s\n"%(fauna_kind[3], fauna_kind[4]))
  file.close()

def two_to_pow(x):
  result = 1
  for i in xrange(x):
    result = result * 2
  return result

fauna_mask = 0x80000000000000000000000000000000
low_fauna_mask =             0x8000000000000000
def save_python_header():
  file = open("./fauna_codes.py","w")
  for i_fauna_kind in xrange(len(fauna_kinds)):
    file.write("%s_1 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | two_to_pow(i_fauna_kind)))
    file.write("%s_2 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64)))
    file.write("%s_3 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64) | two_to_pow(i_fauna_kind)))
  file.close()

print "Exporting flora data..."
save_fauna_kinds()
