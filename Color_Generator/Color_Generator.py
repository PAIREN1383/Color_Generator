from random import randint

def color_generator(n_colors, n_repetitions): # Generate palette of colors.
    for r in range(n_repetitions): # Repeat several times.
        list_colors = []
        while len(list_colors) != n_colors: # How many colors are needed?
            color = ""
            for char in range(6): # Hex color code has 6 characters.
                color += (f"{randint(0, 15):x}")
            if color not in list_colors:
                list_colors.append(color)
        yield list_colors

def file_dir(): # Get the file directory to save the result file.
    full_path = __file__
    indx = full_path[-1::-1].find("\\")
    fdir = full_path[0:1].upper() + full_path[1:-(indx)]
    return fdir

def numerical_list(normal_list): # Create a numerical list to display the color codes.
    num = 1
    result_list = []
    for obj in normal_list:
        result_list.append(f"{num}: {obj}")
        num += 1
    return result_list

def check_name(fil_name):
    if "/" in fil_name or "\\" in fil_name or "<" in fil_name \
        or ">" in fil_name or "?" in fil_name or "|" in fil_name \
            or "*" in fil_name or ":" in fil_name or '"' in fil_name:
        return "Colors.html"
    if fil_name == ".html":
        return "Colors.html"
    return fil_name
    

def file_creator(file_name, number_of_colors, number_of_repetitions): # To write the result into the HTML file.
    START_OF_FILE = """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Generator</title>
</head>
<body>"""
    END_OF_FILE = """\n</body>
</html>"""
    START_OF_CONTENT = "\n    <div style=\"display:inline-block; width:100px; height:100px; background-color:#"
    with open(file_dir() + file_name, "x") as html_file:
        html_file.write(START_OF_FILE)
        list_number = 1
        for list_of_colors in color_generator(number_of_colors, number_of_repetitions):
            copy_list = list_of_colors.copy()
            info_list = numerical_list(copy_list)
            html_file.write(f"\n    <h3>{list_number}. List of color codes: {info_list}</h3>")
            color_number = 1
            for color in list_of_colors:
                END_OF_CONTENT = f"\">{color_number}</div>"
                html_file.write(START_OF_CONTENT + color + END_OF_CONTENT)
                color_number += 1
            html_file.write("\n    <br><br><br>")
            list_number += 1
        html_file.write(END_OF_FILE)
    
   
while True:
    print("-----------------------------------------------\
    \nWelcome to Color Generator program. \
    \n[0] Help \
    \n[1] Color Generator \
    \n[2] Exit \
    \n-----------------------------------------------")
    choose = input("Enter your choice: ")
    print("-----------------------------------------------")
    if choose == "0": # Help
        print(f"""###############################################
Help Content:
  Why was this tool created? 
    You can generate random colors to design a website or cover design for videos etc.


  How can I use it?
    Step one: Open the program.
    
    Step two: Enter '1'.
    
    Step tree: Choose how many colors the color combination contains. Enter a number like 10.
    
    Step four: You need several color combinations for finding an appropriate color combination.
    Enter a number like 100.
    
    Step five: Enter an appropriate name (without these characters: \/:*?"<>|) for new HTML file.
    The results will be in it. You do not need to end the name with '.html'.
    
    Step six: Enter 'q' or 'e' or '2' to exit the program.
    
    Step seven: Find the HTML file near the program and open it.
    It will be saved in the program directory.
    Right here: {file_dir()}



About Me:
  My GitHub Link: https://github.com/PAIREN1383
  Coded By: MohammadAli
###############################################""")
    if choose == "1": # Color Generator
        ncolors = int(input("Choose how many colors the color combination contains (ex: '5'): "))
        nrepetitions = int(input("Enter number of repetitions (ex: '50'): "))
        fname = input("Enter name of the new html file for the result (ex: 'newcolors'): ").strip() + ".html"
        correct_file_name = check_name(fname)
        file_creator(correct_file_name, ncolors, nrepetitions)
    if choose == "2" or choose.lower() == "e" or choose.lower() == "q": # Exit
        break