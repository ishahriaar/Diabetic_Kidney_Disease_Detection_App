# Installation Guide
1. Make sure python and pip are installed on your machine.
2. Create a virtual env(Linux/Mac)<br>
   ```python -m venv env```
   <br>```Note: This step is requared when project dosen't come with virtual env or you want to create your own virtual env.```
3. Activate the virtual env<br>
   Linux/Mac: ```source env/bin/activate```<br>
   Windows: [click here](https://docs.djangoproject.com/en/3.2/howto/windows/)
4. Install all the requirements packages<br>
    ```pip install -r requirements.txt```
   
5. Run ```python manage.py runserver``` from terminal.
6. Open browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)