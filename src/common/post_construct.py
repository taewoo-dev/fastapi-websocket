# from common.handlers.middleware_handler import attach_middleware_handlers
# from common.handlers.exception_handler import attach_exception_handlers
from common.handlers.router_handler import attach_router_handlers
from common.handlers.staticfile_handler import attach_static_file_handlers


def post_construct(app):
    attach_router_handlers(app)
    attach_static_file_handlers(app)
    # attach_exception_handlers(app)
    # attach_middleware_handlers(app)
