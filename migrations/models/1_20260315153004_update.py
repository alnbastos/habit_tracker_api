from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "checkins" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" DATE NOT NULL,
    "notes" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "habit_id" INT NOT NULL REFERENCES "habits" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_checkins_habit_i_ed8e1c" UNIQUE ("habit_id", "date")
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "checkins";"""


MODELS_STATE = (
    "eJztmG1v2zYQgP+KoU8tkBWtFzdFv8mOs3jxy5Aoa9c0EGiJlghTpCtRTYzC/3086v21dh"
    "EvzuBPto531N3D0/HIH5rHbUyDNwMXW0vCtI+dHxpDHpZ/ykMnHQ2tVtkACASaU6VrRUpK"
    "iOaB8JElpHyBaIClyMaB5ZOVIBxewUJKQcgtqUiYk4lCRr6F2BTcwcLFvhy4u9NcNCfCJD"
    "bMbSOBtft7+Y8wGz/iAFTgcbU0FwRTuxBBZKPkplivlGzExIVShNnmpsVp6LFMebUWLmep"
    "NmECpA5m2JevhumFH0JI4HEcfRJl5H2mErmYs7HxAoVU5BBsycXiDJhKbwIVoANv+a377v"
    "Ts9MPv708/SBXlSSo520ThZbFHhorA1NA2mwgmijQUxoybolwhdy6l9egS/RI8EAvi4TfJ"
    "eB5jAq2NYyLIQGYJ9TQkWzCd68ZQccq4MC5wUAVj4MeGnEoNSmSkC1vwiLPmMHAYw88G+O"
    "wFwTcKgunf+vXgUr9+NdE/v1Yj63hkPJv+kahzWQmiEjEdjGf9ElDLxxC+iUR9ukH21JMt"
    "WrYlHvw5zOTTZAz2jNF1vNZt9EeT4Y2hT/4qLAGkKIx0C/gT6av3r4srkE7S+TQyLjvw2P"
    "kymw4VQR4Ix1dvzPSMLxr4hELBTcYfTGTnilkiTcAUFjZfs7esv3mTn1fhA1nBJyjEsHst"
    "lrV1WCGpIrzgPiYOu8JrRXIkXULMqqvA8RZ+mcxzeAQ3SRok0izBfPSQ7umF7JAByrCwUC"
    "EO9JuBfi4rNXCcI2v5gHzbLACFEd7lJUmqWx3yul5ZghhyFAAIA5wuoK1pm1LmzU2TimkP"
    "LdOxPdpve6R+K+QGLvIbuoBY/5eagOeoah56NClmjnDl47u3b1toJU2A1CrtNkl/0I3Gih"
    "t/3rMd+qmS2bGrqu+qOOX+LgmaGrzMDG37mhOcZ43ZeVbOzYWPZRzMWtcjHLLQq+y7BZyF"
    "CZ4ZqewGR+N/PnZsROj6K/s0HF7B4wPGS3iezKbGJQg8zoQLEn06vdXHIEKMhYhSFcXuRW"
    "OrmtFSMsqrYklaDvcbFqUhr3M2LzO1e9tw7DVz7FU4ksBEvuWS77hm9+9zTjFiDR1A0bIE"
    "dC5N90V0155o+/rbn83GhfrbH5UL7O2kP5S5qhBLJRK1nUmXcDzL/u/PsuHK/sWFLVoeF/"
    "ZZF1Y5XzlsN58ac1927nK7VC9jy4ura0xRQ1tavUc/vFVuOoZv9nl21rFPLFerOTzHIydt"
    "p2eU6RxPz0/5we/59Pwd+0Htsa+5j8uZvMw2rtvrbdHHSa3GRk6NFRsO+DR2gBirv0yAe7"
    "mEkG8UmNXs6n/ezKZNJ+XUpATylskA72xiiZMOJYG4P0ysLRQh6va7iPK1Q2lLhgn6dTfa"
    "/+XV7OZf6ingZQ=="
)
