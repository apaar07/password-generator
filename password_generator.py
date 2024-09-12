import random
print("welcome to the password generator!")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['$','%','&','*','@']
numbers = ['1','2','3','4','5','6','7','8','9','0']
pswd_characters = int(input("how many characters would u like your password to be of ?"))
pswd_symbols = int(input("how many symbols would u like in your password ?"))
pswd_numbers = int(input("how many numbers would u like in your password ?"))

# easy

password = ""
for i in range(0,pswd_characters):
        password += random.choice(letters)

for i in range(0,pswd_symbols):
        password += random.choice(symbols)

for i in range(0,pswd_numbers):
        password += random.choice(numbers)

print("your required password is : " , password)

# hard

password_list = []
for i in range(0,pswd_characters):
        password_list.append(random.choice(letters))

for i in range(0,pswd_symbols):
        password_list.append(random.choice(symbols))

for i in range(0,pswd_numbers):
        password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)

password = ""
for i in password_list:
        password+=i
print("your required password is : ",password)
