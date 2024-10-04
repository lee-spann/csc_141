

glossary = {'boolean':'true or false statements',
        'conditional':'if-then statements',
        'string':'sequence of characters',
        'dictionary':'A collection of key-value pairs.',
        'list':'A collection of items in a particular order.',
        'comment':'A note in code that only shows in the code',
     'variable':' a named placeholder that can hold different values',
     'function':'a sequence of commands that can be reused together later in a program',
     'tuple':'a data structure that stores a collection of elements in an ordered and immutable way',
     'float':'a number with a decimal point'} 

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")