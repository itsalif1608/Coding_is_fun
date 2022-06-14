'''https://www.beecrowd.com.br/judge/en/problems/view/1287'''
value = input('Enter your integar: ')
val = ''
value = value.replace(" ","")
value = value.replace(",","")
for i in value:
    if i=='o' or i=='O':
        val+= '0'
    elif i=='l':
        val += '1'
    else:
        val += i
if int(val)>2147483647:
    print('Error')
else:
    print(int(val))
