cpf_send = '69564912046'
nine_digits= cpf_send[:9]
counter_1 = 10

result_digit_1 = 0

for digit in nine_digits:
    result_digit_1 += int(digit) * counter_1
    counter_1 -= 1

digit_1 = (result_digit_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)
counter_2 = 11

result_digit_2 = 0
for digit in ten_digits:
    result_digit_2 += (int(digit)) * counter_2
    counter_2 -= 1
digit_2 = (result_digit_2 *10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0


cpf_generated = f'{nine_digits}{digit_1}{digit_2}'

if cpf_send == cpf_generated:
    print(f'{cpf_send} é válido!')
else:
    print('CPF inválido!')