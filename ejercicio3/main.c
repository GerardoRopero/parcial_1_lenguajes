#include <stdio.h>

extern FILE *yyin;
int yyparse();

int main(int argc, char *argv[]) {

    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error abriendo archivo");
            return 1;
        }
    }

    yyparse();

    return 0;
}
