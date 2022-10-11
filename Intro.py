# while loop
n = True
i = 1
while n:
    if i <= 10:
        print(i)
        i += 1
    else:
        n = False
    
# for loop - printing negative numbers
for i in range (-1, -11, -1) :
    print (i)

# printing sum of numbers
num = int(input('Enter a number:'))
a = 0
for i in range (1, num+1):
    a = a + i
print (a)

# printing prime number between 1 - 50
for i in range (1, 50+1):
    if i > 1:
        for num in range (2, i):
            if (i % num) == 0:
                break
        else:
            print (i)

# Complement of a DNA sequence
def complement(base):
    if base == "A" or base == "a":
        result = "T" 
    elif base == "C" or base == "c":
        result = "G" 
    elif base == "G" or base == "g":
        result = "C" 
    elif base == "T" or base == "t":
        result = "A"
    else:
        result = "N"
    return result

Seq = complement("A")
print(Seq)

S = complement("g")
print(S)

# Complement of string of DNA sequence
Sequence = str(input('Enter a string: '))
base = ''
for letter in Sequence:
    base += complement(letter)
print (base)

# Reverse a string
def reverse(seq):
    rev = ''
    l = len(seq)
    for i in range (l-1, -1, -1):
        rev += seq[i]
    print (rev)
        
reverse('ACTG')

#Reverse complement of Sequence
Sequence = str(input('Enter a string: '))
base = ''
for letter in Sequence:
    base += complement(letter)
print(reverse(base))
