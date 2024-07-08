from AST.expressionNode import ExpressionNode
from lex_token import LexToken


class UnarOperator(ExpressionNode):
    operator: LexToken
    operand: ExpressionNode

    def __init__(self, operator: LexToken, operand: ExpressionNode):
        super().__init__()
        self.operator = operator
        self.operand = operand
