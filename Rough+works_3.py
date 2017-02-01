
# coding: utf-8

# In[3]:

import pandas as pd

print("")
df = pd.read_csv("bookings.csv", sep = ",", names = ["book_name", "tot_psg"])
print(df)


# In[11]:

import sqlite3
import pandas as pd

conn = sqlite3.connect('airline_seating.db')
c = conn.cursor()

c.execute("SELECT * FROM rows_cols;")
for item in c:
    print(item)

total_rows = c.execute("SELECT * FROM rows_cols;").fetchone()[0]
seat_config = c.execute("SELECT * FROM rows_cols;").fetchone()[1]

print("Total rows in this airplane: %d" %total_rows)
print("Seat configuration: %s" %seat_config)

print("")

c = conn.cursor()

#list of pre-booked seats
pre_booked = []

#list of the details of pre-booked seats
pb_row = []
pb_pos = []
pb_psgname = []
pb_seats_list = []

print("List of passengers who have pre-booked their seats:")
c.execute("SELECT * FROM seating where name != '';")
for item in c:
    print(item)
    #pre_booked.append(c)
    row, pos, psgname = item
    pb_seats = str(row)+pos
    print(pb_seats)
    pb_row.append(row)
    pb_pos.append(pos)
    pb_psgname.append(psgname)
    pb_seats_list.append(pb_seats)

print("")
print(pb_row)
print(pb_pos)
print(pb_psgname)
print(pb_seats_list)

print("")
seat = ""
seat_list = []
for number in range(1,total_rows+1):
    #print(number)
    for letter in seat_config:
        #print(letter)
        seat_1 = str(number) + letter
        print(seat_1)
        seat_list.append(seat_1)
print(seat_list)

#initial empty airplane where os represents occupied seats
os = {}
for seat_2 in seat_list:
    os[seat_2] = ""
zip_occ_seats = list(zip(pb_seats_list, pb_psgname))
for occ_seats, occ_psgname in zip_occ_seats:
    os[occ_seats] = occ_psgname
print(os)

#list for number of available seats in each row
number_2 = list(range(1,total_rows+1))
#initial available seats
tot_avail_seats = []
for k in number_2:
    tot_avail_seats.append(len(seat_config))
#zip the row number and number of available seats in form of tuples
avail_seats = list(zip(number_2, tot_avail_seats))
print(avail_seats)

for item_2 in avail_seats:
    for tot_avail_seats in item_2:
        if tot_avail_seats >= 3:
            pass
            #print("2 seats available in this row")

print("")
infile = open("bookings.csv", "r")

for line in infile:
    print(line)



# In[10]:

for pn in df:
    print(pn)


# In[15]:

u = "abcd"
u[:4]


# In[ ]:



