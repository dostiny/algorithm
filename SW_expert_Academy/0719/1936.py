A, B = map(int, input().split())
 
if A == 1:
  if B == 1:
    pass
  elif B == 2:
    print("B")
  elif B == 3:
    print("A")
elif A == 2:
  if B == 1:
    print("A")
  elif B == 2:
    pass
  elif B == 3:
    print("B")
elif A == 3:
  if B == 1:
    print("B")
  elif B == 2:
    print("A")
  elif B == 3:
    pass