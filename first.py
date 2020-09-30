print("hello world")
print('IN THIS PROGRAM WE WILL CREATE A PYTHON PROGRAM TO CALCUTIONS')
print("enter 2 numbers")
x=int(input())
y=int(input())
answer = 0
print("choose any of these option (+,-,*,/) ")
option=input()
if option == 'plus':
  answer=x+y
elif option == 'minus':
  answer=x-y
elif option == 'multiply':
  answer=x*y
elif option == 'div':
  answer=x / y
else:
  print("wrong option")

print(x,option,y,":",answer)