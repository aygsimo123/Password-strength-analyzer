import re 

CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "========================================" + RESET)
print(CYAN + "          PASSWORD STRENGHT ANALYZER" + RESET)
print(CYAN + "========================================" + RESET)


print(CYAN + "[1] Analyze a password" + RESET)
print(CYAN + "[2] Generate a strong password" + RESET )
print(CYAN + "[3] Exit" + RESET + "\n\n ")

option = input(CYAN + "[?] Choose an option : " + RESET)

if bool(re.fullmatch(r"^[123]" , option)) :
	if option == 1 : 
		print("1")
	elif option == 2 :
		print("2")
	elif option == 3 :
		sys.exit()

else : 
	sys.exit()
