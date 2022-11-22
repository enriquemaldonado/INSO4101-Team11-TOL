import psycopg2


class UserDAO:

    def __init__(self):
        dbconfig = {
            'user': 'xnqetbvoclwwxm',
            'password': 'dd9eff208b16bb45d96643a829b693c9cb70493e6c851b59b17dc34ba9dc5fd5',
            'dbname': 'd31mq77kut9iff',
            'dbhost': 'ec2-44-195-100-240.compute-1.amazonaws.com',
            'dbport': 5432
        }

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s " \
                         % (
                         dbconfig['dbname'], dbconfig['user'], dbconfig['password'], dbconfig['dbhost'], dbconfig['dbport'])

        self.conn = psycopg2.connect(connection_url)


    def insertUser(self, uname, uemail, upassword):
        cursor = self.conn.cursor()
        query = "insert into users(uname, uemail, upassword) values (%s, %s, %s) on conflict do nothing returning uid;"
        cursor.execute(query, (uname, uemail, upassword))

        uidfetch = cursor.fetchone()
        if uidfetch is None:
            uid = 0;
        else:
            uid = uidfetch[0]
        self.conn.commit()
        return uid

    def deleteUser(self, user, auth):
        cursor = self.conn.cursor()
        query = "delete from users as u where u.uemail = %s and u.upassword = %s returning *;"
        cursor.execute(query, (user, auth))

        uidfetch = cursor.fetchone()
        result = {}
        if uidfetch is None:
            result["UserID"] = 0
            result["Name"] = 0
            result["Email"] = 0
            result["Password"] = 0
        else:
            result["UserID"] = uidfetch[0]
            result["Name"] = uidfetch[1]
            result["Email"] = uidfetch[2]
            result["Password"] = uidfetch[3]
        self.conn.commit()
        return result