'''
Using a Loop print the value of the motorbike until the value of the bike falls
every following year until it falls below £1000 by using function 
and passing parameters.
Question from last week task
Function will be shown by the define = def, then passing parameters
using procedures.
'''

i=2000
def function_1():
    print("the value of the motorbike is :£",i)

while i> 1000:
      function_1()
      i= i-(i/100*10)
