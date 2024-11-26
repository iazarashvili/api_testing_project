import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    user_gui_id = os.getenv('USER_GUI_ID')
    web_token = os.getenv('API_TOKEN')
    cms_token = os.getenv('CMS_API_TOKEN')
    izi_box_token = os.getenv('IZI_BOX_TOKEN')


