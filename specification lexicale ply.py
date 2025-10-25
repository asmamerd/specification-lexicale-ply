import ply.lex as lex

t_ignore = ' \t'

def t_error(t):
    raise ValueError(f"Lexical error  {t}")
    
lexer = lex.lex()
