# MarkPoint \- 像书写代码一样书写PPT文件

世人苦 PowerPoint 久矣！

[English Document](../README.md)

## 为何选择 MarkPoint？

MarkPoint 通过将 Markdown 的效率与 PowerPoint 的视觉表现力相结合，彻底改变了技术和学术演示文稿的创建方式。专为重视内容而非装饰的研究人员、工程师和教育工作者打造。

### 代码友好的演示文稿创作
-   **纯文本工作流** - 可在任意代码编辑器（VSCode, Vim 等）中创建幻灯片
-   **原生支持版本控制** - 使用 Git 跟踪变更，告别二进制 `.pptx` 文件
-   **公式优先设计** - 将 LaTeX 数学公式支持作为核心功能，而非事后补救
    ```markpoint
    波动方程：$$ \frac{\partial^2 u}{\partial t^2} = c^2\nabla^2u $$
    ```

### 学术级的简洁体验
-   **自动布局引擎** - 专注内容，无需手动调整像素
-   **精准动画控制** - 用极简语法实现核心动画效果：
    `结论 -->-- 淡入`
-   **主题化模板** - 轻松保持专业品牌形象
    ```markpoint
    theme = #2A5CAA   // 浅蓝色
    background = #F8FBFF 
    ```

### 单一来源，多种输出
-   MP[MarkPoint .mp] -> PPT[PowerPoint]
-   MP -> PDF[讲义 PDF]
-   MP -> MD[Markdown 笔记]
-   MP -> HTML[网页幻灯片]

### 核心功能
| 类别       | 功能                    |
|----------|-----------------------|
| **核心语法** | 标题、列表、引用块、分隔线         |
| **技术元素** | LaTeX 数学公式、代码块、表格     |
| **布局**   | 自动分页、主题配色、智能间距        |
| **工作流**  | PPTX 导出、版本控制、CI/CD 集成 |

### 60 秒快速上手
1.  安装：`pip install markpoint`

2.  创建 `presentation.mp`：

    ```markpoint
    ---
    # MarkPoint之道  
    ## Nejiwwkr  
    ---
    # 分页机制
    当内容超出单页容量时，MarkPoint将自动分页，续页继承原页标题
    使用 "!!!" 触发隐式分页，或使用 "---" 配合 "#" 显式分页
    ---
    # 感谢您的阅读！
    ## MarkPoint渲染生成  
    ---
    ```

3.  编译：`markpoint --original "示例.mp" --target "示例.pptx" --type "pptx"`

## 为谁而设计？
-   撰写讲座幻灯片的学术研究人员
-   创建技术报告的工程师
-   准备课程材料的教育工作者
-   厌恶 GUI 编辑器的开发者

加入逃离 PPT 苦海的行列。
[立即开始 →](https://github.com/Nejiwwkr/MarkPoint) | [查看示例 →](../example/Example.pdf)

## 发展路线图
-   **v0.9** (当前版本)：核心渲染引擎
-   **v1.0**：表格/代码块/动画支持
-   **v2.0**：IDEA/VSC/Vim 语法解析支持