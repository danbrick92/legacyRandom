class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        } 
        value = 0
        rom_ind = 0
        rom_keys = list(mapping.keys())
        while len(s) > 0:
            rom = rom_keys[rom_ind]
            splits = len(s.split(rom)) - 1
            value += (splits * mapping[rom])
            s = s.replace(rom, "")
            rom_ind += 1
        return value 
