def mysteryThree(original_text:str,copied_text:str):
    #this function returns a copy of the input A, repeated as many times as the length of B


    if isinstance(copied_text,str) and isinstance(original_text,str):# checks if A and B is an integer
        return original_text*len(copied_text)

    if not isinstance(copied_text,str):
        return "Error, copied_text must be a string"

    if not isinstance(original_text,str):
        return "Error, original_text must be a string"