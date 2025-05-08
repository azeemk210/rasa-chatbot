import asyncio
import websockets
import json
import aiohttp

async def get_rasa_response(message):
    """Send message to Rasa server and get the response."""
    url = "http://localhost:5005/webhooks/rest/webhook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"sender": "user", "message": message}) as resp:
            if resp.status == 200:
                response_data = await resp.json()
                return response_data
            else:
                return [{"text": "Error from Rasa"}]

async def handle_client(websocket):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            try:
                # Parse the JSON message from the client
                data = json.loads(message)
                if "message" in data:
                    user_message = data["message"]
                    # Get the response from Rasa
                    rasa_responses = await get_rasa_response(user_message)
                    
                    # Prepare the response for the client
                    responses = [resp.get("text", "No response") for resp in rasa_responses]
                    response_text = "\n".join(responses)
                    await websocket.send(json.dumps({"response": response_text}))
                    print(f"Sent: {response_text}")
                else:
                    await websocket.send(json.dumps({"response": "Invalid format"}))
            except json.JSONDecodeError:
                await websocket.send(json.dumps({"response": "Invalid JSON"}))
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    print("WebSocket server started at ws://localhost:8765")
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
