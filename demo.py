'''

Demo run for testing and, well, demonstration purposes

'''

# you can drop the slea folder on a python project and import it using
from slea import slea

# demo run
if __name__ == "__main__":
    # some string to be evaluated
    string = "!(a & ( b | !c ) & d)"

    # values associated with the operands
    operands = {
        "a": True,
        "b": False,
        "c": True,
        "d": False,
    }

    # some function that will tell the values of the operands
    def value_of_example(operand, argument):
        # you can use 'argument' to pass the values of the operands
        # in this case I used a set
        try:
            return argument.get(operand)
        except Exception as e:
            return False

        # or you can set the values internally if you want
        # if operand == "a": return True
        # elif operand == "b": return False
        # elif operand == "c": return True
        # elif operand == "d": return False
        # else: return False
    
    # the variable that will receive the tree (actually it's a list)
    output_tree = []
    
    # greeting
    print(".:", slea.get_program_info(),":."); print()

    # information
    print("This is a demo run that will evaluate the expression in the .py file"); print()
    print("You can tune the string and the operand values by editting the demo file"); print()

    # the string
    print("The string to be evaluated is:")
    print(string)
    print()

    # the operands
    print("And the operands are:")
    for i in operands:
        print(i, "=", operands.get(i))
    print()

    # checks if the string passes the syntax analysis
    error_code = slea.evaluate_syntax(string)
    # in case of error    
    if not error_code == len(string):
        print("syntax error on the indicator ('<=') character:")
        counter = 0
        for i in string:
            print(i, end="")
            if counter == error_code:
                print("<=", end="")

            counter += 1
        print()

    else:
        # if the syntax is correct, mounts the tree
        output_tree = slea.get_syntax_tree(string)

        # shows the output_tree
        print("This is the tree that was generated:", output_tree); print()

        # gets the result of the expression
        value = slea.evaluate_syntax_tree(output_tree, value_of_example, operands)
        print("The result is:", value); print()


    print("Bye!")