from flask import Flask;
from llmops.internal.router import Router;
from llmops.config import Config;

class Http(Flask):

    def __init__(self, *args,conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_route(self)
        self.config.from_object(conf)