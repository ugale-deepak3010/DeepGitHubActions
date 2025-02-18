def add(a, b):
  int r=a+b;
  print("\n returning addition as: ");
  print(r);
  return a+b;

def test_add():
  assert add(1,2)==3;
  assert add(1,-1)==0;

#run the project after pushing.
