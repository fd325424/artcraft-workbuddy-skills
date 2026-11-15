# ArtCraft WorkBuddy Skills

把 [ArtCraft](https://github.com/storytold/artcraft) 全套 20 款开源创意软件接入 WorkBuddy 的 AI 技能插件：一款软件一个 `SKILL.md`，外加一个总索引 `artcraft-suite`。

这些插件教智能体**通过软件自己的一等自动化接口（headless CLI / MCP server / JSON 控制通道）去驱动它**，而不是盲点 GUI；正文包含已验证的能力边界、文件格式、命令清单、参数、排错与验证方法。

## 做了哪些本地化

上游 [midasmatterhorn/artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills) 提供了 20 份逐版本审计（evidence-verified）的英文技能原文。本仓库在其基础上：

- frontmatter 增加 `description_zh` 中文触发描述，同时保留英文 `description`，中英双语都能触发；
- 每个技能开头增加「中文速查」：用途、版本基线、自动化入口、中文触发词、相关格式、项目地址、执行前检查；
- 补齐 Windows 路径对照（上游正文以 macOS 路径举例）与「未安装时不得虚构执行结果」的约束；
- frontmatter 统一为单行 YAML 双引号标量，避免不同解析器对多行块的处理差异；
- 新增 `artcraft-suite` 总索引，按需求分发到具体软件，附分组清单与触发词速查。

英文正文保持上游原文不改，便于后续对照更新。

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

## 安装

### WorkBuddy（用户级技能）

```powershell
git clone https://github.com/fd325424/artcraft-workbuddy-skills.git
cd artcraft-workbuddy-skills
$dest = "$env:USERPROFILE\.workbuddy\skills"
Get-ChildItem -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } |
  ForEach-Object { Copy-Item -Recurse -Force $_.FullName $dest }
```

macOS / Linux 同理，把 21 个含 `SKILL.md` 的目录复制到 `~/.workbuddy/skills/`；也可以只复制需要的那一个技能目录。WorkBuddy 会自动扫描该目录，必要时重启会话让技能被发现。

### 其它支持 SKILL.md 标准的 Agent

Claude Code（`~/.claude/skills/`）、Codex / ChatGPT（`~/.agents/skills/`）、OpenCode（`~/.config/opencode/skills/`）、Gemini CLI（`~/.gemini/skills/`）等都可直接复制目录使用。

### 前置条件

**技能只是驾驶手册，不含软件本体。** 要真正执行 CLI / MCP 命令，需先用 [ArtCraft Launcher](https://github.com/storytold/craft-launcher) 安装对应软件。未安装时技能只提供能力边界、格式说明与操作步骤，不会虚构执行结果。ArtCraft Studio 是云端计费的生成工作台，没有 CLI、MCP 或本地推理。

## 使用

直接说软件名或描述任务即可触发，例如「用 PhotoCraft 批量导图」「把这个 .pptx 用 DeckCraft 导出 PDF」「FilmCraft 粗剪怎么脚本化」；不确定用哪个软件时加载 `artcraft-suite` 索引。

确认软件已安装后，**优先 headless CLI / MCP / 控制通道**，命令与工具数量以本机实测为准（例如 `<app>-cli commands`、`--help`）。Windows 下 CLI 可能未加入 PATH，需使用绝对路径调用。

## 实测记录

在 Windows 上对 PhotoCraft 0.23.1 与 DesignCraft 0.20.1 做过完整冒烟测试：headless CLI、MCP stdio、GUI 启动均正常；真实任务（PNG→JPG 转换、文档创建与引擎命令、保存 `.pcraft`、示例文档渲染 PNG、导出 PDF、保存 `.designcraft`、生成缩略图）全部成功；中文路径读写正常。

实测数量与技能正文口径一致：PhotoCraft 1009 条引擎命令 / 26 个 MCP 工具 / 19 个 serve 方法，DesignCraft 555 条命令 / 26 个 MCP 工具。`validate-pdf` 对默认导出的普通 PDF 判定不满足 PDF/X-4 属预期结果，需要印前合规时请用 `--pdf-options` 指定 PDF/X 再校验。

## 复现与更新

`tools/build_skills.py` 是可复现的生成脚本：

```sh
git clone https://github.com/midasmatterhorn/artcraft-skills.git upstream-src
python tools/build_skills.py            # 默认从 ./upstream 读取，输出到 ./skills-out
CRAFT_UPSTREAM_DIR=/path/to/upstream-src CRAFT_SKILLS_OUT=/path/to/out python tools/build_skills.py
```

上游更新后重新生成，保留 frontmatter 与「中文速查」段落即可。

## 来源与许可

- 技能正文：[midasmatterhorn/artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills)，MIT，Copyright (c) 2026 midasmatterhorn。按 MIT 要求，其版权与许可声明完整保留在 [LICENSE](LICENSE)。
- 软件本体：[storytold](https://github.com/storytold) 及各独立仓库，MIT / Apache-2.0 双协议。
- 本仓库新增的中文描述、速查表、索引与脚本同样以 MIT 许可提供。

ArtCraft、PhotoCraft、DesignCraft 等名称归各自项目所有，本仓库为非官方的社区本地化插件。
