def update_profile(request, **kwargs):
    user = kwargs['user']
    backend = kwargs['backend']
    
    user.profile.update_social_auth_data(backend, kwargs['response'])
