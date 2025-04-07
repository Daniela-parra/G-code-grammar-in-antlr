from antlr4 import *
import sys
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from antlr4.error.ErrorListener import ErrorListener
import json

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en línea {line}, columna {column}: {msg}")

def process_gcode(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    input_stream = InputStream(input_text)
    lexer = gcodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()  
    
    parser = gcodeParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    # Procesamiento mejorado
    commands = []
    current_command = None
    
    for token in token_stream.tokens:
        if token.type == lexer.GCODE or token.type == lexer.MCODE or \
           token.type == lexer.TCODE or token.type == lexer.FCODE or \
           token.type == lexer.SCODE:
            if current_command:  
                commands.append(current_command)
            current_command = {
                "comando": token.text,
                "tipo": lexer.symbolicNames[token.type],
                "linea": token.line,
                "parametros": []
            }
        elif token.type == lexer.AXIS or token.type == lexer.LETTER:
            if current_command:
                current_command["parametros"].append({
                    "tipo": "parametro",
                    "nombre": token.text,
                    "valor": None  
                })
        elif token.type == lexer.NUMBER:
            if current_command and current_command["parametros"]:
                current_command["parametros"][-1]["valor"] = float(token.text) if '.' in token.text else int(token.text)
    
    if current_command:  
        commands.append(current_command)

    # Generar JSON 
    output = {
        "metadata": {
            "archivo": file_path,
            "total_comandos": len(commands)
        },
        "comandos": commands
    }

    json_path = file_path.replace('.gcode', '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"JSON generado en: {json_path}")
    print(f"Total de comandos procesados: {len(commands)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python gcode_parser.py archivo.gcode")
        sys.exit(1)
    
    process_gcode(sys.argv[1])