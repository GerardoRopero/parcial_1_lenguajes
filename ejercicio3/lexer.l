%{
#include "parser.tab.h"
#include <stdlib.h>
%}

%%

sqrt            { return SQRT; }

[0-9]+(\.[0-9]+)? {
                    yylval.num = atof(yytext);
                    return NUMBER;
                 }

"("             { return LPAREN; }
")"             { return RPAREN; }
\n              { return EOL; }

[ \t]           ;

.               { return yytext[0]; }

%%

int yywrap() {
    return 1;
}
