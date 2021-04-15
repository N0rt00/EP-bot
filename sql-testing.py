import mysql.connector
import time

time = str(time.time())
output = []


card = "4E 0F 7B 9I"
card = list(card)
card.insert(0, "'")
card.append("'")
card = ''.join(card)

mydb = mysql.connector.connect(
  host="localhost",
  user="samthornton",
  password="Bl0cks#123",
  database="Myki"
)

mycursor = mydb.cursor()

def card_info(card):
    command = "select * from myki where myki_number = " + card
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    for x in myresult:
        return(x)

output = card_info(card)
last_time = float(output[-1])

mycursor.execute("start transaction")

if output[1] == 1:
    print('touched off')
    command = "update myki set touched_on = 0 where id = " + str(output[0])
    mycursor.execute(command)

    if (last_time + 7200) < float(time) and output[-2] <= 2:
        command = "update myki set balance = balance - 4.50 where id = " + str(output[0])
    elif output[-2] == 1 and last_time + 7200 > time:
        command = "update myki set balance = balance - 9.00 where id = " + str(output[0])
    mycursor.execute(command)

else:
    print('touched on')
    command = "update myki set touched_on = 1, times_day = times_day + 1 ,touched_time = " + time + " where id = " + str(output[0])
    mycursor.execute(command)

print(output)

print(card_info(card))
mycursor.execute("rollback")
