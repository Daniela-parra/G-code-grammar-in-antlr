from antlr4 import *
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en línea {line}, columna {column}: {msg}")

def test_gcode(input_text):
    input_stream = InputStream(input_text)
    lexer = gcodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gcodeParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))
    

    print("Tokens reconocidos:")
    for token in token_stream.tokens:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"
        print(f"{token.text} -> {token_name}")

if __name__ == "__main__":
    test_gcode("G90 G21 M03 X50 Y30 Z10 F1500 S200 T1")
