#LIBRAY BOOK ISSUE(USE OF OR).

def library_book(has_card,has_permission):
    if has_card==True or has_permission==True:
        return "BOOK ISSUED"
    else:
        return "CANNOT ISSUE"
print(library_book(False,False))
