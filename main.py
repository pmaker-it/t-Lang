from lexer import Lexer

CODE = "TEST= (3-5); p TEST;"

lexer = Lexer(CODE)
lexer.analysis()
lexer.print_token_list()


