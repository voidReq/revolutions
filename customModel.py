import rotate
import sympy as sp

x1, x2, y1, y2, z1, z2 = -10, 10, -10, 10, -10, 10

# Figures out which axis to rotate it about type
def graphNow(axis, func, value):
    if axis == 'x':
        rotate.rotateX(func, value, x1, x2, y1, y2, z1, z2, axis)
    elif axis == 'y':
        rotate.rotateY(func, value, x1, x2, y1, y2, z1, z2, axis)
    else:
        print("Invalid axis. Please enter 'x=$' or 'y=$'.")


def setBounds(axis):
    global x1, x2, y1, y2, z1, z2  # Use global variables to update bounds
    negativeBound = input(f"What's your negative bound for {axis} (enter just an int value): ").strip()

    try:
        negativeBound = int(negativeBound)
    except ValueError:
        print("Please enter a valid integer.")
        return

    positiveBound = input(f"What's your positive bound for {axis} (enter just an int value): ").strip()

    try:
        positiveBound = int(positiveBound)
    except ValueError:
        print("Please enter a valid integer.")
        return

    match axis:
        # bounding stuff
        case "x":
            x1, x2 = negativeBound, positiveBound
        case "y":
            y1, y2 = negativeBound, positiveBound
        case "z":
            z1, z2 = negativeBound, positiveBound
        case _:
            print(f"Invalid axis {axis}. Please choose 'x', 'y', or 'z'.")
            return
    print(f"Bounds for {axis}-axis set to: {negativeBound} to {positiveBound}")


def main():
    try:
        func_input = input("Enter a function in terms of x (e.g., 2*x**2, 4*sin(x), etc.): ")
        x = sp.symbols('x')
        func = sp.sympify(func_input) # make it sympify
    except Exception as e:
        print(f"Error parsing: {e}")
        return

    axis_input = input("Which **linear** thingy you wanna rotate about? (Enter 'x=$' or 'y=$'): ").strip().lower()

    try:
        axis, value = axis_input.split('=')
        axis = axis.strip() # takes the equation on the right bit
        value = float(value.strip())
    except ValueError:
        print("Invalid input. Please follow the syntax 'x=$' or 'y=$'.")
        print("Examples:\ny=4\nx=-1\nx=0\ny=413")
        return

    while True:
        procedureQuestion = """
        Options:
        [0]: Graph the function
        [1]: New function
        [2]: Set X boundaries
        [3]: Set Y boundaries
        [4]: Set Z boundaries
        [5]: Exit
        """
        proceedQuestion = input(procedureQuestion).strip().lower()

        if proceedQuestion == '0':
            graphNow(axis, func, value)
        elif proceedQuestion == '1':
            main()
        elif proceedQuestion == '2':
            setBounds("x")
        elif proceedQuestion == '3':
            setBounds("y")
        elif proceedQuestion == '4':
            setBounds("z")
        elif proceedQuestion == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()
