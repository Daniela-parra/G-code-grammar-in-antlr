from antlr4 import *
import sys
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en línea {line}, columna {column}: {msg}")

def test_gcode(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    input_stream = InputStream(input_text)
    lexer = gcodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gcodeParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()
    print("\n Árbol de análisis sintáctico:")
    print(Trees.toStringTree(tree, None, parser))
    

    print("Tokens reconocidos:")
    for token in token_stream.tokens:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"
        print(f"{token.text} -> {token_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python test_gcode.py archivo_prueba.gcode")
    else:
        test_gcode(sys.argv[1])
