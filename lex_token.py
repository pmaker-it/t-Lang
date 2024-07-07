class LexToken:
    token_type: str
    text: str
    pos: int

    def __init__(self, token_type: str, text: str, pos: int):
        self.token_type = token_type
        self.text = text
        self.pos = pos
