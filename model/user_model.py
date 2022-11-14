import mysql.connector
import json
class user_model():
    def __init__(self):
        #connection establishment
        #using self variable become global variable
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="saadb")
            self.con.autocommit=True #This will automatically commit DML query
            self.cur=self.con.cursor(dictionary=True)
            print("Connected Successfully")
        except:
            print("Connection not with database")

    def user_getall_moddel(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        #print(result)
    
    def user_addone_moddel(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
       # print(data['name']) print single field
         # print(data) print all record
        return "user created successfully!"
    
    def user_update_moddel(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount >0:
            return "user updated successfully!"
        else:
            return"Nothing to update"
    
    def user_delete_moddel(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount >0:
            return "user deleted successfully!"
        else:
            return"Nothing to delete"
    