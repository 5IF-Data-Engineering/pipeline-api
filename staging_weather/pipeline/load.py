import psycopg2
from event_streaming.settings import (
    POSTGRES_PORT,
    POSTGRES_HOST,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
)


def load_data_year(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather_year (year,  avg_temperature, min_temperature,
                max_temperature, avg_humidity, avg_rain, max_rain, min_rain,
                avg_wind_speed, max_wind_speed, min_wind_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)
        """
        params = (
            data["year"],
            data["avg_temperature"],
            data["min_temperature"],
            data["max_temperature"],
            data["avg_humidity"],
            data["avg_rain"],
            data["max_rain"],
            data["min_rain"],
            data["avg_wind_speed"],
            data["max_wind_speed"],
            data["min_wind_speed"],
        )
        cur.execute(query, params)
        conn.commit()
    cur.close()
    conn.close()


def load_data_month(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather_month (month,  avg_temperature, min_temperature,
                max_temperature, avg_humidity, avg_rain, max_rain, min_rain,
                avg_wind_speed, max_wind_speed, min_wind_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)
        """
        params = (
            data["month"],
            data["avg_temperature"],
            data["min_temperature"],
            data["max_temperature"],
            data["avg_humidity"],
            data["avg_rain"],
            data["max_rain"],
            data["min_rain"],
            data["avg_wind_speed"],
            data["max_wind_speed"],
            data["min_wind_speed"],
        )
        cur.execute(query, params)
        conn.commit()
    cur.close()
    conn.close()


def load_data_hour(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather_hour (hour,  avg_temperature, min_temperature,
                max_temperature, avg_humidity, avg_rain, max_rain, min_rain,
                avg_wind_speed, max_wind_speed, min_wind_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)
        """
        params = (
            data["hour"],
            data["avg_temperature"],
            data["min_temperature"],
            data["max_temperature"],
            data["avg_humidity"],
            data["avg_rain"],
            data["max_rain"],
            data["min_rain"],
            data["avg_wind_speed"],
            data["max_wind_speed"],
            data["min_wind_speed"],
        )
        cur.execute(query, params)
        conn.commit()
    cur.close()
    conn.close()


def load_data_year_month(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather_year_month (id, year, month,  avg_temperature, min_temperature,
                max_temperature, avg_humidity, avg_rain, max_rain, min_rain,
                avg_wind_speed, max_wind_speed, min_wind_speed)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)
        """
        data_month = str(data["month"])
        if data["month"] < 10:
            data_month = "0" + str(data["month"])
        params = (
            str(data["year"]) + data_month,
            data["year"],
            data["month"],
            data["avg_temperature"],
            data["min_temperature"],
            data["max_temperature"],
            data["avg_humidity"],
            data["avg_rain"],
            data["max_rain"],
            data["min_rain"],
            data["avg_wind_speed"],
            data["max_wind_speed"],
            data["min_wind_speed"],
        )
        cur.execute(query, params)
        conn.commit()
    cur.close()
    conn.close()


def load_data_weekday_weekend(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather_weekday_weekend (day_type, avg_temperature, min_temperature,
                max_temperature, avg_humidity, avg_rain, max_rain, min_rain,
                avg_wind_speed, max_wind_speed, min_wind_speed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)
        """
        params = (
            data["day_type"],
            data["avg_temperature"],
            data["min_temperature"],
            data["max_temperature"],
            data["avg_humidity"],
            data["avg_rain"],
            data["max_rain"],
            data["min_rain"],
            data["avg_wind_speed"],
            data["max_wind_speed"],
            data["min_wind_speed"],
        )
        cur.execute(query, params)
        conn.commit()
    cur.close()
    conn.close()