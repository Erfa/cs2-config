import argparse
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


def parse_csgo_config(filename):
    return config.parseFile(filename, parseAll=True)

def minify_argument(argument):
    return '"' + argument + '"'

def minify_command(command):
    if command['args']:
        return command['cvar'] + ' ' + ' '.join(minify_argument(arg) for arg in command['args']) + ';'
    else:
        return command['cvar'] + ';'

def minify_cfg(cfg):
    lines = []
    line = ''

    for cmd in cfg['commands']:
        minified_cmd = minify_command(cmd)

        if len(line) + len(minified_cmd) >= 512:
            lines.append(line)
            line = ''

        line += minified_cmd

    lines.append(line)
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Minify a complex CS:GO config into one line.')
    parser.add_argument('filename', help='The entry point for your config', type=argparse.FileType('r'))
    args = parser.parse_args()

    result = parse_csgo_config(args.filename)

    print json.dumps(result.asDict(), indent=4)

    print minify_cfg(result)
