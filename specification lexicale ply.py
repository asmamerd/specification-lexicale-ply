import ply.lex as lex



tokens = [
    'COLON',
    'RIGHT_ARROW_1',
    'RIGHT_ARROW_2',
    'LBRACE',
    'RBRACE',
    'INHERIT',
    'EOL',
    'STRING',
    'STEREO',
    'ACTOR_TEXT',
    'USE_CASE_TEXT',
    'ID',
    'STARTUML',
    'ENDUML',
    'AS',
    'ACTOR',
    'USECASE',
    'PACKAGE',
    'INCLUDES',
    'EXTENDS',
]



t_COLON = r':'
t_RIGHT_ARROW_1 = r'->'
t_RIGHT_ARROW_2 = r'.>'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<|--'
t_EOL = r'\n'
t_STRING = r'"([^"\\]*(\\.[^"\\]*)*)"'
t_STEREO = r'<<[^<>]+>>'
t_ACTOR_TEXT = r':[A-Za-z_][A-Za-z0-9_]*:'
t_USE_CASE_TEXT = r':[A-Za-z_][A-Za-z0-9_]*:'
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
t_STARTUML = r'@startuml'
t_ENDUML = r'@enduml'
t_ACTOR = r'actor'
t_USECASE = r'usecase'
t_AS = r'as'
t_INCLUDES = r'includes'
t_EXTENDS = r'extends'
t_PACKAGE = r'package'



t_ignore = ' \t'



def t_error(t):
    raise ValueError(f"Lexical error  {t}")



lexer = lex.lex()