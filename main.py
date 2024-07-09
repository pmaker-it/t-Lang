from lexer import Lexer
from parser import Parser

CODE = """
    TEST = 5 + 9 + (4 + 6); 
    p TEST;
    OUT = TEST + 30;
    p OUT + TEST + 10;
"""

lexer = Lexer(CODE)
lexer.analysis()
lexer.print_token_list()

tokens = lexer.tokenList
parse_tokens = []
for token in tokens:
    parse_tokens.append(token)

parser = Parser(parse_tokens)

root_node = parser.parse_code()
print("AST построено!")

parser.run(root_node)
