def main():
    x = 1 # x represents an int value
    y = [1, 2, 3] # y represents a list 
    m(x, y) # Invoke f with arguments x and y
    print("x is " + str(x))
    print("y[0] is " + str(y[0]))
    
    print (x)
    print (y)

def m(number, numbers):
    number = 1001 # Assign a new value to number
    numbers[0] = 5555 # Assign a new value to numbers[0]

main()