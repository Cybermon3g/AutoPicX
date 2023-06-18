import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("15762061"))
API_HASH = environ.get("364d3fa8f95aae815d62cf981ab1afe3")
SESSION = environ.get("1BVtsOGYBu5nutjr3lkgoCCxsBn_0g6EuliScNGyIwwKpcTTqMj0rYMjMhls1dEHPNJeRjTuS8xf66mYhaXfsuwi_2BoAvp8q2MZWhAa86O0q9GYOv-FvvrkAN-xVoK1GO767CilUjRlM1TijozfBXJ2HdJXDOZZVK0mlMigAHE2MajnOAcl92i4zJRjkdrL333kASdvGR_WcEZUpUXhUSUfpk5HB0Qe1d_djXG4_-8B4TfkzjA2g-auTqwTosoZ05ypW9NM-1sXQqYsoS-zQ3fgPxGXemC_TD3o15MbIBM9Pwlviork_VbUbQXQ7JuWi9_dOnxcp_7ZGNPxemM9TLujxtUxSQPk=")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001227879771"))


if SESSION is not None:
    session = StringSession(str(SESSION))
else:
    session = "pyrobot"

try:
    client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )
    client.start()
    
except Exception as e:
    print(e)

