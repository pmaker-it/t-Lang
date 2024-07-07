class TokenType:
    name: str
    regex: str

    def __init__(self, name: str, regex: str):
        self.name = name
        self.regex = regex

