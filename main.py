from Lexer import Lexer


if __name__ == '__main__':
    code = '''
    Var a, b, c, d;
    a := 5 b := 21 c := 31;
    d := b "*" 2 "-" (c "-" a);
    '''
    lexer = Lexer(code)
    lexer.analysis()
    print(lexer.token_list)


# ident = r'(^[a-zA-Z])([a-zA-Z]*)'
# # operand = r'([a-zA-Z]*)|([0-9]*)'
# const = r'[\d]'
# razdel = r'[();]'
# oper = ['-', '+', '*', '/', ':=']
# un_oper = r'-'
# key_word = ['Var']
#
#
# def read_file(file):
#     with open(file, mode='r') as f:
#         line = 1
#         s = f.readline()
#         print_shapka()
#         while s:
#             for i in s.split():
#                 token_check(i, line)
#             s = f.readline()
#             line += 1
#
#
# def token_check(el, row_number):
#     if el in key_word:
#         print(el, 'KEY WORD', row_number)
#         return
#     if el in oper:
#         print(el, 'OPER', row_number)
#     if re.match(ident, el):
#         print(el, 'IDENT', row_number)
#     if re.search(un_oper, el):
#         print(re.search(un_oper, el).group(), 'UN_OPER', row_number)
#     if re.search(const, el):
#         print(re.search(const, el).group(), 'CONST', row_number)
#     if re.search(razdel, el):
#         print(re.search(razdel, el).group(), 'RAZDEL', row_number)
#     # if re.match(operand, el):
#     #     print('OPERAND')
#
#
# def print_shapka():
#     print('token', 'class token', 'line')
#
#
# if __name__ == '__main__':
#     file = 'text.txt'
#     read_file(file)