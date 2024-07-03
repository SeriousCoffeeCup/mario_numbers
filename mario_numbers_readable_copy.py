"""
QUESTION 3 MARIO NUMBERS 

Q3: Super Mario
Mario needs to jump over a sequence of Piranha plants called level. 
level is represented as a string of empty spaces (' '), indicating no plant, and P's ('P'), indicating the presence of a plant. 
Mario only moves forward and can either step (move forward one spot) or jump (move forward two spots) from each position. 
How many different ways can Mario traverse a level without stepping or jumping into a Piranha plant ('P')? 
Assume that every level begins with an empty space (' '), where Mario starts, and ends with an empty space (' '), where Mario must end up.

Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

( Intended Solution type: recursion tree, which this isn't. )

"""

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

Just treat each plant as a multiplication operator.

Future work: stop missing discrete math lectures and get comfortable with induction proof-ing this

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
tester_mario()


"""
Q3 Brute Force Examples

g or G =: grass aka Space
s or S =: step 
P =: piranha plant
J =: jump, which works on GPG but S does not.

G
    1 
    step 

GG
    1
    step step 

GGG
    2
    step step step
    jump

GGGG
    SSS
    JS
    SJ
    3

GGGGG
    SSSS
    
    JJ
    
    JSS
    SJS
    SSJ
    


1. Max_J: How many jumps are there : G // 3 -> how many loops
2. Jump-torics -> j = Max_J, j = Max_J - 1, j = Max_J - 2 
    -> Out of JJJ, how many J becomes SS? 
    None, 1
    1 ->  SS torics
    2 -> SS torics
    
3. SS torics
~~How many S are not interchangeable with J : G % 3  -> add to end, and, their possible positions lend to torics~~
Given how many J and S there are, what are their possible positions?


GGGGGG
    SSSSSS
    
    JJS
    SJJ
    JSJ
    
    JSSS
    SJSS
    SSJS
    SSSJ
    
GGGGGGG
    SSSSSSS
    
    JJJ
    
    JJSS
    JSJS
    JSSJ
    SJJS
    SJSJ
    SSJJ
    
    JSSSS
    SJSSS
    SSJSS
    SSSJS
    SSSSJ


GG GG GG GG 
    JJSSS
    JJSJS
    JJSSJ
    JSJJS
    JSJSJ
    JSSJJ
    SJJJS
    SJJSS
    SJSJJ
    SSJJS


GG GG GG GG 
    JJSSS
    JJSJS
    JJSSJ
    JSJJS
    JSJSJ
    JSSJJ
    SJJJS
    SJJSS
    SJSJJ
    SSJJS

ggggPgggg

SSS J SSS

4 spaces -> 3 orderings
SJ
JS
SSS

6 orderings on both sides 
+ 1 jump in middle


Oh wait 
Are they multiplicative?
Hm.

SSS J SSS
SSS J SJ
SSS J JS 

SJ J SSS
SJ J SJ
SJ J JS 

JS J SSS
JS J SJ
JS J JS 

Ah.
3 x 3  = 9

gggPggggPgPgggPggPgPggggPgggggPg

ggg 3  :  2
P
gggg 4  : 3
P
g 1   : 1
P
ggg 3   : 2
P
gg 2   : 1
P 
g 1   : 1
P
gggg 4   : 3
P
ggggg 5   : 5
P
g 1   : 1

2 * 3 * 2 * 3 * 5 
2 * 3 * 3 * 10 
2 * 9 * 10 
18 * 10 

"""