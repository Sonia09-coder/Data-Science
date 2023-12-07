#Functions with output:
'''def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())

format_name("sOnIA","BhAGAt ")'''

def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs."
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    print("This got printed")

print(format_name(input("What's your first name? "),input("What's your last name?")))
