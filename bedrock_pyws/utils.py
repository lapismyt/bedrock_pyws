from bedrock.utils import rawtext, boolean, numeric

async def escape_name(name):
    name = name.replace("\"", "\\\"")
    return "\""+name+"\""

async def set_block(server, block, coords, data=None, mode="replace"):
    x, y, z = coords
    if data is None:
        await server.run(f"setblock {x} {y} {z} {block} 0 {mode}")
    else:
        await server.run(f"setblock {x} {y} {z} {block} {data} {mode}")

async def broadcast_message(server, text):
    await server.run(f"tellraw @a {rawtext(text)}")

async def send_message(server, player, text):
    await server.run(f"tellraw {escape_name(player)} {rawtext(text)}")

async def kill_player(server, player):
    await server.run(f"kill {escape_name(player)}")
