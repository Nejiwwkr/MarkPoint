# MarkPoint \- Write PPT files like writing codes  

The world has long suffered under the tyranny of PowerPoint.

[中文文档](docs/README-zh.md)

## Why chose markpoint?

MarkPoint revolutionizes technical and academic presentations by combining the efficiency of Markdown with PowerPoint's visual power. Built for researchers, engineers, and educators who value content over decoration.

### Code-Friendly Presentation Authoring  
-   **Pure text workflow** \- Create slides in any code editor (VSCode, Vim, etc.)  
-   **Version control ready** \- Track changes with Git instead of binary `.pptx` files  
-   **Formula-first design** \- LaTeX math support as a core feature, not an afterthought  
    ```markpoint
    The wave equation: $$ \frac{\partial^2 u}{\partial t^2} = c^2\nabla^2u $$
    ```

### Academic-Grade Simplicity  
-   **Automatic layout engine** \- Focus on content, not pixel-pushing  
-   **Meaningful animations** \- Minimal syntax for essential effects:  
    `Conclusion -->-- fade`  
-   **Themed templates** \- Maintain professional branding effortlessly  
    ```markpoint
    theme = #2A5CAA   // University blue
    background = #F8FBFF
    ```

### One Source, Multiple Outputs  
-   MP[MarkPoint .mp] -> PPT[PowerPoint]
-   MP -> PDF[Handout PDF]
-   MP -> MD[Markdown Notes]
-   MP -> HTML[Web Slides]

### Key Features  
| Category        | Capabilities                                    |
|-----------------|-------------------------------------------------|
| **Core Syntax** | Headers, Lists, Blockquotes, Dividers           |
| **Technical**   | LaTeX Math, Code Blocks, Tables                 |
| **Layout**      | Auto-Pagination, Theme Colors, Smart Spacing    |
| **Workflow**    | PPTX Export, Version Control, CI/CD Integration |

### Get Started in 60 Seconds  
1.  Install: `pip install markpoint`  

2.  Create `presentation.mp`: 

    ```markpoint
    ---
    # Art of MarkPoint  
    ## Nejiwwkr  
    ---
    # Page Turning
    When the height of page is not enough to hold the text, the markpoint will turn the pages automatically, which follows the same title of the original page  
    Use "!!!" to implicitly force the automatically turning to happen, or use "---" and "#" to explicitly turn the page
    ---
    # Thank you for reading!
    ## rendered by markpoint  
    ---
    ```

3.  Compile: `markpoint --original "Example.mp" --target "Example.pptx" --type "pptx"`  


## Designed For  
-   Academic researchers writing lecture slides  
-   Engineers creating technical reports  
-   Educators preparing course materials  
-   Developers who hate GUI editors

Join thousands who've escaped PowerPoint prison. [Get Started →](https://github.com/Nejiwwkr/MarkPoint)|[See Examples →](example/Example.pptx)  


## Roadmap  
-   **v0.9** (Current): Core rendering engine  
-   **v1.0**: Tables/Code blocks/Animation support  
-   **v2.0**: IDEA/VSC/Vim Syntax Support