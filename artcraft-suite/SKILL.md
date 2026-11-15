---
name: artcraft-suite
description: "Index and dispatcher for all 20 ArtCraft Craft App Suite skills (ArtCraft Studio, PhotoCraft, LightCraft, VectorCraft, FigCraft, DesignCraft, WordCraft, DeckCraft, GridCraft, PdfCraft, EffectCraft, FilmCraft, AniCraft, SoundCraft, CADCraft, Craft Anything, SolidCraft, TextureCraft, MaterialCraft, MailCraft). Trigger whenever the user mentions ArtCraft, the Craft Apps, the ArtCraft Launcher, asks which ArtCraft app handles a job, or wants to install, automate, script, drive, or troubleshoot any of these open-source creative apps."
description_zh: "ArtCraft 全套 20 款开源创意软件的技能总索引与分发器。用户提到 ArtCraft、Craft Apps、ArtCraft Launcher，或询问某件事该用哪个 Craft 软件、想安装/自动化/排错时，先加载本技能定位到具体软件技能。"
display_name: "ArtCraft 全套技能索引"
version: "1.0.0-wb"
source_app: "https://github.com/storytold/artcraft"
localized_by: "WorkBuddy localization"
---

# ArtCraft 全套技能索引（20 款软件 + 1 个索引）

ArtCraft 是 [storytold](https://github.com/storytold) 开源的一整套 pure-Rust 创意软件（Craft App Suite），由 [ArtCraft Launcher](https://github.com/storytold/craft-launcher) 统一安装与更新。本目录下的 20 个技能插件，一款软件一个，教 AI 智能体**真正能做什么、不能做什么、以及怎么通过 headless CLI / MCP server / JSON 控制通道驱动它**，而不是盲点 GUI。

## 怎么用

- 直接说软件名或需求：例如「用 PhotoCraft 批量导图」「把这个 .pptx 用 DeckCraft 导出 PDF」「FilmCraft 粗剪怎么脚本化」，对应技能会自动触发；也可以用 `/<技能名>` 显式调用。
- 拿不准用哪个软件时，看下面分组表，再加载对应技能读细节。
- 每个技能正文开头有「中文速查」，包含版本基线、自动化入口、中文触发词、Windows 路径对照和**执行前检查**。

## 前提（务必先确认）

1. **技能不等于软件本体**。这些插件是驾驶手册，不含可执行文件。要真正跑命令，需先用 ArtCraft Launcher 安装对应软件；未安装时只能提供方案、格式知识与操作步骤，**不要虚构执行结果**。
2. 用 `where <软件名>-cli` 和 `<软件名>-cli --version` 确认安装与版本；命令 / 工具数量以本机实测为准，正文数据来自上游固定 commit。
3. Windows 下二进制带 `.exe`，配置与日志在 `%APPDATA%` / `%LOCALAPPDATA%`；上游正文里的 macOS 路径（`~/Library/Application Support/...`、`/Applications/...`）只作概念对照。
4. ArtCraft Studio 是云端计费的生成工作台，**没有 CLI、MCP、控制通道、本地推理和项目文件**；其余多数软件提供 headless CLI + MCP + 控制通道。

## 本机安装状态

- 本仓库不含任何特定机器的路径。请按 README 的方法确认软件与 CLI 是否安装。
- 技能插件是驾驶手册，不含软件本体；未安装时只提供能力边界、格式与命令参考。

## 软件清单

### AI 生成与创作工作台

| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |
|---|---|---|---|---|
| `artcraft-studio` · ArtCraft Studio | AI 图像 / 视频 / 音乐 / 3D 网格生成工作台 | 0.41.1 | 无 CLI | [GitHub](https://github.com/storytold/artcraft) |
| `craft-anything` · Craft Anything | ArtCraft 的逆向工程 / clean-room 重建工作台：分析网站、桌面或手机应用，交给编码代 | 0.6.1 | `craft-anything-cli` | [GitHub](https://github.com/storytold/craft-anything) |

### 图像 / 摄影 / 矢量

| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |
|---|---|---|---|---|
| `photocraft` · PhotoCraft | 开源纯 Rust 图像编辑器 | 0.23.1 | `photocraft-cli`（8 子命令） | [GitHub](https://github.com/storytold/photocraft) |
| `lightcraft` · LightCraft | 开源纯 Rust 照片库与非破坏性 RAW 显影 | 0.21.1 | `lightcraft-cli` | [GitHub](https://github.com/storytold/lightcraft) |
| `vectorcraft` · VectorCraft | 开源纯 Rust 矢量插画 | 0.24.1 | `vectorcraft-cli`（7 子命令） | [GitHub](https://github.com/storytold/vectorcraft) |
| `texturecraft` · TextureCraft | Substance 3D Painter 工作流的 3D 纹理绘制：PBR 图层、遮罩、生成器、网格贴图 | 0.6.1 | `texturecraft-cli`，与 MaterialCraft 的 .mcmat 材质 | [GitHub](https://github.com/storytold/texturecraft) |
| `materialcraft` · MaterialCraft | 节点式程序化材质设计器 | 0.4.1 | `materialcraft-cli`；.mcmat 可交给 TextureCraft 使用 | [GitHub](https://github.com/storytold/materialcraft) |

### 设计 / 排版 / 文档

| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |
|---|---|---|---|---|
| `figcraft` · FigCraft | 离线优先的界面设计、原型与白板工具 | 0.18.1 | `figcraft-cli` | [GitHub](https://github.com/storytold/figcraft) |
| `designcraft` · DesignCraft | InDesign 级页面排版与出版 | 0.20.1 | headless CLI | [GitHub](https://github.com/storytold/designcraft) |
| `wordcraft` · WordCraft | 开源纯 Rust 文字处理 | 0.18.1 | `wordcraft-cli` | [GitHub](https://github.com/storytold/wordcraft) |
| `deckcraft` · DeckCraft | PowerPoint 兼容的演示文稿 | 0.18.1 | 329 条命令 | [GitHub](https://github.com/storytold/deckcraft) |
| `gridcraft` · GridCraft | 开源纯 Rust 电子表格 | 0.19.1 | `gridcraft-cli` | [GitHub](https://github.com/storytold/gridcraft) |
| `pdfcraft` · PdfCraft | Acrobat Pro 级 PDF 工作台 | 0.21.1 | `pdfcraft-cli` | [GitHub](https://github.com/storytold/pdfcraft) |

### 动画 / 视频 / 音频

| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |
|---|---|---|---|---|
| `anicraft` · AniCraft | 开源 2D 矢量动画工作室 | 0.2.1 | `anicraft-cli`（render / GIF / commands / exec  | [GitHub](https://github.com/storytold/anicraft) |
| `effectcraft` · EffectCraft | 纯 Rust 合成 / VFX 工具 | 0.24.1 | `effectcraft-cli` | [GitHub](https://github.com/storytold/effectcraft) |
| `filmcraft` · FilmCraft | 专业非线性视频剪辑 | 0.20.1 | `filmcraft-cli` | [GitHub](https://github.com/storytold/filmcraft) |
| `soundcraft` · SoundCraft | 纯 Rust DAW | 0.20.1 | `soundcraft-cli` | [GitHub](https://github.com/storytold/soundcraft) |

### 工程 / CAD / 办公

| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |
|---|---|---|---|---|
| `cadcraft` · CADCraft | AutoCAD 风格 2D CAD | 0.20.1 | `cadcraft-cli` | [GitHub](https://github.com/storytold/cadcraft) |
| `solidcraft` · SolidCraft | Tangency Labs 的参数化 3D CAD：草图约束、特征时间线、钣金、装配、运动研究、WASM | 0.41.0 | `solidcraft-cli` | [GitHub](https://github.com/tangency-labs/solidcraft) |
| `mailcraft` · MailCraft | 社区版 Outlook 形态的邮件 / 日历 / 联系人 / 任务客户端 | 0.12.0 | 338 条引擎命令 | [GitHub](https://github.com/UCS-Care-Group/mailcraft) |

## 触发词速查

- `artcraft-studio`：ArtCraft、AI 出图、图生视频、Nano Banana、Sora、Midjourney、Omni API、生成任务失败、生成记录
- `craft-anything`：Craft Anything、逆向、复刻软件、clean-room 重建、拆解某应用、三宽度截图比对
- `photocraft`：PhotoCraft、修图、抠图、图层、蒙版、批量导图、PDF 转画板、PSD 检查、色彩管理
- `lightcraft`：LightCraft、RAW 显影、照片管理、批量导出、预设、目录 catalog、冲图
- `vectorcraft`：VectorCraft、矢量图、钢笔路径、SVG 编辑、插画、形状布尔运算
- `texturecraft`：TextureCraft、3D 贴图绘制、PBR 材质、烘焙法线/AO、智能材质、纹理集导出
- `materialcraft`：MaterialCraft、节点材质、PBR 贴图、可平铺纹理、SBS、材质烘焙导出
- `figcraft`：FigCraft、UI 设计、原型、自动布局、组件、变量、开发者模式、白板、思维导图
- `designcraft`：DesignCraft、排版、杂志、画册、串文、基线网格、印前预检、PDF/X-4、EPUB 分章
- `wordcraft`：WordCraft、文档排版、docx 编辑、加密 Word、导出 PDF、目录脚注
- `deckcraft`：DeckCraft、PPT、幻灯片、母版、SmartArt、切换动画、放映、导出 PDF
- `gridcraft`：GridCraft、表格、xlsx、公式、函数、批量计算、图表、打印导出
- `pdfcraft`：PdfCraft、合并拆分 PDF、OCR、表单、签名、密文、转 Word、PDF 修复
- `anicraft`：AniCraft、做动画、弹跳球、补间、逐帧、精灵图、导出 GIF/Lottie
- `effectcraft`：EffectCraft、合成、关键帧、特效、跟踪、rotoscoping、Lottie、渲染队列、插件
- `filmcraft`：FilmCraft、粗剪、多机位、调色、LUT、字幕、H.264 导出、EDL/AAF 交接
- `soundcraft`：SoundCraft、多轨录音、混音、MIDI 编辑、插件、自动化、bounce 导出
- `cadcraft`：CADCraft、CAD 图纸、DXF、DWG、XCLIP、块参照、标注、SHX 字体
- `solidcraft`：SolidCraft、3D 建模、草图约束、拉伸旋转、钣金、装配体、STEP 导出
- `mailcraft`：MailCraft、邮件客户端、.pst 导入、日历联系人、IMAP 配置、邮箱迁移

## 来源与许可

- 技能正文：[midasmatterhorn/artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills)（evidence-verified，逐版本审计），按 WorkBuddy 规范做了中文触发、Windows 路径与执行前检查的本地化。
- 软件本体：[storytold/artcraft](https://github.com/storytold/artcraft) 及各独立仓库，MIT / Apache-2.0 双协议；上游技能仓库许可见其 `LICENSE`。
- 上游若更新，重新下载各 `SKILL.md` 并保留本地化的 frontmatter 与「中文速查」段落即可。
