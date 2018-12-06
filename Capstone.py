#This is the .py file that contains all of the Capstone projects completed from the course

def my_pi(): #This function asks for an input and will return the number of decimal places in pi
    num = int(input("Please input an integer between 2 and 83: "))
    pi = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862' #85 total, 84 without 3
    #given num, I want to count past the 3 and return pi to that nth digit
    num += 2
    return pi[0:num]

def my_e(): #This is the same as above but this time it's for Euler's Number
    num = int(input("Please input an integer between 2 and 25: "))
    e = '2.7182818284590452353602874713527'
    num += 2
    return e[0:num]

def myfib(num): #Fibonacci sequence, given a number as an argument and iterate through the sequence
    a,b = 0,1
    for _ in range(num):
        yield a
        a,b = b,a+b
    #print(list(myfib(5))) is used to test this method 

def primefactorization(number):
    i = 2
    factors = []
    while i < number:
        if (number%i)==0:
            factors.append(i)
            number = number/i
        else:
            i = i+1
    print(factors)

def palindromecheck(word):
    reversedword = word[::-1]
#     if word.lower() == reversedword.lower():
#         return True
#     else:
#         return False
    return True if word.lower() == reversedword.lower() else False

def fizzbuzz(numberArray):
    for number in numberArray:
        if number % 3 == 0 and number % 5 ==  0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

def addDigits(number):
    
            
    while len(str(number)) > 1: #while the number of digits is greater than 2
        b = str(number)
        c = [] 
        for digit in b:
            c.append (int(digit))
        number = sum(c) #11
        newarray = [] #create an array
        number = str(number) #convert to a string
        for digit in number: #append to a list
            newarray.append(int(digit))
        number = sum(newarray) #sum of that list
    else:
        return number

def nextGreaterElement(nums1,nums2):
    
    newarray = []
    #mylist = range(0,(len(nums2)-1))
    iteration = 3
    nums2.append(None)
    for digit in nums1:
        for i in range(4):
            if digit == nums2[i] and nums2[i + 1] > digit: #if the next index in nums2 > nums1 original digit
                newarray.append(nums2[i + 1])
            elif digit == nums2[i] and nums2[i + 1] < digit:
                newarray.append(-1)
            elif digit == nums2[i] and nums2.index(i) == iteration:
                newarray.append(-1)
    print(newarray)
    # mylist1 = [4,1,2]
    # mylist2 = [1,3,4,2]

    # nextGreaterElement(mylist1,mylist2)

def singleNumber(nums):
    tmp = 0
    for num in nums:
        tmp ^= num
    print(tmp)

mynum1 = [2,2,1]
mynum2 = [4,1,2,1,2]

singleNumber(mynum2)



