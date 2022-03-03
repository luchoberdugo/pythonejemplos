l_in = [3, -4, 0, 7, -1, 4, 2, 0]

l2 = []
for n in l_in:
  if n > 0:
    l2.append(n)
  elif n < 0:
    l2.append(n * -1)
  else:
    n != 0
print(l2)

print()

l_out = [n if n > 0 else -n for n in l_in if n != 0]
print(l_out)
