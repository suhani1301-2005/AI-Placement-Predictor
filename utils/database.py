
import mysql.connector
import pandas as pd
import bcrypt
import streamlit as st

def connect_db():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        port=int(st.secrets["DB_PORT"]),
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"]
    )
def fetch_predictions():

    conn = connect_db()

    query = """
    SELECT * FROM prediction_history
    ORDER BY created_at DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def save_prediction(gender, ssc_p, hsc_p, degree_p,
                    workex, etest_p, mba_p,
                    prediction, probability):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO prediction_history
    (gender, ssc_p, hsc_p, degree_p,
     workex, etest_p, mba_p,
     prediction, probability)

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        gender,
        ssc_p,
        hsc_p,
        degree_p,
        workex,
        etest_p,
        mba_p,
        prediction,
        probability
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    # ===============================
# USER AUTHENTICATION
# ===============================

def email_exists(email):

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email=%s"

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user is not None


def register_user(name, email, password):

    conn = connect_db()
    cursor = conn.cursor()

    # Password Hashing
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    query = """
    INSERT INTO users(name,email,password)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            name,
            email,
            hashed_password.decode()
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def login_user(email, password):

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE email=%s
    """

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:

        if bcrypt.checkpw(
            password.encode(),
            user["password"].encode()
        ):

            return user

    return None
