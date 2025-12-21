from typing import Set, List

admins: Set[str] = {"admin_bob", "alice_admin", "john_admin", "user5"}
editors: Set[str] = {"user1", "user5", "editor_anna", "alice_admin"}
banned: Set[str] = {"user1", "spammer", "john_admin", "malicious_user"}

access_attempts: List[str] = ["user1", "user5", "admin_bob", "spammer", "editor_anna", 
                               "guest_user", "alice_admin", "john_admin", "unknown_user"]

def find_super_users(admins_set: Set[str], editors_set: Set[str]) -> Set[str]:

    return admins_set.intersection(editors_set)

def find_banned_non_admins(banned_set: Set[str], admins_set: Set[str], 
                           attempts_list: List[str]) -> List[str]:

    result = []
    for user in attempts_list:
        if user in banned_set and user not in admins_set:
            result.append(user)
    return result

def find_users_without_roles(admins_set: Set[str], editors_set: Set[str], 
                             attempts_list: List[str]) -> List[str]:
 
    users_with_roles = admins_set.union(editors_set)
    
    result = []
    for user in attempts_list:
        if user not in users_with_roles:
            result.append(user)
    return result

if __name__ == "__main__":
    print("Исходные данные:")
    print(f"Администраторы: {admins}")
    print(f"Редакторы: {editors}")
    print(f"Заблокированные: {banned}")
    print(f"Попытки входа: {access_attempts}")
    print()
    
    super_users = find_super_users(admins, editors)
    print("1. Супер-пользователи (одновременно администраторы и редакторы):")
    print(f"   {super_users if super_users else 'Нет супер-пользователей'}")
    print()
    
    banned_non_admins = find_banned_non_admins(banned, admins, access_attempts)
    print("2. Заблокированные не-администраторы (из списка попыток входа):")
    print(f"   {banned_non_admins if banned_non_admins else 'Таких пользователей нет'}")
    print()
    
    users_without_roles = find_users_without_roles(admins, editors, access_attempts)
    print("3. Пользователи без ролей (ни админ, ни редактор):")
    print(f"   {users_without_roles if users_without_roles else 'Таких пользователей нет'}")
