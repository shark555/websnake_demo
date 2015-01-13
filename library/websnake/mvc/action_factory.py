from exceptions.no_action_exception import NoActionException
from mvc.controller import Controller


class ActionFactory:
    @staticmethod
    def create(name, controller: Controller):
        if not name in controller.__class__.__dict__:
            raise NoActionException()
        return controller.__class__.__dict__[name]