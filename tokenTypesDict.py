from tokenType import TokenType

TokenTypesDict = {
    "NUMBER": TokenType(name="NUMBER", regex=r"[0-9]*"),
    "VARIABLE": TokenType(name="VARIABLE", regex=r"[A-Z]*"),
    "SEMICOLON": TokenType(name="SEMICOLON", regex=r";"),
    "SPACE": TokenType(name="SPACE", regex=r"[ \\n\\r\\t]"),
    "ASSIGN": TokenType(name="ASSIGN", regex=r"="),
    "PRINT": TokenType(name="PRINT", regex=r"p"),
    "ADD": TokenType(name="ADD", regex=r"add"),
    "SUB": TokenType(name="SUB", regex=r"sub"),
    "LPAR": TokenType(name="LPAR", regex=r"\\("),
    "RPAR": TokenType(name="RPAR", regex=r"\\)"),

}
