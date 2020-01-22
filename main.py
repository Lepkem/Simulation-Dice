from random import randint

def throwdice(amount_of_sides=6):
    die1 = randint(1, amount_of_sides)
    die2 = randint(1, amount_of_sides)
    sum_die = die1 + die2
    return sum_die

def simulation(func, wished_outcome, runs):
    counter =0 
    i =0
    while i<runs:
        f = func
        i+=1
        if f == wished_outcome:
            counter += 1
    return(f'The program was run {runs} times and the amount of favorable outcomes was {counter}'), (f'\n This means that the chance for this even to happen, is P= {(float(counter)/float(runs))*1.00000}')

print(simulation(throwdice(), 7, 10000))