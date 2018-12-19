from pprint import pprint
from classes.lexic import Token
from classes.exceptions import SyntaxError


class Syntaxer():

    def __init__(self, lexem: list):
        if not lexem:
            raise Exception("Empty lexem list")

        self.lexem = lexem

        self.current_lexem = lexem[0]
        self.current_lexem_index = 0

    def run(self):
            self.statement()

    def set_next_lexem(self):

        if (self.current_lexem_index + 1) == len(self.lexem):
            raise Exception('Statement ended')

        self.current_lexem_index += 1
        self.current_lexem = self.lexem[self.current_lexem_index]

    def statement(self):

        if self.current_lexem.type == Token.Keyword and self.current_lexem.value == 'if':
            self.set_next_lexem()
            self.condition()

            if self.current_lexem.type == Token.Keyword and self.current_lexem.value == 'then':
                self.set_next_lexem()
                self.state()
            else:
                raise SyntaxError(self.current_lexem)
        else:
            raise SyntaxError(self.current_lexem)

    def condition(self):
        self.log_exp()
        self.set_next_lexem()

        while self.current_lexem.type == Token.LogicalOperation:
                self.set_next_lexem()
                self.log_exp()
                self.set_next_lexem()

        pass

    def log_exp(self):
        if self.current_lexem.type != Token.Delimiter or self.current_lexem.value != '(':
            raise SyntaxError(self.current_lexem)

        self.set_next_lexem()
        self.operand()
        self.set_next_lexem()
        self.comparison()
        self.set_next_lexem()
        self.operand()
        self.set_next_lexem()

        if self.current_lexem.type != Token.Delimiter or self.current_lexem.value != ')':
            raise SyntaxError(self.current_lexem)

    def operand(self):
        if self.current_lexem.type not in [Token.Integer, Token.Identifier, Token.Literal]:
            raise SyntaxError(self.current_lexem)

    def comparison(self):
        if self.current_lexem.type != Token.ComparisonOperator:
            raise SyntaxError(self.current_lexem)
        pass

    def state(self):
        if self.current_lexem.type != Token.Identifier:
            raise SyntaxError(self.current_lexem)

        self.set_next_lexem()

        if self.current_lexem.value != ':=':
            raise SyntaxError(self.current_lexem)

        self.set_next_lexem()

        if self.current_lexem.type != Token.Literal:
            raise SyntaxError(self.current_lexem)

        self.set_next_lexem()

        if self.current_lexem.value != ';':
            raise SyntaxError(self.current_lexem)