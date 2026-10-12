# 来源与整理口径

[返回首页](../README.md) · [SoK 正文](sok.md) · [文献原始快照](source-corpus.md)

## 来源

本仓库整理自以下材料，快照日期为 **2026-10-12**：

- [SoK 修改对话](https://chatgpt.com/share/6acca420-93d0-83e9-9b15-4ac78ad3bbdd)：用于确定最终文章结构、七类安全任务和五项技术设计。
- 对话附件 **Agentic_System_安全研究_SoK_终稿.md**：作为 [sok.md](sok.md) 的基础稿。仓库版本在第 2、3 节补充文献分布统计与图示，并按现有技术的具体不足修订第 3 节小结与第 5 节贡献总结。原始导入版本保留在 Git 历史中。
- [Agentic Security 文献映射与证据附表](https://chatgpt.com/space/page_6036c46b131481919853c86313b89f9d)：已保存为 [source-corpus.md](source-corpus.md)，保留全部 85 条记录和未纳入候选。原文中的“正文”链接指向早期草稿；仓库分类使用对话终稿。

以上 ChatGPT Page 链接可能需要源账户权限。所有文献记录和 SoK 正文均提供仓库内副本，日常查阅无需访问源 Page。

## 原始检索口径

原附表以 2025–2026 年安全四大会议官方录用名单和议程为入口，结合 LLM、agent、fuzzing、testing、repair、program analysis 等关键词及任务语义筛选，再追踪作者页面、公开论文和参考文献。附表记录了全文方法、实验和局限的核对结果。

官方入口：[CCS 2025](https://www.sigsac.org/ccs/CCS2025/accepted-papers/) · [CCS 2026](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [S&P 2025](https://sp2025.ieee-security.org/accepted-papers.html) · [S&P 2026](https://sp2026.ieee-security.org/accepted-papers.html) · [NDSS 2025](https://www.ndss-symposium.org/ndss2025/accepted-papers/) · [NDSS 2026](https://www.ndss-symposium.org/ndss2026/accepted-papers/) · [USENIX 2025](https://www.usenix.org/conference/usenixsecurity25/technical-sessions) · [USENIX 2026](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)。

该快照包含 **85 篇**：CCS 23 篇、NDSS 19 篇、IEEE S&P 16 篇、USENIX Security 27 篇。文献属性为 60 项研究系统与反馈流程、21 项边界对照、4 项评测与方法背景。

2027 年仅补入 **AhFuzz（NDSS）** 与 **SelfOp（IEEE S&P）**，录用依据分别来自作者/课题组页面和合作者机构页面；保持“作者或机构确认录用”标记。该快照不表示完整年度覆盖。

## 本次仓库整理

从原附表逐行导入论文标题、会议、年份、全文链接、录用依据，以及“具体瓶颈／技术机制／结果解释与局限”。按原顺序赋予 P001–P085 稳定编号，并检查数量、重复项和字段一致性。

任务分类、关联任务、系统简称和 D1–D5 技术标签为本仓库依据终稿及附表作出的编辑映射。分类理由及容易混淆的边界见[映射说明](mapping.md)。本次迁移使用既有全文分析记录，未重新精读全部 85 篇论文或独立复现实验。

主页只保留短介绍；逐篇分析保留原附表中的证据条件和局限。未填充来源中不存在的作者列表、BibTeX、代码仓库或量化结果。部分全文链接为预印本或调研时取得的公开 PDF，发表年份取会议年份。

SoK 中新增的统计由 `data/papers.json` 直接汇总，分母统一为全部 85 篇。安全任务使用唯一主分类 `category`，五项技术设计使用可多选的 `designs`；同一技术标签下每篇只计一次。相邻主题、评测背景和未标注技术标签的论文保留在分母中，百分比保留一位小数。统计基于当前编辑映射，未修改逐篇分类或技术标签。

## 候选与框架参考

原附表记录了 14 篇已找到会议名单但尚未取得可核查全文的候选，见[原始候选列表](source-corpus.md#全文或录用条件未满足的候选)。这些候选不计入 85 篇。

终稿引用的 *SoK: Automated Vulnerability Repair: Methods, Tools, and Assessments*（USENIX Security 2025）用于说明任务组织方法，原 85 篇附表未单独收录它，因此保留为正文参考。AIxCC SoK 已在原语料中，以 P085 计数一次。更早的 SoK 分析框架参考保留在原始附表末尾，不扩充本次语料数。

## 仓库维护

`data/papers.json` 保存当前文献和分类，`data/taxonomy.json` 定义分类。更新时同步编辑首页、逐篇分析、分类映射和会议索引，保持编号与统计一致。原始材料保持为快照；后续修正以当前数据和提交历史为准。

仓库结构参考 [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) 的目录、分组、简短介绍和贡献指南形式。内容许可采用对话建议的 [CC BY 4.0](../LICENSE)。
