// 2010924
grammar MT22;  

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF ;
decls: decl decls | decl;
decl: variablesdecl | functiondecl ;

//Statements
stm: matchStm | unmatchStm;
matchStm: IF LP expr RP matchStm ELSE matchStm
		| otherStm;
unmatchStm: IF LP expr RP stm
		  | IF LP expr RP matchStm ELSE unmatchStm;
otherStm: block_stm 
		  | call_stm 
		  | return_stm 
		  | continue_stm 
		  | break_stm 
		  | do_while_stm 
          | while_stm 
		  | for_stm
		  | assign_stm;
// stm:if_stm 
// 	|block_stm 
// 	| call_stm 
// 	| return_stm 
// 	| continue_stm 
// 	| break_stm 
// 	| do_while_stm 
// 	| while_stm 
// 	| for_stm
// 	| assign_stm;

// Block Statements

block_stm: LCURB list_vardecl_stm RCURB;
list_vardecl_stm: list_vardecl_stmprime | ;
list_vardecl_stmprime: vardecl_stmprime list_vardecl_stmprime | vardecl_stmprime;
vardecl_stmprime: variablesdecl | stm;

functiondecl: ID COLON FUNCTION (array_type | atomic_types) LP listparams RP (INHERIT ID)? block_stm;
listparams: listparamsprime | ;
listparamsprime: paramdecl COMMA listparamsprime | paramdecl;

// Call Statements

call_stm: ID LP listexps RP SEMICOL;

// Return Statements

return_stm: RETURN (expr | ) SEMICOL;

// Continue Statements

continue_stm: CONTINUE SEMICOL;

// Break Statements

break_stm: BREAK SEMICOL;

// Do while Statements

do_while_stm: DO block_stm WHILE LP expr RP SEMICOL;

// While Statements

while_stm: WHILE LP expr RP stm;

// For Statements

for_stm: FOR LP lhs EQUAL expr COMMA expr COMMA expr RP stm;

//If Statements

// if_stm: IF LP expr RP stm (ELSE stm)?;

// Assign Statements

assign_stm: lhs EQUAL expr SEMICOL;
lhs: ID | ID LSQAB listexpsprime RSQAB;

// Function declarations

// functiondecl: ID COLON FUNCTION (array_type | atomic_types) LP listparams RP (INHERIT ID)?;
// listparams: listparamsprime | ;
// listparamsprime: paramdecl COMMA listparamsprime | paramdecl;

// Parameters

paramdecl: INHERIT ? OUT ? ID COLON (array_type | atomic_types_for_param);

// Variables declarations

// vardecls: vardecl | ID EQ_COMPO expr SEMICOL
// vardecl : ID COMMA vardecl COMMA expr SEMICOL | ID EQ_COMPO expr

variablesdecl: list_id assi_components SEMICOL | ID recursion_assi expr SEMICOL;
list_id: ID COMMA list_id | ID;
recursion_assi: COMMA ID recursion_assi expr COMMA | assi_components_EQ;

assi_components: COLON (atomic_types_for_param | array_type);
assi_components_EQ: COLON (atomic_types_for_param | array_type) EQUAL;


// Atomic types

atomic_types: BOOLEAN | INTERGER | FLOAT | STRING | VOID | AUTO; // Sử dụng các keyword đã có sẵn. 
atomic_types_for_param: BOOLEAN | INTERGER | FLOAT | STRING | AUTO;

// Array type

array_type: ARRAY LSQAB dimensions RSQAB OF element_type;
dimensions: INTLIT COMMA dimensions | INTLIT;
element_type: atomic_types;

// Literals

arraylit: LCURB listexps RCURB;
listexps: listexpsprime | ;
listexpsprime: expr COMMA listexpsprime | expr;

// Expressions

expr: expr1 STRINGCON expr1 | expr1;
expr1: expr2 (ISEQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSTHANOREQ | GREATERTHANOREQ) expr2 | expr2;
expr2: expr2 (AND | OR ) expr3 | expr3;
expr3: expr3 (ADD | SUBTRAC) expr4 | expr4;
expr4: expr4 (MULTI | DIVIS | MODUL) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUBTRAC expr6 | expr7;
expr7: ID LSQAB listexpsprime RSQAB | expr8;
expr8: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | ID | arraylit | subexpr | callexpr;
subexpr: LP expr RP;
callexpr: ID LP listexps RP;


INTLIT: ('0'|[1-9]([0-9] | '_'[0-9])*) {self.text = self.text.replace('_','');};

// FLOATLIT: INTPART DECPART EXPPART { self.text = self.text.replace('_',''); } 
// 		  | INTPART DECPART { self.text = self.text.replace('_',''); } 
// 		  | INTPART EXPPART { self.text = self.text.replace('_',''); } 
// 		  | DECPART EXPPART { self.text = self.text.replace('_',''); } ;
// fragment INTPART: INTLIT;
// fragment DECPART: '.'[0-9]+;
// fragment EXPPART: [eE][-+]?[0-9]+;

FLOATLIT: INTPART DECPART EXPPART { self.text = self.text.replace('_',''); } 
		  | INTPART DECPART { self.text = self.text.replace('_',''); } 
		  | INTPART EXPPART { self.text = self.text.replace('_',''); } 
		  | DECPART EXPPART { self.text = self.text.replace('_',''); } ;
		  
fragment INTPART: INTLIT;
fragment DECPART: '.'[0-9]*;
fragment EXPPART: [eE][-+]?[0-9]+;

BOOLLIT: TRUE | FALSE;


STRINGLIT: '"' CHARINSTR* '"' {self.text = self.text[1:-1]};
fragment CHARINSTR: ~[\n\r"\\] | '\\' ['btnfr"\\];

// Seperators
LP: '('; RP: ')'; // Left and right parentheses ( )
LCURB: '{'; RCURB: '}'; // Left and right curly brackets: { }
LSQAB: '['; RSQAB: ']'; // Left and right square brackets: [ ]
DOT: '.'; // .
COMMA: ','; // ,
SEMICOL: ';'; // ;
COLON: ':'; // :

// Operators

EQUAL: '=';

ADD: '+'; SUBTRAC: '-'; MULTI: '*'; DIVIS: '/'; MODUL: '%'; // Arithmetic Operators
NOT: '!'; AND: '&&'; OR: '||'; ISEQUAL: '=='; //  Logical Operators
NOTEQUAL: '!='; LESSTHAN: '<'; LESSTHANOREQ: '<='; GREATERTHAN: '>'; GREATERTHANOREQ: '>='; // Relational Operators
STRINGCON: '::'; 


// KEYWORDS
AUTO: 'auto'; BREAK: 'break'; BOOLEAN: 'boolean'; DO: 'do'; ELSE: 'else';
FALSE: 'false'; FLOAT: 'float'; FOR: 'for'; FUNCTION: 'function'; IF: 'if';
INTERGER: 'integer'; RETURN: 'return'; STRING: 'string'; TRUE: 'true'; WHILE: 'while';
VOID: 'void'; OUT: 'out'; CONTINUE: 'continue'; OF: 'of'; INHERIT: 'inherit';
ARRAY: 'array';

// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]*;

//  Program comment
CMSINGLE: '//' ~[\r\n]* -> skip;
CMMULTI: '/*' .*? '*/' ->skip;
WS : [ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' CHARINSTR* [\r\n]? EOF? {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' CHARINSTR* ESC_PART {raise IllegalEscape(self.text[1:])};
fragment ESC_PART: '\\' ~[btnfr'"\\] | '\\';


ERROR_CHAR:. {raise ErrorToken(self.text)};
