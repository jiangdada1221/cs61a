def funA(fn):
    print('A')
    fn()
    return 'fuck!'

@funA
def funB():
    print('i am B')
