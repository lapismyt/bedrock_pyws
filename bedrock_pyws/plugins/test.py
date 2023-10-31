from bedrock_pyws.plugin import BasePlugin
from bedrock_pyws.plugin import on_game_event
from bedrock_pyws.plugin import on_server_event
from bedrock_pyws.utils import send_message

class Plugin(BasePlugin):
    """Plugin for testing plugin system"""
    name = "TestPlugin"

    @on_game_event("block_broken")
    async def block_breaking_handler(self, ctx):
        await broadcast_message(ctx.server, f"Сломан блок {ctx.id} игроком {ctx.player.name}")
