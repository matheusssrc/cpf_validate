cpf = '69564912046'

def calculate_first_digit(cpf: str, start_multiplier: int):
    first_nine_digits= cpf[:9]
    formula_1_result = sum(
        int(digit) * multiplier 
        for digit, multiplier 
        in zip(first_nine_digits, range(start_multiplier, 1, -1))
    )
    formula_2_result = (formula_1_result * 10) % 11
    return str(formula_2_result) if formula_2_result <= 9 else "0"

first_digit = calculate_first_digit(cpf, 10)

nine_digits = cpf[:9]

ten_digits = nine_digits + first_digit
counter_2 = 11

result_digit_2 = 0
for digit in ten_digits:
    result_digit_2 += (int(digit)) * counter_2
    counter_2 -= 1
digit_2 = (result_digit_2 *10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0


cpf_generated = f'{nine_digits}{first_digit}{digit_2}'

if cpf == cpf_generated:
    print(f'{cpf} é válido!')
else:
    print('CPF inválido!')