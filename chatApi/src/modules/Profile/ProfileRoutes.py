from chatApi.src.classes.Router import Router
from chatApi.src.modules.Profile.actions.GetProfileList import GetProfileList
from chatApi.src.modules.Profile.actions.GetProfile import GetProfile
from chatApi.src.modules.Profile.actions.CreateProfile import CreateProfile

def ProfileRoutes():
    router = Router()
    
    router.get('profile/all', GetProfileList())
    router.get('profile', GetProfile())
    router.post('profile', CreateProfile())

    return router.getRoutes()
