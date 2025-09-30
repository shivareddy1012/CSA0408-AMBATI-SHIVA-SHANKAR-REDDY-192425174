users = {
    "owner": {"read": True, "write": True, "execute": True},
    "group": {"read": True, "write": False, "execute": True},
    "others": {"read": True, "write": False, "execute": False}
}

for user_type, perms in users.items():
    perm_str = ''.join(['r' if perms["read"] else '-',
                        'w' if perms["write"] else '-',
                        'x' if perms["execute"] else '-'])
    print(f"{user_type.capitalize()} permissions: {perm_str}")
