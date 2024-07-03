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
    



    def max_jumps(n):
        # How many 3 can fit into this n?
        # num_J = n // 3
        if n <= 0 :
            return 0
        
        num_J = (n-1) // 2
        # This is BOTH max jumps _and_ max # of possible defectors that defect from J to SS
        #   is equal to loops needed to count all combinatorics
        
        return num_J

    def tester_permu_multiset():
        print("permu_multiset")
        total_space = 7
        for n in range(total_space + 1):
            print(f"n {n}")
            max_j = max_jumps(n)
            for j_num in range(max_j + 1):
                steps = n - ((2*j_num) +1)
                print(f"Space: {n},  Jumps: {j_num}, Steps: {steps} : {permu_multiset(j_num, steps)}")
    tester_permu_multiset()        
        
    
    def mario_number_predicter(n):
        # Assuming just spaces for now

        
        return 1 + max_jumps(n) # + (jump_number(n) * jump_torics(n))
    
    # print("Mario Numbers")
    # for n in range(8):
        # print(f"{n} : {mario_number_predicter(n)} : {max_jumps(n)}")

if __name__ == "__main__":
    main()
    
"""
G = grass aka Space
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
    
"""