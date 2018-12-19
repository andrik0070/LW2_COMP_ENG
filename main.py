from pprint import pprint
from classes.syntax import Syntaxer
from classes.exceptions import SyntaxError

from classes.lexic import Lexer, Token
#
# with open("./data/program_text.txt", 'r') as file:
#     program_text = file.read()
#     lexer = Lexer(program_text)

with open("./data/program_text.txt", 'r') as file:
    program_text = file.read()
    lexer = Lexer(program_text)

    lexems = lexer.tokenise()

    pprint(lexems)

    with open("./lexems.txt", 'w+') as lexem_file:
        lexem_file.truncate()
        for token in lexems:
            lexem_file.write(token.__str__() + '\n')


    syntaxer = Syntaxer(lexems)

    with open("./syntax_errors.txt", 'w+') as syntax_error_file:
        syntax_error_file.truncate()

        try:
            syntaxer.run()
            syntax_error_file.write('Errors not found!')
        except SyntaxError as e:
            syntax_error_file.write(str(e))
        except Exception as e:
            pprint(e)
            pprint('Expression is invalid')




    # lexems = [Token(Token.Keyword, 'if'), Token(Token.Delimiter, '('), Token(Token.Identifier, 'Status'),
    #       Token(Token.ComparisonOperator, '='),
    #       Token(Token.Identifier, 'csError'), Token(Token.Delimiter, ')'), Token(Token.Keyword, 'then'),
    #       Token(Token.Identifier, 'key'), Token(Token.DoubleDelimiter, ':='),
    #       Token(Token.Literal, ' '), Token(Token.Delimiter, ';')]

    # syntaxer = Syntaxer(lexems)
    #
    # syntaxer.run()
