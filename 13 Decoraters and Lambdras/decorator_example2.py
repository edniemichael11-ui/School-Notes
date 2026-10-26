is_admin = False

def admin_required(func):
    def wrapper(*args, **kwargs):
        if is_admin:
            return func(*args, **kwargs)
        else:
            print("Access Denied. Admin privileges required")
    return wrapper

@admin_required
def delete_user(username):
    print(f"{username} Deleted")



if __name__ == "__main__":
    is_admin = True
    delete_user("Michael")
