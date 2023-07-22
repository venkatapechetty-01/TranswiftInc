DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',  
        'NAME': 'TranswiftInc',
        'HOST': '.\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
