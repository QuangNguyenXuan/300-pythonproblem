word = input("Enter a word")
user_word = word.lower()
flg = "no"
# a e i o u
for i in user_word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        flg = "yes"


file = open("vowlfile.txt","w")
if flg == "yes":
    print("Your word is "+user_word)
else:
    file.write(user_word)
    file.close()
    print("It did not contian any vowel that is "+user_word)

