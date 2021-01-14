# Logging configuration

The logging configuration of this module can be easily overwritten from the application that uses it.


## Modify logging level, via config file

For instance, if you want to enable DEBUG logs for this module, you can do so easily overriding the `bmi` logger 
configuration, from your logging config file.

You just need to add something similar to the following example to your logging config file:

```
[loggers]
keys=root,<your_app_logger>,bmi

[logger_bmi]
level=DEBUG
handlers=<your_stream_handler>
qualname=bmi
propagate=0
```