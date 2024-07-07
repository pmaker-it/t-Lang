from lexer import Lexer

CODE = "55555"

lexer = Lexer(CODE)
lexer.analysis()
print(lexer.tokenList[0].text)
