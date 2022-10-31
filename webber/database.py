
import sqlite3
import psycopg2


class DBManager:
    def __init__(self,type_="sqlite3",  dbname="unknown.db", host="localhost", user="root", password="root", post_id=5432):
        if type_ == "sqlite3":
            self.dbname = dbname
            self.connector = sqlite3.connect(self.dbname)
            self.cursor = self.connector.cursor()
        elif type_ == "psql":
            self.dbname = dbname
            self.host = host
            self.user = user
            self.password = password
            self.connector = psycopg2.connect(
	        host = hostname,
	        dbname = database,
	        user = username,
	        password = password,
	        port = port_id
            )
            self.cursor = self.connector.cursor()
        else:
            return "sqlite3 yoki psql ni tanlang"
        
    def create_table(self, table_name, **kwargs):
        script = ""
        for column,value_type in kwargs.items():
            script += f"{column} {value_type},"
        try:
            self.cursor.execute(
	        f"""
		CREATE TABLE IF NOT EXISTS {table_name}({script[:-1]});
		""")
            self.connector.commit()
            print("Jadval muvaqqiyatli yaratildi.")
        except:
            raise "DBManagerError: ivalid values"
    def insert_into(self,table_name:str,**kwargs): # ma'lumotlar bazasiga ma'lumot kiritish funksiyasi
        values = ""	# ma'lumotlar bazasi uchun qiymatlar
        get_values = "no"
        formating_values = "no"
        adding_values_to_table = "no"
        saving_values_to_table = "no"
        try:
            for column, value in kwargs.items(): # **kwargsdan ma'lumotlarni ajratib olish sikli
                get_values = "yes"
                value_type = str(type(value)) # qiymat tipini aniqlab olish
                if 'int' not in value_type:	# agar qiymat int bo'lsa
                    values += f"'{value}',"	# qiymatlarga qiymatni o'zini qo'shamiz
                else: # aks holda
                    values += f"{value}," # qimatni '' bir tirnoqlar yordamida qoshamiz 
            formating_values = "yes"
            self.cursor.execute(
		    f"""
		    INSERT INTO {table_name} VALUES({values[:-1]}); 
		    """) # va nihoyat qiymatlarni ma'lumotla bazasiga qo'shamiz
            adding_values_to_table = "yes"
            self.connector.commit() # ma'lumotlar bazasiga saqlaymiz
            saving_values_to_table = "yes"
            print(f"Get values............: {get_values}")
            print(f"Formating values......: {formating_values}")
            print(f"Adding values to table: {adding_values_to_table}")
            print(f"Saving values to table: {saving_values_to_table}")
        except:
            print('[31m', f"Get values: {get_values}")
            print('[31m', f"Formating values: {formating_values}")
            print('[31m', f"Adding values to table: {adding_values_to_table}")
            print('[31m', f"Saving values to table: {saving_values_to_table}")
            raise "DBManagerError: not insert"

    def get(self, table_name):
        script = f"""
        SELECT * FROM {table_name};
        """
        self.cursor.execute(script)
        self.connector.commit()
        return self.cursor.fetchall()
    