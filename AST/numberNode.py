from AST.expressionNode import ExpressionNode
from lex_token import LexToken


class NumberNode(ExpressionNode):
    number: LexToken

    def __init__(self, number: LexToken):
        super().__init__()
        self.number = number
