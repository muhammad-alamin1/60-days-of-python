str = "The best things in life are free! "

try:
    print(str.find("best", 5, 10))
    print(str.index("best", 5, 10))
except (ValueError, IndexError) as ve:
    print(ve)
    
