

def min_max_difference(array):
    
    minimum = array[0]
    maximum = array[0]
    
    for element in array:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
            
    print(minimum, maximum)        
            
    return maximum - minimum


def main():
    difference = min_max_difference([15, 22, 84, 14, 88, 23])

    print(difference)

if __name__ == '__main__':
    main()