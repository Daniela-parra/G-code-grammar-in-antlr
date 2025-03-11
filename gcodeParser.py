# Generated from gcode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,31,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,3,1,24,8,1,
        1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,1,5,29,0,9,1,0,0,0,
        2,15,1,0,0,0,4,25,1,0,0,0,6,27,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,
        10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,
        0,1,14,1,1,0,0,0,15,19,3,4,2,0,16,18,3,6,3,0,17,16,1,0,0,0,18,21,
        1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,
        22,24,5,9,0,0,23,22,1,0,0,0,23,24,1,0,0,0,24,3,1,0,0,0,25,26,7,0,
        0,0,26,5,1,0,0,0,27,28,5,6,0,0,28,29,5,7,0,0,29,7,1,0,0,0,3,11,19,
        23
    ]

class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "GCODE", "MCODE", "TCODE", "FCODE", "SCODE", 
                      "LETTER", "NUMBER", "DIGIT", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_line = 1
    RULE_command = 2
    RULE_parameter = 3

    ruleNames =  [ "program", "line", "command", "parameter" ]

    EOF = Token.EOF
    GCODE=1
    MCODE=2
    TCODE=3
    FCODE=4
    SCODE=5
    LETTER=6
    NUMBER=7
    DIGIT=8
    NEWLINE=9
    WHITESPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gcodeParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcodeParser.LineContext)
            else:
                return self.getTypedRuleContext(gcodeParser.LineContext,i)


        def getRuleIndex(self):
            return gcodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gcodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.line()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                    break

            self.state = 13
            self.match(gcodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(gcodeParser.CommandContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcodeParser.ParameterContext)
            else:
                return self.getTypedRuleContext(gcodeParser.ParameterContext,i)


        def NEWLINE(self):
            return self.getToken(gcodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = gcodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.command()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 16
                self.parameter()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 22
                self.match(gcodeParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GCODE(self):
            return self.getToken(gcodeParser.GCODE, 0)

        def MCODE(self):
            return self.getToken(gcodeParser.MCODE, 0)

        def TCODE(self):
            return self.getToken(gcodeParser.TCODE, 0)

        def FCODE(self):
            return self.getToken(gcodeParser.FCODE, 0)

        def SCODE(self):
            return self.getToken(gcodeParser.SCODE, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = gcodeParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(gcodeParser.LETTER, 0)

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return gcodeParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = gcodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(gcodeParser.LETTER)
            self.state = 28
            self.match(gcodeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





