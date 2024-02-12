text = "Yooooo\n this is some text blud \n heve a good one\n"
text2 = "have a nice day"
with open('test.txt', 'w') as file:
    file.write(text)

with open('test.txt', 'a') as file:
    file.write(text2)