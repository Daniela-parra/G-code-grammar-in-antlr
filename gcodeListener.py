# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete listener for a parse tree produced by gcodeParser.
class gcodeListener(ParseTreeListener):

    # Enter a parse tree produced by gcodeParser#program.
    def enterProgram(self, ctx:gcodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by gcodeParser#program.
    def exitProgram(self, ctx:gcodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by gcodeParser#line.
    def enterLine(self, ctx:gcodeParser.LineContext):
        pass

    # Exit a parse tree produced by gcodeParser#line.
    def exitLine(self, ctx:gcodeParser.LineContext):
        pass


    # Enter a parse tree produced by gcodeParser#command.
    def enterCommand(self, ctx:gcodeParser.CommandContext):
        pass

    # Exit a parse tree produced by gcodeParser#command.
    def exitCommand(self, ctx:gcodeParser.CommandContext):
        pass


    # Enter a parse tree produced by gcodeParser#parameter.
    def enterParameter(self, ctx:gcodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by gcodeParser#parameter.
    def exitParameter(self, ctx:gcodeParser.ParameterContext):
        pass



del gcodeParser