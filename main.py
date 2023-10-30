from bedrock.server import Server

app = Server()

@app.server_event
async def ready(ctx):
    print(f"Готово @ {ctx.host}:{ctx.port}!")

@app.game_event
async def block_broken(ctx):
    await ctx.server.run(f"say Сломан блок {ctx.id} игроком {ctx.player}")

@app.game_event
async def item_used(ctx):
    await ctx.server.run("say Использовали предмет (мне лень писать какой)")

@app.game_event
async def portal_built(ctx):
    await ctx.server.run("say Портал был построен")

@app.game_event
async def item_dropped(ctx):
    await ctx.server.run("say Уронили предмет. Не мыло(")

app.start("lapismyt.space", 6464)
