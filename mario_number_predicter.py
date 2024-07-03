def main():
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)

    # print("Factorials")
    # for i in range(10):
    #     print(f"{i} : {factorial(i)}")

    def combinatorics(n, r):
        top = factorial(n)
        bottom = (factorial(r)) * (factorial(n-r))
        combos = top / bottom 
        if (combos - (int(combos)) == 0.0):
            combos = int(combos)
        return combos 
    
    # print("combinatorics")
    # for n in range(1, 10):
    #     for r in range (1, 4):
    #         if r > n:
    #             continue
    #         print(f"{n}, {r} : {combinatorics(n, r)}")


    print("Mario Numbers")
    def mario_number_predicter(n):
        # Assuming just spaces for now
        def jump_number(n):
            # How many 3 can fit into this n?
            num_J = n // 3
            # This is BOTH max jumps _and_ loops needed to count all combinatorics
            
            starting_pos_num = (n % 3) + 1
            # Wait but then, combinatorics...
            return num_J * starting_pos_num
        
        return 1 + jump_number(n)

    for n in range(8):
        print(f"{n} : {mario_number_predicter(n)}")

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
    JSS
    SJS
    SSJ
    JJ


GGGGGG
    SSSSSS
    
    JJS
    SJJ
    
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
    SJSJ
    SSJJ
    
    JSSSS
    SJSSS
    SSJSS
    SSSJS
    SSSSJ
    
"""