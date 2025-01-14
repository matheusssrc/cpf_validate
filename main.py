def calculate_first_digit(cpf: str, start_multiplier: int):
    first_nine_digits = cpf[:9]
    formula_1_result = sum(
        int(digit) * multiplier 
        for digit, multiplier 
        in zip(first_nine_digits, range(start_multiplier, 1, -1))
    )
    formula_2_result = (formula_1_result * 10) % 11
    return str(formula_2_result) if formula_2_result <= 9 else "0"

def calculate_second_digit(cpf: str):
    ten_digits = cpf[:10]
    result_digit_2 = sum(
        int(digit) * multiplier 
        for digit, multiplier 
        in zip(ten_digits, range(11, 1, -1))
    )
    digit_2 = (result_digit_2 * 10) % 11
    return str(digit_2) if digit_2 <= 9 else "0"

def clean_cpf(cpf):
    return cpf.replace('.', '').replace('-', '')

def format_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def is_valid_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    first_digit = calculate_first_digit(cpf, 10)
    second_digit = calculate_second_digit(cpf[:9] + first_digit)
    
    cpf_generated = cpf[:9] + first_digit + second_digit
    return cpf == cpf_generated

cpf_input = input("Digite o CPF no formato ###.###.###-##: ")
cpf_clean = clean_cpf(cpf_input)

if is_valid_cpf(cpf_clean):
    print(f'{format_cpf(cpf_clean)} é válido!')
else:
    print(f'{format_cpf(cpf_clean)} CPF inválido!')
