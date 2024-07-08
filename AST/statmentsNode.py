from AST.expressionNode import ExpressionNode


class StatementsNode(ExpressionNode):
    code_strings: list[ExpressionNode] = []

    def add_node(self, node: ExpressionNode):
        self.code_strings.append(node)
