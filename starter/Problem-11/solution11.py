
### Problem-11: Find the most frequent character in the paragraph
#	rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!

# File: most_frequent_char.py

from collections import Counter
import string

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# Normalize: lowercase & filter alphabetic characters
cleaned = ''.join(c for c in rhyme.lower() if c in string.ascii_lowercase)

# Count frequency
counts = Counter(cleaned)

# Get most common character
most_common_char, freq = counts.most_common(1)[0]

print(f"Most frequent character: '{most_common_char}' (appears {freq} times)")
