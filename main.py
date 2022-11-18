import math

def modif_fuc(fun):

        def inner(*args, **kwargs):
                var = fun(*args, **kwargs)
                prime_find = var if var%2 == 0 else None
                return f" the 2nd largest number is {var}, this is a {prime_find}".strip()
        return inner


@modif_fuc
def higtnumber_sort(count):
        store_val = []
        start_run, count = True, count
        while start_run:
            store_val.append(int(input("Enter the value you want = ")))
            if len(store_val) > count:
                ver = input(f"Still you want to add Y/N = ").upper()
                if ver == "Y":
                    count += int(input("Enter the loop to run = "))
                else:
                    count = input("Enter the loop to run Y/N = ").upper()
                    if count == "N":
                        start_run = False
        return sorted(store_val)[-2]

print(higtnumber_sort(int(input("Enter the loop = "))))
