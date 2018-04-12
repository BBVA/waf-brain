from aiohttp import web


async def demo_api(request):
    print(".")
    return web.Response(text="OK")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get("/{tail:.*}", demo_api),
        web.post("/{tail:.*}", demo_api)
    ])

    web.run_app(app,
                host="127.0.0.1",
                port=5000)
