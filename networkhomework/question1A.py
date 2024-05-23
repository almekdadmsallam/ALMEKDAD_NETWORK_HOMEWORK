import termcolor
import pyfiglet
# Definition of the first list
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
# Definition of the second list
L2 = [80, 443, 21, 53]
# convert it to dictionary
d = dict(zip(L1, L2))
# Show the output to verify the answer
print(d)
print(termcolor.colored(pyfiglet.figlet_format(
    "supervised by Dr. Muhannad Issa"), color="green"))
