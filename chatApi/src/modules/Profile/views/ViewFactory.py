from chatApi.src.modules.Profile.views.CreateProfileView import CreateProfileView
from chatApi.src.modules.Profile.views.GetAllProfilesView import GetAllProfilesView
from chatApi.src.modules.Profile.views.GetProfileView import GetProfileView

class ViewFactory:

    def CreateProfileView(self, **kwargs):
        return CreateProfileView(**kwargs)

    def GetProfileView(self, **kwargs):
        return GetProfileView(**kwargs)

    def GetAllProfilesView(self, **kwargs):
        return GetAllProfilesView(**kwargs)
