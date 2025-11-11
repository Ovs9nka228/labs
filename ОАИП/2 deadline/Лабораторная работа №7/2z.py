def build_user_profile(user_id, **kwargs):
    profile = {}
    profile["user_id"] = user_id
    for key, value in kwargs.items():
        profile[key] = value
    return profile
profile = build_user_profile(101, name="Анна", status="online", email="anna@example.com")
print(profile)
