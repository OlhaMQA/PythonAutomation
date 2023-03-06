# Prompts the user to enter a numeric value for the side of a quadrilateral,
# handles invalid input, and returns the entered value as a float
def enter_side(side_name) -> float:
    side = input(f'Введи довжину сторони {side_name}: ')
    try:
        side = float(side)
        if side > 0:
            return side
        raise ValueError
    except ValueError:
        print(f'"{side}" не є валідною довжиною сторони опуклого чотирикутника.\n'
              f'Введене значення має бути числом та бути більшим за 0.0\n'
              f'Спробуй ще раз!')
        return enter_side(side_name)


# Returns True if the quadrilateral is a rectangle by the Pythagorean theorem
# AND none of the sides equals 0
# Otherwise returns False
def is_rectangle(s_1, s_2, s_3, s_4) -> bool:
    d1_squared = s_1 ** 2 + s_2 ** 2
    d2_squared = s_3 ** 2 + s_4 ** 2
    if d2_squared == d1_squared:
        return True
    return False


# Checks if the quadrilateral is a square by comparing its sides.
# Sides of the square should be equal
def is_square(s_1, s_2, s_3, s_4) -> bool:
    if s_4 == s_2 == s_3 == s_1:
        return True
    return False


# Calculates the square of a rectangle by 2 sides multiplied
def square_rectangle(s_1, s_2) -> float:
    return s_1*s_2


# User enters 4 sides of the quadrilateral
AB = enter_side('AB')
BC = enter_side('BC')
CD = enter_side('CD')
DA = enter_side('DA')

# User is informed if their quadrilateral is a square
if is_square(AB, BC, CD, DA):
    print("Квадрат!")

# User is informed if their quadrilateral is not a rectangle,
# otherwise the rectangle's square is calculated and printed
if is_rectangle(AB, BC, CD, DA):
    print(f'Площа = {square_rectangle(AB, BC)}')
else:
    print('Не прямокутник :(')
