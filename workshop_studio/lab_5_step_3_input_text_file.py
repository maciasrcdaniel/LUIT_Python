
# get input form an external file 
# with open(filename, 'r' ) as variable_name:
#     <Do something with the variable here>

def open_input(file): 
    with open(file, 'r') as f: 
        text = f.read() # we use read() to read the actual contents of the file
        print(text)
        
def main(): 
    open_input('text.txt')
    
if __name__ == '__main__': 
    main()
    
    