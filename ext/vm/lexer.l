/*
 * Lexer interpretera maszyny wirtualnej do projektu z JFTT2019
 *
 * Autor: Maciek Gębala
 * http://ki.pwr.edu.pl/gebala/
 * 2019-11-12
*/
%option noyywrap
%option yylineno
%option nounput
%{
#include <vector>
#include <utility>

#include "parser.hh"
#include "instructions.hh"

int yylex();
%}
%%
\#.*$  ;
[ \t]+ ;
GET    { yylval = GET; return COM_0; };
PUT    { yylval = PUT; return COM_0; };
LOAD   { yylval = LOAD; return COM_1; };
STORE  { yylval = STORE; return COM_1; };
LOADI  { yylval = LOADI; return COM_1; };
STOREI { yylval = STOREI; return COM_1; };
INC    { yylval = INC; return COM_0; };
DEC    { yylval = DEC; return COM_0; };
ADD    { yylval = ADD; return COM_1; };
SUB    { yylval = SUB; return COM_1; };
SHIFT  { yylval = SHIFT; return COM_1; };
JUMP   { yylval = JUMP; return JUMP_1; };
JPOS   { yylval = JPOS; return JUMP_1; };
JZERO  { yylval = JZERO; return JUMP_1; };
JNEG   { yylval = JNEG; return JUMP_1; };
HALT   { yylval = HALT; return STOP; };
[0-9]+ { yylval = atoll( yytext ); return LABEL; };
\n     ;
.      { return ERROR; }
%%


line :
    COM_0 		{ program.push_back( std::make_pair($1,0) ); }
  | COM_1 LABEL 	{ program.push_back( std::make_pair($1,$2) ); }
  | JUMP_1 LABEL 	{ program.push_back( std::make_pair($1,$2) ); }
  | STOP 		{ program.push_back( std::make_pair($1,0) ); }
  | ERROR 		{ yyerror( program, "Nierozpoznany symbol" ); }
  ;