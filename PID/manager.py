from django.db import models


class UserManager(models.Manager):
    def all_user(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""SELECT login FROM pid_user""")
            result_list = []
            for row in cursor.fetchall():
                result_list.append(row[0])
        return result_list
