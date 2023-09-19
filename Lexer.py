from Token import Token
from TokenType import TokenType
import re

token_type_dictionary = {
    'KEY_WORD': TokenType('KEY_WORD', 'Var'),
    'CONST': TokenType('CONST', '[0-9]*'),
    'IDENTIFIER': TokenType('IDENTIFIER', '[a-zA-Z]*'),
    'SEMICOLON': TokenType('SEMICOLON', ';'),
    'COMMA': TokenType('COMMA', ','),
    'SPACE': TokenType('SPACE', '[ \\n\\t\\r]'),
    'ASSIGN': TokenType('ASSIGN', ':='),
    'PLUS': TokenType('PLUS', '"\+"'),
    'MINUS': TokenType('MINUS', '"\-"'),
    'MUL': TokenType('MUL', '"\*"'),
    'DIV': TokenType('DIV', '"\/"'),
    'LPAR': TokenType('LPAR', '\('),
    'RPAR': TokenType('RPAR', '\)')
}


class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.token_list = list()

    def analysis(self) -> list:
        while self.next_token():
            pass
        return self.token_list

    def next_token(self) -> bool:
        if self.pos >= len(self.code):
            return False

        token_types_values = list(token_type_dictionary.keys())

        for i in token_types_values:
            token_type = token_type_dictionary[i]
            regex = '^' + token_type.reg
            result = re.match(regex, self.code[self.pos:])
            if result and result.group():
                token = Token(token_type, result.group(), self.pos)
                self.pos += len(result.group())
                self.token_list.append(token)
                print([token.type.name, token.text, token.position])
                return True
        assert print(f'На позиции {self.pos} обнаружена ошибка')
