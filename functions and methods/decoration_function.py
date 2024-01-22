"""
La decoration des fonctions est une technique qui permet d'etendre
ou de modifier le comportement d'une fonction sans en alterer le code source.
"""
"""
en python les fonctions sont des objets de premiere classe, ce qui signifie qu'elles peuvent etre traitees comme n'importe quel autre objet(entier,chaine,liste...)
"""

def greet(name):
    return f"Hello, {name}!"

def uppercase_decorator(function_parameter):
    def wrapper(name):
        result = function_parameter(name)
        return result.upper()
    return wrapper

greet_with_uppercase = uppercase_decorator(greet)
print(greet_with_uppercase("Alice"))
"""
Dans cet exemple, uppercase_decorator est une fonction qui prend
 une fonction func en argument, définit une nouvelle fonction 
 wrapper qui enveloppe func en ajoutant une fonctionnalité 
 supplémentaire, puis renvoie cette nouvelle fonction wrapper. 
 La fonction greet_with_uppercase est alors une version décorée 
 de la fonction greet, qui renvoie le message en majuscules.
"""
#Utilisation de la syntaxe @
@uppercase_decorator
def greet2(name):
    return f"Hello 2: {name}"

print(greet2("Jonathan"))

#Decoration de fonction

def greeting_decorator(greeting):
    """
    A decorator that adds a greeting to the result
    of the decorated function.

    Args:
    - greeting (str): The greeting message to be added.

    Returns:
    - function: The decorator function that takes another function and returns a wrapped version.

    Example:
    @greeting_decorator("Hello")
    def greet(name):
        return name

    print(greet("John"))  # Output: "Hello, John"
    """
    def decorator(func):
        """
        The decorator function that wraps another function.

        Args:
        - func (function): The function to be wrapped.

        Returns:
        - function: The wrapped function.

        Example:
        @greeting_decorator("Hello")
        def greet(name):
            return name

        print(greet("John"))  # Output: "Hello, John"
        """
        def wrapper(name):
            """
            The wrapper function that adds the greeting to the result of the decorated function.

            Args:
            - name (str): The input argument for the decorated function.

            Returns:
            - str: The result with the added greeting.

            Example:
            @greeting_decorator("Hello")
            def greet(name):
                return name

            print(greet("John"))  # Output: "Hello, John"
            """
            result = func(name)
            return f"{greeting}, {result}"
        return wrapper
    return decorator

@greeting_decorator("Bonjour")
def greet3(name):
    """
    A simple function that returns a greeting message.

    Args:
    - name (str): The name for the greeting.

    Returns:
    - str: The greeting message.

    Example:
    @greeting_decorator("Hello")
    def greet(name):
        return name

    print(greet("John"))  # Output: "Hello, John"
    """
    return name

# Test the decorated function
print(greet3("Alice"))  # Output: "Bonjour, Alice"
