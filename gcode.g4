grammar gcode;

program : line+ EOF ;

line : command (parameter)* COMMENT? NEWLINE? ;

command : GCODE | MCODE | TCODE | FCODE | SCODE;

parameter : AXIS NUMBER | LETTER NUMBER ; 



GCODE : 'G' DIGIT+ ;
MCODE : 'M' DIGIT+ ;
TCODE : 'T' DIGIT+ ;
FCODE : 'F' DIGIT+ ;
SCODE : 'S' DIGIT+ ;

COMMENT : ';' ~[\r\n]* -> skip ;
AXIS: [XYZE] ;
LETTER : [A-DF-IK-NP-RTVUW];
NUMBER : '-'? DIGIT+ ('.' DIGIT+)? ;
DIGIT : [0-9] ;
NEWLINE : '\r'? '\n' -> skip ;
WHITESPACE : [ \t]+ -> skip ;


