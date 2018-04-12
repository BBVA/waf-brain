import logging
import aiofiles

from sanic import response, Blueprint

from waf_brain.inferring import process_payload

log = logging.getLogger("waf-brain")

waf_blueprint_simulator = Blueprint("waf_brain_simulator")


@waf_blueprint_simulator.route('/<path:[\w\W\/]*>',
                               methods=[
                                   "GET",
                                   "POST",
                                   "PUT",
                                   "DELETE",
                                   "HEAD",
                                   "OPTIONS"
                               ])
async def waf_simulator(request, path):
    MODEL = request.app.config["MODEL"]
    BLOCKING_THRESHOLD = request.app.config["BLOCKING_THRESHOLD"]
    DUMP_FILE = request.app.config["DUMP_FILE"]

    total = []
    for arg, val in request.raw_args.items():
        total.append(process_payload(
            MODEL,
            arg,
            [val],
            True
        ))

    async with aiofiles.open(DUMP_FILE, 'a+') as f:

        await f.writelines(
            [
                f"[sec: {t['time']:.5f}] param: '{t['paramName']}' "
                f"- Scoring: {t['score']} - "
                f"track-id:"
                f"{request.headers.get('WAF-BENCHMARK-TRACK-ID')}\n"
                f"{t['weights']}\n"
                for t in total
            ]
            )

    #
    # Request must be block if the WAF detect and attack?
    #
    if any(x["score"] >= BLOCKING_THRESHOLD for x in total):
        return response.text("Dangerous request detected and blocked",
                             status=403)

    else:
        return response.text("OK", status=200)


__all__ = ("waf_blueprint_simulator", )
