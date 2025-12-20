from injector import Injector
from llmops.internal.server import Http
from llmops.internal.router import Router
import dotenv;
from llmops.config import Config;

# 将 env 加载到环境变量当中.
dotenv.load_dotenv()

config = Config()
injector = Injector()
app = Http(__name__,conf=config, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)