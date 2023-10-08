users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
users_visits = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}
users_visits['Общее количество'] = len(users)
users_visits['Уникальные посещения'] = len(set(users))
print(users_visits)