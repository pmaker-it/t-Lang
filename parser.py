import tokenTypesDict
from AST.binOperatorNode import BinOperatorNode
from AST.expressionNode import ExpressionNode
from AST.numberNode import NumberNode
from AST.statmentsNode import StatementsNode
from AST.unarOperator import UnarOperator
from AST.variableNode import VariableNode
from lex_token import LexToken


class Parser:
    tokens: list[LexToken]
    pos: int = 0
    scope: dict = {}  # Словарь переменных

    def __init__(self, tokens: list[LexToken]):
        self.tokens = tokens

    def parse_code(self) -> ExpressionNode:
        root = StatementsNode()
        while self.pos < len(self.tokens):
            code_string_node = self.parse_expression()
            self.require("SEMICOLON")
            root.add_node(code_string_node)
        return root

    def parse_expression(self) -> ExpressionNode:
        if self.match("VARIABLE") is None:
            print_node = self.parse_print()
            return print_node
        self.pos -= 1
        variable_node = self.parse_variable_or_number()
        assign_operator = self.match("ASSIGN")
        if assign_operator is not None:
            right_formula_node = self.parse_formula()
            binary_node = BinOperatorNode(assign_operator, variable_node, right_formula_node)
            return binary_node

    def parse_print(self) -> ExpressionNode:
        operator_print = self.match("PRINT")
        if operator_print is not None:
            return UnarOperator(operator_print, self.parse_formula())

        raise Exception(f"На позиции {self.pos} обнаружена ошибка")

    def parse_variable_or_number(self) -> ExpressionNode:
        number = self.match("NUMBER")
        if number is not None:
            return NumberNode(number)

        variable = self.match("VARIABLE")
        if variable is not None:
            return VariableNode(variable)

        raise Exception(f"На позиции {self.pos} обнаружена ошибка")

    def parse_formula(self) -> ExpressionNode:
        left_node = self.parse_parentheses()
        operator = self.match("ADD")
        while operator is not None:
            right_node = self.parse_parentheses()
            left_node = BinOperatorNode(operator, left_node, right_node)
            operator = self.match("ADD")
        return left_node

    def parse_parentheses(self) -> ExpressionNode:
        if self.match("LPAR") is not None:
            node = self.parse_formula()
            self.require("RPAR")
            return node
        else:
            return self.parse_variable_or_number()

    def require(self, token_type: str) -> LexToken:
        token = self.match(token_type)
        if not token:
            raise Exception(f"На позиции {self.pos} обнаружена ошибка")
        return token

    def match(self, token_type: str) -> LexToken | None:
        # По текущей позиции возвращает токен из списка
        if self.pos < len(self.tokens):
            current_token = self.tokens[self.pos]
            if current_token.token_type.name == token_type:
                self.pos += 1
                return current_token
        return None
