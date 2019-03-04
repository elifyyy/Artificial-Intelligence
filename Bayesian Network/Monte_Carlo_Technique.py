import random

#P(+D)

def prob_positive_D():
    counter = 0
    for i in range(0,100000):
        a, b, c, d, e, = None, None, None, None, None
        random_number = random.random()
        if(random_number<=0.2):
            a=True
            if(random.random()<=0.8):
                b=True
            else:
                b=False
            if (random.random() <= 0.2):
                c = True
            else:
                c = False
            if(b==True and c==True):
                if (random.random() <= 0.8):
                    d = True
                    counter=counter+1
                else:
                    d = False

            elif (b == True and c== False):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1
                else:
                    d = False
            elif (b == False and c== True):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                    counter = counter + 1
                else:
                    d = False

        else:
            a=False
            if (random.random() <= 0.2):
                b = True
            else:
                b = False
            if (random.random() <= 0.05):
                c = True
            else:
                c = False

            if (b == True and c == True):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1
                else:
                    d = False

            elif (b == True and c == False):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1
                else:
                    d = False
            elif (b == False and c == True):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                    counter = counter + 1
                else:
                    d = False

    return (counter/100000)




#P(+D,-A)

def prob_positive_D_negatif_A():
    counter = 0
    for i in range(0, 100000):
        a, b, c, d, e, = None, None, None, None, None
        random_number = random.random()
        if (random_number <= 0.2):
            a = True
            if (random.random() <= 0.8):
                b = True
            else:
                b = False
            if (random.random() <= 0.2):
                c = True
            else:
                c = False
            if (b == True and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == True and c == False):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                else:
                    d = False

        else:
            a = False
            if (random.random() <= 0.2):
                b = True
            else:
                b = False
            if (random.random() <= 0.05):
                c = True
            else:
                c = False

            if (b == True and c == True):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1 # a is false and d is true
                else:
                    d = False

            elif (b == True and c == False):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1  # a is false and d is true
                else:
                    d = False
            elif (b == False and c == True):
                if (random.random() <= 0.8):
                    d = True
                    counter = counter + 1  # a is false and d is true
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                    counter = counter + 1  # a is false and d is true
                else:
                    d = False

    return (counter / 100000)


# P(+E|-B) = P(+E,-B)/ P(-B)

def prob_positive_E_given_negative_B():
    counter1=0 #counter for P(+E,-B)
    counter2=0 #counter for P(-B)
    for i in range(0, 100000):
        a,b,c,d,e, = None,None,None,None,None
        random_number = random.random()
        if (random_number <= 0.2):
            a = True
            if (random.random() <= 0.8):
                b = True
            else:
                b = False
                counter2=counter2+1
            if (random.random() <= 0.2):
                c = True
                if(random.random()<=0.8):
                    e=True
                    if(b==False):
                        counter1 = counter1 +1;
                else:
                    e=False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                    if (b == False):
                        counter1 = counter1 + 1;
                else:
                    e = False
        else:
            a=False
            if (random.random() <= 0.2):
                b = True
            else:
                b = False
                counter2 = counter2 + 1
            if (random.random() <= 0.05):
                c = True
                if (random.random() <= 0.8):
                    e = True
                    if (b == False):
                        counter1 = counter1 + 1;
                else:
                    e = False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                    if (b == False):
                        counter1 = counter1 + 1;
                else:
                    e = False
    return (counter1/counter2)



#P(+A|+D,-E) = P(+A,+D,-E) / P(+D,-E)

def prob_positive_A_given_positive_D_negative_E():
    counter1 = 0  # counter for P(+A,+D,-E)
    counter2 = 0  # counter for P(+D,-E)
    for i in range(0, 100000):
        a, b, c, d, e, = None, None, None, None, None
        random_number = random.random()
        if (random_number <= 0.2):
            a = True
            if (random.random() <= 0.8):
                b = True
            else:
                b = False
            if (random.random() <= 0.2):
                c = True
                if (random.random() <= 0.8):
                    e = True
                else:
                    e = False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                else:
                    e = False
            if (b == True and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == True and c == False):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                else:
                    d = False
            if(d==True and e==False): # a is true -outer if statement- , P(+A,+D,-E)
                counter1 = counter1 +1
                counter2 = counter2 +1 #P(+D,-E) also increment when a is false.


        else:
            a=False
            if (random.random() <= 0.2):
                b = True
            else:
                b = False
            if (random.random() <= 0.05):
                c = True
                if (random.random() <= 0.8):
                    e = True
                else:
                    e = False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                else:
                    e = False
            if (b == True and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == True and c == False):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == True):
                if (random.random() <= 0.8):
                    d = True
                else:
                    d = False
            elif (b == False and c == False):
                if (random.random() <= 0.05):
                    d = True
                else:
                    d = False
            if (d == True and e == False):
                counter2 = counter2 + 1  # P(+D,-E) also increment when a is true.

    return (counter1/counter2)



#P(+B,-E|+A)= P(+B,-E,+A) / P (+A)

def prob_positive_B_negative_A_given_positive_A():
    counter1 = 0  # counter for P(+B,-E,+A)
    counter2 = 0  # counter for P(+A)
    for i in range(0, 100000):
        a, b, c, d, e, = None, None, None, None, None
        random_number = random.random()
        if (random_number <= 0.2):
            a = True
            counter2 = counter2 + 1  # P(+A)
            if (random.random() <= 0.8):
                b = True
            else:
                b = False
            if (random.random() <= 0.2):
                c = True
                if (random.random() <= 0.8):
                    e = True
                else:
                    e = False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                else:
                    e = False

            if (b == True and e == False):  # a is true -outer if statement- , P(+B,-E)
                counter1 = counter1 + 1
        else:
            a = False
            if (random.random() <= 0.2):
                b = True
            else:
                b = False
            if (random.random() <= 0.05):
                c = True
                if (random.random() <= 0.8):
                    e = True
                else:
                    e = False
            else:
                c = False
                if (random.random() <= 0.6):
                    e = True
                else:
                    e = False
            if (d == True and e == False):
                counter2 = counter2 + 1  # P(+D,-E) also increment when a is true.

    return (counter1 / counter2)




positive_D_negatif_A = prob_positive_D_negatif_A()
positive_D = prob_positive_D()
positive_A_given_positive_D_negative_E=prob_positive_A_given_positive_D_negative_E()
positive_B_negative_A_given_positive_A=prob_positive_B_negative_A_given_positive_A()
print("P(+D)")
print(positive_D)
print("P(+D,-A)")
print(positive_D_negatif_A )
print("P(+E|-B)")
print(prob_positive_E_given_negative_B() )
print("P(+A|+D,-E)")
print(positive_A_given_positive_D_negative_E)
print("P(+B,-E|+A)")
print(positive_B_negative_A_given_positive_A)