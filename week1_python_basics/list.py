lst = [1,2,3,4,5]

lst.pop(2)

print(lst)

try: 
    lst.remove(6)
except ValueError:
    print("Value Error")
except:
    print("Not found")

