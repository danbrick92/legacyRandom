import copy
from collections import Counter

class Solution:
    def gen_hash(self, s1): # O(26) -> O(1)
        self.perm_dict = Counter(s1)
    
    def reset(self): # O(26) -> O(1)
        start = None
        self.cur_dict = self.perm_dict.copy()
        return start
    
    def first_found_soft_reset(self, start, i, s2):
        first = start + s2[start:i+1].index(s2[i]) # O(s2) - overcome this, hash map storing each value and indices we came across O(1)
                
        for char in s2[start:first]: # do not include first b/c we would have subbed 1  # O(s2) - overcome this, reference indexes after 0(1)
            self.cur_dict[char] = self.cur_dict[char] + 1 
                
        start = first + 1
        return start
        
    def check_hit(self): # O(26) -> O(1)
        if sum(list(self.cur_dict.values())) == 0:
            return True
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create hashmap for s1
        self.gen_hash(s1)
        
        # Check if in hashmap
        start = self.reset()
        for i in range(len(s2)): # O(s2)
            val = self.cur_dict.get(s2[i]) # O(1)
            
            if val is None: # this letter not found in s2, reset from scratch
                start = self.reset()
                
            elif val == 0: # too many of this character...go back to first ref and recalculate
                start = self.first_found_soft_reset(start, i, s2)
                    
            else:
                start = i if start is None else start
                    
                self.cur_dict[s2[i]] = val - 1
                
                if self.check_hit():
                    return True
        
        return False