''' My Utilities. They are here.'''

import colors as c

def ask(question, color = c.green):
    print(c.green + question)
    answer = input(c.cyan + '--> ')
    answer = answer.lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
    color = ask("What is your name in color?",c.random_color())
