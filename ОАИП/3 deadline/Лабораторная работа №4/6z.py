import datetime
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.posts = []
        self.registration_date = datetime.datetime.now()
        print(f"Создан пользователь: {self.username} (ID: {self.user_id})")
    def create_post(self, content):
        """Создать новый пост"""
        post = Post(content, self)
        self.posts.append(post)
        return post
    def get_user_info(self):
        """Получить информацию о пользователе"""
        return f"Пользователь: {self.username}\nEmail: {self.email}\nЗарегистрирован: {self.registration_date.strftime('%d.%m.%Y %H:%M')}\nПостов: {len(self.posts)}"
    def show_all_posts(self):
        """Показать все посты пользователя"""
        print(f"\n=== Все посты пользователя {self.username} ===")
        if len(self.posts) == 0:
            print("У пользователя пока нет постов")
        else:
            for post in self.posts:
                print(f"\n{post.get_post_info()}")
class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now()
        self.comments = []
        print(f"Создан новый пост от {author.username}")
    def add_comment(self, user, comment_text):
        """Добавить комментарий к посту"""
        comment = Comment(comment_text, user, self)
        self.comments.append(comment)
        return comment
    def delete_post(self):
        """Удалить пост (вместе с комментариями)"""
        print(f"Удаляем пост и все комментарии к нему")
        if self in self.author.posts:
            self.author.posts.remove(self)
        return True
    def get_post_info(self):
        """Получить информацию о посте"""
        info = f"Пост от: {self.author.username}\n"
        info += f"Дата: {self.created_at.strftime('%d.%m.%Y %H:%M')}\n"
        info += f"Содержимое: {self.content}\n"
        info += f"Комментариев: {len(self.comments)}"
        if len(self.comments) > 0:
            info += "\nКомментарии:"
            for i, comment in enumerate(self.comments, 1):
                info += f"\n  {i}. {comment.get_comment_info()}"
        return info
    def show_comments(self):
        """Показать все комментарии к посту"""
        print(f"\n=== Комментарии к посту ===")
        print(f"Пост: '{self.content[:50]}...'")
        if len(self.comments) == 0:
            print("Пока нет комментариев")
        else:
            for comment in self.comments:
                print(f"\n{comment.get_comment_info()}")
class Comment:
    def __init__(self, text, author, post):
        self.text = text
        self.author = author
        self.post = post
        self.created_at = datetime.datetime.now()
        print(f"Добавлен комментарий от {author.username}")
    def get_comment_info(self):
        """Получить информацию о комментарии"""
        return f"{self.author.username}: {self.text}\n   ({self.created_at.strftime('%d.%m.%Y %H:%M')})"
if __name__ == "__main__":
    print("=== СОЦИАЛЬНАЯ СЕТЬ ===\n")
    print("1. Создаем пользователей:")
    user1 = User(1, "Анна", "anna@example.com")
    user2 = User(2, "Борис", "boris@example.com")
    user3 = User(3, "Виктор", "viktor@example.com")
    print("\n" + "="*50 + "\n")
    print("2. Пользователь 1 создает пост:")
    post1 = user1.create_post("Привет всем! Сегодня отличный день для прогулки в парке!")
    print("\n" + "="*50 + "\n")
    print("3. Другие пользователи комментируют пост:")
    comment1 = post1.add_comment(user2, "Согласен! Погода просто замечательная!")
    comment2 = post1.add_comment(user3, "Я только что вернулся из парка - там красиво!")
    comment3 = post1.add_comment(user1, "Спасибо за комментарии! Присоединяйтесь!")
    print("\n" + "="*50 + "\n")
    print("4. Информация о посте:")
    print(post1.get_post_info())
    print("\n" + "="*50 + "\n")
    print("5. Пользователь 2 создает свой пост:")
    post2 = user2.create_post("Кто смотрел новый фильм? Поделитесь впечатлениями!")
    post2.add_comment(user1, "Я смотрел! Очень понравилось!")
    post2.add_comment(user3, "Еще не видел, но собираюсь в выходные")
    print("\n" + "="*50 + "\n")
    print("6. Все посты пользователя Анна:")
    user1.show_all_posts()
    print("\n" + "="*50 + "\n")
    print("7. Все посты пользователя Борис:")
    user2.show_all_posts()
    print("\n" + "="*50 + "\n")
    print("8. Удаляем пост 1:")
    post1.delete_post()
    print("\n" + "="*50 + "\n")
    print("9. Проверяем посты пользователя 1 после удаления:")
    user1.show_all_posts()
    print("\n" + "="*50 + "\n")
    print("10. Создаем еще один пост:")
    post3 = user3.create_post("Рекомендую книгу 'Мастер и Маргарита' - шедевр!")
    post3.add_comment(user1, "Одна из моих любимых книг!")
    post3.add_comment(user2, "Читал в школе, нужно перечитать")
    print("\n" + "="*50 + "\n")
    print("11. Информация о посте 3:")
    print(post3.get_post_info())
    print("\n" + "="*50 + "\n")
    print("12. Демонстрация связей между объектами:")
    test_comment = post3.comments[0]
    print(f"Комментарий: '{test_comment.text}'")
    print(f"Автор комментария: {test_comment.author.username}")
    print(f"Пост комментария: '{test_comment.post.content[:30]}...'")
    print("\n" + "="*50 + "\n")
    print("13. Информация о пользователях:")
    print(user1.get_user_info())
    print()
    print(user2.get_user_info())
    print()
    print(user3.get_user_info())
