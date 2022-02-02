#monthly expenses
jan=2200,
February=2350,
March=2600,
April=2130,
May=2190,
#create list
exe=[2200,2350,2600,2130,2190]
print(exe)
#1.in feb how much dollars extra u spent compare to jan.
print("in  feb this much ammount   extra spent comared jan:",exe[1]-exe[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print("this much ammount was total exepenses in first quater of the year:",exe[0]+exe[1]+exe[2])
#3.3. Find out if you spent exactly 2200 dollars in any month.
print("did i spent exactly 2000$ in any month?:",2200 in exe)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exe.append(1980)
print("exepenses at the end of the june month:",exe)
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this.
exe[3]=exe[3]-200
print("exepenses after 200$ return in april:",exe)

