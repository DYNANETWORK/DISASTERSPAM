from Kannadiga import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Kannadiga import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/541d199b91a724b624712.jpg"

ZAID_Help = "â¤ï¸ð âÎ¹ÑÎ±ÑÑÑÑ ÑÏÎ±Ð¼Ð²ÏÑ ðâ¤ï¸\n\n"
 
ZAID_Help += f"_ÆÆÆÆÆCÊÉÖ ÇÊÇÉ¨ÊÇÉ®ÊÉ É¨Õ¼ ÉÉ¨ÖÇÖÈ¶ÉÊ ÖÖÇÊÉ®ÖÈ¶Ö_\n\n"

ZAID_Help += f" â§ ððð´ðð±ð¾ð ð²ð¼ð³ð â§\n\n"

ZAID_Help += f" `.ping` - to check ping\n `.alive` - To Check Bot Alive/Version (Only Main Userbot Will Reply)\n .`restart` - To Restart All Spam Bot \n `.addecho` - To Add Echo \n `.rmecho` - To Remove Echo \n `.addsudo` - To Add Sudo User Using Spam Bot \n\n"
 
ZAID_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

ZAID_Help += f" `.leave` - To Leave Public/Private Channel/Groups\n\n"
 
ZAID_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

ZAID_Help += f" `.raid` - To Raid\n `.replyraid` - To Active Reply Raid\n `.dreplyraid` - To Deactivate Reply Raid\n `.spam` - This Is Used For Normal Spam\n `.bigspam` - This Is Used For Big Spam\n `.uspam` - This Is Used For Unlimited Spam Unt You Restart The Bots!!\n `.delayspam` - This Is Used For Delay Spam\n\n"

ZAID_Help += f" .zaidspam - Éª á´¡ÉªÊÊ ê±á´É¢É¢á´ê±á´ á´á´É´'á´ á´ê±á´ á´ÊÉªê± á´á´á´á´á´É´á´ððâ§\n\n"

ZAID_Help += f"Â© @DISASTER_SUPPORT\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=ZAID_Help,
                                  buttons=[
        [
        Button.url("â¤ï¸ á´Êá´É´É´á´Ê â¤ï¸", "https://t.me/DISASTER_SUPPORT")
        ] 
        ]
        )                                                         
