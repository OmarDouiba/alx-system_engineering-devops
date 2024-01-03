# Web server

### What is a Child Process?

Although it may sound like something out of a parenting handbook or a psychological journal, the term child process actually has nothing to do with human development. If you run a Unix or Linux dedicated server, you have likely encountered child processes without even knowing it. Therefore, it is good to know what child processes are and how they work.

A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

In normal server operations, the kernel may initiate child processes, and other programs, such as Apache, may have them as well. Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

To view all running processes along with their child processes in a “tree” format, use the following command:

```
$ ps axf
```

[ documentation.](https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes)

[res](https://www.youtube.com/watch?v=AZg4uJkEa-4)

# Resources

- [How the web works](https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw)
- [Nginx](https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA)
- [How to Configure Nginx](https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw)
- [Child process concept page](https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg)
- [Root and sub domain](https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ)
- [HTTP requests](https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw)
- [HTTP redirection](https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ)
- [Not found HTTP response code](https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw)
- [Logs files on Linux](https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg)

## Videos
- 

man or help:

```
- scp
- curl
```

- [my Own resume](https://docs.google.com/document/d/1x-pSSpMjP3iJmJsz3ctHyi7dAXM0xXendJxgE6e6_7A/edit)

- [How to use sed](https://docs.google.com/document/d/1z6418EWkgTLWjhcM5DUB7zFFOtNLJvxyN4iRZWHmhO4/edit)
