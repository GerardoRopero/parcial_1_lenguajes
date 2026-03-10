%{
#include <stdio.h>
#include "newton.h"

void yyerror(const char *s);
int yylex();
%}

/* tipo de datos de los valores */
%union {
    double num;
}

%token SQRT
%token <num> NUMBER
%token LPAREN RPAREN EOL

%%

input:
      | input line
;

line:
      SQRT LPAREN NUMBER RPAREN EOL
      {
          double r = sqrt_newton($3);
          printf("sqrt(%f) = %f\n", $3, r);
      }
;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}
