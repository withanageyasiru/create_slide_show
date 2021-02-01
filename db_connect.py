import mysql.connector
import numpy as np

class db_connect:
  mydb = None
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="image_data"
    )

  def get_image(self,id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM image where img_id IN (%s)" % ','.join([str(x) for x in id]))
    image = mycursor.fetchall()
    return np.array(image)

  def get_all_image(self):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM image")
    images = mycursor.fetchall()
    return np.array(images)

  def get_callout(self,id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM callouts where clo_id = " + str(id))
    callout = mycursor.fetchone()
    return np.array(callout)

  def get_font(self,id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM allfonts where font_id = " + str(id))
    font = mycursor.fetchone()
    return np.array(font)

  def get_content(self,id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM content where cnt_id = " + str(id))
    content = mycursor.fetchone()
    return np.array(content)

  def get_delay(self,id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM alldelays where delay_id = " + str(id))
    delay = mycursor.fetchone()
    return np.array(delay)


