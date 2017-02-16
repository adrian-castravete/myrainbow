==========================
My Rainbow Logging Handler
==========================

Just a wrapper over rainbow-logging-handler to add support for changing
the default colours via a ``~/.rainbowrc`` file.

I felt the need to do this because the default rainbow_logging_handler puts
white colour for some text in the output which is **not** visible should your
background happen to be white.

Also doing it this way helps not having to spam projects with
``rainbow_logging_handler`` config variables.

The RC file is *yaml*,
Here's an example of configuration in the RC file:

.. code:: yaml

    color_name: [black, null, true]
    color_levelno: [black, null, false]
    color_levelname: [black, null, true]
    color_pathname: [blue, null, true]
    color_filename: [blue, null, true]
    color_module: [yellow, null, true]
    color_lineno: [cyan, null, true]
    color_funcName: [green, null, false]
    color_created: [black, null, false]
    color_asctime: [black, null, true]
    color_msecs: [black, null, false]
    color_relativeCreated: [black, null, false]
    color_thread: [black, null, false]
    color_threadName: [black, null, false]
    color_process: [black, null, false]
    color_message_debug: [cyan, null, false]
    color_message_info: [black, null, false]
    color_message_warning: [yellow, null, true]
    color_message_error: [red, null, true]
    color_message_critical: [black, red, true]
