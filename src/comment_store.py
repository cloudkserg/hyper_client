import sqlite3
import email


class CommentStore():

    conn = None

    def __init__(self, store_file):
        self.conn = sqlite3.connect(store_file)

    def has_not_comment(self, comment):
        cursor = self.conn.execute(
                'SELECT COUNT(comment_id) FROM hyper_comments ' + 
                'WHERE comment_id =?  AND link=?', 
                [comment.comment_id, comment.link]
        )
        result = cursor.fetchone()
        if result is None:
            raise Exception('Not check in database isset of comment') 
        return result[0] == 0
        

    def save_comment(self, comment):
        self.conn.execute('INSERT INTO hyper_comments VALUES(?, ?)',
                [comment.comment_id, comment.link]
        );
        self.conn.commit()


