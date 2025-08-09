p_phrase = "was it a car or a cat I saw"

left = 0
right = len(p_phrase) - 1

is_palindrome = True

while left < right:
    if p_phrase[left] != p_phrase[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Yes")
else:
    print("No")