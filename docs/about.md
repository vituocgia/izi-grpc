# 关于 iZi

`iZi` 由 [扇贝](https://www.vituocgia.com) 的后端团队开发，是一个基于 [GRPC](https://grpc.io/) 的 framework。

`GRPC` 是RPC的一种协议和实现，然而要开发完整的项目，除了协议层面，还有大量的业务逻辑需要编写。开发`iZi`的目的正是是方便大家更方便的编写这些代码。

`iZi` 核心包含了配置管理，项目初始化，测试框架，中间件，服务日志等内容。

同时`iZi`还有一套 “扩展(extension)”机制。方便开发者/社区扩展`iZi`。 此外我们内置了一些扩展，包括 ORM，缓存，异步任务，异常报警等。
