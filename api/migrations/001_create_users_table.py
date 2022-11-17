steps = [
    [
        # Create the table
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            email citext UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            full_name VARCHAR(100) NOT NULL
        );
        """,
        #  Drop the table
        """
        DROP TABLE users;
        """,
    ],
]
