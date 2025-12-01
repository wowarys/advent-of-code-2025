print(sum(p == 0 for p in __import__('itertools').accumulate([int(n)for n in open("input.txt").read().replace("L","-").replace("R","").split("\n") if n], lambda c, v:(c+v) % 100, initial=50)))
