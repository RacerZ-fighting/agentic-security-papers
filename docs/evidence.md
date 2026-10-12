# 逐篇证据与局限

[返回首页](../README.md) · [SoK 映射](mapping.md) · [来源说明](provenance.md)

瓶颈、机制与局限原样保留自文献附表；任务和设计标签是本仓库新增的编辑分类。原始顺序决定稳定编号，后续新增论文继续递增编号。

<a id="p001"></a>

## P001 · CTF challenges

**[Measuring and Augmenting Large Language Models for Solving Capture-the-Flag Challenges](https://daoyuan14.github.io/papers/CCS25_CTFAgent.pdf)**

CCS 2025 · 研究系统与反馈流程 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744855)

- **主分类：** 自动化渗透测试
- **关联任务：** 漏洞复现与利用验证
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 大模型虽掌握CTF知识，却难以将其对应到具体漏洞，并受静态命令环境与工具反馈不足限制。

**技术机制。** 以代码和利用思路分别检索两阶段知识，结合交互式命令会话、工具提示和反编译器，循环执行至获取旗标或达到轮数上限。

**结果解释与局限。** 每题仅运行一次，环境增强同时更换工具，且检索误导、上下文耗尽及缺乏图形界面能力仍限制结果。

<a id="p002"></a>

## P002 · OCR-APT

**[OCR-APT: Reconstructing APT Stories from Audit Logs using Subgraph Anomaly Detection and LLMs](https://arxiv.org/pdf/2510.15188)**

CCS 2025 · 研究系统与反馈流程 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765219)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 海量审计日志与零散异常告警难以直接还原攻击阶段和关键因果关系，而一次性生成报告容易幻觉。

**技术机制。** 将异常子图序列化并检索，逐步抽取和验证IOC、合并攻击阶段报告，再围绕模型选出的关键IOC补充邻接证据。

**结果解释与局限。** 缺少网络流量使横向移动难以重建，共享实体可能混合多次攻击，报告质量及单提示对照主要为定性证据。

<a id="p003"></a>

## P003 · PromeFuzz

**[PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models](https://raw.githubusercontent.com/TCA-ISCAS/PromeFuzz-ccs-2025/master/paper/ccs25-full.pdf)**

CCS 2025 · 研究系统与反馈流程 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765222)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 传统或直接由大模型生成的模糊测试入口难以满足深层API依赖和使用约束，易产生低覆盖与误用崩溃。

**技术机制。** 联合AST依赖图、文档检索、覆盖导向API调度及编译／运行反馈修复，并将成功修复提炼为可复用约束。

**结果解释与局限。** 比较控制了生成模型但包含额外推理模型与不同查询成本，部分基线生成失败也会放大全库覆盖优势。

<a id="p004"></a>

## P004 · AutoSOUP

**[AutoSOUP: Safety-Oriented Unit Proof Generation for Component-level Memory-Safety Verification](https://arxiv.org/pdf/2605.10712)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 安全规约生成与形式化验证
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 组件级BMC需人工决定范围、循环界与外部环境；过紧假设掩盖缺陷，过松模型产生伪反例。

**技术机制。** 资源感知范围扩展、性质引导循环界精化、调用上下文检验环境前提；LLM处理有界语义任务，CBMC与静态分析验证产物。

**结果解释与局限。** 保证只在scope/bounds/assumptions内成立；间接调用图精度及文件粒度限制；非完整程序安全证明。

<a id="p005"></a>

## P005 · Fuzzing with Stitching

**[Automatic, Expressive, and Scalable Fuzzing with Stitching](https://arxiv.org/pdf/2602.18689)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 固定调用序列限制测试覆盖，任意组合 API 又容易引发误用崩溃和大量误报。

**技术机制。** 用类型和动态状态约束定义可组合测试块，让传统覆盖反馈在运行时拼接，并用代理配置环境、分诊和修复规范。

**结果解释与局限。** 对照实验关闭了修复代理且存在一个基线模型不一致，不能把整体提升归因于多代理协作。

<a id="p006"></a>

## P006 · MoCQ

**[Automatically Learning Vulnerability Patterns for Scalable Static Analysis of Web Applications](https://peng-hui.github.io/data/paper/ccs26:mocq.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 手写静态规则成本高，直接让模型生成查询容易出现语义错误、过拟合及误报。

**技术机制。** 以受限查询语言、符号语义反馈、规则泛化和误报消除构成固定生成执行循环。

**结果解释与局限。** 贡献是受约束的规则合成流程，不能将查询有效率等同于漏洞检测效果或自主规划能力。

<a id="p007"></a>

## P007 · BACAgent

**[BACAgent: LLM-Powered Detection of Broken-Access-Control Vulnerabilities in Web Applications](https://lfysec.github.io/paper/bacagent-ccs26.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 访问控制依赖业务角色、数据归属和框架会话语义，通用静态规则难以完整表达。

**技术机制。** 将静态调用和会话证据、框架文档检索与按需代码取证接入分阶段权限推理。

**结果解释与局限。** 缺少同模型通用代理基线，且不同表格召回率分母不同，不能直接混用。

<a id="p008"></a>

## P008 · CVE-Genie

**[CVE-Genie: An LLM-Based Multi-Agent Framework for Reproducing CVEs](https://sites.cs.ucsb.edu/~chris/research/doc/ccs26_cvegenie.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** CVE 描述缺少可执行环境、利用脚本和统一复现判据，人工复现成本高。

**技术机制。** 将环境构建、利用生成和验证拆成有反馈的工具代理，并以隔离环境、统一 flag 与验证器批评约束成功条件。

**结果解释与局限。** 15例消融预先筛选了完整系统能成功的样本，且验证器会误拒有效利用，不能推出通用多代理优势。

<a id="p009"></a>

## P009 · CircumVolve

**[CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models](https://people.cs.umass.edu/~amir/papers/2026-CCS-CircumVolve.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 手工规避策略语法限制了搜索空间，且必须同时满足审查绕过与目标服务正常响应。

**技术机制。** 让模型在进化搜索框架中修改可执行协议策略，并依据抓包、错误及双重成功判据迭代。

**结果解释与局限。** 没有同模型框架消融，仍依赖人工协议模块与种子，真实审查实验也受地点和时间影响。

<a id="p010"></a>

## P010 · PDFuzzer

**[From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://sites.cs.ucsb.edu/~chris/research/doc/ccs26_pdffuzz.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)

**具体瓶颈。** 庞大文档、未公开 API 与跨调用语义约束使 PDF 阅读器模糊测试难以系统生成有效输入。

**技术机制。** 离线提取语义规范与参数级语法，以关系约束和 SMT 求解组装调用序列，再交给传统变异测试。

**结果解释与局限。** 没有在线覆盖反馈驱动的代理规划；验证仅覆盖三个阅读器，跨生态迁移尚未完成端到端测试。

<a id="p011"></a>

## P011 · LinkDiff

**[From Fix to Flaw: Understanding and Revealing Incomplete Patches for Link Following Vulnerabilities](https://crisprss.github.io/paper/linkdiff.pdf)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 自动化漏洞修复
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 闭源补丁的间接调用隐藏文件操作语义，全量二进制差异又会淹没分析上下文。

**技术机制。** 先静态裁剪文件操作相关差异，再让模型按需调用二进制分析工具，并以历史补丁缺陷分类辅助审计。

**结果解释与局限。** 历史示例与评估集有重叠，消融仅证明静态裁剪的重要性，且补丁不完整不等于立即可利用。

<a id="p012"></a>

## P012 · PBFuzz

**[PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/pdf/2512.04611)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** 动态安全测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 已知漏洞的可达条件与触发条件相互耦合，盲目字节变异难以满足。

**技术机制。** 以源码和调试反馈驱动规划、类型化输入生成器、属性测试及反思循环，持续记忆有效约束。

**结果解释与局限。** 依赖已知漏洞判据，部分成功修改了测试桩，且在线预算未计入静态预处理。

<a id="p013"></a>

## P013 · PrivEscalate

**[PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation](https://arxiv.org/pdf/2609.09087)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 自动化渗透测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 通用Agent盲目枚举、缺少领域策略、长链执行和策略切换失败；已有提权评测规模与扰动测试不足。

**技术机制。** 531 Docker场景；确定性枚举、规则/LLM类别匹配、步骤规划、候选策略切换；执行式root成功判据。

**结果解释与局限。** Sudo/SUID场景占比高；多数model-agent-scenario只跑一次；20步限制；kernel/NFS/service-dependent类不覆盖；策略先验来自评测子类需谨慎泛化。

<a id="p014"></a>

## P014 · SynapseFlow

**[Thinking More, Harnessing Better: Automatic Harness Generation with Dataflow Aggregation and Workflow Decomposition](https://arxiv.org/pdf/2607.07007)**

CCS 2026 · 研究系统与反馈流程 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 逐个 API 生成测试桩容易丢失数据流关联，并在初始化、调用顺序和清理上出错。

**技术机制。** 先以语义流图聚合相关函数，再由预设四阶段流程和失败回滚逐步生成测试桩。

**结果解释与局限。** 阶段分解与回滚被联合消融，且每桩24小时并非每项目总预算相同，不能单独归因于规划。

<a id="p015"></a>

## P015 · ForeDroid

**[ForeDroid: Scenario-Aware Analysis for Android Malware Detection and Explanation](https://sen-chen.github.io/pdf/C59-CCS2025-ForeDroid%20Scenario-Aware%20Analysis%20for%20Android%20Malware%20Detection%20and%20Explanation.pdf)**

CCS 2025 · 边界对照 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765207)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 权限或API分类缺少触发场景与完整跨组件调用链，难以准确解释安卓应用的恶意行为。

**技术机制。** 修补静态调用链后用大模型归纳行为，按功能场景对照良性行为分布检测异常，再生成结构化分析报告。

**结果解释与局限。** 属于固定分析流程而非自主行动智能体，静态分析难以覆盖动态载荷与细粒度运行语义，解释忠实性也未独立量化。

<a id="p016"></a>

## P016 · Give LLMs a Security Course

**[Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection](https://arxiv.org/pdf/2504.16429)**

CCS 2025 · 边界对照 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765049)

- **主分类：** 相邻主题
- **关联任务：** 自动化漏洞修复
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 只检索功能性代码的生成系统缺乏漏洞根因和修复知识，也可能受到含漏洞检索样例的影响。

**技术机制。** 从历史漏洞与补丁提炼安全知识，将生成需求拆为子任务后检索、按风险重排过滤，并注入代码生成提示。

**结果解释与局限。** 目标是预防生成不安全代码而非发现或修复现有漏洞，安全率依赖静态检测器，部分对照同时去除了两个相关模块。

<a id="p017"></a>

## P017 · Oedipus

**[Oedipus: LLM-enchanced Reasoning CAPTCHA Solver](https://geleideng.github.io/publication/oedipus/oedipus.pdf)**

CCS 2025 · 边界对照 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744872)

- **主分类：** 相邻主题
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 直接多模态推理难以稳定处理包含空间关系和多重条件的推理型验证码。

**技术机制。** 用专用语言分解任务并在离线阶段通过语法反馈修正计划，再将计划转译成在线多模态求解步骤。

**结果解释与局限。** 计划依赖人工示例，在线子步骤缺乏主动正确性验证，定位误差和延迟仍较明显。

<a id="p018"></a>

## P018 · ContractGuard

**[ContractGuard: Auditing Semantic Contracts of MCP Tools for Security Violations](https://cdn.luneresearch.com/pdfs/eca78c77-9cbc-4d2e-9ee7-683f2c88d7d0/ac0c51e8750910f7ea2133981baa2b1cf327eab6a91c4932788947f4c1394ae0.pdf)**

CCS 2026 · 边界对照 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 相邻主题
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 工具描述可能隐瞒危险副作用或虚构安全保证，直接输入整个服务代码又噪声过大。

**技术机制。** 以静态切片和按需源码检索生成实现摘要，再逐项核对自然语言契约与实际代码行为。

**结果解释与局限。** 被审计对象属于代理生态，消融正样本来自系统已发现问题，且未验证对审计代理自身的提示注入。

<a id="p019"></a>

## P019 · PiMRef

**[PiMRef: Deducing Ever-evolving Spear-phishing Emails with Knowledge Base Invariants](https://arxiv.org/pdf/2507.15393)**

CCS 2026 · 边界对照 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 生成式鱼叉邮件可不断改写文本，而身份与合法域名关系较稳定但知识维护成本高。

**技术机制。** 代理搜索并浏览权威页面建立身份域名知识库，在线阶段以抽取、匹配和规则检查身份矛盾。

**结果解释与局限。** 没有隔离知识库代理贡献的消融，在线低延迟不含建库成本，知识过期或合法账号被盗仍是盲区。

<a id="p020"></a>

## P020 · When Scammers Talk Back

**[When Scammers Talk Back: Understanding Potentially Unwanted Calls via LLM-Based Interaction](https://yancomm.net/papers/2026%20-%20CCS%20-%20When%20Scammers%20Talk%20Back.pdf)**

CCS 2026 · 边界对照 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 相邻主题
- **关联任务：** 安全事件调查与运维处置
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 被动电话测量难以观察持续互动后才出现的诱导、升级索取与诈骗链条。

**技术机制。** 用低延迟语音对话代理和虚构身份维持蜜罐通话，采集后再进行人工分层抽样与主题编码。

**结果解释与局限。** 收益是获取更丰富的测量材料，并未证明自动识别或阻断能力，合作型人设与号码样本也带来偏差。

<a id="p021"></a>

## P021 · JsDeObsBench

**[JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/pdf/2506.20170)**

CCS 2025 · 评测与方法背景 · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744871)

- **主分类：** 评测与方法背景
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** JavaScript反混淆缺少覆盖多类混淆且可验证执行语义的基准，现有指标也不足以衡量可读性。

**技术机制。** 构造可执行混淆样本，以单示例提示调用模型，并用语法、执行、复杂度与代码相似度四类评估器验证输出。

**结果解释与局限。** 这是基准与固定变换流程，执行检查未反馈到修复循环，且恶意代码上的语义保持率偏低。

<a id="p022"></a>

## P022 · Hieronym

**[Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/pdf/2609.12457)**

CCS 2026 · 评测与方法背景 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 评测与方法背景
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 去符号二进制缺少函数语义名称，仅看局部反编译代码难以恢复上下文。

**技术机制。** 通过分层摘要训练结合全局字符串与局部调用信息预测函数名。

**结果解释与局限。** 属于模型与表示改进，未建立工具反馈闭环，也未验证端到端漏洞发现收益。

<a id="p023"></a>

## P023 · The Deception Delta

**[The Deception Delta: Adversarial Evaluation of LLM-Based Smart Contract Bytecode Forensics](https://arxiv.org/pdf/2609.14098)**

CCS 2026 · 评测与方法背景 · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)

- **主分类：** 评测与方法背景
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 模型可能正确描述资金流却仍把恶意合约判为良性，解释能力不等于安全判断能力。

**技术机制。** 以具备执行真值的欺骗性字节码对多模型和提示策略进行单轮对抗评估。

**结果解释与局限。** 实验没有工具、反编译器或交互，不能据此判断代理式审计系统的失败率。

<a id="p024"></a>

## P024 · EAGLEYE

**[EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](https://www.ndss-symposium.org/wp-content/uploads/2025-399-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis/)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** IoT 隐藏接口的路由名称与层级关系难以靠 URL 枚举发现。

**技术机制。** 从公开请求和固件上下文推断路由模式，用验证反馈修正 LLM 输出，再以路由字典引导黑盒模糊测试。

**结果解释与局限。** 仍需要固件上下文，动态生成的路由和复杂嵌套层级可能遗漏。

<a id="p025"></a>

## P025 · GPTAid

**[Generating API Parameter Security Rules with LLM for API Misuse Detection](https://www.ndss-symposium.org/wp-content/uploads/2025-465-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection/)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** 安全规约生成与形式化验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 直接生成的 API 参数规则常错误或过于笼统，无法可靠转为检测器。

**技术机制。** 生成正确与违反规则的调用程序，以运行错误验证候选规则，差分细化后交给 CodeQL 检测。

**结果解释与局限。** 内存错误导向的动态判据会遗漏不崩溃的逻辑错误，过程内分析也限制覆盖。

<a id="p026"></a>

## P026 · Matter controller security

**[Hidden and Lost Control: on Security Design Risks in IoT User-Facing Matter Controller](https://www.ndss-symposium.org/wp-content/uploads/2025-266-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/hidden-and-lost-control-on-security-design-risks-in-iot-user-facing-matter-controller/)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** Matter 控制器信息和权限可能在应用界面中缺失或失真，跨厂商测试依赖人工和实物。

**技术机制。** 虚拟 Matter 设备提供可控环境，LLM 指导配对与界面搜索，再改变控制器身份和 ACL 检查显示是否正确。

**结果解释与局限。** 自动覆盖六类问题中的四类，凭据限制、有限搜索时间和 UI 判断误差限制完整性。

<a id="p027"></a>

## P027 · LLMPirate

**[LLMPirate: LLMs for Black-box Hardware IP Piracy](https://www.ndss-symposium.org/wp-content/uploads/2025-2059-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/llmpirate-llms-for-black-box-hardware-ip-piracy/)

- **主分类：** 相邻主题
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 硬件电路改写既要保持功能等价，又要突破结构相似性检测，直接生成常失败。

**技术机制。** 按门类型生成可复用改写，将语法、允许操作符和等价性检查结果反馈给 LLM 迭代修正。

**结果解释与局限。** 属于受控的盗版检测器压力测试，结论仅覆盖指定威胁模型、改写空间与检测器。

<a id="p028"></a>

## P028 · PropertyGPT

**[PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](https://www.ndss-symposium.org/wp-content/uploads/2025-1357-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/)

- **主分类：** 安全规约生成与形式化验证
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 形式化验证器依赖昂贵的人工性质规格，缺少可规模化的性质生成。

**技术机制。** 检索人工性质作为参考，生成并按编译反馈修正规格，排序后交给专用证明器验证。

**结果解释与局限。** 可编译不等于性质正确或完备，跨合约建模和有界验证进一步限制保证范围。

<a id="p029"></a>

## P029 · YuraScanner

**[YuraScanner: Leveraging LLMs for Task-driven Web App Scanning](https://www.ndss-symposium.org/wp-content/uploads/2025-388-paper.pdf)**

NDSS 2025 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 传统爬虫不理解多步业务流程，难以到达深层状态。

**技术机制。** 自动生成任务，以页面语义和历史驱动浏览器交互，再用传统 XSS 引擎验证输入点。

**结果解释与局限。** 任务生成、执行和依赖关系都会出错，61.3% 包含部分完成，不能当作漏洞发现成功率。

<a id="p030"></a>

## P030 · PLC logic instruction fuzzing

**[An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs](https://www.ndss-symposium.org/wp-content/uploads/2026-f1081-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/an-llm-driven-fuzzing-framework-for-detecting-logic-instruction-bugs-in-plcs/)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** PLC 指令依赖、跨周期状态和厂商工具使可重置、语义有效的测试程序难以生成。

**技术机制。** 构建语义依赖图，生成并验证修正种子程序，再结合覆盖反馈变异参数，用日志、灯态和通信状态判错。

**结果解释与局限。** 真实硬件与厂商环境仍需搭建和人工复核，514 条告警不能等同于 19 个去重确认漏洞。

<a id="p031"></a>

## P031 · Function-Level TARA

**[Automating Function-Level TARA for Automotive Full-Lifecycle Security](https://www.ndss-symposium.org/wp-content/uploads/2026-s1408-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/automating-function-level-tara-for-automotive-full-lifecycle-security/)

- **主分类：** 相邻主题
- **关联任务：** 自动化渗透测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 静态威胁库难以适应汽车部件细节、系统配置和不断变化的攻击路径。

**技术机制。** 构造子树、组装攻击树和风险评估的专职代理互相检查，以结构化配置、RAG 和微调支持功能级 TARA。

**结果解释与局限。** 仍依赖用户给定威胁场景，渗透测试验证的是选定路径，攻击树整体没有形式化正确性保证。

<a id="p032"></a>

## P032 · BSFuzzer

**[BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection](https://www.ndss-symposium.org/wp-content/uploads/2026-f94-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** BLE 的字段解释和状态转换错误经常绕过传统崩溃判据。

**技术机制。** LLM 从规格中提取状态机与处理规则，构造语义变异并依据设备实际响应检查逻辑偏差。

**结果解释与局限。** 规格提取主要是缓存复用的预处理，复杂状态仍需人工判断，实验仅覆盖 Just Works 配对。

<a id="p033"></a>

## P033 · CHAMELEOSCAN

**[CHAMELEOSCAN: Demystifying and Detecting iOS Chameleon Apps via LLM-Powered UI Exploration](https://www.ndss-symposium.org/wp-content/uploads/2026-f1906-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/chameleoscan-demystifying-and-detecting-ios-chameleon-apps-via-llm-powered-ui-exploration/)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 静态代码与评论分类难以发现运行时伪装转换、混合界面和元数据稀缺的恶意应用。

**技术机制。** 从元数据提出转换假设，结合截图和 UI 树反复决策、执行及验证实际功能变化。

**结果解释与局限。** 总体与 UNKNOWN 子集的精确率分母不同，有限探索可能遗漏延迟、地域或服务器控制的转换。

<a id="p034"></a>

## P034 · Chimera

**[Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation](https://www.ndss-symposium.org/wp-content/uploads/2026-f375-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/chimera-harnessing-multi-agent-llms-for-automatic-insider-threat-simulation/)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** 自动化渗透测试
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 真实内部威胁日志难以获取，脚本合成又缺少组织行为和语义真实性。

**技术机制。** 有角色、记忆、计划和交流能力的多代理在隔离企业环境执行活动，生成用于检测评估的多模态日志。

**结果解释与局限。** 合成日志的逼真度不等于真实攻击者行为，模型选择和分布变化会显著改变结果。

<a id="p035"></a>

## P035 · FirmAgent

**[FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://www.ndss-symposium.org/wp-content/uploads/2026-s1943-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测、漏洞复现与利用验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 固件静态分析误报多且缺少 PoC，动态模糊测试又难通过复杂约束到达危险点。

**技术机制。** 先以模糊测试确定真实输入源与调用关系，再由污点分析代理和 PoC 代理结合反编译语义与种子验证漏洞。

**结果解释与局限。** 依赖成功重托管和反编译，LLM 告警不是证明，主要验证对象仍是命令注入与缓冲区溢出。

<a id="p036"></a>

## P036 · ProtocolGuard

**[ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification](https://www.ndss-symposium.org/wp-content/uploads/2026-f521-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/protocolguard-detecting-protocol-non-compliance-bugs-via-llm-guided-static-analysis-and-dynamic-verification/)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测、安全规约生成与形式化验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 协议语义不合规通常不会崩溃，人工切片和 PoC 编写限制检测规模。

**技术机制。** LLM 连接 RFC 规则与代码切片，合成断言和测试脚本，以执行及报文轨迹反馈修正，再用定向模糊测试验证。

**结果解释与局限。** C 语言和处理器中心切片限制覆盖，回调逻辑可能遗漏，158 个检测结果不等于全部已确认。

<a id="p037"></a>

## P037 · SACK

**[SACK: Systematic Generation of Function Substitution Attacks Against Control-Flow Integrity](https://www.ndss-symposium.org/wp-content/uploads/2026-f2317-paper.pdf)**

NDSS 2026 · 研究系统与反馈流程 · [录用依据](https://www.ndss-symposium.org/ndss-paper/sack-systematic-generation-of-function-substitution-attacks-against-control-flow-integrity/)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** 动态安全测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 验证控制流完整性下的函数替换攻击，需要程序特定的安全语义和手工判据。

**技术机制。** LLM 生成安全判据，执行后反馈修正，再由确定性引擎枚举合法调用目标替换并验证安全破坏。

**结果解释与局限。** 假定已有内存读写能力与源码，历史漏洞上的 419 个攻击不能称为 419 个新漏洞。

<a id="p038"></a>

## P038 · AhFuzz

**[Agentic Orchestration for Hybrid Fuzzing](https://abhikrc.com/pdf/NDSS27.pdf)**

NDSS 2027 · 作者/机构确认录用 · 研究系统与反馈流程 · [录用依据](https://fouzhe.github.io/)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 传统混合模糊测试以模糊器为中心，只在停滞后被动调用符号执行。

**技术机制。** 代理维护覆盖、种子和目标—结果轨迹，主动选择并配置 AFL++ 与 ConcoLLMic，让两类测试器协作探索。

**结果解释与局限。** LLM 调度可能出错且有成本与上下文限制，2027 录用依据为作者和机构公告，尚未找到官方论文列表。

<a id="p039"></a>

## P039 · The Midas Touch

**[The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](https://www.ndss-symposium.org/wp-content/uploads/2025-816-paper.pdf)**

NDSS 2025 · 边界对照 · [录用依据](https://www.ndss-symposium.org/ndss-paper/the-midas-touch-triggering-the-capability-of-llms-for-rm-api-misuse-detection/)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 文档模板匹配遗漏资源分配与释放约束，直接询问 LLM 又容易幻觉。

**技术机制。** 将分配识别、资源对象提取和释放配对拆开，以多种提示与一致性检查交叉验证，再生成 CodeQL 约束。

**结果解释与局限。** 这是结构化推理工作流，不能仅因借鉴 ReAct 就称为自主规划代理。

<a id="p040"></a>

## P040 · Incident Response Planning

**[Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination](https://www.ndss-symposium.org/wp-content/uploads/2026-f358-paper.pdf)**

NDSS 2026 · 边界对照 · [录用依据](https://www.ndss-symposium.org/ndss-paper/incident-response-planning-using-a-lightweight-large-language-model-with-reduced-hallucination/)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 静态响应手册难随环境更新，直接使用大模型生成恢复动作又贵且容易幻觉。

**技术机制。** 微调轻量模型并检索威胁情报，通过候选动作的未来恢复状态模拟进行前瞻规划。

**结果解释与局限。** 22% 改善基于离散动作成本而非实测生产恢复时间，实际 SOC 自主处置尚未验证。

<a id="p041"></a>

## P041 · IoTBec

**[IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework for Black Box IoT devices](https://www.ndss-symposium.org/wp-content/uploads/2026-f634-paper.pdf)**

NDSS 2026 · 边界对照 · [录用依据](https://www.ndss-symposium.org/ndss-paper/iotbec-an-accurate-and-efficient-recurring-vulnerability-detection-framework-for-black-box-iot-devices/)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** 动态安全测试
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 无固件和源码时，传统克隆分析无法寻找复现性漏洞，盲目模糊测试效率低。

**技术机制。** 匹配漏洞与设备接口签名，以 LLM 生成针对性载荷和相关参数变异，再执行并监控真实设备。

**结果解释与局限。** 是工具连接的生成工作流，未展示 LLM 持续重规划；正文的 25 个基准外发现不能全部算首次发现。

<a id="p042"></a>

## P042 · LLMBisect

**[LLMBisect: Breaking Barriers in Bug Bisection with A Comparative Analysis Pipeline](https://www.ndss-symposium.org/wp-content/uploads/2026-s990-paper.pdf)**

NDSS 2026 · 边界对照 · [录用依据](https://www.ndss-symposium.org/ndss-paper/llmbisect-breaking-barriers-in-bug-bisection-with-a-comparative-analysis-pipeline/)

- **主分类：** 自动化漏洞修复
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 基于文本修改位置的提交溯源启发式无法充分理解跨函数漏洞成因。

**技术机制。** 联合补丁、提交说明和代码语义生成候选，经多轮比较、筛选与投票定位引入漏洞的提交。

**结果解释与局限。** 缺少运行验证闭环，候选遗漏和提交说明质量会决定失败，带 Fixes 标签的样本选择也可能偏置结果。

<a id="p043"></a>

## P043 · Agentic Concolic Execution

**[Agentic Concolic Execution](https://dylanjwolff.com/assets/agentic.pdf)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 符号执行依赖精细语义模型，复杂环境与约束难以建模，普通模糊测试又难触达深层路径。

**技术机制。** 用执行轨迹构造可灵活表达的路径约束，由总结与求解代理结合源码、执行和 SMT 工具生成输入。

**结果解释与局限。** 路径约束可能不精确且单次生成成本较高，覆盖率提升不能解释为分析完备或可靠证明。

<a id="p044"></a>

## P044 · GONDAR

**[Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/pdf/2604.01645)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** 漏洞复现与利用验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 覆盖到危险函数并不等于触发漏洞，传统模糊测试难以补齐利用所需的语义条件。

**技术机制。** 探索代理负责抵达目标，模糊测试提供带状态的候选种子，利用代理再根据 sink 语义补齐触发条件。

**结果解释与局限。** 依赖可运行的 harness 和可达入口，难处理复杂反序列化等条件，且基线计算预算并不相同。

<a id="p045"></a>

## P045 · Cottontail

**[Cottontail: Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://arxiv.org/pdf/2504.17542)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 满足路径约束的输入仍可能破坏复杂格式，在解析阶段就被拒绝。

**技术机制。** 把覆盖树筛出的约束交给模型求解并补全结构，再以实际执行反馈修正输入和更新种子。

**结果解释与局限。** 依赖源码与测试入口，复杂大型程序和非结构化输入上的泛化尚未充分验证。

<a id="p046"></a>

## P046 · NEO

**[Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://arxiv.org/pdf/2605.15569)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 跨语言、跨服务的权限语义与调用链超出传统污点分析和一次性代码阅读的能力。

**技术机制。** 以 CodeQL 查询工具按需取上下文，分阶段识别特权操作、跨服务路径和鉴权条件，并用 SMT 与模型判断筛除误报。

**结果解释与局限。** 动态语义与配置覆盖有限，PoV 仍由作者人工验证，不能视为完整的自动利用或形式化证明。

<a id="p047"></a>

## P047 · Incalmo

**[Incalmo: an Autonomous Llm-Assisted System for Red Teaming Multi-Host Networks](https://arxiv.org/pdf/2501.16466)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 自动化渗透测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 单一代理同时处理命令细节、跨主机状态和攻击规划时，长任务容易失去上下文与方向。

**技术机制。** 将高层规划与五类任务执行分离，用任务代理和持久化环境状态服务协同推进。

**结果解释与局限。** 实验网络使用已知漏洞且没有主动防御者，成功标准只是触达至少一个关键资产。

<a id="p048"></a>

## P048 · PILOT

**[PILOT: Command-Line Interface Fuzzing Via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/pdf/2511.20555)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 复杂命令行选项及配套文件让大量功能在有效测试开始前就不可达。

**技术机制。** 以调用路径指导模型使用工具构造执行环境和输入，再用覆盖反馈迭代生成可用种子。

**结果解释与局限。** 主要模型和迭代预算较固定，不同基线使用不同程序子集，不能直接合并成统一胜率。

<a id="p049"></a>

## P049 · PortGPT

**[PortGPT: Towards Automated Backporting Using Large Language Models](https://arxiv.org/pdf/2510.22396)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 自动化漏洞修复
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 旧版本的接口、符号位置和代码结构变化使安全补丁难以直接回移。

**技术机制。** 按补丁块定位相关代码并生成回移方案，再通过应用、自动修复和编译测试反馈逐步校正。

**结果解释与局限。** 编译通过不保证语义正确，跨块依赖与大型结构变化仍需要人工检查。

<a id="p050"></a>

## P050 · SpecAuditor

**[SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](https://yuuoniy.github.io/files/SpecAuditor.pdf)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 通用漏洞模板难以表达项目特有的资源、状态和调用约束，模型直接审计又缺少明确规范。

**技术机制。** 从补丁和文档归纳审计规范，生成静态查询，再由模型按需请求上下文检查和筛选违规报告。

**结果解释与局限。** 严格口径下仅 71/297 条报告属于缺陷，且缺少运行验证，不能把作者筛选后的比较集当成全局召回率。

<a id="p051"></a>

## P051 · R1-Fuzz

**[Specializing Language Models for Textual Fuzzing via Reinforcement Learning](https://arxiv.org/pdf/2509.20384)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)

**具体瓶颈。** 通用模型生成种子的成本较高，传统语法模糊测试又缺少针对未覆盖路径的语义能力。

**技术机制。** 利用路径问题和距离奖励训练专用模型，再以覆盖反馈选择目标并生成供 AFL++ 使用的种子。

**结果解释与局限。** 提升包含模型训练本身的贡献；已读预印本与最终摘要的漏洞数量不一致，需明确版本。

<a id="p052"></a>

## P052 · StepStone

**[StepStone: LLM-Based GPU Kernel Driver Fuzzing via User-Space Libraries](https://www.cs.ucr.edu/~zhiyunq/pub/oakland26_gpu_fuzzing.pdf)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** GPU 驱动接口缺少易用规范，底层参数及依赖关系难以手写建模。

**技术机制。** 从用户态库的公开 API 提取类型和语义，用模型补全依赖与取值约束并修复描述，再驱动内核模糊测试。

**结果解释与局限。** 模型主要参与测试描述生成，库层检查会屏蔽部分底层缺陷，不能替代直接系统调用测试。

<a id="p053"></a>

## P053 · TRIGFUZZ

**[TRIGFUZZ: Triggering Conditions Guided Directed Fuzzing](https://vul337.github.io/TrigFuzz/trigfuzz.pdf)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** 动态安全测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 定向模糊测试即使抵达目标位置，也经常无法满足真正触发漏洞的复杂条件。

**技术机制。** 让模型交互读取源码并抽取触发条件，经动态检查后把条件距离用于种子调度和字节变异。

**结果解释与局限。** 生成条件与动态检查都不完备，依赖已有漏洞线索，公开基准也可能受到训练数据影响。

<a id="p054"></a>

## P054 · SlicePatch

**[Web Application Vulnerability Repair Via Context-Aware Fault Localization and Directed Differential Fuzzing](https://seclab.cse.cuhk.edu.hk/papers/sp26-SlicePatch.pdf)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 自动化漏洞修复
- **关联任务：** 动态安全测试
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 补丁挡住单个 PoC 仍可能被变体绕过，或破坏正常功能，而动态 PHP 又难提供合适修复上下文。

**技术机制。** 通过执行剖析和切片定位缺陷，生成补丁后用 PoC 与定向差分模糊测试检查绕过及回归，再反馈重试。

**结果解释与局限。** 依赖可执行 PoC 与特定漏洞类型的判定器，差分测试仍不能证明补丁完全正确。

<a id="p055"></a>

## P055 · deepSURF

**[deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://arxiv.org/pdf/2506.15648)**

IEEE S&P 2026 · 研究系统与反馈流程 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** Rust 的类型、trait 与调用序列约束使有效的安全 API 测试入口难以自动构造。

**技术机制。** 静态分析先定位可达 unsafe 代码的 API，再用模型扩展 harness，并根据编译错误反复修复后交给模糊测试。

**结果解释与局限。** 反馈主要来自编译阶段，异步、多线程和非内存错误覆盖不足。

<a id="p056"></a>

## P056 · SelfOp

**[SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/pdf/2609.22792)**

IEEE S&P 2027 · 作者/机构确认录用 · 研究系统与反馈流程 · [录用依据](https://seclab.bu.edu/people/gianluca/)

- **主分类：** 漏洞复现与利用验证
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 安全代理缺少密集奖励和专家轨迹，人工调试技能与上下文难以扩展到大量失败任务。

**技术机制。** 把失败结果沿执行轨迹归因到技能文档，汇总跨任务一致的修改意见，在冻结模型和执行框架的情况下优化上下文。

**结果解释与局限。** 目前主要验证小规模 CyberGym 复现任务；录用依据来自作者确认，官方 2027 名单尚未公开。

<a id="p057"></a>

## P057 · TypeForge

**[TypeForge: Synthesizing and Selecting Best-Fit Composite Data Types for Stripped Binaries](https://cdn.luneresearch.com/pdfs/s&p/2025/2019a76d-f2bc-4c6d-8e4b-2c0656ee8d68.pdf)**

IEEE S&P 2025 · 边界对照 · [录用依据](https://sp2025.ieee-security.org/accepted-papers.html)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 剥离符号的二进制缺少复合类型信息，静态约束常产生多个冲突候选。

**技术机制。** 先以类型流图生成候选，再用模型比较反编译代码可读性并筛选最合适的类型。

**结果解释与局限。** 模型只是固定流程中的排序器，没有驱动生成器的动作反馈闭环，因此列为相邻基线。

<a id="p058"></a>

## P058 · GDPR consent violations

**[Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://arxiv.org/pdf/2512.22789)**

IEEE S&P 2026 · 边界对照 · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html)

- **主分类：** 相邻主题
- **关联任务：** 动态安全测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 隐私政策中的同意要求与真实交互页面分离，传统静态扫描难以定位并判断同意表单。

**技术机制。** 浏览器代理按目标寻找表单，再把页面语义转成结构化事实，交给 Datalog 规则判定界面层违规。

**结果解释与局限。** 只覆盖界面同意机制，无法证明后端数据处理是否合规，且缺少强同模型代理消融。

<a id="p059"></a>

## P059 · APPATCH

**[APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching](https://www.usenix.org/system/files/usenixsecurity25-nong.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/nong)

- **主分类：** 自动化漏洞修复
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 固定提示难以获得跨函数上下文并解释漏洞根因。

**技术机制。** APPATCH按程序依赖切片，让模型按需索取函数和示例，再由多个LLM判断补丁有效性。

**结果解释与局限。** 预先给定漏洞位置；任一验证模型认可即可保留补丁，不能视为执行性或形式化证明。

<a id="p060"></a>

## P060 · ELFuzz

**[ELFuzz: Efficient Input Generation via LLM-driven Synthesis Over Fuzzer Space](https://www.usenix.org/system/files/usenixsecurity25-chen-chuyang.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-chuyang)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 生成式模糊测试依赖人工编写语法和语义约束。

**技术机制。** LLM按覆盖集合演化、组合并筛选可执行输入生成器，再为传统模糊测试提供种子。

**结果解释与局限。** 当前主要优化初始种子，依赖模型已有格式知识，不能据覆盖增益直接推断漏洞收益。

<a id="p061"></a>

## P061 · HLPFuzz

**[Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving](https://www.usenix.org/system/files/usenixsecurity25-yang-yupeng.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yupeng)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 语言处理器的深层语义约束使随机变异和专用启发式难以推进。

**技术机制。** HLPFuzz选择关键分支、执行候选输入，并借助调试器分歧分析与LSP查询补充求解上下文。

**结果解释与局限。** 依赖源码、调试和覆盖工具；沿已有示例路径补上下文可能遗漏其他可达路径。

<a id="p062"></a>

## P062 · SAN2PATCH

**[Logs In, Patches Out: Automated Vulnerability Repair via Tree-of-Thought LLM Analysis](https://www.usenix.org/system/files/usenixsecurity25-kim-youngjoon.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/kim-youngjoon)

- **主分类：** 自动化漏洞修复
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 漏洞修复通常需要昂贵的分析、人工定位和修复策略设计。

**技术机制。** SAN2PATCH以理解、定位、策略、生成四阶段思维树搜索候选，再进行构建、PoC和功能验证。

**结果解释与局限。** 仅生成阶段只需日志与源码；完整流程仍需PoC、构建脚本和测试，多位置根因修复仍困难。

<a id="p063"></a>

## P063 · G²Fuzz

**[Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators](https://www.usenix.org/system/files/usenixsecurity25-zhang-kunpeng.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-kunpeng)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** LLM直接生成复杂二进制格式既不可靠又昂贵。

**技术机制。** G²Fuzz生成和变异Python输入生成器，用库构造复杂文件，并在AFL++停滞时引入新特征组合。

**结果解释与局限。** 依赖已有格式生成库或人工规范，目前不能自动处理任意自定义格式。

<a id="p064"></a>

## P064 · PatchAgent

**[PATCHAGENT: A Practical Program Repair Agent Mimicking Human Expertise](https://www.usenix.org/system/files/usenixsecurity25-yu-zheng.pdf)**

USENIX Security 2025 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zheng)

- **主分类：** 自动化漏洞修复
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 已有补丁生成器缺少端到端定位与验证，修复过程无法充分利用失败反馈。

**技术机制。** 以语言服务器检索和补丁验证器形成定位—修改—验证循环，并用反例反馈改进下一轮补丁。

**结果解释与局限。** 92.13%是五种模型配置的并集；依赖PoC与功能测试，通过测试不等于语义正确。

<a id="p065"></a>

## P065 · BugAuditor

**[BugAuditor: Detecting Bugs via Inconsistent Defensive Code Auditing](https://www.usenix.org/system/files/usenixsecurity26-lin-miaoqian.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/lin-miaoqian)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)

**具体瓶颈。** 项目特有的防御约定缺少显式漏洞判据，低频规则容易被忽视。

**技术机制。** BugAuditor从防御代码反推安全意图，用静态筛选、按需上下文和LLM比较定位处理不一致之处。

**结果解释与局限。** 局部分析与AST匹配有覆盖盲区；不一致只是候选信号，最终结果仍需人工核验。

<a id="p066"></a>

## P066 · Bulbasaur

**[Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](https://www.usenix.org/system/files/usenixsecurity26-wang-yiyi.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yiyi)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 通用变异器难以精确协调输入字节以通过困难分支。

**技术机制。** Bulbasaur按长期未覆盖分支触发查询智能体，结合静态上下文和运行时操作数合成可复用变异器。

**结果解释与局限。** 复杂状态约束仍难求解；依赖源码和插桩，覆盖率提升不代表已验证可利用性。

<a id="p067"></a>

## P067 · Firmenstein

**[Firmenstein: Scaling Dynamic Analysis for Linux-Based Firmware Services via API-Centric Intervention Code Synthesis](https://www.usenix.org/system/files/usenixsecurity26-wang-yanzhong.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yanzhong)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 固件重宿主的环境依赖跨越多个二进制，通用替代逻辑难保真。

**技术机制。** Firmenstein以API依赖图支持切片和诊断智能体，再生成环境或执行干预代码以恢复运行。

**结果解释与局限。** 运行失败后的迭代仍有人在环；反编译误差与干预失真限制了端到端自主性。

<a id="p068"></a>

## P068 · SIGMERGE

**[From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports](https://www.usenix.org/system/files/usenixsecurity26-cai.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/cai)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 威胁报告的高层描述难直接转为可执行检测规则。

**技术机制。** SIGMERGE提取命令与TTP，调用专用验证工具迭代纠正结构化攻击描述，再检索知识生成Sigma规则。

**结果解释与局限。** 是预设字段上的有界工具纠错；命令级样例和十个案例不足以证明部署中的总体误报率。

<a id="p069"></a>

## P069 · SPAR

**[Generating Precise Format Specification for Network Protocols Through Adversarial LLM Interactions](https://www.usenix.org/system/files/usenixsecurity26-ye.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/ye)

- **主分类：** 安全规约生成与形式化验证
- **关联任务：** 动态安全测试
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 从RFC提取格式时，语法易得而字段间语义约束容易遗漏。

**技术机制。** SPAR分别生成格式规范和参考解析器，以SMT构造正反例并让二者交叉反馈、迭代修正。

**结果解释与局限。** 相互一致不保证符合标准；树状非递归格式、单RFC和局部约束限定了验证范围。

<a id="p070"></a>

## P070 · H3Act

**[H3Act: Automated Measuring Semantic Conversion Anomalies of HTTP/3-to-HTTP/1.1 Translation in CDNs](https://www.usenix.org/system/files/usenixsecurity26-peng-qihang.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-qihang)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** CDN协议转换不可见，传统测试缺少HTTP/3语义及历史攻击知识。

**技术机制。** H3Act由生成与分析智能体对照客户端和源站日志，经RAG及记忆压缩指导下一批测试。

**结果解释与局限。** 黑盒日志和模型幻觉限制判据可靠性；高延迟、低吞吐及人工确认限制实际规模。

<a id="p071"></a>

## P071 · JScamd

**[JScamd: An Automated Static Taint Analysis Framework for Detecting Cryptographic API Misuses in JavaScript](https://www.usenix.org/system/files/usenixsecurity26-jia-shijie.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-shijie)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** JavaScript动态语义和分散的加密库导致既有污点规则覆盖不足。

**技术机制。** JScamd从安全约束生成API映射和规则，以分析器一致性反馈驱动LLM自纠，再执行专门污点分析。

**结果解释与局限。** 97.78%为人工判定的误用精度，不等于可利用率；仍有较低基准召回及维护者争议。

<a id="p072"></a>

## P072 · PANGOLIN

**[PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/system/files/usenixsecurity26-jia-zhipeng.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-zhipeng)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 物联网隐藏接口及嵌套参数跨越脚本与二进制，单语言分析难以恢复。

**技术机制。** PANGOLIN恢复分派入口和裁剪的多语言调用图，由智能体生成参数规格，再以设备响应纠错。

**结果解释与局限。** 物理设备观测不等于代码覆盖；子模块溢出和重启失联可能漏检或要求人工复位。

<a id="p073"></a>

## P073 · PatchWeaver

**[PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies](https://www.usenix.org/system/files/usenixsecurity26-li-rui.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** 自动化漏洞修复
- **技术设计：** [D2 · 执行环境与前置状态的自动准备](mapping.md#d2)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 修复动作即使当前合规，也可能在后续维护窗口、审批或副本约束下陷入死局。

**技术机制。** PatchWeaver让LLM提议计划，由状态图、类型化策略和短程模拟筛选动作并在漂移后重新规划。

**结果解释与局限。** 模板加模拟的违规率已接近LLM方案；收益主要来自控制与验证，且仍有残余违规。

<a id="p074"></a>

## P074 · BINREX

**[Towards Generality: Task-Adaptive Binary Analysis via Semantic Retrieval and Verifiable Reasoning](https://www.usenix.org/system/files/usenixsecurity26-liu-yuzhe.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yuzhe)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 去符号二进制缺少语义线索，专用分析器难以响应开放式安全查询。

**技术机制。** BINREX分解目标，检索函数语义，合成IDAPython脚本并按局部验证条件执行、修正和汇总证据。

**结果解释与局限。** 依赖反编译质量和验证条件；加壳、虚拟机混淆及动态执行任务不在已证明范围内。

<a id="p075"></a>

## P075 · iFinder

**[Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis](https://www.usenix.org/system/files/usenixsecurity26-lin-ziyu.pdf)**

USENIX Security 2026 · 研究系统与反馈流程 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/lin-ziyu)

- **主分类：** 动态安全测试
- **关联任务：** 程序安全分析与漏洞检测、漏洞复现与利用验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D4 · 基于执行反馈的任务规划与调整](mapping.md#d4)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 核心网隐式信任与分散的协议检查使漏洞定位和可触发性验证困难。

**技术机制。** iFinder以发现、规范核查和PoC执行三类智能体，在容器中根据运行日志反复修正测试。

**结果解释与局限。** PoC可能先触发其他缺陷；仍有12个此类误报，作者需人工匹配预期与实际崩溃位置。

<a id="p076"></a>

## P076 · LLMxCPG

**[LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models](https://www.usenix.org/system/files/usenixsecurity25-lekssays.pdf)**

USENIX Security 2025 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 原始代码分类噪声大，难保留跨函数漏洞上下文。

**技术机制。** LLMxCPG用专门模型生成图查询和切片，再由另一模型判断漏洞；Joern反馈用于训练查询数据。

**结果解释与局限。** 主要是结构化分类流水线，不能将离线训练反馈当作部署时的自主工具闭环。

<a id="p077"></a>

## P077 · MBFuzzer

**[MBFuzzer: A Multi-Party Protocol Fuzzer for MQTT Brokers](https://www.usenix.org/system/files/usenixsecurity25-song-xiangpu.pdf)**

USENIX Security 2025 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/song-xiangpu)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 双端测试遗漏MQTT多方交互，而差异响应需耗费人工解释。

**技术机制。** MBFuzzer以Petri网协调消息，LLM分两步总结重放记录并核对规范中的强制约束。

**结果解释与局限。** 多方指协议参与者而非多个LLM；依赖人工规则和确认，模型过滤可能漏掉真实异常。

<a id="p078"></a>

## P078 · TORCHLIGHT

**[TORCHLIGHT: Shedding LIGHT on Real-World Attacks on Cloudless IoT Devices Concealed within the Tor Network](https://www.usenix.org/system/files/usenixsecurity25-pan-yumingzhi.pdf)**

USENIX Security 2025 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/pan-yumingzhi)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** —
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 经Tor访问的无云物联网攻击难以观察和识别。

**技术机制。** TORCHLIGHT结合出口流量采集与五阶段LLM实体核验、检索和攻击分析，由人工确认漏洞。

**结果解释与局限。** 漏洞总数是整套研究流程的成果，不是自主LLM发现量；加密流量与人工确认限制范围。

<a id="p079"></a>

## P079 · PyGuard

**[Cutting the Gordian Knot: Detecting Malicious PyPI Packages via a Knowledge-Mining Framework](https://www.usenix.org/system/files/usenixsecurity26-guo-wenbo.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/guo-wenbo)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** 相同API序列可能用于正常或恶意行为，单纯语法规则误报严重。

**技术机制。** PyGuard从既有工具错误中挖掘行为模式，结合精确匹配、语义摘要及RAG进行上下文判断。

**结果解释与局限。** 是含专家知识整理的分类流水线；依赖混淆、远程载荷与非Python代码仍有盲区。

<a id="p080"></a>

## P080 · REDOSPECTOR

**[Death by a Thousand Drips: Uncovering Critical Resource Leaks in the Windows Ecosystem](https://www.usenix.org/system/files/usenixsecurity26-dong-feng.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/dong-feng)

- **主分类：** 动态安全测试
- **关联任务：** —
- **技术设计：** [D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 仅看崩溃会漏掉Windows服务中缓慢累积的资源耗尽问题。

**技术机制。** REDOSPECTOR离线使用逆向信息和LLM生成协议种子，再用原生钩子、重复放大和增长趋势判定泄漏。

**结果解释与局限。** 论文明确LLM不与运行服务交互；MCP或外层模糊测试反馈不能自动等同于智能体闭环。

<a id="p081"></a>

## P081 · LeakHunter

**[Exposing Resource-Exhaustion DoS Vulnerabilities with Leak-Oriented Minimum Path Covers](https://www.usenix.org/system/files/usenixsecurity26-zhan.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/zhan)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** Java资源泄漏涉及异常路径，穷举路径会产生组合爆炸。

**技术机制。** LeakHunter以LLM补充资源操作和异常语义，经静态验证后用偏向泄漏的最小路径覆盖筛选见证路径。

**结果解释与局限。** 90个人工确认泄漏中67个具外部触发证据、15个获开发者确认；11.4倍只指路径分析加速。

<a id="p082"></a>

## P082 · Kintsugi

**[Kintsugi: Empowering LLMs to Mitigate Web Vulnerabilities via Runtime Policy Injection](https://www.usenix.org/system/files/usenixsecurity26-peng-yihao.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-yihao)

- **主分类：** 安全事件调查与运维处置
- **关联任务：** 自动化漏洞修复
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 漏洞发现到正式修复的间隔较长，而全局运行时策略容易误伤正常请求。

**技术机制。** Kintsugi从差分系统调用定位危险代码，由LLM划定保护边界，再按正常轨迹生成内核强制策略。

**结果解释与局限。** 这是临时遏制而非根因修复；纯应用语义漏洞和处于正常系统调用包络内的攻击可能绕过。

<a id="p083"></a>

## P083 · VulGenie

**[Patch-Guided Vulnerability Detection: Extracting Java API Security Rules via Attack–Defense Cross-Analysis](https://www.usenix.org/system/files/usenixsecurity26-chen-bofei.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-bofei)

- **主分类：** 程序安全分析与漏洞检测
- **关联任务：** —
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)

**具体瓶颈。** Java安全补丁混有无关修改，难以提炼可迁移的API使用规则。

**技术机制。** VulGenie结合修改行为图、攻防数据流交叉和LLM规则总结，再以自适应静态污点分析查错。

**结果解释与局限。** 属于固定分析流水线；规则和检测覆盖受第三方源码、反射建模及外部利用前提限制。

<a id="p084"></a>

## P084 · CONSET

**[Semantics Over Syntax: Uncovering Pre-Authentication 5G Baseband Vulnerabilities](https://www.usenix.org/system/files/usenixsecurity26-huang-qiqing.pdf)**

USENIX Security 2026 · 边界对照 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/huang-qiqing)

- **主分类：** 动态安全测试
- **关联任务：** 安全规约生成与形式化验证
- **技术设计：** [D1 · 安全规则与规约的自动推断](mapping.md#d1)、[D3 · 基于程序语义的测试输入生成](mapping.md#d3)、[D5 · 基于外部工具的结果验证](mapping.md#d5)

**具体瓶颈。** 语法可接受但语义矛盾的认证前5G配置可使基带进入异常状态。

**技术机制。** CONSET以规范证据限定LLM提取跨字段约束，经DSL检查生成最小违约消息，并在仿真与无线实验中验证。

**结果解释与局限。** 最终PDF为29个OAI崩溃位置而非网页的46个；仅验证特定RRC可用性场景，不是在线智能体。

<a id="p085"></a>

## P085 · AIxCC SoK

**[SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned](https://www.usenix.org/system/files/usenixsecurity26-zhang-cen.pdf)**

USENIX Security 2026 · 评测与方法背景 · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-cen)

- **主分类：** 评测与方法背景
- **关联任务：** 动态安全测试、漏洞复现与利用验证、自动化漏洞修复
- **技术设计：** 未强行映射到五项技术设计

**具体瓶颈。** 竞赛总分混合了漏洞能力、环境工程、资源和提交策略，难以直接比较技术。

**技术机制。** AIxCC SoK系统分析七支决赛系统的代码和轨迹，区分PoV、补丁、SARIF与结果关联流程。

**结果解释与局限。** 属于二手系统化证据；五个无harness项目不计分，既有判据通过也不保证补丁语义正确。
