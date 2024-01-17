# first type of formating

first_variable = "My name is Noutcha"
second_variable = " and I have a million years old"
sentence = first_variable + second_variable
print(sentence)

# second type of formating

sentence_2 = "{} {}".format(first_variable,second_variable)
print(sentence_2)

sentence_3 = "{1} {0}".format(second_variable,first_variable)

# third type of formating

name = "Jonathan"
age = 25
height = 1.75

formatted_string = f"My name is {name}, I'm {age}, and my height is {height:.2f} meters."
print(formatted_string)
"""
{}, {:.2f} are placeholders for values in the format() method and f-string. The :.2f specifies that the float should be formatted with two decimal places.
"""