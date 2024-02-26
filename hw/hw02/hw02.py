HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    if x < 10:
        return 1 if x == 8 else 0

    if(x % 10 == 8):
        return 1 + num_eights(x // 10)
    else:
        return num_eights(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # sum, i = 1,1
    # boo = True
    # while i != n:
    #     if i % 8 == 0 or num_eights(i):
    #         boo = not boo
    #     if boo == True:
    #         sum += 1
    #     else:
    #         sum -= 1
    #     i+=1
    # return sum
    def pp_helper(i,bool):
        if i == n:
            return 1

        if i % 8 == 0 or num_eights(i):
            if bool :
                return -1 + pp_helper(i+1,not bool)
            else:
                return 1 + pp_helper(i+1,not bool)

        elif bool:
            return 1 + pp_helper(i+1,bool)
        else:
            return -1 + pp_helper(i+1,bool)
    return pp_helper(1,True)



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def missing_helper(remaining,last_digit):

        if remaining < 10 and last_digit-1 == remaining:
            return 0
        if (remaining % 10 == last_digit) or (remaining % 10 == last_digit - 1):
            return missing_helper(remaining//10,remaining%10)
        else:
            return 1 + missing_helper(remaining,last_digit-1)
    if n <10:
        return 0
    else:
        return missing_helper(n,n%10)



def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_helper(total,coin_value):
        print("Debug:",total,coin_value)
        if total == coin_value:
            return 1
        if total < 0:
            return 0
        if coin_value > total:
            return 0

        ways_using_current_coin = count_helper(total - coin_value,coin_value)

        next_coin = next_largest_coin(coin_value)

        if next_coin:
            ways_using_next_coin = count_helper(total,next_coin)
        else:
            ways_using_next_coin = 0

        return ways_using_current_coin + ways_using_next_coin

    return count_helper(total,1)











def any(a, b, pred):
    """Returns True if any numbers from a to b inclusive satisfy
    pred.

    >>> any(1, 4, lambda x: x % 2 == 0)
    True
    >>> any(-5, 2, lambda x: x * x == -3 * x)   # -3 satisfies pred
    True
    >>> any(1, 6, lambda x: x % 7 == 0)
    False
    >>> any(0, 6, lambda x: x % 7 == 0)
    True
    """
    "*** YOUR CODE HERE ***"

    if a > b:
        return False
    if pred(a):
        return True
    return any(a+1,b,pred)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
