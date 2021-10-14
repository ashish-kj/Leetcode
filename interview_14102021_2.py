#inputs
name = list(input())
typed = list(input())

mod_name = list()
mod_typed = list()
new_entry = list()

i = 0
letter_counter = 0

while(i < len(name) - 1):
    if name[i] == name[i+1]:
        letter_counter += 1
    else:
        mod_name.append([name[i],letter_counter+1])
        letter_counter = 0
    i += 1
mod_name.append([name[i],letter_counter+1])

i = 0
letter_counter = 0

while(i < len(typed) - 1):
    if typed[i] == typed[i+1]:
        letter_counter += 1
    else:
        mod_typed.append([typed[i],letter_counter+1])
        letter_counter = 0
    i += 1
mod_typed.append([typed[i],letter_counter+1])

print(mod_name)
print(mod_typed)

if(len(mod_name)!=len(mod_typed)):
            print("False + Break")

i = 0
letter_counter = 0

while(i<len(mod_name)):
    if(mod_name[i][0] == mod_typed[i][0] and mod_name[i][1] <= mod_typed[i][1]):
        i+=1
    else:
        letter_counter +=1
        break
if(letter_counter == 1):
    print(False)
else:
    print(True)