text = #Insert your text here!
x = 1

#Depending to your text size, change the
#'50' parameter in order to centralize your 
#string correctly.
for i in range(len(text)):
    if ((x % 2) == 0):
        print("{:^50}".format(text[i] * (x + 1)))
        x = x + 2
    else:
        print("{:^50}".format(text[i] * x))
        x = x + 1
    