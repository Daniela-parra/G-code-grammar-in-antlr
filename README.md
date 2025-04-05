# 📟 G-code Parser

Este proyecto es un **analizador de código G-code** usando **ANTLR4 en Python**.  

##  Descripción

El programa analiza y valida comandos G-code comunes utilizados en **impresoras 3D**  
Usa **ANTLR4** para generar un lexer y un parser que identifican instrucciones como:

- **GCODE (G90, G21, etc.)**
- **MCODE (M03, etc.)**
- **TCODE (T1, etc.)**
- **FCODE (F1500, etc.)**
- **SCODE (S200, etc.)**

## Generar archivos python 
-> java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 gcode.g4

## Ejecutar
-> python test_gcode.py archivo_prueba.gcode
