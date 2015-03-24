"Hello world"[1] //H

"Hello world"[1:3] //Hel

"{0}".format("Hello world")//Hello world
"{wow}".format(wow="ABC")//ABC
"{0[0],0[1]}".format(["Hello"," world"])//Hello world

number = 10
string = "Hello world"

string + number //Error
print(string,number) //Hello world10
string + str(number) //Hello world10

len(string) //11

for s in string:
  print(s+"1")
  //H1l1l1o1 1w1o1r1l1d1

int("12") //12

colors = dict(green='#123',red='#321')
color = "green color hex code is {green}, and red color hex code is {red}" //#123,#321
