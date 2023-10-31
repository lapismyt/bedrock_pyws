import os, sys
import importlib

class BasePlugin:
    """Base plugin"""
    name = "BasePlugin"

    def __init__(self):
        self.description = self.__doc__
        self.server_event_handlers = {}
        self.game_event_handlers = {}
    
def on_server_event(event_type):
    def decorator(func):
        async def wrapper(self, *args, **kwargs):
            self.server_event_handlers[event_type] = func
            await func(self, *args, **kwargs)
        return wrapper
    return decorator
    
def on_game_event(event_type):
    def decorator(func):
        async def wrapper(self, *args, **kwargs):
            self.game_event_handlers[event_type] = func
            await func(self, *args, **kwargs)
        return wrapper
    return decorator

class PluginManager:
    def __init__(self, server):
        plugins = []
        plugin_files = os.listdir("bedrock_pyws/plugins")
        sys.path.insert(0, "bedrock_pyws/plugins")
        for filename in plugin_files:
            if not filename.endswith(".py"):
                continue
            name = os.path.splitext(filename)[0]
            plugin = importlib.import_module(name)
            plugins.append(plugin.Plugin)
        self.plugins = plugins

    async def server_event(self, ctx, event_type):
        for p in self.plugins:
            if event_type in p.server_event_handlers.keys():
                await p.server_event_handlers[event_type](ctx)

    async def game_event(self, ctx, event_type):
        for p in self.plugins:
            if event_type in p.game_event_handlers.keys():
                await p.game_event_handlers[event_type](ctx)
