from config import dispatcher

from handlers import commands
from handlers import lastoperations
from handlers import newoperation
from handlers import other
from handlers import profile
from handlers import settings


dispatcher.include_routers(
    commands.router,
    lastoperations.router,
    newoperation.router,
    other.router,
    profile.router,
    settings.router
)