import logging
import argparse
import os

from waf_brain.data import WAFBrainRunningConfig
from waf_brain.helpers import get_log_level

log = logging.getLogger("waf-brain")


def argument_parser():
    parser = argparse.ArgumentParser(
        description='WAF-brain: the clever and efficient Firewall for the Web'
    )
    parser.add_argument(
        '-v',
        action='count',
        dest="verbosity",
        help='log level',
        default=3
    )

    # -------------------------------------------------------------------------
    # Parser: serve
    # -------------------------------------------------------------------------
    server = parser.add_argument_group("Server Options")
    server.add_argument(
        '--backend-timeout',
        help="timeout to connect to the backend",
        default=5
    )
    server.add_argument(
        '-A', '--protected-url',
        help='address service to protect with the WAF',
        default="http://127.0.0.1:5000"
    )
    server.add_argument(
        '-l', '--listen', help='listen address. Default: 127.0.0.1',
        default="127.0.0.1"
    )
    server.add_argument(
        '-p', '--port',
        help='listen port for service. Default: 8000',
        type=int,
        default=8000
    )
    server.add_argument(
        '-b', '--backlog', help='maximum concurrent connections',
        default=512
    )

    behavior = parser.add_argument_group("WAF Behavior")
    behavior.add_argument(
        '--blocking-mode',
        action="store_true",
        help="enables active blocking of dangerous request",
        default=False
    )
    behavior.add_argument(
        '--blocking-threshold',
        help="if the dangerous levels is upper this number, "
             "and blocking mode is enabled, WAF will block a request",
        default="16"
    )
    behavior.add_argument(
        '-M', '--model',
        help="model used for WAF",
        default="model_feat-5_botneck-101"
    )

    testing = parser.add_argument_group("Enable testing mode")
    testing.add_argument(
        '-T', '--enable-testing',
        action="store_true",
        help="enable testing mode",
        default=False
    )
    testing.add_argument(
        '--dump-file',
        help="dump file to track each request",
        default="dump.txt"
    )
    testing.add_argument(
        '-a', '--access-log',
        action="store_true",
        help="enable access log for each request",
        default=False
    )

    return parser


def list_models():
    models_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               "models"))

    print()
    print("Available models: ")
    for m in os.listdir(models_path):
        if m.endswith("h5"):
            print(f"  - {m.replace('.h5', '')}")
    print()


def serve():

    parser = argument_parser()
    parsed_cmd = parser.parse_args()

    # set logger level
    log.setLevel(get_log_level(parsed_cmd.verbosity))

    #
    # Run actions
    #
    from waf_brain.service.make_web_app import make_app

    config = WAFBrainRunningConfig.from_argparser(parsed_cmd)

    #
    # Print summary
    #

    app = make_app(config.to_dict)

    print()
    print(f"[*] Model: {os.path.basename(config.model)} - "
          f"threshold: {config.blocking_threshold}")

    app.run(
        host=parsed_cmd.listen,
        port=int(parsed_cmd.port),
        backlog=int(parsed_cmd.backlog),
        access_log=parsed_cmd.access_log)


if __name__ == '__main__':
    serve()
