import anydbm

db = anydbm.open('Test','c') #create

db['Record'] = 'Value'
db['Record1'] = 'Value'

for k,v in db.iteritems():
  print k,'\t', v

db.close()

#you can't write a non-string key or value!
