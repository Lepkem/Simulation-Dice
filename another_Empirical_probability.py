from random import randint
Bithdaydouble = 365
def rnd_bd(bd = Bithdaydouble):
    return randint(1,bd)
def experiment(bd = Bithdaydouble):
    birthdays = set()
    count = 0
    while len(birthdays) < bd:
        count += 1
        birthdays.add(rnd_bd())
    return count
def simulate(N = 1000):
    freqs = []
    for _ in range(N):
        outcome = experiment()
        freqs.append(outcome)
    return sum(freqs)/N


#print(simulate(100))
