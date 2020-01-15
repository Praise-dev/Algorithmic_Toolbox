# python3
import sys

def min_stops(arr, l):
    n= len(arr)
    current_position = 0
    number_of_refills = 0
    i = 1
    while (current_position <= n):
        if(current_position +i < n):
            # print(current_position)
            if( (arr[current_position + i] - arr[current_position]) > l ):
                if current_position == current_position +i-1:
                    return "impossible to get to destination"
                current_position += i-1
                print(arr[current_position])
                number_of_refills += 1
                print(number_of_refills) 
                i = 1
            else:
                i +=1
        else: 
            return number_of_refills
               
    
def compute_min_refills(distance, tank, stops):
    # write your code here
    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

