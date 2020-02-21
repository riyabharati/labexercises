"""Write a function called show_stars(rows). If rows is 5, it should print the following:
 *
 **
 ***
 ****
 *****  """


rows=5
def show_stars(rows):
    star = ""
    for i in range(rows):
        star = star + "*"
        print(star)
    print()

show_stars(rows)
