def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Example usage
n = int(input())
print(f"Trailing zeros in {n}!: {count_trailing_zeros(n)}")
##2##
def number_to_words(n):
    def one(num):
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return ones[num]
    
    def two_less_20(num):
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        return teens[num - 10]
    
    def ten(num):
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        return tens[num]
    
    def two(num):
        if not num:
            return ""
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            return ten(num // 10) + (" " + one(num % 10) if num % 10 else "")
    
    def three(num):
        hundred = num // 100
        rest = num % 100
        if hundred and rest:
            return one(hundred) + " Hundred " + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + " Hundred"
        return ""
    
    if n == 0:
        return "Zero"
    
    num_str = ""
    billions = n // 1_000_000_000
    millions = (n // 1_000_000) % 1_000
    thousands = (n // 1_000) % 1_000
    remainder = n % 1_000
    
    if billions:
        num_str += three(billions) + " Billion"
    if millions:
        num_str += " " if num_str else ""
        num_str += three(millions) + " Million"
    if thousands:
        num_str += " " if num_str else ""
        num_str += three(thousands) + " Thousand"
    if remainder:
        num_str += " " if num_str else ""
        num_str += three(remainder)
    
    return num_str


num = int(input())
word_form = number_to_words(num)
print(f"{num} in words: {word_form}")
