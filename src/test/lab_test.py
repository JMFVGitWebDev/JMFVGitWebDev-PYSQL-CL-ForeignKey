import sqlite3
import unittest

from src.main.lab import problem1


def _has_text_affinity(declared_type):
    declared_type = (declared_type or "").upper()
    return any(marker in declared_type for marker in ("CHAR", "CLOB", "TEXT"))


def _has_integer_affinity(declared_type):
    return "INT" in (declared_type or "").upper()


class LabTest(unittest.TestCase):
    def test_problem1(self):
        """
        This test calls the function with the SQL syntax that you wrote, then:
        1. Attempts to insert a valid row into the post table to ensure the table was created correctly.
        2. Checks that id, post, and user_fk actually have the expected types - not just any type. SQLite
           will happily store a string in an INTEGER-declared column (and vice versa) regardless of what was
           declared, so a successful insert alone doesn't prove the student used the right datatypes.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO post (post, user_fk) VALUES ('test post123', 1)")
            conn.commit()
            cur.execute("PRAGMA table_info(post);")
            columns = {row[1].lower(): row[2] for row in cur.fetchall()}
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        self.assertIn("id", columns, "id column was not found")
        self.assertTrue(
            _has_integer_affinity(columns["id"]),
            f"id should be an integer type, but it was declared as '{columns['id']}'",
        )

        self.assertIn("post", columns, "post column was not found")
        self.assertTrue(
            _has_text_affinity(columns["post"]),
            f"post should be a text type (e.g. varchar(255)), but it was declared as '{columns['post']}'",
        )

        self.assertIn("user_fk", columns, "user_fk column was not found")
        self.assertTrue(
            _has_integer_affinity(columns["user_fk"]),
            f"user_fk should be an integer type (e.g. int), but it was declared as '{columns['user_fk']}'",
        )

    def test_problem1_ref_integrity(self):
        """
        This test uses a fresh copy of the table (from a new call to problem1()) and checks if you can input a
        fk that doesn't exist in the users table.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO post (post, user_fk) VALUES ('test post123', 100)")
            conn.commit()
            print("problem1: foreign key constraint not added.")
            self.fail("insert with an invalid user_fk was allowed through")
        except sqlite3.IntegrityError:
            pass
        finally:
            conn.close()


if __name__ == "__main__":
    unittest.main()
