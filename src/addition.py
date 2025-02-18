def add(a, b):
  print(" returning addition as: ");
  print(a+b);
  return a+b;

def test_add():
  assert add(1,2)==3;
  assert add(1,-1)==0;

add(2,2);
#run the project after pushing.
