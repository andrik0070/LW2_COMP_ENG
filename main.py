from pprint import pprint
from classes.syntax import Syntaxer

from classes.lexic import Lexer, Token
#
# with open("./data/program_text.txt", 'r') as file:
#     program_text = file.read()
#     lexer = Lexer(program_text)

lexems = [Token(Token.Keyword, 'if'), Token(Token.Delimiter, '('), Token(Token.Identifier, 'Status'),
          Token(Token.ComparisonOperator, '='),
          Token(Token.Identifier, 'csError'), Token(Token.Delimiter, ')'), Token(Token.Keyword, 'then'),
          Token(Token.Identifier, 'key'), Token(Token.DoubleDelimiter, ':='),
          Token(Token.Literal, ' '), Token(Token.Delimiter, ';')]

syntaxer = Syntaxer(lexems)

syntaxer.run()
