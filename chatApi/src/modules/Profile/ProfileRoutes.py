from chatApi.src.framework.classes.Router import Router
from chatApi.src.modules.Profile.ProfileController import ProfileController

def ProfileRoutes():
    router = Router()
    profile_controller = ProfileController()
    
    router.get('profile/all', profile_controller.get_all_profiles)
    router.get('profile', profile_controller.get_profile)
    router.post('profile', profile_controller.create_profile)

    return router.getRoutes()
