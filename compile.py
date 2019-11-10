import json
from pyparsing import Word, alphanums, ZeroOrMore, OneOrMore, Literal, LineEnd, Or, Group, ParserElement, restOfLine, QuotedString


ParserElement.setDefaultWhitespaceChars(' \t')

EOL = LineEnd().suppress()
SEMI_COLON = Literal(";").suppress()

comment = Literal('//') + restOfLine
terminator = Or([OneOrMore(EOL), OneOrMore(SEMI_COLON)])
name = Word(alphanums + '_')

argument = Or([name, QuotedString('"')])
command = Group(name('cvar') + Group(ZeroOrMore(argument))('args') + terminator)

config = Group(ZeroOrMore(command))('commands').ignore(comment)

result = config.parseFile('test.cfg', parseAll=True)
print json.dumps(result.asDict(), indent=4)
