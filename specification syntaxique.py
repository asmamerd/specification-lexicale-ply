import ply.lex as lex 
import ply.yacc as yacc

def p_start(p):
    'start : eols STARTUML name EOL defs ENDUML eols'
    p[0]= ('start ' p[3],p[5])

def p_eols(p):
    '''eols : EOL eols
          | empty'''
    pass 

def p_name(p):
    '''name : ID
         | empty'''
    p[0] = p[1] if len(p) > 1 else None

def p_defs(p):
    '''defs : one_def EOL 
	        |defs one_def EOL '''
    if len(p) == 4: p[0] = [p[1]] + p[3] 
    else: p[0] = [] 

def p_one_def(p):
    '''one_def : ACTOR def_act aliases stereo
             | ACTOR_TEXT aliases stereo
             | USECASE def_uc aliases stereo
             | USE_CASE_TEXT aliases stereo
             | var arrow var ucl_link
	     | var INHERIT var 
             | PACKAGE ID LBRACE defs RBRACE
             | empty'''
    pass

def p_stereo(p):
    '''stereo : STEREO
               | empty'''
    pass

def p_arrow(p):
    '''arrow : RIGHT_ARROW_1
             | RIGHT_ARROW_2'''
    p[0] = p[1]  

def p_var(p):
    '''var : ID
           | USE_CASE_TXT
           | ACTOR_TXT  '''

def p_actor_def(p):
    'actor_def : ACTOR actor_alias stereo EOL'
    print(f"Défini acteur: {p[2]} avec stéréotype {p[3]}")

def p_usecase_def(p):
    'usecase_def : USECASE usecase_alias stereo EOL'
    print(f"Défini cas d'utilisation: {p[2]} avec stéréotype {p[3]}")
 
def p_package(p):
    'package_def : PACKAGE ID LBRACE defs RBRACE'
    print(f"Défini package: {p[2]}")

def p_actor_alias(p):
    '''actor_alias : AS ID
                   | empty'''

def p_usecase_alias(p):
    '''usecase_alias : AS ID
                     | empty'''
    
def p_empty(p):
    'empty :'

def p_error(p):
    print("Erreur syntaxique à la ligne {}".format(p.lineno if p else "Inconnu"))

parser = yacc.yacc()

def parse_input(data):
    parser.parse(data)