import sqlite3


class PachicoPipeline:
    conn = sqlite3.connect('pachico.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `pachico` (
                                                title varchar(100),
                                                description text
                                                )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]

        self.cursor.execute(f"""select * from pachico where title = '{title}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `pachico`
                                            (`title`, `description`)
                                            values (?, ?)""", (title, description))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
