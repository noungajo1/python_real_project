def my_function(parameter1, parameter2):
    #Function body
    #Perform tasks using parameters and other statements
    results = parameter1 + parameter2
    return results  #Return statement (optional)

result = my_function(23,12)
print(result)

def dynamic_parameters_exemple(*args):
    print(type(args))  #tuple
    print(args)
    for arg in args:
        print(arg)

#Call the fuction with different numbers of arguments
dynamic_parameters_exemple(2,3,1)
dynamic_parameters_exemple(True,42,'je suis le meilleur',[2,3,4,5])

def combined_parameters_examples(param1,param2,*argument_list):
    print(f"param1: {param1}")
    print(f'param2: {param2}')
    for arg in argument_list:
        print(arg)
    #print(f'first argument from list of argument : {argument_list[0]}')

#Call the function with different numbers of arguments
combined_parameters_examples(1,2)
combined_parameters_examples(True,42,'combinaison',[3,2,4])