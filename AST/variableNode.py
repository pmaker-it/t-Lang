from AST.expressionNode import ExpressionNode
from lex_token import LexToken


class VariableNode(ExpressionNode):
    variable: LexToken

    def __init__(self, variable: LexToken):
        super().__init__()
        self.variable = variable
