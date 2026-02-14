"""
Question 7:  take input sentence having "python" and replace 'python' with 'pythons' 
"""

sent = input("Enter a sentence contaning word (python): ")  
# The replce method: original_string.replace(old, new)
new_sent = sent.replace("python", "pythons")
print("Updated sentence:", new_sent)
