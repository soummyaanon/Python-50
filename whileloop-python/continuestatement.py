#Prints all letters except "e" & "s"

i = 0
a = 'Github repository'


while i < len(a):
    if a [i] == 'e' or a[i] == 's':
        i += 1
        continue

    print ('Current Letter :', a[i])
    i +=1