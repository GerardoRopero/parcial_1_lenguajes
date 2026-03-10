grammar MacLaurin;

prog : 'exp' INT NUMBER EOF ;

INT : [0-9]+ ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

WS : [ \t\r\n]+ -> skip ;
