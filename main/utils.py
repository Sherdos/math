import re
def solve_descriminant(equation):

    # Извлекаем числа, знаки и буквы из уравнения
    numbers = [float(match) if '.' in match else int(match) for match in re.findall(r'[-+]?\d*\.\d+|\d+', equation)]
    operators = re.findall(r'[-+]', equation)
    variables = re.findall(r'[a-zA-Z]', equation)

solve_descriminant("25x + 3y - 5 ")