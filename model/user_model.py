import mysql.connector
import json
class user_model():
  def __init__(self):
    #connection establishment
    try:
      self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='flask_schema')
      self.conn.autocommit=True
      self.cur=self.conn.cursor(dictionary=True)
      print("success")
    except:
      print('error')
  def user_getall_model(self):
    self.cur.execute("SELECT * from users")
    res=self.cur.fetchall()
    if len(res)>0:
      return json.dumps(res)
    else:
      return "<h1>No data found</h1>"
  
  def user_addone_model(self,data):
    self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) values('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
    
    return "user created successfully"
  
  def user_update_model(self,data):
    self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
    if self.cur.rowcount>0:
      return "user updated successfully"
    else:
      return "Nothing to update"
    
  def user_delete_model(self,id):
    self.cur.execute(f"DELETE FROM users WHERE id={id}")
    if self.cur.rowcount>0:
      return "user deleted successfully"
    else:
      return "Nothing to delete"