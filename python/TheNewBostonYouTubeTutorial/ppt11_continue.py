numbersTaken = [2, 7, 13, 15, 17, 19]

print("\nHere are all the numbers still available:")

for n in range(1, 20+1):
    if n in numbersTaken:
        '''
        Whenever you get to the word 'continue' everything
        after the word 'continue' in the loop is skipped 
        and go to the next iteration of the loop; so, if
        something was after it wouldn't break out of the 
        loop completely and stop the loop.
        '''

        continue
    print(n)
