'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, useless_param=None):
    # Your code here
    return eating_cookies_helper(n, 0)

def eating_cookies_helper(n, curr):
    diff = n - curr
    solution_count = 0
    if diff == 0:
        return 1
    if diff >= 3:
        solution_count += eating_cookies_helper(n, curr+3)
    if diff >= 2:
        solution_count += eating_cookies_helper(n, curr+2)
    if diff >= 1:
        solution_count += eating_cookies_helper(n, curr+1)
    return solution_count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
