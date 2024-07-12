def isPalindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Create a reversed version of the number
    original_number = x
    reversed_version = 0
    while x > 0:
        reversed_version = reversed_version * 10 + x % 10
        x //= 10
    
    # Check if the original number is the same as the reversed number
    return original_number == reversed_version