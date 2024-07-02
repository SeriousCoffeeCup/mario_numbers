LAB_SOURCE_FILE=__file__


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    EIGHT = 8
    # check type 
    
    # negative numbers...
    # if n < 0:
    #     n *=1 # we're only interested in individual digits. Division would flip flop operations below.
    
    # Decimal digits, bother with or not?
    
    left_bound = 10
    last_digit = 11 # take care of base case : a digit can only be 9 or greater, so, pick any 2 digit integer to start off with
    
    # Retrieve 2 digits in a row instead of do just 1 
    if n > left_bound:
        curr_digit = (n % (left_bound **2 ))  // left_bound # Guess I'll have to draw out my expectations for absolutely everything, by hand, before I run the program
        last_digit = (n % left_bound) 
        if (curr_digit == last_digit) and (curr_digit == EIGHT) and isinstance(curr_digit, int):
            return True 
        else:
            return double_eights( (n // left_bound))
    
    return False

def tester_double_eights():
    parameters = [1288, 880, 538835, 284682, 588138, 78]
    expected = [True, True, True, False, True, False]
    for index, i in enumerate(parameters):
        print(f"n : {i} : {double_eights(i)} : Expected: {expected[index]}")
# tester_double_eights()

def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return False # by the time we hit this, the search is over
        elif x == y:
            return True # True automatically, when question is "can x reach y"
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
            # Branches out like a tree, left or right, f or g 
    return can_reach

def tester_make_onion():
    print()
    parameters = [(5, 25, 4), (5, 25, 3), (1, 1, 0)]
    expected = [True, False, True]
    up = lambda x : x + 1
    double = lambda x : x * 2 
    for index, i in enumerate(parameters):
        can_reach = make_onion(up, double)
        print(f"n : {i} : {can_reach(i[0], i[1], i[2] )} : Expected: {expected[index]}")
# tester_make_onion()

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. 
        if P then J
        if _ then S or J
        if PP then 0, cannot traverse
    Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    "*** YOUR CODE HERE ***"    
    # If there's characters other than space and P
        # str.make(trans()) -> check if str empty or ig just iterate through and return 0 if so, but... too much work    


    # Jump =: move forward 2 spots
        # Minimal of 3 needed in sequence still
            # If yes, then, can jump
                # If P in middle of 1st 3 characters, then Jump only. 1 path.
                    # P cannot start or terminate a level string -> implement this check later?   **
                # Else, then can step forward twice OR jump
                    # 2 paths alternative to each other 
                    # This.... does this add to the paths? Or doesn't it... multiplies the existing path by 2?
                    # Oh... We multiply, not add.
        # level[2:] means move forward by 2 slices 
    # Step =: move forward 1 spot
        # Minimal of 1 in sequence 
        # level[1:] means move forward by 1 slice 
    
    # Base Case: Came to end of level
    if len(level) <= 1: # ==  0 or == 1 depending on the system you intend 
        # return 0 # return identity value, 1 for multiplicative counting and 0 for additive counting 
        return 1  # Branching factor is 1
    
    # level sequence cannot start or end on P.
        # If P at start, Mario has been eaten.
        # If P at end, this is an impossible level, with no safe space to stand at the end.
    # level cannot have 'PP' . Can't jump over nor step over. Placed into short-circuit position to minimize such calculations.
    if level[0] == 'P' or level[-1] == 'P' or  'PP' in level:
        return 0
    
    # Len >= 3 means can Jump
    if len(level) >= 3: 
        if level[0] + level[1] + level[2] == ' P ':
            path_num = 1 * mario_number(level[2:]) 
            return path_num # The issue for later is if we denote this with a + 1 or + 0
        else: # Empty plains 
            # return 2 * mario_number(level[2:]) # What about stepping forward once and then jumping?
                #  Thus, this is not perfectly modular.
            path_num =  2 * mario_number(level[1:])
            return path_num 
                # It is not possible to step forward once more after being mid-jump...
                    # Maybe it is easier if I modularize this somehow...
    else:
        path_num = 1 * mario_number(level[1:]) # Doesn't matter 1: or 2:. We're near the end already.
        return path_num 

def tester_mario():

    parameters = list()
    
    # len_0 = [('', 1)]
    # parameters += len_0
    
    # illegal_P = [('P  ', 0), ('  P', 0), ('  PP ', 0) ]
    # parameters += illegal_P
    
    case3 = ('   P ', 2)
    # Case 3 variations:
    # step step jump _ _ 
    # or 
    # jump _ jump _ _
    parameters += [ (' P ', 1), ('   ', 2), case3]
    
    provided_doctests = [(' P P ', 1), (' P P  ', 1), ('  P P ', 1), ('   P P ', 2), (' P PP ', 0), ('    ', 3), ('    P    ', 9), ('   P    P P   P  P P    P     P ', 180)]
    parameters += provided_doctests

    for index, p in enumerate(parameters):
        print(f"{index} : n : {p} : {mario_number(p[0])} : Expected: {p[1]}")
tester_mario()

def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 2012 and t = 2, we have that the subsequences are
        2
        0
        1
        2
        20
        21
        22
        01
        02
        12
    and of these, the maxumum number is 22, so our answer is 22.

    >>> max_subseq(2012, 2)
    22
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    "*** YOUR CODE HERE ***"

