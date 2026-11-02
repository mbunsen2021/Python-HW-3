# Question 4
# Madison Bunsen
#Z23631556

def testif(b: bool, testname: str, msgOK: str ="", msgFailed: str ="") -> None:
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false
otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return 


def ed_read(filename: str, from_: int = 0, to: int =-1) -> str:
    """ Reads a file and returns a string from the file, with file positions in the 
    half open range

    Args: 
     filename: name of the file
     from_: start of the index
     to: end of the index
    
    Preconditions: 
     the file is readable 
     0 <= from_ <= to when to != -1

    Postconditions:
     file is not modified
     
    Returns: 
    If to == -1, content between from_ and the end will be returned otherwise,
    the characters in the half-open range

    Raises: 
     if to exceeds the file length then the function raises IndexError and is 
     passed to the caller
     
    """
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()
    if to == -1:
        to = len(text)
    elif to > len(text):
        raise IndexError(f"to {to} exceeds file length {len(text)}")
    return text [from_:to]



def ed_find(filename: str, search_str: str) -> list[int]:
    """Finds then returns every occurence of a string in a file
    
    Args:
     filename: name of the file being searched
     search_str: string that is being searched for

    Preconditions:
     the file exists and search_str is not empty

    Postconditions:
     file is not modified 

    Raises: 
     ValueError if search_str is empty
     FileNotFoundError, IOError passed to the caller unchanged


    Returns:
     a list of the starting characters in the file in increasing order
     where search_str offurs or [] if the search_str does not occur
    
    """
    if search_str == "":
      raise ValueError (f"search_str can't be empty")

    with open (filename, "r", encoding = "utf-8") as f:
       text = f.read()  
    positions = []
    start = 0 

    index = text.find(search_str, start)
    while index != -1:
        positions.append(index)
        start = index + 1
        index = text.find(search_str, start)

    return positions
    

def ed_replace(filename: str, search_str: str, replace_with: str, occurrence: int = -1) -> int:
    """Replaces the occurences of a string with another string
    
    Args: 
     filename (str): name of the file being modified
     search_str (str): string being searched 
     replace_with (str): string that will replace the old string
     occurrence (int): index of the single occurence to replace. if the value is -1
     then all will be replaced
    
    Preconditions:
     The file exists and is readable and writable
     search_str is not empty
     occurrence >= -1

    Postconditions:
     if  occurence == -1 then all the occurences in the file will be replaced
     if the occurence is >= 0 then the file will only replace the occurence with index occurence
     if search_str doesnt occur then the file is not changed 

    Raises:
     ValueError if search_str is empty or occurrence < -1
     FileNotFoundError, IOError passed to the caller unchanged

    Returns:
     number of times the string was replaced if any 
    
    """
    if search_str == "":
        raise ValueError (f"search_str can't be empty")

    if occurrence < -1:
        raise ValueError("occurrence must be more than -1")

    
    with open(filename, "r", encoding = "utf-8") as f:
        text = f.read()

    if occurrence == -1:
        count = text.count(search_str)
        new_text = text.replace(search_str, replace_with)

    else:
        positions = ed_find(filename, search_str)
        if occurrence >= len(positions):
            return 0
        pos = positions[occurrence]
        new_text = text[:pos] + replace_with + text[pos + len(search_str):]
        count = 1 

    if count > 0:
        with open(filename, "w", encoding ="utf-8") as f:
            f.write(new_text)
    return count






def ed_append(filename: str, string: str) -> int:
    """Appending a string to the end of a file
    
    Args: 
     filename (str): name of file to append to 
     string (str): text to append 

    Preconditions:
     files directory is writable

    Postconditions: 
     file has appended text but the existing content is untouched

    Return:
     number of characters written

    Raises: 
     IOError: passed to caller if file cant be written

    """
    with open(filename, "a", encoding = "utf-8") as f:
        return f.write(string)


def reset_file(filename: str, content: str) -> None:
    """Overwrite filename with content"""
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(content)


def test_ed_find() -> None:
    """Test file for ed_find function"""
    tf = "test_find.txt"
    reset_file(tf, "01234567890123456789")

    result = ed_find(tf, "345")
    testif(result == [3,13], "ed_find: two matches", msgFailed = f"got {result}")

    testif(ed_find(tf, "356") == [], "ed_find: no match")
    testif(ed_find(tf, "0") == [0,10], "ed_find: match at start")
    testif(ed_find(tf, "9") == [9,19], "ed_find: match at end")

    reset_file(tf, "aaa")
    testif(ed_find(tf, "aa") == [0,1], "ed_find: overlapping")

    try:
        ed_find(tf, "")
        testif(False, "ed_find: empty search_str raises ValueError")
    except ValueError:
        testif(True, "ed_find: empty search_str raises ValueError")


def test_ed_replace() -> None:
    """Test file for ed_replace function"""
    tr = "test_replace.txt"

    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "345", "ABCDE", 1)
    testif(count == 1, "ed_replace one (index 1): count")
    testif(ed_read(tr) == "0123456789012ABCDE6789", "ed_replace one (index 1): content")

    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "345", "ABCDE", 0)
    testif(count == 1, "ed_replace one (index 0): count")
    testif(ed_read(tr) == "012ABCDE67890123456789", "ed_replace one (index 0): content")

    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "345", "ABCDE")
    testif(count == 2, "ed_replace all: count")
    testif(ed_read(tr) == "012ABCDE6789012ABCDE6789", "ed_replace all: content")

    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "345", "X")
    testif(count == 2, "ed_replace shorter text: count")
    testif(ed_read(tr) == "012X6789012X6789", "ed_replace shorter text: content")


    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "345", "ABCDE", 5)
    testif(count == 0, "ed_replace occurrence too large: count")
    testif(ed_read(tr) == "01234567890123456789", "ed_replace occurrence too large: file unchanged")

  
    reset_file(tr, "01234567890123456789")
    count = ed_replace(tr, "356", "ABCDE")
    testif(count == 0, "ed_replace not found: count")
    testif(ed_read(tr) == "01234567890123456789", "ed_replace not found: file unchanged")


def main () -> None:
    """Calling the tests to make sure the functions work"""
    print("Madison Bunsen, Z23631556")

    demo = "demo.txt"
    reset_file(demo, "")


    print("\n ed_append")
    print("characters:", ed_append(demo, "0123456789"))
    print("characters:", ed_append(demo, "0123456789"))

    print("\n ed _read")
    print(ed_read(demo, 3, 9))
    print(ed_read(demo, 3))

    try:
        ed_read(demo, 0, 20)
    except IndexError as e:
        print("IndexError:", e)


    print("\n ed_find")
    print(ed_find(demo, "345"))
    print(ed_find(demo, "356"))

    print("\n ed_replace")

    count = ed_replace(demo, "345", "ABCDE", 1)
    print("replaced:", count, " file:", ed_read(demo))


    reset_file(demo, "01234567890123456789")

    count = ed_replace(demo, "345", "ABCDE")

    print("replaced:", count, " file:", ed_read(demo))


 
    print("\n unit tests:")
    test_ed_replace()
    test_ed_find()


main()


