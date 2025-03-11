grammar gcode;

program : line+ EOF ;

line : command (parameter)* NEWLINE? ;

command : GCODE | MCODE | TCODE | FCODE | SCODE;

parameter : LETTER NUMBER ; 

comment : '(' .*? ')' | ';' .*? ;

GCODE : 'G' DIGIT+ ;
MCODE : 'M' DIGIT+ ;
TCODE : 'T' DIGIT+ ;
FCODE : 'F' DIGIT+ ;
SCODE : 'S' DIGIT+ ;
LETTER : [A-Z] ;
NUMBER : '-'? DIGIT+ ('.' DIGIT+)? ;
DIGIT : [0-9] ;
NEWLINE : '\r'? '\n' -> skip ;
WHITESPACE : [ \t]+ -> skip ;
