import math; from random import randrange as r; from numba import jit

# -------------------------------------------------------------------- U L T R A   C O M P A C T --------------------------------------------------------------------
c: str; l: int;
def read_codes():
    global c, l; ls, Codes = r(100, 999), ' Codes File '; l = r(100, ls);
    with open('data\codes.bf', 'w') as f: 
        f.write(f'{Codes:-^80}\n');
        for i in range(ls):
            f.write(" " * 33); f.write(f'{r(1000, 9999)}-{r(1000, 9999)}-{r(1000, 9999)}\n'); 
        f.close();
    with open('data\codes.bf', 'r') as f: c = f.readlines()[l].replace(' ', '').replace('\n', ''); print(c); f.close(); return c;
    
read_codes();

# -------------------------------------------------------------------- N O T   S P A C E D --------------------------------------------------------------------

c: str; l: int;
def read_codes():
    global c; 
    ls: int = r(100, 999);
    Codes: str = ' Codes File ';
    l = r(100, ls);
    with open('data\codes.bf', 'w') as f:
        f.write(f'{Codes:-^80}\n');
        for i in range(ls):
            for z in range(33):
                f.write(" ");
            f.write(f'{r(1000, 9999)}-{r(1000, 9999)}-{r(1000, 9999)}\n');
        f.close();
    with open('data\codes.bf', 'r') as f:
        c = f.readlines()[l];
        c = c.replace(' ', '');
        c = c.replace('\n', '');
        print(c);
        f.close();
        
read_codes();



# -------------------------------------------------------------------- S P A C E D    O U T --------------------------------------------------------------------

c: str; l: int;

def read_codes():
    global c; 
    
    ls: int = r(100, 999);
    Codes: str = ' Codes File ';
    l = r(100, ls);
    
    with open('data\codes.bf', 'w') as f:
        f.write(f'{Codes:-^80}\n');
        for i in range(ls):
            
            for z in range(33):
                f.write(" ");
                
            f.write(f'{r(1000, 9999)}-{r(1000, 9999)}-{r(1000, 9999)}\n');
            
        f.close();
        
    with open('data\codes.bf', 'r') as f:
        c = f.readlines()[l];
        c = c.replace(' ', '');
        c = c.replace('\n', '');
        
        print(c);
        
        f.close();
        
read_codes();