
def printboard(xstate, zstate):
    
    zero =  'x' if xstate[0] else ('0' if zstate[0] else 0 ) 
    one = 'x' if xstate[1] else ('1' if zstate[1] else 1 )
    two =  'x' if xstate[2] else ('2' if zstate[2] else 2 ) 
    there =  'x' if xstate[3] else ('3' if zstate[3] else 3 ) 
    four =  'x' if xstate[4] else ('4' if zstate[4] else 4 ) 
    five =  'x' if xstate[5] else ('5' if zstate[5] else 5 ) 
    six =  'x' if xstate[6] else ('6' if zstate[6] else 6 ) 
    seven =  'x' if xstate[7] else ('7' if zstate[7] else 7 ) 
    eight = 'x' if xstate[8] else ('8' if zstate[8] else 8 )

    print(f" {zero} | {one} | {two} |")
    print(f"---|---|---|")
    print(f" {there} | {four} | {five} |")
    print(f"---|---|---|")
    print(f" {six} | {seven} | {eight} |")
    
if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("welcome to tic tac toe")
    while(True):
        printboard(xstate, zstate)
        if(True == 1):
            print("x's chance")
            value = int( input("plase inter a value"))
            xstate[value] = 1
        else:    
            print("x's chance")
            value = int( input("plase inter a value"))
            zstate[value] = 1
      
        break