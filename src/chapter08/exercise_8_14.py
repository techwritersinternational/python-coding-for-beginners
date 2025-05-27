from space_utils import spacecraft_status
from space_utils import *
from space_utils import spacecraft_status as status
from space_utils import send_message

spacecraft_status(life_support="Optimal", propulsion="85% efficiency", navigation="Online")

launch_shuttle(use_upper_deck=True)

status(life_support="Optimal", propulsion="85% efficiency", navigation="Online")

send_message("The stars are beautiful.")