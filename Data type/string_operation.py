"""
Puisqu'un data type est une classe, elle a des methodes.
voici celles qui concernent les string
"""

all_string_method = dir("string")
#print(all_string_method)
mon_string = "Je suis le meilleur"
length_of_string = len(mon_string)
print(length_of_string)
lower_mon_string = mon_string.lower()
print(lower_mon_string)
upper_mon_string = mon_string.upper()
print(upper_mon_string)
delete_space_mon_string = mon_string.strip()
print(delete_space_mon_string)
replace_je_suis_by_nous_sommes_mon_string = mon_string.replace("Je suis","Nous sommes")
print(replace_je_suis_by_nous_sommes_mon_string)
find_expression_get_first_element_index_mon_string = mon_string.find("meilleur")
print(find_expression_get_first_element_index_mon_string)
devide_mon_string = mon_string.split(" ")
print(devide_mon_string)
add_separator_list_string = " separator ".join(devide_mon_string)
print(add_separator_list_string)
end_with_bon_mon_string = mon_string.endswith("bon")
print(end_with_bon_mon_string)
start_with_je_mon_string = mon_string.startswith("Je")
print(start_with_je_mon_string)
number_specific_letter = mon_string.count("e")
print(number_specific_letter)
