

favorite_languages = {'jen':'python', 'sarah':'c', 'edward':'rust', 'phil':'python'}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['phil', 'lee', 'jayden', 'jordan', 'sarah', 'jaymeir', 'danny']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")