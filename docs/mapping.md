# SoK 分类与文献映射

[返回首页](../README.md) · [SoK 全文](sok.md) · [逐篇分析](evidence.md)

## 与正文结构对应

| SoK 部分 | 本仓库入口 |
| --- | --- |
| [1 研究范围与文献检索](sok.md#sok-1) | [来源与筛选口径](provenance.md)、[会议索引](venues.md) |
| [2 传统安全任务及其技术挑战](sok.md#sok-2) | 首页七类任务，另列相邻主题与评测背景 |
| [3 关键技术设计](sok.md#sok-3) | 下文 D1–D5 跨任务索引 |
| [4 实验设计与有效性评估](sok.md#sok-4) | 逐篇分析的“结果解释与局限” |
| [5 技术贡献与发展方向](sok.md#sok-5) | 结合机制、验证条件和局限归纳贡献 |

## 分类规则

主分类按研究的主要任务目标确定，每篇只计数一次。`related_tasks` 记录次要任务，`designs` 允许多选。两类交叉标签都不用于计算论文总数。文献属性沿用原附表，独立于任务类别。

边界条目的处理：LinkDiff 按补丁完整性审计归入修复，LLMBisect 按根因定位支撑归入修复，Kintsugi 按运行时缓解归入运维；SelfOp 按已评估的 CyberGym 漏洞复现任务归类。Chimera 支撑事件检测评估，列在安全事件类。硬件 IP、汽车风险建模与隐私合规等列入相邻主题。

技术标签表示与 SoK 讨论维度的对应关系，既可用于主体系统，也可用于比较方法或评测。D4 包含固定流程中的反馈修正、证据获取和离线技能改进；D5 包含不同强度的工具检查和日志证据核对。具体控制权、发生阶段和验证强度以逐篇机制与局限为准。空标签表示不强行套入五项设计。

## 按技术设计查阅

<a id="d1"></a>

### D1 · 安全规则与规约的自动推断

[SoK §3.1](sok.md#sok-d1) · Security Rule and Specification Inference

从代码、文档或历史样例生成可供安全工具使用的规则、查询、约束或规约。

[PromeFuzz](evidence.md#p003)、[AutoSOUP](evidence.md#p004)、[Fuzzing with Stitching](evidence.md#p005)、[MoCQ](evidence.md#p006)、[BACAgent](evidence.md#p007)、[PDFuzzer](evidence.md#p010)、[LinkDiff](evidence.md#p011)、[PBFuzz](evidence.md#p012)、[Give LLMs a Security Course](evidence.md#p016)、[ContractGuard](evidence.md#p018)、[PiMRef](evidence.md#p019)、[EAGLEYE](evidence.md#p024)、[GPTAid](evidence.md#p025)、[PropertyGPT](evidence.md#p028)、[PLC logic instruction fuzzing](evidence.md#p030)、[Function-Level TARA](evidence.md#p031)、[BSFuzzer](evidence.md#p032)、[FirmAgent](evidence.md#p035)、[ProtocolGuard](evidence.md#p036)、[SACK](evidence.md#p037)、[The Midas Touch](evidence.md#p039)、[Agentic Concolic Execution](evidence.md#p043)、[GONDAR](evidence.md#p044)、[Cottontail](evidence.md#p045)、[NEO](evidence.md#p046)、[SpecAuditor](evidence.md#p050)、[StepStone](evidence.md#p052)、[TRIGFUZZ](evidence.md#p053)、[GDPR consent violations](evidence.md#p058)、[HLPFuzz](evidence.md#p061)、[BugAuditor](evidence.md#p065)、[Bulbasaur](evidence.md#p066)、[SIGMERGE](evidence.md#p068)、[SPAR](evidence.md#p069)、[H3Act](evidence.md#p070)、[JScamd](evidence.md#p071)、[PANGOLIN](evidence.md#p072)、[iFinder](evidence.md#p075)、[MBFuzzer](evidence.md#p077)、[PyGuard](evidence.md#p079)、[LeakHunter](evidence.md#p081)、[Kintsugi](evidence.md#p082)、[VulGenie](evidence.md#p083)、[CONSET](evidence.md#p084)

<a id="d2"></a>

### D2 · 执行环境与前置状态的自动准备

[SoK §3.2](sok.md#sok-d2) · Environment and State Preparation

准备软件依赖、验证环境、设备环境或多步交互所需的状态。

[CTF challenges](evidence.md#p001)、[AutoSOUP](evidence.md#p004)、[Fuzzing with Stitching](evidence.md#p005)、[CVE-Genie](evidence.md#p008)、[PrivEscalate](evidence.md#p013)、[Matter controller security](evidence.md#p026)、[YuraScanner](evidence.md#p029)、[CHAMELEOSCAN](evidence.md#p033)、[Chimera](evidence.md#p034)、[Incalmo](evidence.md#p047)、[PILOT](evidence.md#p048)、[GDPR consent violations](evidence.md#p058)、[Firmenstein](evidence.md#p067)、[PatchWeaver](evidence.md#p073)

<a id="d3"></a>

### D3 · 基于程序语义的测试输入生成

[SoK §3.3](sok.md#sok-d3) · Semantics-Guided Test Generation

生成 Harness、输入生成器、变异器或满足语义约束的测试输入。

[PromeFuzz](evidence.md#p003)、[Fuzzing with Stitching](evidence.md#p005)、[CVE-Genie](evidence.md#p008)、[CircumVolve](evidence.md#p009)、[PDFuzzer](evidence.md#p010)、[PBFuzz](evidence.md#p012)、[SynapseFlow](evidence.md#p014)、[EAGLEYE](evidence.md#p024)、[GPTAid](evidence.md#p025)、[PLC logic instruction fuzzing](evidence.md#p030)、[BSFuzzer](evidence.md#p032)、[FirmAgent](evidence.md#p035)、[ProtocolGuard](evidence.md#p036)、[SACK](evidence.md#p037)、[AhFuzz](evidence.md#p038)、[IoTBec](evidence.md#p041)、[Agentic Concolic Execution](evidence.md#p043)、[GONDAR](evidence.md#p044)、[Cottontail](evidence.md#p045)、[PILOT](evidence.md#p048)、[R1-Fuzz](evidence.md#p051)、[StepStone](evidence.md#p052)、[TRIGFUZZ](evidence.md#p053)、[deepSURF](evidence.md#p055)、[ELFuzz](evidence.md#p060)、[HLPFuzz](evidence.md#p061)、[G²Fuzz](evidence.md#p063)、[Bulbasaur](evidence.md#p066)、[SPAR](evidence.md#p069)、[H3Act](evidence.md#p070)、[PANGOLIN](evidence.md#p072)、[iFinder](evidence.md#p075)、[REDOSPECTOR](evidence.md#p080)、[CONSET](evidence.md#p084)

<a id="d4"></a>

### D4 · 基于执行反馈的任务规划与调整

[SoK §3.4](sok.md#sok-d4) · Feedback-Guided Planning and Execution

按需获取证据，结合执行轨迹调整步骤、修复产物或维护任务状态；发生阶段须结合逐篇机制阅读。

[CTF challenges](evidence.md#p001)、[OCR-APT](evidence.md#p002)、[PromeFuzz](evidence.md#p003)、[MoCQ](evidence.md#p006)、[BACAgent](evidence.md#p007)、[CVE-Genie](evidence.md#p008)、[CircumVolve](evidence.md#p009)、[LinkDiff](evidence.md#p011)、[PBFuzz](evidence.md#p012)、[PrivEscalate](evidence.md#p013)、[SynapseFlow](evidence.md#p014)、[Oedipus](evidence.md#p017)、[ContractGuard](evidence.md#p018)、[When Scammers Talk Back](evidence.md#p020)、[Matter controller security](evidence.md#p026)、[LLMPirate](evidence.md#p027)、[PropertyGPT](evidence.md#p028)、[YuraScanner](evidence.md#p029)、[PLC logic instruction fuzzing](evidence.md#p030)、[CHAMELEOSCAN](evidence.md#p033)、[Chimera](evidence.md#p034)、[FirmAgent](evidence.md#p035)、[ProtocolGuard](evidence.md#p036)、[AhFuzz](evidence.md#p038)、[Incident Response Planning](evidence.md#p040)、[Agentic Concolic Execution](evidence.md#p043)、[GONDAR](evidence.md#p044)、[Cottontail](evidence.md#p045)、[NEO](evidence.md#p046)、[Incalmo](evidence.md#p047)、[PILOT](evidence.md#p048)、[PortGPT](evidence.md#p049)、[SpecAuditor](evidence.md#p050)、[TRIGFUZZ](evidence.md#p053)、[SlicePatch](evidence.md#p054)、[deepSURF](evidence.md#p055)、[SelfOp](evidence.md#p056)、[GDPR consent violations](evidence.md#p058)、[APPATCH](evidence.md#p059)、[ELFuzz](evidence.md#p060)、[HLPFuzz](evidence.md#p061)、[SAN2PATCH](evidence.md#p062)、[G²Fuzz](evidence.md#p063)、[PatchAgent](evidence.md#p064)、[BugAuditor](evidence.md#p065)、[Bulbasaur](evidence.md#p066)、[Firmenstein](evidence.md#p067)、[SIGMERGE](evidence.md#p068)、[SPAR](evidence.md#p069)、[H3Act](evidence.md#p070)、[JScamd](evidence.md#p071)、[PANGOLIN](evidence.md#p072)、[PatchWeaver](evidence.md#p073)、[BINREX](evidence.md#p074)、[iFinder](evidence.md#p075)

<a id="d5"></a>

### D5 · 基于外部工具的结果验证

[SoK §3.5](sok.md#sok-d5) · Tool-Based Validation

利用编译、运行、测试、形式化工具或原始事件证据检查产物；检查强度因任务而异。

[CTF challenges](evidence.md#p001)、[OCR-APT](evidence.md#p002)、[PromeFuzz](evidence.md#p003)、[AutoSOUP](evidence.md#p004)、[Fuzzing with Stitching](evidence.md#p005)、[MoCQ](evidence.md#p006)、[CVE-Genie](evidence.md#p008)、[CircumVolve](evidence.md#p009)、[PBFuzz](evidence.md#p012)、[PrivEscalate](evidence.md#p013)、[SynapseFlow](evidence.md#p014)、[Oedipus](evidence.md#p017)、[JsDeObsBench](evidence.md#p021)、[The Deception Delta](evidence.md#p023)、[EAGLEYE](evidence.md#p024)、[GPTAid](evidence.md#p025)、[Matter controller security](evidence.md#p026)、[LLMPirate](evidence.md#p027)、[PropertyGPT](evidence.md#p028)、[YuraScanner](evidence.md#p029)、[PLC logic instruction fuzzing](evidence.md#p030)、[BSFuzzer](evidence.md#p032)、[CHAMELEOSCAN](evidence.md#p033)、[FirmAgent](evidence.md#p035)、[ProtocolGuard](evidence.md#p036)、[SACK](evidence.md#p037)、[AhFuzz](evidence.md#p038)、[Incident Response Planning](evidence.md#p040)、[IoTBec](evidence.md#p041)、[Agentic Concolic Execution](evidence.md#p043)、[GONDAR](evidence.md#p044)、[Cottontail](evidence.md#p045)、[NEO](evidence.md#p046)、[PILOT](evidence.md#p048)、[PortGPT](evidence.md#p049)、[StepStone](evidence.md#p052)、[TRIGFUZZ](evidence.md#p053)、[SlicePatch](evidence.md#p054)、[deepSURF](evidence.md#p055)、[GDPR consent violations](evidence.md#p058)、[ELFuzz](evidence.md#p060)、[HLPFuzz](evidence.md#p061)、[SAN2PATCH](evidence.md#p062)、[PatchAgent](evidence.md#p064)、[Bulbasaur](evidence.md#p066)、[Firmenstein](evidence.md#p067)、[SIGMERGE](evidence.md#p068)、[SPAR](evidence.md#p069)、[H3Act](evidence.md#p070)、[JScamd](evidence.md#p071)、[PANGOLIN](evidence.md#p072)、[PatchWeaver](evidence.md#p073)、[BINREX](evidence.md#p074)、[iFinder](evidence.md#p075)、[REDOSPECTOR](evidence.md#p080)、[LeakHunter](evidence.md#p081)、[Kintsugi](evidence.md#p082)、[CONSET](evidence.md#p084)

## 完整映射

| 编号 | 论文 / 系统 | 主分类 | 关联任务 | 技术设计 |
| --- | --- | --- | --- | --- |
| P001 | [CTF challenges](evidence.md#p001) | 自动化渗透测试 | 漏洞复现与利用验证 | [D2](#d2) [D4](#d4) [D5](#d5) |
| P002 | [OCR-APT](evidence.md#p002) | 安全事件调查与运维处置 | — | [D4](#d4) [D5](#d5) |
| P003 | [PromeFuzz](evidence.md#p003) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P004 | [AutoSOUP](evidence.md#p004) | 安全规约生成与形式化验证 | 程序安全分析与漏洞检测 | [D1](#d1) [D2](#d2) [D5](#d5) |
| P005 | [Fuzzing with Stitching](evidence.md#p005) | 动态安全测试 | — | [D1](#d1) [D2](#d2) [D3](#d3) [D5](#d5) |
| P006 | [MoCQ](evidence.md#p006) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) [D5](#d5) |
| P007 | [BACAgent](evidence.md#p007) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) |
| P008 | [CVE-Genie](evidence.md#p008) | 漏洞复现与利用验证 | — | [D2](#d2) [D3](#d3) [D4](#d4) [D5](#d5) |
| P009 | [CircumVolve](evidence.md#p009) | 动态安全测试 | — | [D3](#d3) [D4](#d4) [D5](#d5) |
| P010 | [PDFuzzer](evidence.md#p010) | 动态安全测试 | — | [D1](#d1) [D3](#d3) |
| P011 | [LinkDiff](evidence.md#p011) | 自动化漏洞修复 | 程序安全分析与漏洞检测 | [D1](#d1) [D4](#d4) |
| P012 | [PBFuzz](evidence.md#p012) | 漏洞复现与利用验证 | 动态安全测试 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P013 | [PrivEscalate](evidence.md#p013) | 自动化渗透测试 | — | [D2](#d2) [D4](#d4) [D5](#d5) |
| P014 | [SynapseFlow](evidence.md#p014) | 动态安全测试 | — | [D3](#d3) [D4](#d4) [D5](#d5) |
| P015 | [ForeDroid](evidence.md#p015) | 程序安全分析与漏洞检测 | — | — |
| P016 | [Give LLMs a Security Course](evidence.md#p016) | 相邻主题 | 自动化漏洞修复 | [D1](#d1) |
| P017 | [Oedipus](evidence.md#p017) | 相邻主题 | — | [D4](#d4) [D5](#d5) |
| P018 | [ContractGuard](evidence.md#p018) | 相邻主题 | 程序安全分析与漏洞检测 | [D1](#d1) [D4](#d4) |
| P019 | [PiMRef](evidence.md#p019) | 安全事件调查与运维处置 | — | [D1](#d1) |
| P020 | [When Scammers Talk Back](evidence.md#p020) | 相邻主题 | 安全事件调查与运维处置 | [D4](#d4) |
| P021 | [JsDeObsBench](evidence.md#p021) | 评测与方法背景 | 程序安全分析与漏洞检测 | [D5](#d5) |
| P022 | [Hieronym](evidence.md#p022) | 评测与方法背景 | 程序安全分析与漏洞检测 | — |
| P023 | [The Deception Delta](evidence.md#p023) | 评测与方法背景 | 程序安全分析与漏洞检测 | [D5](#d5) |
| P024 | [EAGLEYE](evidence.md#p024) | 动态安全测试 | 程序安全分析与漏洞检测 | [D1](#d1) [D3](#d3) [D5](#d5) |
| P025 | [GPTAid](evidence.md#p025) | 程序安全分析与漏洞检测 | 安全规约生成与形式化验证 | [D1](#d1) [D3](#d3) [D5](#d5) |
| P026 | [Matter controller security](evidence.md#p026) | 动态安全测试 | — | [D2](#d2) [D4](#d4) [D5](#d5) |
| P027 | [LLMPirate](evidence.md#p027) | 相邻主题 | — | [D4](#d4) [D5](#d5) |
| P028 | [PropertyGPT](evidence.md#p028) | 安全规约生成与形式化验证 | — | [D1](#d1) [D4](#d4) [D5](#d5) |
| P029 | [YuraScanner](evidence.md#p029) | 动态安全测试 | — | [D2](#d2) [D4](#d4) [D5](#d5) |
| P030 | [PLC logic instruction fuzzing](evidence.md#p030) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P031 | [Function-Level TARA](evidence.md#p031) | 相邻主题 | 自动化渗透测试 | [D1](#d1) |
| P032 | [BSFuzzer](evidence.md#p032) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D5](#d5) |
| P033 | [CHAMELEOSCAN](evidence.md#p033) | 动态安全测试 | 程序安全分析与漏洞检测 | [D2](#d2) [D4](#d4) [D5](#d5) |
| P034 | [Chimera](evidence.md#p034) | 安全事件调查与运维处置 | 自动化渗透测试 | [D2](#d2) [D4](#d4) |
| P035 | [FirmAgent](evidence.md#p035) | 动态安全测试 | 程序安全分析与漏洞检测、漏洞复现与利用验证 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P036 | [ProtocolGuard](evidence.md#p036) | 动态安全测试 | 程序安全分析与漏洞检测、安全规约生成与形式化验证 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P037 | [SACK](evidence.md#p037) | 漏洞复现与利用验证 | 动态安全测试 | [D1](#d1) [D3](#d3) [D5](#d5) |
| P038 | [AhFuzz](evidence.md#p038) | 动态安全测试 | — | [D3](#d3) [D4](#d4) [D5](#d5) |
| P039 | [The Midas Touch](evidence.md#p039) | 程序安全分析与漏洞检测 | — | [D1](#d1) |
| P040 | [Incident Response Planning](evidence.md#p040) | 安全事件调查与运维处置 | — | [D4](#d4) [D5](#d5) |
| P041 | [IoTBec](evidence.md#p041) | 漏洞复现与利用验证 | 动态安全测试 | [D3](#d3) [D5](#d5) |
| P042 | [LLMBisect](evidence.md#p042) | 自动化漏洞修复 | 程序安全分析与漏洞检测 | — |
| P043 | [Agentic Concolic Execution](evidence.md#p043) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P044 | [GONDAR](evidence.md#p044) | 动态安全测试 | 漏洞复现与利用验证 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P045 | [Cottontail](evidence.md#p045) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P046 | [NEO](evidence.md#p046) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) [D5](#d5) |
| P047 | [Incalmo](evidence.md#p047) | 自动化渗透测试 | — | [D2](#d2) [D4](#d4) |
| P048 | [PILOT](evidence.md#p048) | 动态安全测试 | — | [D2](#d2) [D3](#d3) [D4](#d4) [D5](#d5) |
| P049 | [PortGPT](evidence.md#p049) | 自动化漏洞修复 | — | [D4](#d4) [D5](#d5) |
| P050 | [SpecAuditor](evidence.md#p050) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) |
| P051 | [R1-Fuzz](evidence.md#p051) | 动态安全测试 | — | [D3](#d3) |
| P052 | [StepStone](evidence.md#p052) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D5](#d5) |
| P053 | [TRIGFUZZ](evidence.md#p053) | 漏洞复现与利用验证 | 动态安全测试 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P054 | [SlicePatch](evidence.md#p054) | 自动化漏洞修复 | 动态安全测试 | [D4](#d4) [D5](#d5) |
| P055 | [deepSURF](evidence.md#p055) | 动态安全测试 | 程序安全分析与漏洞检测 | [D3](#d3) [D4](#d4) [D5](#d5) |
| P056 | [SelfOp](evidence.md#p056) | 漏洞复现与利用验证 | — | [D4](#d4) |
| P057 | [TypeForge](evidence.md#p057) | 程序安全分析与漏洞检测 | — | — |
| P058 | [GDPR consent violations](evidence.md#p058) | 相邻主题 | 动态安全测试 | [D1](#d1) [D2](#d2) [D4](#d4) [D5](#d5) |
| P059 | [APPATCH](evidence.md#p059) | 自动化漏洞修复 | — | [D4](#d4) |
| P060 | [ELFuzz](evidence.md#p060) | 动态安全测试 | — | [D3](#d3) [D4](#d4) [D5](#d5) |
| P061 | [HLPFuzz](evidence.md#p061) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P062 | [SAN2PATCH](evidence.md#p062) | 自动化漏洞修复 | — | [D4](#d4) [D5](#d5) |
| P063 | [G²Fuzz](evidence.md#p063) | 动态安全测试 | — | [D3](#d3) [D4](#d4) |
| P064 | [PatchAgent](evidence.md#p064) | 自动化漏洞修复 | — | [D4](#d4) [D5](#d5) |
| P065 | [BugAuditor](evidence.md#p065) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) |
| P066 | [Bulbasaur](evidence.md#p066) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P067 | [Firmenstein](evidence.md#p067) | 动态安全测试 | — | [D2](#d2) [D4](#d4) [D5](#d5) |
| P068 | [SIGMERGE](evidence.md#p068) | 安全事件调查与运维处置 | — | [D1](#d1) [D4](#d4) [D5](#d5) |
| P069 | [SPAR](evidence.md#p069) | 安全规约生成与形式化验证 | 动态安全测试 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P070 | [H3Act](evidence.md#p070) | 动态安全测试 | — | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P071 | [JScamd](evidence.md#p071) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D4](#d4) [D5](#d5) |
| P072 | [PANGOLIN](evidence.md#p072) | 动态安全测试 | 程序安全分析与漏洞检测 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P073 | [PatchWeaver](evidence.md#p073) | 安全事件调查与运维处置 | 自动化漏洞修复 | [D2](#d2) [D4](#d4) [D5](#d5) |
| P074 | [BINREX](evidence.md#p074) | 程序安全分析与漏洞检测 | — | [D4](#d4) [D5](#d5) |
| P075 | [iFinder](evidence.md#p075) | 动态安全测试 | 程序安全分析与漏洞检测、漏洞复现与利用验证 | [D1](#d1) [D3](#d3) [D4](#d4) [D5](#d5) |
| P076 | [LLMxCPG](evidence.md#p076) | 程序安全分析与漏洞检测 | — | — |
| P077 | [MBFuzzer](evidence.md#p077) | 动态安全测试 | — | [D1](#d1) |
| P078 | [TORCHLIGHT](evidence.md#p078) | 安全事件调查与运维处置 | — | — |
| P079 | [PyGuard](evidence.md#p079) | 程序安全分析与漏洞检测 | — | [D1](#d1) |
| P080 | [REDOSPECTOR](evidence.md#p080) | 动态安全测试 | — | [D3](#d3) [D5](#d5) |
| P081 | [LeakHunter](evidence.md#p081) | 程序安全分析与漏洞检测 | — | [D1](#d1) [D5](#d5) |
| P082 | [Kintsugi](evidence.md#p082) | 安全事件调查与运维处置 | 自动化漏洞修复 | [D1](#d1) [D5](#d5) |
| P083 | [VulGenie](evidence.md#p083) | 程序安全分析与漏洞检测 | — | [D1](#d1) |
| P084 | [CONSET](evidence.md#p084) | 动态安全测试 | 安全规约生成与形式化验证 | [D1](#d1) [D3](#d3) [D5](#d5) |
| P085 | [AIxCC SoK](evidence.md#p085) | 评测与方法背景 | 动态安全测试、漏洞复现与利用验证、自动化漏洞修复 | — |
