

def refactor_text(text:str) -> str:
    text = text.replace("_", '\\_')
    text = text.replace(".", '\\.')
    text = text.replace("!", '\\!')
    text = text.replace("?", '\\?')
    text = text.replace("+", '\\+')
    text = text.replace("-", '\\-')
    text = text.replace("(", '\\(')
    text = text.replace(")", '\\)')
    return text
