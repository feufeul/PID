from . import models
#from django import models


class UserManager():
    def all_user(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""SELECT login FROM PID_user""")
            result_list = []
            for row in cursor.fetchall():
                result_list.append(row[0])
        return result_list


class ShowManager():
    def all_show(self):
        result_list = models.Show.objects.all()
        from django.db import connection
 #       with connection.cursor() as cursor:
  #          cursor.execute("""SELECT title, price, bookable FROM pid_show""")
   #         result_list = []
    #        for row in cursor.fetchall():
     #           result_list.append(row)
        for i in result_list:
            print(i.login)
        return result_list
