from aiohttp import web


__handlers = {}


@web.middleware
async def error_handler(request, handler):
    try:
        return await handler(request)
    except (Exception, BaseException) as e:
        exc_fn = __handlers.get(e.__class__)
        if exc_fn:
            return await exc_fn(e, request)
        else:
            for exc_class, exc_fn in __handlers.items():
                if issubclass(e.__class__, exc_class):
                    return await exc_fn(e, request)
            else:
                raise


def register(exc):
    def decorator(fn):
        __handlers[exc] = fn
        return fn
    return decorator
