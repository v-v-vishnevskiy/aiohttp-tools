from voluptuous import Schema, REMOVE_EXTRA, Invalid, MultipleInvalid


def _add_error(err_exception, result):
    key = []
    for item in err_exception.path:
        if isinstance(item, str):
            key.append(item)
        else:
            if hasattr(item, 'schema'):
                key.append(getattr(item, 'schema'))
    if key:
        key = '.'.join(key)
        if key not in result:
            result[key] = err_exception.msg
    else:
        raise err_exception


def _harvest_errors(err_exception, result=None):
    if result is None:
        result = {}
    if isinstance(err_exception, MultipleInvalid):
        for error in err_exception.errors:
            _harvest_errors(error, result)
    else:
        _add_error(err_exception, result)
    return result


def validator(schema: dict, extra=REMOVE_EXTRA):
    def view_decorator(fn):
        _schema = Schema(schema, extra=extra)

        async def wrapper(request):
            data = dict(await request.post())
            errors = {}
            try:
                data = _schema(data)
            except Invalid as e:
                errors.update(_harvest_errors(e))
            request.validation_errors = errors
            request.validated_data = data
            return await fn(request)
        return wrapper
    return view_decorator
