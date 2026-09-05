import re 
import sys

CYAN = "\033[96m"
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"

print(CYAN + "========================================" + RESET)
print(CYAN + "          PASSWORD STRENGHT ANALYZER" + RESET)
print(CYAN + "========================================" + RESET)


print(CYAN + "[1] Analyze a password" + RESET)
print(CYAN + "[2] Generate a strong password" + RESET )
print(CYAN + "[3] Exit" + RESET + "\n\n ")

option = input(CYAN + "[?] Choose an option : " + RESET)

if bool(re.fullmatch(r"[123]" , option)) :
	if option == "1" : 
		password = input ("Enter the password : ")
		if bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}" , password)) :
			print(GREEN + "[+] Strong password! It meets all security requirements" + RESET)
		else : 
		    print(RED + "[-] Weak password! It must contain:" + RESET)
		    print(RED + "    - At least 8 characters" + RESET)
		    print(RED + "    - At least one uppercase letter (A-Z)" + RESET)
	   	    print(RED + "    - At least one lowercase letter (a-z)" + RESET)
    		    print(RED + "    - At least one number (0-9)" + RESET)
		    print(RED + "    - At least one special character" + RESET)
	elif option == "2" :
		print("2")
	elif option == "3" :
		sys.exit()

else : 
	sys.exit()
