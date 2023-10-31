from bedrock.server import Server
from bedrock import consts
from bedrock_pyws import utils
from bedrock_pyws.plugin import PluginManager
import os, sys
import time

server = Server()
plugin_manager = PluginManager(server)

@server.server_event
async def ready(ctx):
    print(f"Ready @ {ctx.host}:{ctx.port}")
    await plugin_manager.server_event(ctx, "ready")

@server.server_event
async def connect(ctx):
    print(f"New connection: {ctx.data}")
    await plugin_manager.server_event(ctx, "connect")

@server.game_event
async def app_paused(ctx):
    await plugin_manager.game_event(ctx, "app_pause")

@server.game_event
async def app_resumed(ctx):
    await plugin_manager.game_event(ctx, "app_resumed")

@server.game_event
async def app_suspended(ctx):
    await plugin_manager.game_event(ctx, "app_suspended")

@server.game_event
async def block_broken(ctx):
    await plugin_manager.game_event(ctx, "block_broken")

@server.game_event
async def block_placed(ctx):
    await plugin_manager.game_event(ctx, "block_placed")

@server.game_event
async def boss_killed(ctx):
    await plugin_manager.game_event(ctx, "boss_killed")

@server.game_event
async def cauldron_used(ctx):
    await plugin_manager.game_event(ctx, "cauldron_used")

@server.game_event
async def crafting_session_completed(ctx):
    await plugin_manager.game_event(ctx, "crafting_session_completed")

@server.game_event
async def connection_failed(ctx):
    await plugin_manager.game_event(ctx, "connection_failed")

@server.game_event
async def entity_spawned(ctx):
    await plugin_manager.game_event(ctx, "entity_spawned")

@server.game_event
async def hardware_info(ctx):
    await plugin_manager.game_event(ctx, "hardware_info")

@server.game_event
async def item_acquired(ctx):
    await plugin_manager.game_event(ctx, "item_acquired")

@server.game_event
async def item_crafted(ctx):
    await plugin_manager.game_event(ctx, "item_crafted")

@server.game_event
async def item_destroyed(ctx):
    await plugin_manager.game_event(ctx, "item_destroyed")

@server.game_event
async def item_dropped(ctx):
    await plugin_manager.game_event(ctx, "item_dropped")

@server.game_event
async def item_enchanted(ctx):
    await plugin_manager.game_event(ctx, "item_enchanted")

@server.game_event
async def item_smelted(ctx):
    await plugin_manager.game_event(ctx, "item_smelted")

@server.game_event
async def item_used(ctx):
    await plugin_manager.game_event(ctx, "item_used")

@server.game_event
async def join_cancelled(ctx):
    await plugin_manager.game_event(ctx, "join_cancelled")

@server.game_event
async def jukebox_used(ctx):
    await plugin_manager.game_event(ctx, "jukebox_used")

@server.game_event
async def menu_shown(ctx):
    await plugin_manager.game_event(ctx, "menu_shown")

@server.game_event
async def mob_interaction(ctx):
    await plugin_manager.game_event(ctx, "mob_interaction")

@server.game_event
async def mob_killed(ctx):
    await plugin_manager.game_event(ctx, "mob_killed")

@server.game_event
async def performance_metrics(ctx):
    await plugin_manager.game_event(ctx, "performance_metrics")

@server.game_event
async def player_died(ctx):
    await plugin_manager.game_event(ctx, "player_died")

@server.game_event
async def player_join(ctx):
    await plugin_manager.game_event(ctx, "player_join")

@server.game_event
async def player_leave(ctx):
    await plugin_manager.game_event(ctx, "player_leave")

@server.game_event
async def player_message(ctx):
    await plugin_manager.game_event(ctx, "player_message")

@server.game_event
async def player_teleported(ctx):
    await plugin_manager.game_event(ctx, "player_teleported")

@server.game_event
async def player_travelled(ctx):
    await plugin_manager.game_event(ctx, "player_travelled")

@server.game_event
async def player_transform(ctx):
    await plugin_manager.game_event(ctx, "player_transform")

@server.game_event
async def portal_built(ctx):
    await plugin_manager.game_event(ctx, "portal_built")

@server.game_event
async def portal_used(ctx):
    await plugin_manager.game_event(ctx, "portal_used")

@server.game_event
async def special_mob_built(ctx):
    await plugin_manager.game_event(ctx, "special_mob_built")

@server.game_event
async def world_loaded(ctx):
    await plugin_manager.game_event(ctx, "world_loaded")

@server.game_event
async def world_unloaded(ctx):
    await plugin_manager.game_event(ctx, "world_unloaded")

server.start(os.getenv("BEDROCK_WS"), 6464)
