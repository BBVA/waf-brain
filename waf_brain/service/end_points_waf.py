import aiofiles
import aiohttp
import logging

from sanic import response, Blueprint

from waf_brain.inferring import process_payload

log = logging.getLogger("waf-brain")

waf_blueprint = Blueprint("waf_brain")


@waf_blueprint.route('/<path:[\w\W\/]*>',
                     methods=[
                         "GET",
                         "POST",
                         "PUT",
                         "DELETE",
                         "HEAD",
                         "OPTIONS"
                     ])
async def waf(request, path):
    MODEL = request.app.config["MODEL"]
    PROTECTED_URL = request.app.config["PROTECTED_URL"]
    BLOCKING_MODE = request.app.config["BLOCKING_MODE"]
    BLOCKING_THRESHOLD = request.app.config["BLOCKING_THRESHOLD"]
    TIMEOUT_BACKEND = request.app.config["TIMEOUT_BACKEND"]

    total = []
    for arg, val in request.raw_args.items():
        total.append(process_payload(
            MODEL,
            arg,
            [val],
            False
        ))

    #
    # Request must be block if the WAF detect and attack?
    #
    if BLOCKING_MODE:
        if any(x["score"] >= BLOCKING_THRESHOLD for x in total):
            return response.text("Dangerous request detected and blocked",
                                 status=403)


    #
    # Send the original request to the api
    #
    async with aiohttp.ClientSession(cookies=request.cookies,
                                     read_timeout=TIMEOUT_BACKEND) as session:

        async with session.request(
                request.method,
                PROTECTED_URL,
                headers=request.headers,
                data=request.body,
                params=request.raw_args) as resp:

            body = await resp.text()

            return response.raw(
                body=body.encode(),
                status=resp.status,
                headers=dict(resp.headers),
                content_type=resp.content_type
            )


__all__ = ("waf_blueprint", )
