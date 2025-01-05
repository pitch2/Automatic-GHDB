import argparse
import webbrowser

# Setting argparse
parser = argparse.ArgumentParser(description='Automatic Google Dorks')
parser.add_argument('-a', '--autobrowser', action='store_true', help='Open in web browser your research')
parser.add_argument('-t', '--type', type=str, metavar='', required=False , help='Type document (ex : pdf, odt, xml, csv...)')
parser.add_argument('-r', '--research', type=str, metavar='', required=False , help='Add research (ex: Thomas) and add "" for multiple word')
parser.add_argument('-u', '--inurl', type=str, metavar='', required=False , help='Searches for a URL matching one (ex: /phpmyadmin/setup)')
parser.add_argument('-s', '--site', type=str, metavar='', required=False , help='Searches for a URL matching one (ex: lemonde.fr )')
parser.add_argument('-i', '--intitle', type=str, metavar='', required=False , help='Searches for occurrences of keywords in title all or one')
parser.add_argument('--before', type=str, metavar='', required=False , help='before date (yyyy-mm-dd)')
parser.add_argument('--after', type=str, metavar='', required=False , help='after date (yyyy-mm-dd)')
parser.add_argument('--numrange_one', type=str, metavar='', required=False , default=False, help='Used to locate specific numbers in your searches (first number)')
parser.add_argument('--numrange_two', type=str, metavar='', required=False , default=False, help='Used to locate specific numbers in your searches (second number)')


args = parser.parse_args()

# Simplify args
web = args.autobrowser 
type = args.type
research = args.research
inurl = args.inurl
site = args.site
intitle = args.intitle
before = args.before
after = args.after
numrange_1 = args.numrange_one
numrange_2 = args.numrange_two

# Basic var
expression = []
error = False

if research:
    expression.append(f"'{research}'")

if type:
    expression.append(f":{type}")
    
if before:
    expression.append(f"before:{before}")
    
if after:
    expression.append(f"after:{after}")

if inurl:
    expression.append(f"inurl:'{inurl}'")
    
if site:
    expression.append(f"site:'{site}'")
    
if intitle:
    expression.append(f"intitle:'{intitle}'")
    
if numrange_1 and numrange_2 :
    expression.append(f"numrange:{numrange_1}..{numrange_2}")

if (numrange_1 and (numrange_2==False)) or ((numrange_1==False) and numrange_2):
    print("Error : give numrange_1 AND numrange_2")
    error = True
    
if error != True:
    expression = (" ".join(expression))
    print(expression)
    if web:
        webbrowser.open_new_tab(f"https://www.google.com/search?q={expression.replace(' ', '+')}")

#python3 main.py -i "/phpmyadmin" -t pdf --after 2024-10-10
#python3 main.py -r "Thomas Pesquet" -s 'lemonde.fr'