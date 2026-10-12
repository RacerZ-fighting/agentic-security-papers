# Awesome Agentic Systems for Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated collection of research papers on agentic systems for security, organized by security tasks and aligned with our SoK.

**Agentic System 如何解决传统安全技术面临的困难？** 本仓库整理 LLM 与安全工具结合的研究，覆盖漏洞检测、动态测试、漏洞复现、形式化验证、漏洞修复、渗透测试与安全运维。

收录 **85 篇**，文献快照截至 **2026-10-12**。以 2025–2026 年安全四大会议为主，补充 2 篇作者或机构确认录用的 2027 年论文。

文献属性：**60 项研究系统与反馈流程 · 21 项边界对照 · 4 项评测与方法背景**。这些属性沿用原始文献附表；系统的控制方式和反馈阶段见逐篇分析。

[SoK 全文](docs/sok.md) · [逐篇证据与局限](docs/evidence.md) · [任务与技术设计映射](docs/mapping.md) · [按会议与年份浏览](docs/venues.md) · [数据](data/papers.json) · [贡献指南](CONTRIBUTING.md)

## Contents

- [程序安全分析与漏洞检测 · Program Analysis and Vulnerability Detection](#analysis)（15）
- [动态安全测试 · Dynamic Security Testing](#testing)（32）
- [漏洞复现与利用验证 · Vulnerability Reproduction and Exploit Validation](#reproduction)（6）
- [安全规约生成与形式化验证 · Security Specification and Formal Verification](#verification)（3）
- [自动化漏洞修复 · Automated Vulnerability Repair](#repair)（7）
- [自动化渗透测试 · Automated Penetration Testing](#pentesting)（3）
- [安全事件调查与运维处置 · Security Investigation and Operational Remediation](#operations)（8）
- [相邻主题 · Related Topics](#adjacent)（7）
- [评测与方法背景 · Benchmarks and Methodological Background](#background)（4）
- [Scope and Organization](#scope-and-organization)
- [Contributing](#contributing)
- [License](#license)

## Scope and Organization

一级目录对应 SoK 第 2 节的七类安全任务，跨任务研究按主要产出归类；相邻主题及评测背景单列。每篇论文只在首页出现一次，关联任务和五项技术设计可在[映射表](docs/mapping.md)中交叉检索。

原附表通过会议名单、作者页面和公开全文核对录用与技术内容。本次仓库整理保留其标题、来源、机制和局限，并新增任务分类与 SoK 映射。详细检索口径与未纳入候选见[来源说明](docs/provenance.md)。

条目按年份降序、同年标题字母序排列。**研究系统**包含固定反馈流程；**边界对照**用于比较模型辅助方法；**评测背景**用于讨论评价方法。标签不表示自主程度或实验强弱。

<a id="analysis"></a>

## 程序安全分析与漏洞检测 · Program Analysis and Vulnerability Detection

源码、二进制、访问控制、API 误用及静态分析规则。

- **[Automatically Learning Vulnerability Patterns for Scalable Static Analysis of Web Applications](https://peng-hui.github.io/data/paper/ccs26:mocq.pdf)**（MoCQ） · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p006)
  以受限查询语言、符号语义反馈、规则泛化和误报消除构成固定生成执行循环。

- **[BACAgent: LLM-Powered Detection of Broken-Access-Control Vulnerabilities in Web Applications](https://lfysec.github.io/paper/bacagent-ccs26.pdf)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p007)
  将静态调用和会话证据、框架文档检索与按需代码取证接入分阶段权限推理。

- **[BugAuditor: Detecting Bugs via Inconsistent Defensive Code Auditing](https://www.usenix.org/system/files/usenixsecurity26-lin-miaoqian.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/lin-miaoqian) · [分析](docs/evidence.md#p065)
  BugAuditor从防御代码反推安全意图，用静态筛选、按需上下文和LLM比较定位处理不一致之处。

- **[Cutting the Gordian Knot: Detecting Malicious PyPI Packages via a Knowledge-Mining Framework](https://www.usenix.org/system/files/usenixsecurity26-guo-wenbo.pdf)**（PyGuard） · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/guo-wenbo) · [分析](docs/evidence.md#p079)
  PyGuard从既有工具错误中挖掘行为模式，结合精确匹配、语义摘要及RAG进行上下文判断。

- **[Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://arxiv.org/pdf/2605.15569)**（NEO） · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p046)
  以 CodeQL 查询工具按需取上下文，分阶段识别特权操作、跨服务路径和鉴权条件，并用 SMT 与模型判断筛除误报。

- **[Exposing Resource-Exhaustion DoS Vulnerabilities with Leak-Oriented Minimum Path Covers](https://www.usenix.org/system/files/usenixsecurity26-zhan.pdf)**（LeakHunter） · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/zhan) · [分析](docs/evidence.md#p081)
  LeakHunter以LLM补充资源操作和异常语义，经静态验证后用偏向泄漏的最小路径覆盖筛选见证路径。

- **[JScamd: An Automated Static Taint Analysis Framework for Detecting Cryptographic API Misuses in JavaScript](https://www.usenix.org/system/files/usenixsecurity26-jia-shijie.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-shijie) · [分析](docs/evidence.md#p071)
  JScamd从安全约束生成API映射和规则，以分析器一致性反馈驱动LLM自纠，再执行专门污点分析。

- **[Patch-Guided Vulnerability Detection: Extracting Java API Security Rules via Attack–Defense Cross-Analysis](https://www.usenix.org/system/files/usenixsecurity26-chen-bofei.pdf)**（VulGenie） · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-bofei) · [分析](docs/evidence.md#p083)
  VulGenie结合修改行为图、攻防数据流交叉和LLM规则总结，再以自适应静态污点分析查错。

- **[SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](https://yuuoniy.github.io/files/SpecAuditor.pdf)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p050)
  从补丁和文档归纳审计规范，生成静态查询，再由模型按需请求上下文检查和筛选违规报告。

- **[Towards Generality: Task-Adaptive Binary Analysis via Semantic Retrieval and Verifiable Reasoning](https://www.usenix.org/system/files/usenixsecurity26-liu-yuzhe.pdf)**（BINREX） · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yuzhe) · [分析](docs/evidence.md#p074)
  BINREX分解目标，检索函数语义，合成IDAPython脚本并按局部验证条件执行、修正和汇总证据。

- **[ForeDroid: Scenario-Aware Analysis for Android Malware Detection and Explanation](https://sen-chen.github.io/pdf/C59-CCS2025-ForeDroid%20Scenario-Aware%20Analysis%20for%20Android%20Malware%20Detection%20and%20Explanation.pdf)** · CCS 2025 · `边界对照` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765207) · [分析](docs/evidence.md#p015)
  修补静态调用链后用大模型归纳行为，按功能场景对照良性行为分布检测异常，再生成结构化分析报告。

- **[Generating API Parameter Security Rules with LLM for API Misuse Detection](https://www.ndss-symposium.org/wp-content/uploads/2025-465-paper.pdf)**（GPTAid） · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection/) · [分析](docs/evidence.md#p025)
  生成正确与违反规则的调用程序，以运行错误验证候选规则，差分细化后交给 CodeQL 检测。

- **[LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models](https://www.usenix.org/system/files/usenixsecurity25-lekssays.pdf)** · USENIX Security 2025 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays) · [分析](docs/evidence.md#p076)
  LLMxCPG用专门模型生成图查询和切片，再由另一模型判断漏洞；Joern反馈用于训练查询数据。

- **[The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](https://www.ndss-symposium.org/wp-content/uploads/2025-816-paper.pdf)** · NDSS 2025 · `边界对照` · [录用依据](https://www.ndss-symposium.org/ndss-paper/the-midas-touch-triggering-the-capability-of-llms-for-rm-api-misuse-detection/) · [分析](docs/evidence.md#p039)
  将分配识别、资源对象提取和释放配对拆开，以多种提示与一致性检查交叉验证，再生成 CodeQL 约束。

- **[TypeForge: Synthesizing and Selecting Best-Fit Composite Data Types for Stripped Binaries](https://cdn.luneresearch.com/pdfs/s&p/2025/2019a76d-f2bc-4c6d-8e4b-2c0656ee8d68.pdf)** · IEEE S&P 2025 · `边界对照` · [录用依据](https://sp2025.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p057)
  先以类型流图生成候选，再用模型比较反编译代码可读性并筛选最合适的类型。

<a id="testing"></a>

## 动态安全测试 · Dynamic Security Testing

模糊测试、符号执行、Web 扫描、协议与固件测试，以及测试环境和 Harness 准备。

- **[Agentic Orchestration for Hybrid Fuzzing](https://abhikrc.com/pdf/NDSS27.pdf)**（AhFuzz） · NDSS 2027 · 作者/机构确认录用 · `研究系统` · [录用依据](https://fouzhe.github.io/) · [分析](docs/evidence.md#p038)
  代理维护覆盖、种子和目标—结果轨迹，主动选择并配置 AFL++ 与 ConcoLLMic，让两类测试器协作探索。

- **[Agentic Concolic Execution](https://dylanjwolff.com/assets/agentic.pdf)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p043)
  用执行轨迹构造可灵活表达的路径约束，由总结与求解代理结合源码、执行和 SMT 工具生成输入。

- **[An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs](https://www.ndss-symposium.org/wp-content/uploads/2026-f1081-paper.pdf)**（PLC logic instruction fuzzing） · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/an-llm-driven-fuzzing-framework-for-detecting-logic-instruction-bugs-in-plcs/) · [分析](docs/evidence.md#p030)
  构建语义依赖图，生成并验证修正种子程序，再结合覆盖反馈变异参数，用日志、灯态和通信状态判错。

- **[Automatic, Expressive, and Scalable Fuzzing with Stitching](https://arxiv.org/pdf/2602.18689)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p005)
  用类型和动态状态约束定义可组合测试块，让传统覆盖反馈在运行时拼接，并用代理配置环境、分诊和修复规范。

- **[BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection](https://www.ndss-symposium.org/wp-content/uploads/2026-f94-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/) · [分析](docs/evidence.md#p032)
  LLM 从规格中提取状态机与处理规则，构造语义变异并依据设备实际响应检查逻辑偏差。

- **[Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](https://www.usenix.org/system/files/usenixsecurity26-wang-yiyi.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yiyi) · [分析](docs/evidence.md#p066)
  Bulbasaur按长期未覆盖分支触发查询智能体，结合静态上下文和运行时操作数合成可复用变异器。

- **[CHAMELEOSCAN: Demystifying and Detecting iOS Chameleon Apps via LLM-Powered UI Exploration](https://www.ndss-symposium.org/wp-content/uploads/2026-f1906-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/chameleoscan-demystifying-and-detecting-ios-chameleon-apps-via-llm-powered-ui-exploration/) · [分析](docs/evidence.md#p033)
  从元数据提出转换假设，结合截图和 UI 树反复决策、执行及验证实际功能变化。

- **[CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models](https://people.cs.umass.edu/~amir/papers/2026-CCS-CircumVolve.pdf)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p009)
  让模型在进化搜索框架中修改可执行协议策略，并依据抓包、错误及双重成功判据迭代。

- **[Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/pdf/2604.01645)**（GONDAR） · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p044)
  探索代理负责抵达目标，模糊测试提供带状态的候选种子，利用代理再根据 sink 语义补齐触发条件。

- **[Cottontail: Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://arxiv.org/pdf/2504.17542)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p045)
  把覆盖树筛出的约束交给模型求解并补全结构，再以实际执行反馈修正输入和更新种子。

- **[Death by a Thousand Drips: Uncovering Critical Resource Leaks in the Windows Ecosystem](https://www.usenix.org/system/files/usenixsecurity26-dong-feng.pdf)**（REDOSPECTOR） · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/dong-feng) · [分析](docs/evidence.md#p080)
  REDOSPECTOR离线使用逆向信息和LLM生成协议种子，再用原生钩子、重复放大和增长趋势判定泄漏。

- **[deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://arxiv.org/pdf/2506.15648)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p055)
  静态分析先定位可达 unsafe 代码的 API，再用模型扩展 harness，并根据编译错误反复修复后交给模糊测试。

- **[FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://www.ndss-symposium.org/wp-content/uploads/2026-s1943-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/) · [分析](docs/evidence.md#p035)
  先以模糊测试确定真实输入源与调用关系，再由污点分析代理和 PoC 代理结合反编译语义与种子验证漏洞。

- **[Firmenstein: Scaling Dynamic Analysis for Linux-Based Firmware Services via API-Centric Intervention Code Synthesis](https://www.usenix.org/system/files/usenixsecurity26-wang-yanzhong.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yanzhong) · [分析](docs/evidence.md#p067)
  Firmenstein以API依赖图支持切片和诊断智能体，再生成环境或执行干预代码以恢复运行。

- **[From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://sites.cs.ucsb.edu/~chris/research/doc/ccs26_pdffuzz.pdf)**（PDFuzzer） · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p010)
  离线提取语义规范与参数级语法，以关系约束和 SMT 求解组装调用序列，再交给传统变异测试。

- **[H3Act: Automated Measuring Semantic Conversion Anomalies of HTTP/3-to-HTTP/1.1 Translation in CDNs](https://www.usenix.org/system/files/usenixsecurity26-peng-qihang.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-qihang) · [分析](docs/evidence.md#p070)
  H3Act由生成与分析智能体对照客户端和源站日志，经RAG及记忆压缩指导下一批测试。

- **[PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/system/files/usenixsecurity26-jia-zhipeng.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-zhipeng) · [分析](docs/evidence.md#p072)
  PANGOLIN恢复分派入口和裁剪的多语言调用图，由智能体生成参数规格，再以设备响应纠错。

- **[PILOT: Command-Line Interface Fuzzing Via Path-Guided, Iterative Large Language Model Prompting](https://arxiv.org/pdf/2511.20555)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p048)
  以调用路径指导模型使用工具构造执行环境和输入，再用覆盖反馈迭代生成可用种子。

- **[ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification](https://www.ndss-symposium.org/wp-content/uploads/2026-f521-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/protocolguard-detecting-protocol-non-compliance-bugs-via-llm-guided-static-analysis-and-dynamic-verification/) · [分析](docs/evidence.md#p036)
  LLM 连接 RFC 规则与代码切片，合成断言和测试脚本，以执行及报文轨迹反馈修正，再用定向模糊测试验证。

- **[Semantics Over Syntax: Uncovering Pre-Authentication 5G Baseband Vulnerabilities](https://www.usenix.org/system/files/usenixsecurity26-huang-qiqing.pdf)**（CONSET） · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/huang-qiqing) · [分析](docs/evidence.md#p084)
  CONSET以规范证据限定LLM提取跨字段约束，经DSL检查生成最小违约消息，并在仿真与无线实验中验证。

- **[Specializing Language Models for Textual Fuzzing via Reinforcement Learning](https://arxiv.org/pdf/2509.20384)**（R1-Fuzz） · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p051)
  利用路径问题和距离奖励训练专用模型，再以覆盖反馈选择目标并生成供 AFL++ 使用的种子。

- **[StepStone: LLM-Based GPU Kernel Driver Fuzzing via User-Space Libraries](https://www.cs.ucr.edu/~zhiyunq/pub/oakland26_gpu_fuzzing.pdf)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p052)
  从用户态库的公开 API 提取类型和语义，用模型补全依赖与取值约束并修复描述，再驱动内核模糊测试。

- **[Thinking More, Harnessing Better: Automatic Harness Generation with Dataflow Aggregation and Workflow Decomposition](https://arxiv.org/pdf/2607.07007)**（SynapseFlow） · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p014)
  先以语义流图聚合相关函数，再由预设四阶段流程和失败回滚逐步生成测试桩。

- **[Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis](https://www.usenix.org/system/files/usenixsecurity26-lin-ziyu.pdf)**（iFinder） · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/lin-ziyu) · [分析](docs/evidence.md#p075)
  iFinder以发现、规范核查和PoC执行三类智能体，在容器中根据运行日志反复修正测试。

- **[EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](https://www.ndss-symposium.org/wp-content/uploads/2025-399-paper.pdf)** · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis/) · [分析](docs/evidence.md#p024)
  从公开请求和固件上下文推断路由模式，用验证反馈修正 LLM 输出，再以路由字典引导黑盒模糊测试。

- **[ELFuzz: Efficient Input Generation via LLM-driven Synthesis Over Fuzzer Space](https://www.usenix.org/system/files/usenixsecurity25-chen-chuyang.pdf)** · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-chuyang) · [分析](docs/evidence.md#p060)
  LLM按覆盖集合演化、组合并筛选可执行输入生成器，再为传统模糊测试提供种子。

- **[Hidden and Lost Control: on Security Design Risks in IoT User-Facing Matter Controller](https://www.ndss-symposium.org/wp-content/uploads/2025-266-paper.pdf)**（Matter controller security） · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/hidden-and-lost-control-on-security-design-risks-in-iot-user-facing-matter-controller/) · [分析](docs/evidence.md#p026)
  虚拟 Matter 设备提供可控环境，LLM 指导配对与界面搜索，再改变控制器身份和 ACL 检查显示是否正确。

- **[Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving](https://www.usenix.org/system/files/usenixsecurity25-yang-yupeng.pdf)**（HLPFuzz） · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yupeng) · [分析](docs/evidence.md#p061)
  HLPFuzz选择关键分支、执行候选输入，并借助调试器分歧分析与LSP查询补充求解上下文。

- **[Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators](https://www.usenix.org/system/files/usenixsecurity25-zhang-kunpeng.pdf)**（G²Fuzz） · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-kunpeng) · [分析](docs/evidence.md#p063)
  G²Fuzz生成和变异Python输入生成器，用库构造复杂文件，并在AFL++停滞时引入新特征组合。

- **[MBFuzzer: A Multi-Party Protocol Fuzzer for MQTT Brokers](https://www.usenix.org/system/files/usenixsecurity25-song-xiangpu.pdf)** · USENIX Security 2025 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/song-xiangpu) · [分析](docs/evidence.md#p077)
  MBFuzzer以Petri网协调消息，LLM分两步总结重放记录并核对规范中的强制约束。

- **[PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models](https://raw.githubusercontent.com/TCA-ISCAS/PromeFuzz-ccs-2025/master/paper/ccs25-full.pdf)** · CCS 2025 · `研究系统` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765222) · [分析](docs/evidence.md#p003)
  联合AST依赖图、文档检索、覆盖导向API调度及编译／运行反馈修复，并将成功修复提炼为可复用约束。

- **[YuraScanner: Leveraging LLMs for Task-driven Web App Scanning](https://www.ndss-symposium.org/wp-content/uploads/2025-388-paper.pdf)** · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/) · [分析](docs/evidence.md#p029)
  自动生成任务，以页面语义和历史驱动浏览器交互，再用传统 XSS 引擎验证输入点。

<a id="reproduction"></a>

## 漏洞复现与利用验证 · Vulnerability Reproduction and Exploit Validation

从已知漏洞或给定安全目标出发，生成并验证 PoC、PoV 或攻击见证。

- **[SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/pdf/2609.22792)** · IEEE S&P 2027 · 作者/机构确认录用 · `研究系统` · [录用依据](https://seclab.bu.edu/people/gianluca/) · [分析](docs/evidence.md#p056)
  把失败结果沿执行轨迹归因到技能文档，汇总跨任务一致的修改意见，在冻结模型和执行框架的情况下优化上下文。

- **[CVE-Genie: An LLM-Based Multi-Agent Framework for Reproducing CVEs](https://sites.cs.ucsb.edu/~chris/research/doc/ccs26_cvegenie.pdf)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p008)
  将环境构建、利用生成和验证拆成有反馈的工具代理，并以隔离环境、统一 flag 与验证器批评约束成功条件。

- **[IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework for Black Box IoT devices](https://www.ndss-symposium.org/wp-content/uploads/2026-f634-paper.pdf)** · NDSS 2026 · `边界对照` · [录用依据](https://www.ndss-symposium.org/ndss-paper/iotbec-an-accurate-and-efficient-recurring-vulnerability-detection-framework-for-black-box-iot-devices/) · [分析](docs/evidence.md#p041)
  匹配漏洞与设备接口签名，以 LLM 生成针对性载荷和相关参数变异，再执行并监控真实设备。

- **[PBFuzz: Agentic Directed Fuzzing for PoV Generation](https://arxiv.org/pdf/2512.04611)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p012)
  以源码和调试反馈驱动规划、类型化输入生成器、属性测试及反思循环，持续记忆有效约束。

- **[SACK: Systematic Generation of Function Substitution Attacks Against Control-Flow Integrity](https://www.ndss-symposium.org/wp-content/uploads/2026-f2317-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/sack-systematic-generation-of-function-substitution-attacks-against-control-flow-integrity/) · [分析](docs/evidence.md#p037)
  LLM 生成安全判据，执行后反馈修正，再由确定性引擎枚举合法调用目标替换并验证安全破坏。

- **[TRIGFUZZ: Triggering Conditions Guided Directed Fuzzing](https://vul337.github.io/TrigFuzz/trigfuzz.pdf)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p053)
  让模型交互读取源码并抽取触发条件，经动态检查后把条件距离用于种子调度和字节变异。

<a id="verification"></a>

## 安全规约生成与形式化验证 · Security Specification and Formal Verification

安全性质、协议规约、验证环境与组件级证明的生成和检查。

- **[AutoSOUP: Safety-Oriented Unit Proof Generation for Component-level Memory-Safety Verification](https://arxiv.org/pdf/2605.10712)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p004)
  资源感知范围扩展、性质引导循环界精化、调用上下文检验环境前提；LLM处理有界语义任务，CBMC与静态分析验证产物。

- **[Generating Precise Format Specification for Network Protocols Through Adversarial LLM Interactions](https://www.usenix.org/system/files/usenixsecurity26-ye.pdf)**（SPAR） · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/ye) · [分析](docs/evidence.md#p069)
  SPAR分别生成格式规范和参考解析器，以SMT构造正反例并让二者交叉反馈、迭代修正。

- **[PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](https://www.ndss-symposium.org/wp-content/uploads/2025-1357-paper.pdf)** · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/) · [分析](docs/evidence.md#p028)
  检索人工性质作为参考，生成并按编译反馈修正规格，排序后交给专用证明器验证。

<a id="repair"></a>

## 自动化漏洞修复 · Automated Vulnerability Repair

根因定位、补丁生成、回移与补丁完整性检查。

- **[From Fix to Flaw: Understanding and Revealing Incomplete Patches for Link Following Vulnerabilities](https://crisprss.github.io/paper/linkdiff.pdf)**（LinkDiff） · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p011)
  先静态裁剪文件操作相关差异，再让模型按需调用二进制分析工具，并以历史补丁缺陷分类辅助审计。

- **[LLMBisect: Breaking Barriers in Bug Bisection with A Comparative Analysis Pipeline](https://www.ndss-symposium.org/wp-content/uploads/2026-s990-paper.pdf)** · NDSS 2026 · `边界对照` · [录用依据](https://www.ndss-symposium.org/ndss-paper/llmbisect-breaking-barriers-in-bug-bisection-with-a-comparative-analysis-pipeline/) · [分析](docs/evidence.md#p042)
  联合补丁、提交说明和代码语义生成候选，经多轮比较、筛选与投票定位引入漏洞的提交。

- **[PortGPT: Towards Automated Backporting Using Large Language Models](https://arxiv.org/pdf/2510.22396)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p049)
  按补丁块定位相关代码并生成回移方案，再通过应用、自动修复和编译测试反馈逐步校正。

- **[Web Application Vulnerability Repair Via Context-Aware Fault Localization and Directed Differential Fuzzing](https://seclab.cse.cuhk.edu.hk/papers/sp26-SlicePatch.pdf)**（SlicePatch） · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p054)
  通过执行剖析和切片定位缺陷，生成补丁后用 PoC 与定向差分模糊测试检查绕过及回归，再反馈重试。

- **[APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching](https://www.usenix.org/system/files/usenixsecurity25-nong.pdf)** · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/nong) · [分析](docs/evidence.md#p059)
  APPATCH按程序依赖切片，让模型按需索取函数和示例，再由多个LLM判断补丁有效性。

- **[Logs In, Patches Out: Automated Vulnerability Repair via Tree-of-Thought LLM Analysis](https://www.usenix.org/system/files/usenixsecurity25-kim-youngjoon.pdf)**（SAN2PATCH） · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/kim-youngjoon) · [分析](docs/evidence.md#p062)
  SAN2PATCH以理解、定位、策略、生成四阶段思维树搜索候选，再进行构建、PoC和功能验证。

- **[PATCHAGENT: A Practical Program Repair Agent Mimicking Human Expertise](https://www.usenix.org/system/files/usenixsecurity25-yu-zheng.pdf)** · USENIX Security 2025 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zheng) · [分析](docs/evidence.md#p064)
  以语言服务器检索和补丁验证器形成定位—修改—验证循环，并用反例反馈改进下一轮补丁。

<a id="pentesting"></a>

## 自动化渗透测试 · Automated Penetration Testing

CTF、权限提升与多主机攻击任务中的状态维护和操作选择。

- **[Incalmo: an Autonomous Llm-Assisted System for Red Teaming Multi-Host Networks](https://arxiv.org/pdf/2501.16466)** · IEEE S&P 2026 · `研究系统` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p047)
  将高层规划与五类任务执行分离，用任务代理和持久化环境状态服务协同推进。

- **[PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation](https://arxiv.org/pdf/2609.09087)** · CCS 2026 · `研究系统` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p013)
  531 Docker场景；确定性枚举、规则/LLM类别匹配、步骤规划、候选策略切换；执行式root成功判据。

- **[Measuring and Augmenting Large Language Models for Solving Capture-the-Flag Challenges](https://daoyuan14.github.io/papers/CCS25_CTFAgent.pdf)**（CTF challenges） · CCS 2025 · `研究系统` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744855) · [分析](docs/evidence.md#p001)
  以代码和利用思路分别检索两阶段知识，结合交互式命令会话、工具提示和反编译器，循环执行至获取旗标或达到轮数上限。

<a id="operations"></a>

## 安全事件调查与运维处置 · Security Investigation and Operational Remediation

日志调查、威胁检测与模拟、响应规划及受运行策略约束的漏洞处置。

- **[Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation](https://www.ndss-symposium.org/wp-content/uploads/2026-f375-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/chimera-harnessing-multi-agent-llms-for-automatic-insider-threat-simulation/) · [分析](docs/evidence.md#p034)
  有角色、记忆、计划和交流能力的多代理在隔离企业环境执行活动，生成用于检测评估的多模态日志。

- **[From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports](https://www.usenix.org/system/files/usenixsecurity26-cai.pdf)**（SIGMERGE） · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/cai) · [分析](docs/evidence.md#p068)
  SIGMERGE提取命令与TTP，调用专用验证工具迭代纠正结构化攻击描述，再检索知识生成Sigma规则。

- **[Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination](https://www.ndss-symposium.org/wp-content/uploads/2026-f358-paper.pdf)** · NDSS 2026 · `边界对照` · [录用依据](https://www.ndss-symposium.org/ndss-paper/incident-response-planning-using-a-lightweight-large-language-model-with-reduced-hallucination/) · [分析](docs/evidence.md#p040)
  微调轻量模型并检索威胁情报，通过候选动作的未来恢复状态模拟进行前瞻规划。

- **[Kintsugi: Empowering LLMs to Mitigate Web Vulnerabilities via Runtime Policy Injection](https://www.usenix.org/system/files/usenixsecurity26-peng-yihao.pdf)** · USENIX Security 2026 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-yihao) · [分析](docs/evidence.md#p082)
  Kintsugi从差分系统调用定位危险代码，由LLM划定保护边界，再按正常轨迹生成内核强制策略。

- **[PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies](https://www.usenix.org/system/files/usenixsecurity26-li-rui.pdf)** · USENIX Security 2026 · `研究系统` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui) · [分析](docs/evidence.md#p073)
  PatchWeaver让LLM提议计划，由状态图、类型化策略和短程模拟筛选动作并在漂移后重新规划。

- **[PiMRef: Deducing Ever-evolving Spear-phishing Emails with Knowledge Base Invariants](https://arxiv.org/pdf/2507.15393)** · CCS 2026 · `边界对照` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p019)
  代理搜索并浏览权威页面建立身份域名知识库，在线阶段以抽取、匹配和规则检查身份矛盾。

- **[OCR-APT: Reconstructing APT Stories from Audit Logs using Subgraph Anomaly Detection and LLMs](https://arxiv.org/pdf/2510.15188)** · CCS 2025 · `研究系统` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765219) · [分析](docs/evidence.md#p002)
  将异常子图序列化并检索，逐步抽取和验证IOC、合并攻击阶段报告，再围绕模型选出的关键IOC补充邻接证据。

- **[TORCHLIGHT: Shedding LIGHT on Real-World Attacks on Cloudless IoT Devices Concealed within the Tor Network](https://www.usenix.org/system/files/usenixsecurity25-pan-yumingzhi.pdf)** · USENIX Security 2025 · `边界对照` · [录用依据](https://www.usenix.org/conference/usenixsecurity25/presentation/pan-yumingzhi) · [分析](docs/evidence.md#p078)
  TORCHLIGHT结合出口流量采集与五阶段LLM实体核验、检索和攻击分析，由人工确认漏洞。

<a id="adjacent"></a>

## 相邻主题 · Related Topics

安全代码生成、验证码、MCP 工具审计、诈骗测量、硬件 IP、汽车风险建模与隐私合规。

- **[Automating Function-Level TARA for Automotive Full-Lifecycle Security](https://www.ndss-symposium.org/wp-content/uploads/2026-s1408-paper.pdf)** · NDSS 2026 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/automating-function-level-tara-for-automotive-full-lifecycle-security/) · [分析](docs/evidence.md#p031)
  构造子树、组装攻击树和风险评估的专职代理互相检查，以结构化配置、RAG 和微调支持功能级 TARA。

- **[Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://arxiv.org/pdf/2512.22789)** · IEEE S&P 2026 · `边界对照` · [录用依据](https://sp2026.ieee-security.org/accepted-papers.html) · [分析](docs/evidence.md#p058)
  浏览器代理按目标寻找表单，再把页面语义转成结构化事实，交给 Datalog 规则判定界面层违规。

- **[ContractGuard: Auditing Semantic Contracts of MCP Tools for Security Violations](https://cdn.luneresearch.com/pdfs/eca78c77-9cbc-4d2e-9ee7-683f2c88d7d0/ac0c51e8750910f7ea2133981baa2b1cf327eab6a91c4932788947f4c1394ae0.pdf)** · CCS 2026 · `边界对照` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p018)
  以静态切片和按需源码检索生成实现摘要，再逐项核对自然语言契约与实际代码行为。

- **[When Scammers Talk Back: Understanding Potentially Unwanted Calls via LLM-Based Interaction](https://yancomm.net/papers/2026%20-%20CCS%20-%20When%20Scammers%20Talk%20Back.pdf)** · CCS 2026 · `边界对照` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p020)
  用低延迟语音对话代理和虚构身份维持蜜罐通话，采集后再进行人工分层抽样与主题编码。

- **[Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection](https://arxiv.org/pdf/2504.16429)** · CCS 2025 · `边界对照` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3765049) · [分析](docs/evidence.md#p016)
  从历史漏洞与补丁提炼安全知识，将生成需求拆为子任务后检索、按风险重排过滤，并注入代码生成提示。

- **[LLMPirate: LLMs for Black-box Hardware IP Piracy](https://www.ndss-symposium.org/wp-content/uploads/2025-2059-paper.pdf)** · NDSS 2025 · `研究系统` · [录用依据](https://www.ndss-symposium.org/ndss-paper/llmpirate-llms-for-black-box-hardware-ip-piracy/) · [分析](docs/evidence.md#p027)
  按门类型生成可复用改写，将语法、允许操作符和等价性检查结果反馈给 LLM 迭代修正。

- **[Oedipus: LLM-enchanced Reasoning CAPTCHA Solver](https://geleideng.github.io/publication/oedipus/oedipus.pdf)** · CCS 2025 · `边界对照` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744872) · [分析](docs/evidence.md#p017)
  用专用语言分解任务并在离线阶段通过语法反馈修正计划，再将计划转译成在线多模态求解步骤。

<a id="background"></a>

## 评测与方法背景 · Benchmarks and Methodological Background

反混淆基准、函数语义恢复、对抗评测与 AIxCC SoK。

- **[Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary](https://arxiv.org/pdf/2609.12457)** · CCS 2026 · `评测背景` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p022)
  通过分层摘要训练结合全局字符串与局部调用信息预测函数名。

- **[SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned](https://www.usenix.org/system/files/usenixsecurity26-zhang-cen.pdf)**（AIxCC SoK） · USENIX Security 2026 · `评测背景` · [录用依据](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-cen) · [分析](docs/evidence.md#p085)
  AIxCC SoK系统分析七支决赛系统的代码和轨迹，区分PoV、补丁、SARIF与结果关联流程。

- **[The Deception Delta: Adversarial Evaluation of LLM-Based Smart Contract Bytecode Forensics](https://arxiv.org/pdf/2609.14098)** · CCS 2026 · `评测背景` · [录用依据](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [分析](docs/evidence.md#p023)
  以具备执行真值的欺骗性字节码对多模型和提示策略进行单轮对抗评估。

- **[JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/pdf/2506.20170)** · CCS 2025 · `评测背景` · [录用依据](https://dl.acm.org/doi/10.1145/3719027.3744871) · [分析](docs/evidence.md#p021)
  构造可执行混淆样本，以单示例提示调用模型，并用语法、执行、复杂度与代码相似度四类评估器验证输出。

## Contributing

欢迎通过 Issue 或 Pull Request 补充论文、修正分类和报告链接问题。请同时提供全文、录用依据，以及与具体安全任务的关系。更新方式见[贡献指南](CONTRIBUTING.md)。

## License

文献整理、分类与原创说明采用 [CC BY 4.0](LICENSE)。构建脚本采用 [MIT](scripts/LICENSE)。被引用论文与第三方材料保留各自的版权和许可证。
