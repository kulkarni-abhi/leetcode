class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                dfs(i+1, comb)
                comb.pop()

        # In the leetcode problems, it is clearly asked that element in range 1 to n.
        # so not starting from 0, and upto n+1 so that n is also included.
        dfs(1, [])
        return result

"""
Design Logic :--
e.g. 
Find all combinations of 3 elements from the list of 5 elements
mylist = [A, B, C, D, E]
R = 3
n = 5                      

                                                       [ ]
                                                        |
                                                        |
                                ,------------------------------,------------,
                                |                              |            |
                                |                              |            |
                                A                              B            C     <-------- Level #1 (Pick 1 element in sequence until r = 3)
                                |                              |            | 
                                |                              |            |
                        ,-------------,----------,        ,---------,       |
                        |             |          |        |         |       |
                        AB           AC          AD       BC        BD      CD    <-------- Level #2 (Pick 2 elements in sequence until r = 3)
                        |             |          |        |         |       |
                     ,---,---,     ,-----,       |    ,-------,     |       |
                     |   |   |     |     |       |    |       |     |       |
                    ABC ABD ABE   ACD  ACE      ADE  BCD     BCE   BDE     CDE    <-------- Level #3 (Pick 3 elements in sequence until r = 3)
"""
