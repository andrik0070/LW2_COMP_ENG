from classes.lexic import Token


class UnrecognizedLexem(Exception):
    pass


class SyntaxError(Exception):
    def __init__(self, token: Token):
        Exception.__init__(self)
        self.token = token

    def __str__(self):
        return "Wrong token '" + str(self.token.value) + "' at position " + '{0}:{1}'.format(self.token.line_no + 1,
                                                                                             self.token.line_pos)
