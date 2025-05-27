from multiverse_utils import launch
from multiverse_utils import messenger
from multiverse_utils import status

from multiverse_utils import *

from multiverse_utils import messenger as me

launch.launch_shuttle(True)
messenger.send_message("The stars are beautiful.")
status.spacecraft_status(life_support="Optimal", propulsion="85% efficiency", navigation="Online")

me.send_message("The stars are beautiful.")