# Contributing

欢迎补充 Agentic Systems for Security 相关论文、改进分类，以及修正文献信息或链接。

## 收录范围

本仓库围绕 SoK 的七类安全任务组织文献，当前快照以 2025–2026 年 IEEE S&P、USENIX Security、ACM CCS 和 NDSS 主会为范围，并单独标注已确认录用的 2027 年论文。新的年份和会议范围应在更新时明确说明。

每篇论文应提供可访问的全文和可核查的录用依据。使用作者或机构公告作为依据时，需要明确标注。尚无全文或仅有预印本的候选可通过 Issue 记录，满足当前收录要求后再进入主列表。

说明论文解决的安全任务、技术机制和验证局限。模型与工具的固定组合、有反馈的工作流和自主 Agent 都可以作为研究或比较对象；请准确描述控制方式和反馈阶段。

## 更新流程

1. 检查 [数据](data/papers.json) 和[会议索引](docs/venues.md)，确认论文尚未收录；预印本与会议版本按同一工作处理。
2. 编辑 `data/papers.json`。新增条目使用下一个稳定编号，如 `P086`；保留已有编号。
3. 依据 `data/taxonomy.json` 选择一个主分类，补充 `related_tasks` 和 `designs`。跨任务标签可以多选，不重复收录同一论文。
4. 填写 `title`、`short_name`、`year`、`venue`、`role`、`url`、`acceptance_label`、`acceptance_url`、`acceptance_status`、`bottleneck`、`mechanism` 和 `limitations`。未知信息应核实后再填写，不推测作者、DOI 或代码仓库。
5. 运行下列命令，并把生成的 Markdown 一起提交：

```sh
python3 scripts/build.py
python3 scripts/build.py --check
```

脚本只使用 Python 标准库。README、逐篇分析、映射表和会议索引均由数据生成；介绍或排版需要调整时，修改 `scripts/build.py` 中对应模板。

## 分类与证据

- 主分类按主要任务目标确定；硬件、隐私合规等相邻研究放在 `adjacent`。
- `role` 取 `研究系统与反馈流程`、`边界对照` 或 `评测与方法背景`。它与任务类别独立。
- `acceptance_status` 取 `conference-listed` 或 `author-confirmed`。当前 2027 年条目使用后者。
- D1–D5 对应 SoK §3.1–§3.5。不要仅因论文使用 LLM、包含多个 Agent 或运行过测试，就推断其具有自主规划或独立验证能力。
- 对编译成功、代码覆盖、漏洞触发、安全影响和补丁正确性分别表述；统计结果注明样本与预算边界。

修正现有条目时，在 PR 中附来源并解释变化。`docs/source-corpus.md` 是最初 85 篇的来源快照，保持原样；后续修订在当前数据及 Git 历史中记录。若研究范围确需删除旧条目，应同时调整保留原始 ID 的校验规则，并说明原因。

## 许可证

文献整理与原创说明采用 [CC BY 4.0](LICENSE)，构建脚本采用 [MIT](scripts/LICENSE)。请提供论文和代码的官方或作者链接；第三方全文仍遵循其原有许可。
