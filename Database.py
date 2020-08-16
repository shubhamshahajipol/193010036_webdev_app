import sqlite3
db = sqlite3.connect('Registration')
rs = db.cursor()

#rs.execute('''create table Register(name varchar(50), email varchar(100), password varchar(10))''')
#db.commit()
rs.execute('''insert into Register values('shubh', '@gmail.com', 'shubham1234#')''')
db.commit()
rs.execute('select * from Register')
for i in rs:
    print(i)