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
"""
QUESTION 3 MARIO NUMBERS START

I focused a little too hard on this and out came this solution.
Should have been a recursion tree solution, I know.
This is more discrete math-like.
"""

"""
PHASE 1
"""
def factorial(n):
    """factorials function. Avoiding all library use."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def test_factorials():
    print("Factorials")
    for i in range(10):
        print(f"{i} : {factorial(i)}")

def cascading_sum(n):
    if n <= 1:
        return 1
    return n + cascading_sum(n-1)

def test_cascading_sum():
    print("cascading_sum")
    for i in range(10):
        print(f"{i} : {cascading_sum(i)}")

"""
PHASE 2: Fitting in Jumps
"""
def max_jumps_in_space(max_space):
    # How many 3 can fit into this n?
    # num_J = n // 3
    if max_space <= 0 :
        return 0
    
    num_J = (max_space-1) // 2
    # This is BOTH max jumps _and_ max # of possible defectors that defect from J to SS
    #   is equal to loops needed to count all combinatorics
    
    return num_J

def max_jumps_in_steps(max_steps):
    if max_steps <= 0:
        return 0
    num_J = (max_steps) // 2
    
    return num_J 


"""
PHASE 3 : Combinatorics
"""
def permu_torics(n, r, ignore_order = False):
    # Out of n, choose r
    top = factorial(n)
    # bottom = (factorial(r)) * (factorial(n-r))
    bottom = factorial(n-r)
    
    if ignore_order:
        bottom *= factorial(r)
    
    combos = top / bottom 
    
    if (combos - (int(combos)) == 0.0):
        combos = int(combos)
    return combos 

def test_permu_torics():
    print("permu_torics")
    for n in range(1, 10):
        for r in range (1, 4):
            if r > n:
                continue
            print(f"{n}, {r} : {permu_torics(n, r)}")

def permu_multiset(J, S):
    # Num of possible orderings of n letters of J and r letters of S
    top = factorial( (J + S) )
    bottom = factorial(J) * factorial(S)
    
    perm = top / bottom 
    
    if (perm - (int(perm)) == 0.0):
        perm = int(perm)
    return perm 

def tester_permu_multiset():
    print("permu_multiset")
    total_space = 7
    # max_possible_steps = total_space - 1 
    
    for n in range(total_space + 1):
        print(f"n {n}")
        max_j = max_jumps_in_space(n) # This is kinda roundabout and not so clearly correct
        for j_num in range(max_j + 1):
            steps = n - ((2*j_num) +1)
            print(f"Space: {n},  Jumps: {j_num}, Steps: {steps} : {permu_multiset(j_num, steps)}")
# tester_permu_multiset()        
    
"""
PHASE 4: Permutations of Pure Grass
"""
def pure_grass_mario_num(total_space = 7, debugging_view = False):
    paths = 0
    
    max_steps = total_space - 1
    max_j = max_jumps_in_space(total_space)
    
    # Tiers of Jumps num, from 0 jumps to max Jumps 
    for j_num in range(max_j + 1):
        steps = max_steps - (2*j_num)  # Steps logic cleared up
        
        orderings = permu_multiset(j_num, steps)
        paths += orderings
        
        if debugging_view:
            print(f"Space: {total_space},  Jumps: {j_num}, Steps: {steps} : Orderings {orderings}")
    
    if debugging_view:
        print(f"Paths: {paths}")
    return paths

def test_plains():
    # for n in range(total_space + 1):
    space = 5
    for n in range(space + 1):
        print(f"Space {n} : Predicted {pure_grass_mario_num(n)}")



"""
PHASE 5: Piranha Plants are Multiplication Marks:   3-orderings P 3-orderings = 9 => 3 * 3 = 9 
"""


def readable_level(level):
    """
    g or G for grass
    
    Ain't nobody can read empty spaces.
    """
    return level.replace(' ', 'G')
    
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
    # Decide on how to model this first
    # and then count 
    """
    Solution Explanation:
    
    Difficulty comes from empty spaces of size 3 or more.
    Let 1 empty space ' ' be referred to as "grass", denoted as g or G.

    s or S =: step 
    g or G =: grass aka Empty Space
    P =: piranha plant
    J =: jump, which works on GPG but S does not.
    
    These have only 1 path:
        GPG
        GGPG
        GGPGGPG -> step jump jump
        Not complex at all.
    
    GGG allows jumping. Over grass.
        G -> step -> G -> step -> G
        or 
        jump
    
    Let's call GGG as a plain ( of grass ).
    
    GGGG allows jumping starting on 1st or 2nd G.
        3 paths.
        
    Pattern so far:
    GGGG -> SSS. Mario can take 3 steps to cross.
    GGGG -> JS
                -> SJ
                Mario can jump.
    In all situations, 2 S is interchangeable with J.
    
    So,
    calculate the plains' complexity, and that's most of the problem.
    
    GGGGG         Max Space = 5
    ->
    max 4 steps possible
    max 2 jumps possible
    
    So, permutation nCr where
    n = ( #S + #J ) 
    r = #S     
        or #J works too. It's symmetrical.
    
    Max Steps = Total Space - 1 
    Max Jumps = (Total Space - 1) // 2 
    
    Space: 5,  Jumps: 0, Steps: 4 : Orderings 1
    Space: 5,  Jumps: 1, Steps: 2 : Orderings 3
    Space: 5,  Jumps: 2, Steps: 0 : Orderings 1
    
    Total Orderings = 5
    
    On Plants:
        How do piranha plants interact with this?
    
    Well.
    
    They just split up grasslands.
    
    GPG only has 1 path over it -> J.
    
    GGGGPGGGG
    -> becomes
    SSS J SSS 
    
    SSS -> JS or SJ
    
    So:
    
    SSS J SSS
    SSS J SJ
    SSS J JS 

    SJ J SSS
    SJ J SJ
    SJ J JS 

    JS J SSS
    JS J SJ
    JS J JS 
    
    To get all permutations of GGGGPGGGG, multiply permutations of GGGG by permutations of GGGG.
    3 * 3 = 9.
    
    Future work: use proof by induction and etc to mathematically prove all this work.
    
    """
    # Translate to readable
    if ' ' in level:
        level = readable_level(level)
    # print(level)
    
    
    # break up the sequence
    def split_level(level):
        # Split method https://www.w3schools.com/python/ref_string_split.asp 
        return level.split('P')
    level_list = split_level(level)
    
    # Convert to numbers
    def convert_lvl_to_size(level_l):
        # array of predetermined size - this is faster than append
        seg_sizes = [1] * len(level_l)
        
        for index, element in enumerate(level_l):
            seg_sizes[index] = len(element)
        
        return seg_sizes
    
    seg_sizes = convert_lvl_to_size(level_list)
    # print(level_list)
    # print(seg_sizes)
    """
    Example:
    ' P  P   P    P     P'
    gPggPgggPggggPgggggP
    ['g', 'gg', 'ggg', 'gggg', 'ggggg', '']
    [1, 2, 3, 4, 5, 0]
    
    Most interestingly, edge occupied by P becomes 0 automatically.
    If we multiply these factors now, product would be 0.
    However, P hugging an edge is illegal.
    So, coincidentally, this might actually be wanted behavior.
    More processing ado, though.
    """
    # f one edge is zero. return 0
    if (seg_sizes[0] == 0) or (seg_sizes[-1] == 0):
        return 0
    
    def find_product(factors_list):
        prod = 1
        for factor in factors_list:
            prod *= factor 
        return prod
    
    # The most elegant way of ruling out illegal cases:
    if (find_product(seg_sizes) == 0):
        return 0
    """
    Otherwise:
    if level[0] == 'P' or level[-1] == 'P' or  'PP' in level:
        return 0
    
    but on level length of 0 or 1, rightmost logic breaks, and thus needs a len() safeguard....
    
    """
    
    def convert_s_to_plains_num(total_spaces):
        paths = [1] * len(total_spaces)
        
        for index, element in enumerate(total_spaces):
            paths[index] = pure_grass_mario_num(element)
        
        return paths
    orderings = convert_s_to_plains_num(seg_sizes)
    
    # print(orderings)
    
    mario_num = find_product(orderings)
    # print(f"Mario Number: {mario_num} of {level}")
    return mario_num
    
def tester_mwp():
    # mario_number(' P ')
    # mario_number('  P  ')
    # mario_number('  P   P ')
    # mario_number(' P  P   P    P     P')
    mario_number(' P  P   P    P     P ')

# tester_mwp()



def tester_mario():
    parameters = list()
    
    len_0 = [('', 1)]
    parameters += len_0
    
    illegal_P = [('P  ', 0), ('  P', 0), ('  PP ', 0) ]
    parameters += illegal_P
    
    case3 = ('   P ', 2)
    # Case 3 variations:
    # step step jump _ _ 
    # or 
    # jump _ jump _ _
    parameters += [ (' P ', 1), ('   ', 2), case3]
    
    provided_doctests = [(' P P ', 1), (' P P  ', 1), ('  P P ', 1), ('   P P ', 2), (' P PP ', 0), ('    ', 3), ('    P    ', 9), ('   P    P P   P  P P    P     P ', 180)]
    parameters += provided_doctests

    for index, p in enumerate(parameters):
        # print(f"{index} : n : {p} : {mario_number(p[0])} : Expected: {p[1]}")
        # print(f"{index} : {readable_level(p[0])} : Original: '{p[0]}'")
        # spaces = len(p[0])
        # print(f"{index} : {readable_level(p[0])} : {pure_grass_mario_num(spaces)} : Expected: {p[1]}")
        
        print(f"{index} : {readable_level(p[0])} : {mario_number(p[0])} : Expected: {p[1]}")
# tester_mario()
"""
QUESTION 3 MARIO NUMBERS END
"""

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
    # Rule out illegal cases?
    
    if (10 ** t) > n:
        # n has insufficient digits
        return n
    
    if t == 0:
        return 0
    
    # Check type
    if n < 0:
        n *=1 
    
    # Make a list of the digits 
    def convert_to_digits(n):
        """
        n becomes list of digits  
        """
        digit_horde = list()
        left_bound = 10
        while n > 0:
            digit = (n % left_bound)
            digit_horde.append(digit)
            n = n // left_bound
        
        # Reverse slicing the list - just makes thinking easier
        digit_horde = digit_horde[::-1]
            # Starting from leftmost digits, of greatest magnitutde, makes sure each highest digit is on the "leftmost" possible
        return digit_horde
    # print(n)
    digit_list = convert_to_digits(n)
    # print(digit_list)
    
    
    def subseq_builder(unsorted_digit_list, t):
        """
        1st pass, take highest digit and find all its instances in unsorted.
        
        If there aren't enough digits to its right, however, then disqualify it, until all of the max number is found.
        
        There could be multiple instances of the digit. But that would show up on the sorted_list, so index+= 1 is fine.
        
        """
        """
        Find highest digit's indices
        """
        sorted_digits = list(unsorted_digit_list)
        sorted_digits.sort(reverse=True)
        # print(sorted_digits)
        
        instances_of_HD = list()
        sorted_index = 0
        while (len(instances_of_HD) == 0):
            # highest_digit = max(unsorted_digit_list)
            highest_digit = sorted_digits[sorted_index]
            instances_of_HD = [ (index, digit) for index, digit in enumerate(unsorted_digit_list) if ((digit == highest_digit) and (  len(unsorted_digit_list[index::]) >= t  ))]
            # print(instances_of_HD)
            
            sorted_index+=1
        
        contender_lists = [unsorted_digit_list[c[0]::] for c in instances_of_HD]
        # print(contender_lists)
        
        modded_contender_lists = list()
        for ct in contender_lists:
            for _ in range( len(ct) - t ):
                ct.remove(min(ct))
            # print(f"Resulting CT {ct}")
            modded_contender_lists.append(ct)
        
        # print(f"Modded CT List {modded_contender_lists}")
        
        ct_values = list()
        for element in modded_contender_lists:
            ct_value = 0
            for indx, ele in enumerate(element[::-1]):
                ct_value += (ele * (10 ** indx))
            ct_values.append(ct_value)
        # print(ct_values)
        return (max(ct_values))
    subseq_max = subseq_builder(digit_list, t)
    return subseq_max
    
def test_subseq():
    # print(f"Max: {max_subseq(876594321, 2)}")
    # print(f"Max: {max_subseq(879365943219, 2)}")
    # print(f"Max: {max_subseq(879365943219, 3)}")
    # print(f"Max: {max_subseq(8793659543219, 4)}")
    print(f"Max: {max_subseq(20225, 3)}")
# test_subseq()


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

