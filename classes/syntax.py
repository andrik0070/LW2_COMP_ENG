from classes.lexic import Token


class Syntaxer():

    def __init__(self, lexem: list):
        if not lexem:
            raise Exception("Empty lexem list")

        self.lexem = lexem

        self.current_lexem = lexem[0]
        self.current_lexem_index = 0

    def set_next_lexem(self):

        if (self.current_lexem_index + 1) == len(self.lexem):
            pass

        self.current_lexem_index += 1
        self.current_lexem = self.lexem[self.current_lexem_index]

    def statement(self):

        if self.current_lexem.type == Token.Keyword and self.current_lexem.value == 'if':
            self.condition()

            self.set_next_lexem()

            if self.current_lexem.type == Token.Keyword and self.current_lexem == 'then':
                self.state()

    def condition(self):
        pass

    def state(self):
        pass
