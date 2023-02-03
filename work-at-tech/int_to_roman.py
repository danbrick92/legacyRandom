class Solution:
    def intToRoman(self, num: int) -> str:
        retval = ''
        int_to_rom_items = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        while num > 0:
            for item in int_to_rom_items:
                if num - item[0] >= 0:
                    num -= item[0]
                    retval += item[1]
                    break 
        
        return retval