def roman_to_int(s):
    roman_to_dec = {
        "I" : 1,
        "V" : 5,
        "X" : 10, 
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    final_int = 0
    for x in range(0, len(s) - 1): 
        if roman_to_dec[s[x]] < roman_to_dec[s[x+1]]:
            final_int -= roman_to_dec[s[x]]
        else:
            final_int += roman_to_dec[s[x]]
    
    return final_int + roman_to_dec[s[-1]]

print(roman_to_int('MCMXCIV'))  