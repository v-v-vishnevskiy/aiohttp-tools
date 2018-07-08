# aiohttp-tools

- [Errors handling](#Errors-handling)


## Errors handling

```python
from aiohttp.web_exceptions import HTTPNotFound
import aiohttp_mako
from aiohttp_tools import error


@error.register(HTTPNotFound)
async def not_found(e, request):
    return aiohttp_mako.render_template('404.html', request, {})


@error.register(Exception)
async def server_error(e, request):
    return aiohttp_mako.render_template('500.html', request, {})


def init(app):
    app.middlewares.append(error.error_handler)
```
