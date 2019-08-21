# READ ME

Please insert your postgresql  `username` and `password` .

    params = {'host': 'server_name',
          'database': 'database',
          'user': 'user_name',
          'password': 'password'}

### Also edit your `table_names` and `column_names`
        commands = ("""     CREATE TABLE hvh_metrics.table_name (table_name_id SERIAL PRIMARY KEY,
                            Char_Column VARCHAR(255),
                            Text_Column TEXT,
                            Integer_Column NUMERIC(10),
                            Float_Column NUMERIC(10,2),
                            Date_Column DATE,
                            sysdatecreated timestamp NULL DEFAULT now(),
                            sysdatemodified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL)""")
