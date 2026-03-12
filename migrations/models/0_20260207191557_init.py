from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "habits" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "color" VARCHAR(7) NOT NULL,
    "frequency" VARCHAR(10) NOT NULL,
    "category" VARCHAR(50) NOT NULL,
    "is_archived" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "habits"."frequency" IS 'DAILY: daily\nWEEKLY: weekly\nMONTHLY: monthly\nANNUALLY: annually';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl21P2zAQgP9KlU9MYgg6CohvKWRrtzaZIAwGQ5GbuInVxO4SB6gQ/30+J2le2kQtgk"
    "ElPjW+F/vu8dX2PSoBc7Af7fTQiHDluPWoUBRg8VFWbLcUNJ3mYhBwNPKlpQcmUoRGEQ+R"
    "DRONkR9hIXJwZIdkygmjQkpj3wchs4UhoW4uiin5G2OLMxdzD4dCcXMrxIQ6+AFH2XA6sc"
    "YE+04pUuLA2lJu8dlUyvqUf5WGsNrIspkfBzQ3ns64x+jcmlCZoospDhHHMD0PYwgfokvz"
    "zDJKIs1NkhALPg4eo9jnhXRXZGAzCvxENJFM0IVVPrf39g/3j74c7B8JExnJXHL4lKSX55"
    "44SgK6qTxJPeIosZAYc27yd4HciYfC5egy+wo8EXIVXoaqiV4myPHlJfNC/AL0YPmYutwT"
    "w73d3QZav9Szk556tiWsPkE2TJRxUt16qmonOkCaIyxGtkDSxA81RVhxexbQtNj+I88GfK"
    "Z2ZULMQRT99YvUtobqlQQazFLNwNC/ZeYFyicDo1uBK3ixcJ0CnTtsZoU2/ZsznIe11XlY"
    "rc1xiEUe1J4tR6jROJAY+yIkRG28gLM0wRsjVU7V/uD3cctBxJ/9oZea9gOG9xhPYDw0dL"
    "MHgoBR7oFE1fULdQAiRGmMfF9msf6hsdKZ0XBkVHfFFrRcFtZsSk1dF3w2s7Q7q3Ds1HPs"
    "LHAkkYVC2yN3eMnt32XMx4jWvADKnhWgI+H6WkTXfROtfv52DWNQOn+7/eoBezHsaqJWJW"
    "JhRDguvhIKBRpiSNtCfJHrqdBwEuCaMi15Vrg6qetO9vFOy1bk4BhUnBbJDdt05/WH2rmp"
    "Dn+WwJ+qpgaadunSy6RbB5USn0/SuuybvRYMW9eGrkmCLOJuKFfM7cxrBWJCMWcWZfcWcg"
    "ovz0yagSltbDx1nrmxZc+PjX3TjZXBQy80nhRe9SAYIXtyj0LHWtCwNquzXVQF7aAqQRS5"
    "cleALUSZNocqDontKUvaxlSz3dQ3otzmo298yVJ/5b7xDofR0oan/gVTcNnMB0y701nhBS"
    "Osap8wUle+auGvsQbE1HwzAb5K+y1W5Jguuc++nxt6XY84d6mAvKAiwRuH2Hy75ZOI375P"
    "rA0UIevmLrzacFcuI5gAuvA3vV6e/gGaiJIT"
)
