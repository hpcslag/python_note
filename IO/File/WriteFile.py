s = "Hello world this file created by python3 file module"

try:
  FILE = open('Test.txt')
  FILE.write("{0}".format(s))
  FILE.close()
  print("Write file -> Test.txt ")
except IOError as e:
  print(e)
