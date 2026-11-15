# -*- coding: utf-8 -*-
"""Build WorkBuddy skill plugins for the whole ArtCraft Craft App Suite."""
import io, os, re

SRC = os.environ.get("CRAFT_UPSTREAM_DIR", os.path.join(os.getcwd(), "upstream"))
DST = os.environ.get("CRAFT_SKILLS_OUT", os.path.join(os.getcwd(), "skills-out"))

# slug -> (中文名, 用途, 版本基线, GitHub, 触发词, 格式, 自动化说明, 特别提醒)
META = {
    "artcraft-studio": (
        "ArtCraft Studio · AI 生成工作台",
        "AI 图像 / 视频 / 音乐 / 3D 网格生成工作台（Rust + React 桌面端），调用 Omni API 与 fal / Midjourney / Sora / Grok / World Labs 等供应商",
        "0.41.1 @ 07ebde1", "https://github.com/storytold/artcraft",
        "ArtCraft、AI 出图、图生视频、Nano Banana、Sora、Midjourney、Omni API、生成任务失败、生成记录",
        "无本地项目文件",
        "无 CLI、无 MCP、无控制通道；只能通过文档排错、写调用代码、检查任务队列 / 产物",
        "云端计费、无本地推理。绝不读取或外泄用户存储的 cookies 与 API key，也不要承诺离线生成或 GUI 自动化。",
    ),
    "photocraft": (
        "PhotoCraft · 图像编辑",
        "开源纯 Rust 图像编辑器（类 Photoshop）：图层、蒙版、调整图层、实时文字、矢量、智能对象、真实 PSD 读写",
        "0.23.1 @ 45066c4", "https://github.com/storytold/photocraft",
        "PhotoCraft、修图、抠图、图层、蒙版、批量导图、PDF 转画板、PSD 检查、色彩管理",
        ".pcraft .psd .psb .xcf .ora .atn .asl",
        "`photocraft-cli`（8 子命令）、26 工具 MCP、loopback JSON 控制通道、headless serve",
        "早期 alpha，不要承诺 Photoshop 级 PSD 保真或生成式 AI 功能。",
    ),
    "lightcraft": (
        "LightCraft · 图片库与 RAW 显影",
        "开源纯 Rust 照片库与非破坏性 RAW 显影（类 Lightroom Classic）",
        "0.21.1 @ 361e3bc", "https://github.com/storytold/lightcraft",
        "LightCraft、RAW 显影、照片管理、批量导出、预设、目录 catalog、冲图",
        ".lcpreset .lcprint catalog.snap catalog.log DNG CR3 ARW NEF RAF",
        "`lightcraft-cli`、MCP server、JSON 控制通道；另有独立 WebAssembly 构建",
        "RAW 格式支持范围以正文实测为准，CR3 等可能仅支持预览。",
    ),
    "vectorcraft": (
        "VectorCraft · 矢量插画",
        "开源纯 Rust 矢量插画（类 Illustrator），带脚本引擎与多通道自动化",
        "0.24.1 @ f4922aa", "https://github.com/storytold/vectorcraft",
        "VectorCraft、矢量图、钢笔路径、SVG 编辑、插画、形状布尔运算",
        ".vectorcraft .drawcraft .vctemplate .svg .ai",
        "`vectorcraft-cli`（7 子命令）、33 工具 MCP、30 方法 JSON 控制通道、浏览器 JS API、进程内 JS 脚本引擎",
        "",
    ),
    "figcraft": (
        "FigCraft · 界面设计与原型",
        "离线优先的界面设计、原型与白板工具（类 Figma Design 工作流）",
        "0.18.1 @ 4acc293", "https://github.com/storytold/figcraft",
        "FigCraft、UI 设计、原型、自动布局、组件、变量、开发者模式、白板、思维导图",
        ".figcraft",
        "`figcraft-cli`、MCP server、JSON 控制通道",
        "",
    ),
    "designcraft": (
        "DesignCraft · 页面排版与出版",
        "InDesign 级页面排版与出版（IDML/INDD 导入、PDF/X、EPUB、预检、批量导出）",
        "0.20.1 @ 33a4678", "https://github.com/storytold/designcraft",
        "DesignCraft、排版、杂志、画册、串文、基线网格、印前预检、PDF/X-4、EPUB 分章",
        ".designcraft .idml .indd .indt .dcbook .dclib .ase",
        "headless CLI、MCP server、JSON 控制通道",
        "",
    ),
    "wordcraft": (
        "WordCraft · 文字处理",
        "开源纯 Rust 文字处理（类 Word），读写 .docx（含加密文档）、导出 PDF/PNG",
        "0.18.1 @ 079f478", "https://github.com/storytold/wordcraft",
        "WordCraft、文档排版、docx 编辑、加密 Word、导出 PDF、目录脚注",
        ".docx .doc .odt .ott .fodt .mht .mhtml",
        "`wordcraft-cli`、18 工具 MCP、localhost JSON 控制通道、headless 截图工具",
        "alpha 阶段；导出时可用严格检查拒绝静默不完整的渲染。",
    ),
    "deckcraft": (
        "DeckCraft · 演示文稿",
        "PowerPoint 兼容的演示文稿（母版、形状、图表、SmartArt、切换、动画、放映）",
        "0.18.1 @ 7cc73ab", "https://github.com/storytold/deckcraft",
        "DeckCraft、PPT、幻灯片、母版、SmartArt、切换动画、放映、导出 PDF",
        ".deckcraft .pptx .potx .ppsx .rtf .md",
        "329 条命令、`deckcraft-cli`（12 子命令）、25 工具 MCP、JSON 控制通道、window.deckcraft 页面 API",
        "",
    ),
    "gridcraft": (
        "GridCraft · 电子表格",
        "开源纯 Rust 电子表格（类 Excel），读写真实 .xlsx",
        "0.19.1 @ 476448d", "https://github.com/storytold/gridcraft",
        "GridCraft、表格、xlsx、公式、函数、批量计算、图表、打印导出",
        ".xlsx .xlsm .csv",
        "`gridcraft-cli`、MCP server、live JSON 控制通道",
        "涉及本地表格任务时，注意与 WorkBuddy 自带的表格技能区分：本技能专用于驱动 GridCraft 软件本体。",
    ),
    "pdfcraft": (
        "PdfCraft · PDF 工作台",
        "Acrobat Pro 级 PDF 工作台（阅读、组织、批注、表单、签名、密文、OCR、印前、转换）",
        "0.21.1 @ b503b2e", "https://github.com/storytold/pdfcraft",
        "PdfCraft、合并拆分 PDF、OCR、表单、签名、密文、转 Word、PDF 修复",
        ".pdf",
        "`pdfcraft-cli`、MCP server、UI 控制通道",
        "",
    ),
    "effectcraft": (
        "EffectCraft · 动态图形与视觉特效",
        "纯 Rust 合成 / VFX 工具（类 After Effects）：合成、关键帧、308 特效、表达式、跟踪、抠像、Lottie、WASM 插件",
        "0.24.1 @ 582344d", "https://github.com/storytold/effectcraft",
        "EffectCraft、合成、关键帧、特效、跟踪、rotoscoping、Lottie、渲染队列、插件",
        ".aep .aepx .json（repro 脚本）",
        "`effectcraft-cli`、可重放 repro 脚本、WASM ABI 1/2 效果插件与外部 helper",
        "AE 工程交换是有明确子集的，不能假定所有 .aep 特性可往返。",
    ),
    "filmcraft": (
        "FilmCraft · 视频剪辑",
        "专业非线性视频剪辑（剪辑、多机位、调色、特效、字幕、混音、导出），类 Premiere 工作流",
        "0.20.1 @ cedf0c9", "https://github.com/storytold/filmcraft",
        "FilmCraft、粗剪、多机位、调色、LUT、字幕、H.264 导出、EDL/AAF 交接",
        ".fcproj .prfpset",
        "`filmcraft-cli`、控制通道、MCP server、window.filmcraft 页面 API",
        "不要假定 Premiere 独有特性（.prproj 导入、第三方插件、上传目的地）存在。",
    ),
    "anicraft": (
        "AniCraft · 2D 矢量动画",
        "开源 2D 矢量动画工作室（类 Adobe Animate）：舞台、时间轴、图层、关键帧、补间、元件、骨骼、相机、声音",
        "0.2.1 @ d0beaf2", "https://github.com/storytold/anicraft",
        "AniCraft、做动画、弹跳球、补间、逐帧、精灵图、导出 GIF/Lottie",
        ".anicraft .fla .xfl .svg .png .wav .mp3",
        "`anicraft-cli`（render / GIF / commands / exec / run / serve / MCP）、5 工具 MCP、240 条命令引擎",
        "早期 alpha；不要凭 Animate 或 SWF 的经验推断其行为。",
    ),
    "soundcraft": (
        "SoundCraft · 数字音频工作站",
        "纯 Rust DAW（类 Pro Tools）：多轨音频/MIDI、混音台、CLAP/VST3/AU 插件、自动化、录制、bounce、环绕声",
        "0.20.1 @ a52bbdc", "https://github.com/storytold/soundcraft",
        "SoundCraft、多轨录音、混音、MIDI 编辑、插件、自动化、bounce 导出",
        ".scraft .scraftz .scgrp",
        "`soundcraft-cli`、JSON 控制通道、MCP server",
        "",
    ),
    "cadcraft": (
        "CADCraft · 2D CAD 制图",
        "AutoCAD 风格 2D CAD（DXF/DWG、块与外部参照、光栅附着、MTEXT、多重引线）",
        "0.20.1 @ 7526dc6", "https://github.com/storytold/cadcraft",
        "CADCraft、CAD 图纸、DXF、DWG、XCLIP、块参照、标注、SHX 字体",
        ".dxf .dwg .png .jpg .bmp .tif",
        "`cadcraft-cli`、MCP server、JSON 控制通道、浏览器 page API",
        "",
    ),
    "craft-anything": (
        "Craft Anything · 软件逆向与 AI 重建",
        "ArtCraft 的逆向工程 / clean-room 重建工作台：分析网站、桌面或手机应用，交给编码代理重建并逐轮比对",
        "0.6.1 @ 48a9c5a", "https://github.com/storytold/craft-anything",
        "Craft Anything、逆向、复刻软件、clean-room 重建、拆解某应用、三宽度截图比对",
        "任意工程 / 归档 / 二进制输入",
        "`craft-anything-cli`、内置检查工具链（反汇编、反编译、归档、浏览器、数据库、抓包）",
        "需要配合编码代理（上游以 Claude Code 为首选）；遵守原软件许可，不做侵权复制。",
    ),
    "solidcraft": (
        "SolidCraft · 参数化 3D CAD",
        "Tangency Labs 的参数化 3D CAD：草图约束、特征时间线、钣金、装配、运动研究、WASM 命令插件",
        "0.41.0 @ 3c8efdb", "https://github.com/tangency-labs/solidcraft",
        "SolidCraft、3D 建模、草图约束、拉伸旋转、钣金、装配体、STEP 导出",
        ".step .stp .iges .igs .3mf .stl .obj .glb .urdf .dxf",
        "`solidcraft-cli`、沙箱化 WebAssembly 命令插件",
        "由 Tangency Labs 独立开发，不属于 Autodesk / Dassault 产品。",
    ),
    "texturecraft": (
        "TextureCraft · 3D 纹理绘制",
        "Substance 3D Painter 工作流的 3D 纹理绘制：PBR 图层、遮罩、生成器、网格贴图烘焙、纹理集导出",
        "0.6.1 @ 34a1961", "https://github.com/storytold/texturecraft",
        "TextureCraft、3D 贴图绘制、PBR 材质、烘焙法线/AO、智能材质、纹理集导出",
        ".tcraft .tcmat .gltf .glb",
        "`texturecraft-cli`，与 MaterialCraft 的 .mcmat 材质互通",
        "",
    ),
    "materialcraft": (
        "MaterialCraft · 程序化材质",
        "节点式程序化材质设计器（类 Substance Designer）：171 函数 SBS 库、可平铺 PBR、3D 预览、贴图导出",
        "0.4.1 @ 65f7bfd", "https://github.com/storytold/materialcraft",
        "MaterialCraft、节点材质、PBR 贴图、可平铺纹理、SBS、材质烘焙导出",
        ".sbs .mcraft .mcmat",
        "`materialcraft-cli`；.mcmat 可交给 TextureCraft 使用",
        "",
    ),
    "mailcraft": (
        "MailCraft · 邮件日历客户端",
        "社区版 Outlook 形态的邮件 / 日历 / 联系人 / 任务客户端（IMAP/SMTP、Graph OAuth、EWS、JMAP）",
        "0.12.0 @ 92eb10c", "https://github.com/UCS-Care-Group/mailcraft",
        "MailCraft、邮件客户端、.pst 导入、日历联系人、IMAP 配置、邮箱迁移",
        ".mailcraft .eml .mbox .ics .vcf .pst",
        "338 条引擎命令、85 条窗口命令、20 工具 MCP、loopback JSON 控制通道、`mailcraft-cli`（14 子命令）",
        "这是第三方社区应用，与 WorkBuddy 自带的 QQ 邮箱 / Agent Mail 技能不是一回事。公开 beta。",
    ),
}

# 本机实测（2026-11-14）：已安装且带 CLI 的应用 -> CLI 绝对路径
LAUNCHER = "ArtCraft Launcher"
LOCAL = {}  # 可选：{slug: r"本机 CLI 绝对路径"}

GROUPS = [
    ("AI 生成与创作工作台", ["artcraft-studio", "craft-anything"]),
    ("图像 / 摄影 / 矢量", ["photocraft", "lightcraft", "vectorcraft", "texturecraft", "materialcraft"]),
    ("设计 / 排版 / 文档", ["figcraft", "designcraft", "wordcraft", "deckcraft", "gridcraft", "pdfcraft"]),
    ("动画 / 视频 / 音频", ["anicraft", "effectcraft", "filmcraft", "soundcraft"]),
    ("工程 / CAD / 办公", ["cadcraft", "solidcraft", "mailcraft"]),
]

HEAD = """## 中文速查（WorkBuddy 本地化 · 先读这段）

| 项 | 内容 |
|---|---|
| **软件** | {zh} |
| **用途** | {purpose} |
| **版本基线** | {ver}（上游源码实测，Launcher 自动更新后可能更新） |
| **自动化入口** | {auto} |
| **中文触发词** | {triggers} |
| **相关格式** | {formats} |
| **项目地址** | {repo} |
| **技能原文** | https://github.com/midasmatterhorn/artcraft-skills/tree/main/{slug} |
| **本机安装状态** | {local} |

**执行前检查（Windows 本机）**

1. 先确认软件是否安装，本机状态见上表。`where {cli}` 找不到不代表没装（部分 CLI 未加入 PATH，需用绝对路径）。**未安装时只给方案、格式说明与操作步骤，不要假装命令已经执行成功，也不要虚构结果文件。**
2. 上游正文以 macOS 路径举例（`/Applications/...`、`~/Library/Application Support/...`）。Windows 下可执行文件带 `.exe`，配置与日志位于 `%APPDATA%` / `%LOCALAPPDATA%`，安装通常在 `%LOCALAPPDATA%\\Programs` 或 `C:\\Program Files`。若 WorkBuddy 运行在服务会话（session 0）里没有桌面，改用 headless CLI 或 MCP，别试图弹 GUI。
3. **优先 headless CLI / MCP server / JSON 控制通道，不要盲点 GUI。** 命令数、工具数与参数以本机实测为准（例如 `{cli} commands`、`{cli} --help`）；正文里的版本号与统计来自上游固定 commit。
{note}
---

以下为上游 evidence-verified 技能正文（英文原文，保留不改）：

"""

TAIL = """

---

**来源与维护**：本插件按 WorkBuddy 技能规范本地化制作——正文取自 [midasmatterhorn/artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills) 的 evidence-verified 原文，新增中文触发描述、Windows 路径对照与执行前检查。ArtCraft 软件本体见 [storytold](https://github.com/storytold)，以 MIT / Apache-2.0 双协议开源；上游技能仓库的许可以其 `LICENSE` 为准。软件需通过 [ArtCraft Launcher](https://github.com/storytold/craft-launcher) 单独安装，本插件只提供驾驶手册，不含软件本体。
"""


import json


def split_fm(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    return m.group(1), m.group(2)


def yaml_quote(s):
    return json.dumps(s, ensure_ascii=False)


def parse_upstream_fm(fm):
    """把上游 name/description 解析出来，统一改成单行 YAML 双引号标量。"""
    name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
    m = re.search(r"^description:\s*(.*)$", fm, re.M)
    val = m.group(1).strip()
    tail = fm[m.end():]
    if val in (">-", ">", "|-", "|"):
        desc = " ".join(l.strip() for l in tail.splitlines() if l.strip())
    elif val.startswith('"'):
        try:
            desc = json.loads(val)
        except Exception:
            desc = val.strip('"')
    else:
        desc = val
    return name, desc


def build():
    os.makedirs(DST, exist_ok=True)
    made = []
    for slug, (zh, purpose, ver, repo, triggers, formats, auto, note) in META.items():
        src = os.path.join(SRC, slug + ".SKILL.md")
        text = io.open(src, encoding="utf-8").read()
        fm, body = split_fm(text)
        cli = slug + "-cli" if slug != "artcraft-studio" else "artcraft-studio"
        note_txt = ("4. **特别注意**：" + note) if note else ""
        local = "请在本机自行确认软件与 CLI 是否安装（见 README 的安装与验证章节）。"
        head = HEAD.format(
            zh=zh, purpose=purpose, ver=ver, auto=auto,
            triggers=triggers, formats=formats, repo=repo, slug=slug,
            cli=cli, note=note_txt, local=local,
        )
        desc_zh = (zh + "。" + purpose.split("（")[0][:60] + "。当用户提到 "
                   + triggers.split("、")[0] + " 等相关需求时触发；提供该软件的能力边界、"
                   "文件格式、CLI / MCP / 控制通道用法与排错指引。软件未安装时仅作知识参考，不得虚构执行结果。")
        extra = (
            "\ndescription_zh: " + yaml_quote(desc_zh)
            + "\ndisplay_name: " + yaml_quote(zh)
            + '\nversion: "1.0.0-wb"'
            + "\nsource_app: " + yaml_quote(repo)
            + "\nsource_skill: " + yaml_quote("https://github.com/midasmatterhorn/artcraft-skills/tree/main/" + slug)
            + '\nlocalized_by: "WorkBuddy localization"'
        )
        name, desc = parse_upstream_fm(fm)
        newfm = "name: " + name + "\ndescription: " + yaml_quote(desc) + extra
        out = "---\n" + newfm + "\n---\n\n" + head + body.rstrip() + TAIL
        d = os.path.join(DST, slug)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "SKILL.md")
        io.open(p, "w", encoding="utf-8", newline="\n").write(out)
        made.append((slug, len(out)))
    return made


def build_index():
    lines = []
    lines.append("---")
    lines.append("name: artcraft-suite")
    lines.append('description: "Index and dispatcher for all 20 ArtCraft Craft App Suite skills (ArtCraft Studio, PhotoCraft, LightCraft, VectorCraft, FigCraft, DesignCraft, WordCraft, DeckCraft, GridCraft, PdfCraft, EffectCraft, FilmCraft, AniCraft, SoundCraft, CADCraft, Craft Anything, SolidCraft, TextureCraft, MaterialCraft, MailCraft). Trigger whenever the user mentions ArtCraft, the Craft Apps, the ArtCraft Launcher, asks which ArtCraft app handles a job, or wants to install, automate, script, drive, or troubleshoot any of these open-source creative apps."')
    lines.append('description_zh: "ArtCraft 全套 20 款开源创意软件的技能总索引与分发器。用户提到 ArtCraft、Craft Apps、ArtCraft Launcher，或询问某件事该用哪个 Craft 软件、想安装/自动化/排错时，先加载本技能定位到具体软件技能。"')
    lines.append('display_name: "ArtCraft 全套技能索引"')
    lines.append('version: "1.0.0-wb"')
    lines.append('source_app: "https://github.com/storytold/artcraft"')
    lines.append('localized_by: "WorkBuddy localization"')
    lines.append("---")
    lines.append("")
    lines.append("# ArtCraft 全套技能索引（20 款软件 + 1 个索引）")
    lines.append("")
    lines.append("ArtCraft 是 [storytold](https://github.com/storytold) 开源的一整套 pure-Rust 创意软件（Craft App Suite），由 [ArtCraft Launcher](https://github.com/storytold/craft-launcher) 统一安装与更新。本目录下的 20 个技能插件，一款软件一个，教 AI 智能体**真正能做什么、不能做什么、以及怎么通过 headless CLI / MCP server / JSON 控制通道驱动它**，而不是盲点 GUI。")
    lines.append("")
    lines.append("## 怎么用")
    lines.append("")
    lines.append("- 直接说软件名或需求：例如「用 PhotoCraft 批量导图」「把这个 .pptx 用 DeckCraft 导出 PDF」「FilmCraft 粗剪怎么脚本化」，对应技能会自动触发；也可以用 `/<技能名>` 显式调用。")
    lines.append("- 拿不准用哪个软件时，看下面分组表，再加载对应技能读细节。")
    lines.append("- 每个技能正文开头有「中文速查」，包含版本基线、自动化入口、中文触发词、Windows 路径对照和**执行前检查**。")
    lines.append("")
    lines.append("## 前提（务必先确认）")
    lines.append("")
    lines.append("1. **技能不等于软件本体**。这些插件是驾驶手册，不含可执行文件。要真正跑命令，需先用 ArtCraft Launcher 安装对应软件；未安装时只能提供方案、格式知识与操作步骤，**不要虚构执行结果**。")
    lines.append("2. 用 `where <软件名>-cli` 和 `<软件名>-cli --version` 确认安装与版本；命令 / 工具数量以本机实测为准，正文数据来自上游固定 commit。")
    lines.append("3. Windows 下二进制带 `.exe`，配置与日志在 `%APPDATA%` / `%LOCALAPPDATA%`；上游正文里的 macOS 路径（`~/Library/Application Support/...`、`/Applications/...`）只作概念对照。")
    lines.append("4. ArtCraft Studio 是云端计费的生成工作台，**没有 CLI、MCP、控制通道、本地推理和项目文件**；其余多数软件提供 headless CLI + MCP + 控制通道。")
    lines.append("")
    lines.append("## 本机安装状态")
    lines.append("")
    lines.append("- 本仓库不含任何特定机器的路径。请按 README 的方法确认软件与 CLI 是否安装。")
    lines.append("- 技能插件是驾驶手册，不含软件本体；未安装时只提供能力边界、格式与命令参考。")
    lines.append("")
    lines.append("## 软件清单")
    lines.append("")
    for gname, slugs in GROUPS:
        lines.append("### " + gname)
        lines.append("")
        lines.append("| 技能 / 软件 | 用途 | 版本基线 | 主要自动化入口 | 仓库 |")
        lines.append("|---|---|---|---|---|")
        for s in slugs:
            zh, purpose, ver, repo, triggers, formats, auto, note = META[s]
            purpose_short = purpose.split("（")[0][:52]
            auto_short = auto.split("、")[0][:46]
            lines.append("| `{s}` · {zh2} | {p} | {v} | {a} | [GitHub]({r}) |".format(
                s=s, zh2=zh.split(" · ")[0], p=purpose_short, v=ver.split(" @ ")[0], a=auto_short, r=repo))
        lines.append("")
    lines.append("## 触发词速查")
    lines.append("")
    for gname, slugs in GROUPS:
        for s in slugs:
            zh, purpose, ver, repo, triggers, formats, auto, note = META[s]
            lines.append("- `{s}`：{t}".format(s=s, t=triggers))
    lines.append("")
    lines.append("## 来源与许可")
    lines.append("")
    lines.append("- 技能正文：[midasmatterhorn/artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills)（evidence-verified，逐版本审计），按 WorkBuddy 规范做了中文触发、Windows 路径与执行前检查的本地化。")
    lines.append("- 软件本体：[storytold/artcraft](https://github.com/storytold/artcraft) 及各独立仓库，MIT / Apache-2.0 双协议；上游技能仓库许可见其 `LICENSE`。")
    lines.append("- 上游若更新，重新下载各 `SKILL.md` 并保留本地化的 frontmatter 与「中文速查」段落即可。")
    lines.append("")
    d = os.path.join(DST, "artcraft-suite")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "SKILL.md")
    io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    return (len("\n".join(lines)), p)


if __name__ == "__main__":
    made = build()
    n, p = build_index()
    print("generated", len(made), "app skills + 1 index skill")
    for slug, size in made:
        print("  %-18s %7d bytes" % (slug, size))
    print("  %-18s %7d bytes  <- INDEX" % ("artcraft-suite", n))
    print("destination:", DST)
