import dis
def add1(a,b):
    """
    Parameters
    ----------
    a : Any Integer
    b : Any Integer

    Returns
    ----------
    c: Any Integer
    """
    c=a+b;
    print("value of c is", c)
    #return c

def add():
    """
    Parameters
    ----------
    None
    

    Returns
    ----------
    c: Any Integer
    """
    a=6
    b=3
    c=a+b;
    print("value of c is", c)
    #return c

def main():
  c=5
  add1(3,8)

if __name__ == '__main__':
  main()


