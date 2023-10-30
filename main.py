def hello(name):
    print('hello ' + name)

def msg(name) -> str:
    return 'hello ' + name

if __name__ == '__main__':
    hello('bob')
    hello('alice')

    print(msg('bob'))
    print(msg('alice'))