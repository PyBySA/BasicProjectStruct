
import traceback
from utils.notfication_system import generate_notification

try:
    pass

except Exception as e:
    generate_notification(f'inside the exception block{traceback.print_exc()}')
