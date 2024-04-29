# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        # Инициализация объекта пользователя с ID, именем и уровнем доступа
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        # Возвращает идентификатор пользователя
        return self._user_id

    def get_name(self):
        # Возвращает имя пользователя
        return self._name

    def set_name(self, name):
        # Устанавливает новое имя пользователя
        self._name = name

    def get_access_level(self):
        # Возвращает уровень доступа пользователя
        return self._access_level

    def __str__(self):
        # Возвращает строковое представление объекта User
        return f"User(ID={self._user_id}, Name={self._name}, Access Level={self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        # Инициализация объекта администратора с уровнем доступа 'admin'
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []  # Список для хранения пользователей

    def add_user(self, user):
        # Добавляет пользователя в список, если он еще не добавлен
        if user not in self._user_list:
            self._user_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("User already in list.")

    def remove_user(self, user):
        # Удаляет пользователя из списка, если он в нем присутствует
        if user in self._user_list:
            self._user_list.remove(user)
            print(f"User {user.get_name()} removed.")
        else:
            print("User not found in list.")

    def list_users(self):
        # Выводит информацию о всех пользователях в списке
        for user in self._user_list:
            print(user)

    def __str__(self):
        # Возвращает строковое представление объекта Admin
        return f"Admin(ID={self._user_id}, Name={self._name}, Access Level={self._access_level})"


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin("1", "Alice")

    # Создаем несколько пользователей
    user1 = User("2", "Bob")
    user2 = User("3", "Charlie")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Вывод списка пользователей
    admin.list_users()

    # Удаление пользователя
    admin.remove_user(user1)

    # Вывод списка пользователей после удаления
    admin.list_users()