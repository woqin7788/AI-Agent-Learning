from pathlib import Path
import importlib


class AnalyzerPluginLoader:

    @staticmethod
    def load(plugin_dir):
        # 把传入的目录转换成 Path 对象
        plugin_path = Path(plugin_dir)

        # 如果目录不存在，直接报错
        if not plugin_path.exists():
            raise FileNotFoundError(
                f"插件目录不存在: {plugin_dir}"
            )

        # 遍历插件目录中的所有 Python 文件
        for file in plugin_path.glob("*.py"):

            # __init__.py 只是包初始化文件，不是 Analyzer
            if file.name == "__init__.py":
                continue

            # 获取文件名，不包含 .py
            module_name = file.stem

            # 组合成完整的模块名称
            # 例如：
            # analyzers/customer_analyzer.py
            # ↓
            # analyzers.customer_analyzer
            full_module_name = f"analyzers.{module_name}"
            # 打印一下到底发现了哪些文件
            print(f"【发现插件】{full_module_name}")

            # 动态导入模块
            # 模块加载后，里面的 register() 会自动执行
            importlib.import_module(full_module_name)
            print(f"【加载完成】{full_module_name}")