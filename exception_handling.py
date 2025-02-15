from tkinter.font import names

# this is a tuple, an ordered, immutable collection of elements -- it is characterised by commas separating the values
names_tuple = "Rod", "Jane", "Freddie"

# try is a standardised keyword; it clarifies what we would like the program to attempt (acknowledging that it may not work/may cause an error)
# if an error occurs, Python will jump to the most appropriate except block
try:
    # some print commands to show whether the try block is running successfully
    print("######## TRY ########")
    print("The TRY block attempts to run")

    # prints the tuple as above
    print(f"Original Tuple: {names_tuple}")

    # the sorted function returns a list containing all items from the iterable in ascending order
    names_sorted_as_list = sorted(names_tuple)

    # when the new list (converted from the original tuple) is printed, it organises the elements in ascending alphabetical order
    print(names_sorted_as_list)

    # using the append method, Bungle is added to the end of the list (lists are mutable, while tuples are not)
    names_sorted_as_list.append("Bungle")
    print("Added Bungle: ", names_sorted_as_list)

    print("Attempt to manipulate the tuple...")
    # tuples are immutable, so Zippy cannot be added to the original tuple
    # trying to do this will trigger a TypeError and the last bit of the try block -- print("Is this code reached?") -- will not run
    names_tuple[0] = "Zippy"
    print("Is this code reached?")


# except catches and handles any errors (or exceptions) -- and they can be specific like "FileNotFoundError" and "TypeError" or general like "Exception"
# FileNotFoundError catches and handles errors where a file cannot be found
except FileNotFoundError as error:

    # this except block will only run if the code runs into a FileNotFoundError - which it doesn't - so the next three lines do not print
    print("######## EXCEPT: FileNotFoundError ########")
    print("The EXCEPT/CATCH block only runs if this error happens")
    print(f"The following file cannot be found: {error.filename}. Please try another file")


# TypeError catches and handles errors that occur when an operation between incompatible data types is tried (e.g. "5" + 5)
# attempting to add an element to the tuple after its creation will trigger a TypeError, so this except block will run
except TypeError as error:
    # these are all printed
    print("######## EXCEPT: TypeError ########")
    print("Oh dear, that is not allowed on that type")
    # this displays the error message that was caught be the except block (can help with debugging as it shows the exact issue)
    print(error)


# this is a catch-all exception - it will catch and handle any errors that occur in the try block, regardless of type
# since the most relevant except block was the TypeError one, that runs, and this except block does not
except Exception as error:
    print("######## EXCEPT: Exception ########")
    print("Generic catch-all except/catch block")
    print(error)


# the finally block tidies up things, like closing files/releasing resources -- it always runs
finally:
    # since the finally block always runs, the next two lines are printed
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")

    # this checks if names_tuple is True (i.e. is not empty)
    # if it is True that names_tuple is not empty...
    if names_tuple:
        # ...then replace it with a None value
        # this is how python tidies up/signals that names_tuple is no longer needed
        names_tuple = None

print("After exception handling is finished... the program can continue")