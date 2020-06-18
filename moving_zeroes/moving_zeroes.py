'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    non_zero_spot = 0
    zero_spot = len(arr)-1
    while non_zero_spot < zero_spot:
    # for i in range(len(arr)):
        if arr[non_zero_spot] == 0 and arr[zero_spot] != 0:
            arr[non_zero_spot], arr[zero_spot] = arr[zero_spot], arr[non_zero_spot]
        elif arr[non_zero_spot] != 0:
            non_zero_spot += 1
        elif arr[zero_spot] == 0:
            zero_spot -= 1
        # if arr[i] == 0:
        #     for j in range(len(arr)-1, i, -1):
        #         if arr[j] != 0:
        #             arr[j], arr[i] = arr[i], arr[j]
        #             break
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")