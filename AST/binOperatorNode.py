from AST.expressionNode import ExpressionNode
from lex_token import LexToken


class BinOperatorNode(ExpressionNode):
    operator: LexToken
    leftNode: ExpressionNode
    rightNode: ExpressionNode

    def __init__(self, operator: LexToken, left_node: ExpressionNode, right_node: ExpressionNode):
        super().__init__()
        self.operator = operator
        self.leftNode = left_node
        self.rightNode = right_node


