class Solution(object):
    def romanToInt(self, s):
        roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            if i < length - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
                total -= roman_to_int_map[s[i]]
            else:
                total += roman_to_int_map[s[i]]
                
        return total
    pass


