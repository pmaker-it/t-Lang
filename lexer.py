from lex_token import LexToken
from tokenTypesDict import TokenTypesDict
import re


class Lexer:
    code: str
    pos: int = 0
    tokenList: list[LexToken] = []

    def __init__(self, code: str):
        self.code = code

    def analysis(self) -> list[LexToken]:
        while self.next_token():
            print(len(self.tokenList))
        return self.tokenList

    def next_token(self) -> bool:
        if self.pos >= len(self.code):
            return False
        token_types_values = list(TokenTypesDict.values())
        for item in range(len(token_types_values)):
            token_type = token_types_values[item]
            result = re.match(token_type.regex, self.code[self.pos:])
            if result:
                lex_token = LexToken(token_type, result[0], self.pos)
                self.pos += len(result[0])
                self.tokenList.append(lex_token)
                return True
        raise Exception(f"На позиции {self.pos} обнаружена ошибка")
