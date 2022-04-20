from functools import reduce

# reduce é usada para acumular
# map é usada para cada item de uma lista

#reduce recebe uma função e um iterável
# x é o primeiro valor e y é o segundo do iterável
# depois, x passa a ser o resultado de x com y, e y passa a ser o terceiro valor do iterável

meio = lambda x: x[int((len(x)/2) - 0.5)] if len(x) % 2 == 1 else ''

print(meio('SQL'))
print(meio('Python'))
print(meio('C++'))
print(meio('Ruby'))
print(meio('PHP'))
print(meio('R'))


def sortString(str):
	return ''.join(sorted(str))
	
print(sortString(' PYTHON'))

def sortString2(str):
	return reduce(lambda a, b: a + b, sorted(str))
	
str = ' PYTHON'
print(sortString2(str))