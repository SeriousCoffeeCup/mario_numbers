def main():
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)

    # print("Factorials")
    # for i in range(10):
    #     print(f"{i} : {factorial(i)}")
    
    def cascading_sum(n):
        if n <= 1:
            return 1
        return n + cascading_sum(n-1)

    # print("cascading_sum")
    # for i in range(10):
    #     print(f"{i} : {cascading_sum(i)}")

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
    
    # print("permu_torics")
    # for n in range(1, 10):
    #     for r in range (1, 4):
    #         if r > n:
    #             continue
    #         print(f"{n}, {r} : {permu_torics(n, r)}")

    def permu_multiset(J, S):
        # Num of possible orderings of n letters of J and r letters of S
        top = factorial( (J + S) )
        bottom = factorial(J) * factorial(S)
        
        perm = top / bottom 
        
        if (perm - (int(perm)) == 0.0):
            perm = int(perm)
        return perm 
    



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

    def tester_permu_multiset():
        print("permu_multiset")
        total_space = 7
        # max_possible_steps = total_space - 1 
        
        for n in range(total_space + 1):
            print(f"n {n}")
            max_j = max_jumps_in_space(n) # This is kinda roundabout and not soclearly correct
            for j_num in range(max_j + 1):
                steps = n - ((2*j_num) +1)
                print(f"Space: {n},  Jumps: {j_num}, Steps: {steps} : {permu_multiset(j_num, steps)}")
    # tester_permu_multiset()        
        
    
    def pure_plains_mario_number_predicter(total_space = 7):
        paths = 0
        
        max_j = max_jumps_in_space(total_space)
        
        for j_num in range(max_j + 1):
            steps = total_space - ((2*j_num) +1) # This can't be accurate. // Floor division is a destructive arithmetical step.
            
            orderings = permu_multiset(j_num, steps)
            paths += orderings
            print(f"Space: {total_space},  Jumps: {j_num}, Steps: {steps} : Orderings {orderings}")
            
        print(f"Paths: {paths}")
        return paths
    
    def test_plains():
        print("Mario Numbers")
        # for n in range(total_space + 1):
        space = 4
        for n in range(space + 1):
            print(f"{n} : {pure_plains_mario_number_predicter(n)}")
        
    def readable_level(level):
        # g for grass
        return level.replace(' ', 'g')
    
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

        # for index, p in enumerate(parameters):
            # print(f"{index} : n : {p} : {mario_number(p[0])} : Expected: {p[1]}")
            # print(f"{index} : {readable_level(p[0])} : Original: '{p[0]}'")
            # spaces = len(p[0])
            # print(f"{index} : {readable_level(p[0])} : {pure_plains_mario_number_predicter(spaces)} : Expected: {p[1]}")
    # tester_mario()
    # print(pure_plains_mario_number_predicter(4))

if __name__ == "__main__":
    main()
    
"""
g or G = grass aka Space
s or S = step 
P = plan
J = jump, which only works on GPG

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
    SSSS
    JS
    SJ
    3

GGGGG
    SSSSS
    
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

GG GG P GG GG 
SSS J SSS


"""