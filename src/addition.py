def add(a, b):
  print("\n returning addition as: "+(a+b));
  return a+b;

def test_add():
  assert add(1,2)==3;
  assert add(1,-1)==0;

#run the project after pushing.
