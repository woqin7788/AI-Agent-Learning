# 保存所有已经注册的 Analyzer
# 这里不依赖 Interface，也不依赖 Factory，
# 从根本上避免循环引用。

analyzers = {}


def register(name, analyzer_class):
    print(f"【注册】{name}")
    # 把 Analyzer 类保存到注册表
    analyzers[name] = analyzer_class


def get(name):
    # 打印当前要查找的 Analyzer
    print(f"【查找】{name}")

    # 打印当前注册表里到底有哪些 Analyzer
    print(f"【注册表】{list(analyzers.keys())}")
    # 根据名称获取 Analyzer 类
    return analyzers.get(name)