og_string=input("enter the input sentence")
s=og_string.split()
l=s[::-1]
rev=''.join(l)
print(f"original string:{og_string}")
print(f"string in reverse order is:{rev}")

