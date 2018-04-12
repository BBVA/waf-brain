import os.path

from argparse import Namespace

from waf_brain.exceptions import WAFBrainException


class WAFBrainRunningConfig:

    def __init__(self,
                 protected_url: str,
                 verbosity: bool = 1,
                 listen_addr: str = "127.0.0.1",
                 listen_port: int = 8080,
                 blocking_mode: bool = False,
                 blocking_threshold: int = 25,
                 model: str = "model_feat-5_botneck-101",
                 dump_file: str = "dump.txt",
                 enable_testing: bool = False,
                 timeout_backend: int = 5,
                 backlog: int = 512):

        self.backlog = backlog
        self.verbosity = verbosity
        self.listen_port = listen_port
        self.listen_addr = listen_addr
        self.protected_url = protected_url
        self.enable_testing = bool(enable_testing)
        self.blocking_mode = blocking_mode
        self.timeout_backend = int(timeout_backend)
        self.blocking_threshold = 0
        if blocking_threshold:
            self.blocking_threshold = int(blocking_threshold)

        self.blocking_threshold /= 100

        #
        # Fix model path
        #
        if not model.endswith("h5"):
            model = f"{model}.h5"

        # If exists in local path -> get absolute path
        if os.path.exists(model):
            os.path.abspath(model)

        else:
            # Get local model
            model = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "models",
                    model
                )
            )

        if not os.path.exists(model):
            raise WAFBrainException(f"Can't find model path: {model}")

        self.model = model

        #
        # Fix dump file
        #
        if os.path.isabs(dump_file):
            self.dump_file = dump_file
        else:
            self.dump_file = os.path.abspath(
                os.path.join(
                    os.getcwd(),
                    dump_file
                )
            )

    @classmethod
    def from_argparser(cls, argparser_input: Namespace):
        return WAFBrainRunningConfig(
            verbosity=argparser_input.verbosity,
            blocking_mode=argparser_input.blocking_mode,
            blocking_threshold=argparser_input.blocking_threshold,
            protected_url=argparser_input.protected_url,
            listen_addr=argparser_input.listen,
            listen_port=argparser_input.port,
            backlog=argparser_input.backlog,
            timeout_backend=argparser_input.backend_timeout,
            enable_testing=argparser_input.enable_testing,
            dump_file=argparser_input.dump_file,
            model=argparser_input.model
        )

    @property
    def to_dict(self) -> dict:
        return {
            x: y
            for x, y in self.__dict__.items() if not x.startswith("_")
        }


__all__ = ("WAFBrainRunningConfig",)
