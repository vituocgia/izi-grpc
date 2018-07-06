# 内置信号

izi_grpc 支持信号(基于 [blinker](https://github.com/jek/blinker))，并内置了一些信号(`blinker.Signal`)，位于 `izi_grpc.signals` 中

### `server_started`

grpc server 启动前触发，Sender 为 `izi_grpc.server.Server`对象，无额外参数。

### `server_stopped`

grpc server 结束后触发，Sender 为 `izi_grpc.server.Server`对象，无额外参数。
