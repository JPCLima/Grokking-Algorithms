# Recursion

>Recursion is where a function calls itself.

Example: Look for a key
````python
def lookForKey(box):
    for item in box:
        if item.is_a_box():
            lookForKey(item)
        elif item.is_a_key():
            print("Found the Key!!")
````
Recursion is to make the soluction clear, there is no performace benefits in using recursion. 

If the recursion is called in the incorrect way can case a infinite loop. When you write recursive function you need to tell when stop. The recursive functions has two parts:

+ **Recursive case** when the function calls itself
+ **Base case** is when  the function doesn't call itself again
  
Example: 

````python
def countdown(i):
    if i <= 0:
        return
    else:
        countdown(i)        
````
The *if <= 0* is the base case and the *else* the recursive case.

# Recap
* Recursion is when a function calls itself
* Every recursive function has two cases: the base case
and the recursive case.
* A stack has two operations: push and pop
* All function calls go onto the call stack
* The call stack can get very large, which takes up a lot of memory.




