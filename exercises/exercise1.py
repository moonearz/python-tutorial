"""
Exercise: write a program to print a message to the terminal 5 times, then a different message 5 times

extra credit -- make the messages alternate

extra extra credit -- make the messages follow the pattern ab ba ab ba ab
"""

message1 = "what's up brother?"
message2 = "special teams, special plays, special players"

for i in range(10):
    if i < 5:
        print(message1)
    else:
        print(message2)

""" 
#extra credit
for i in range(5):
    print(message1)
    print(message2)
"""

""" 
#extra extra credit
for i in range(5):
    if i % 2 == 0:
        print(message1)
        print(message2)
    else:
        print(message2)
        print(message1)
"""