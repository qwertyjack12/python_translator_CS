from TokenType import TokenType


class Token:
    def __init__(self, type: TokenType, text: str, position: int):
        self.type = type
        self.text = text
        self.position = position
