sum = 0

p = input("Size of your pizza(S/M/L):")

if(p=='S'):
    sum+=100
elif(p=='M'):
    sum+=200
elif(p=='L'):
    sum+=300
else:
    print(f'The size of pizza {p} does not exist')
    print('Thank you')

if(p=='S' or p=='M' or p=='L'):
    s = input("Do you want to add pepperoni(Y/N):")

    if(s=='Y'):
        if(p=='S'):
            sum+=30
        elif (p=='M' or p=='L'):
            sum+=50
        else:
            pass

    ch = input("DO you want to add extra cheese(Y/N):")

    if(ch=='Y'):
        sum+=20
    else:
        pass

    print(f'The cost of your pizza is: {sum} \nThank you! Vist again')
