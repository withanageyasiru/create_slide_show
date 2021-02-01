1. Create and activate a Python 3 Virtual environment.

```python3 -m venv env```

```source env/bin/activate```

2. Install Requirements.

```pip install opencv-python```

```pip install Pillow```

```pip install mysql-connector-python```

3. Install MySQL and create a database in it.

4. Add images paths and delays to database

5. Run the app to store the details of the images.

```python main.py```

### Instructions for run the code

1. configure database details in db_connect.py
```python
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="image_data"
    )
```

2. for create gif , first import as follows  
```python
from create_GIF import create_gif
```
3. Call the create_gif method with giving following parameters 
```python
def create_gif(images: # paths of images as list,
               out_directory: # directory for save the output,
               delay: # delay in milliseconds
```
