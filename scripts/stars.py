import github as g

def get_stars(user, *args, **kwargs):
    ref = g.Github(*args, **kwargs)
    user_ref = ref.get_user(user)
    return (star for star in user_ref.get_starred())
