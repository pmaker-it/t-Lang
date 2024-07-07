from lexer import Lexer

CODE = """
    TEST = 5 + 9 + (4 - 6); 
    p TEST;
    OUT = TEST + 30;
    p OUT + TEST - 10;
"""

lexer = Lexer(CODE)
lexer.analysis()
lexer.print_token_list()


