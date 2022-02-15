from client import Client
import asyncio

async def main():
    body = {
        "message": {
            "html": "",
            "text": "",
            "subject": "",
            "from_email": "info@fasttask.net",
            "to": [
                {
                    "email":"info@fasttask.net",
                    "name":"",
                    "type":"to",
                }
            ],
            "html": "",
        }
    }
    api_key = "..."
    resp = await Client(api_key=api_key).send_message(body=body)
    print(resp)

if __name__ == "__main__":
    asyncio.run(main())