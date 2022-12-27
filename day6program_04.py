Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('{0},{1},{2}'.format('apple','banana','corrot','pen'))
apple,banana,corrot
print('{0},{1}{0}{0}{3}{2}'.format('apple','banana','corrot','pen'))
apple,bananaappleapplepencorrot
print('{0},{1} {0}{0}{3}{2}'.format('apple','banana','corrot','pen'))
apple,banana appleapplepencorrot
print('{0},{1},{0},{0},{3}{2}'.format('apple','banana','corrot','pen'))
apple,banana,apple,apple,pencorrot
print('{},{},{}'.format('apple','banana','corrot','pen'))
apple,banana,corrot
print('Ganguly purchased a kg of{},a dozen of{}and half kg of{}'.format('apple','banana','carrot','pen'))
Ganguly purchased a kg ofapple,a dozen ofbananaand half kg ofcarrot
print('Ganguly purchased a kg of{},a dozen of{}and half kg of{}'.format('apple','banana','carrot'))
Ganguly purchased a kg ofapple,a dozen ofbananaand half kg ofcarrot
print('Ganguly purchased a kg of{0}and{2},Manohar purchased a dozen of{1},and Arun purchased half kg of{2}'.format('apple','banana','carrot'))
Ganguly purchased a kg ofappleandcarrot,Manohar purchased a dozen ofbanana,and Arun purchased half kg ofcarrot
print('{2},{1},{0}'.format('apple','banana','carrot'))
carrot,banana,apple
print('{2},{1},{1},{0}'.format('apple','banana','carrot'))
carrot,banana,banana,apple
print('{2},{1},{0}'.format(*'abcd'))
c,b,a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
print('coordinates:{latitude},{longitude}'.format(latitude='37.24N)',longitude='-115.81W'))
coordinates:37.24N),-115.81W
print('coordinates:{latitude},{longitude}'.format(latitude='37.24N)',longitude='-115.81W'))
coordinates:37.24N),-115.81W
print('welcome:{name},your college is:{college}'.format(name='ram',college='MTICA'))
welcome:ram,your college is:MTICA
print('welcome:{name},your college is:{college}'.format(name='silpa',college='MTICA'))
welcome:silpa,your college is:MTICA
coord={latitude':'37.24N','longitude':'-115.81W'}
       
SyntaxError: invalid decimal literal
coord={latitude':'37.24N','longitude':'-115.81W'}
       
SyntaxError: invalid decimal literal
coord={latitude': '37.24N','longitude':'-115.81W'}
       
SyntaxError: invalid decimal literal
coord={'latitude': '37.24N','longitude':'-115.81W'}
       
print('coordinates':{latitude},{longitude}'.format(**coord)
      
SyntaxError: unterminated string literal (detected at line 1)
print('coordinates:{latitude},{longitude}'.format(**coord)
      