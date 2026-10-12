#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build the Markdown indexes from the curated corpus (Python standard library only)."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
VENUES = ['CCS', 'NDSS', 'IEEE S&P', 'USENIX Security']


def load_data():
    corpus = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    taxonomy = json.loads((ROOT / 'data/taxonomy.json').read_text(encoding='utf-8'))
    papers = corpus['papers']
    categories = {item['id']: item for item in taxonomy['categories']}
    designs = {item['id']: item for item in taxonomy['designs']}
    seen_ids, seen_titles, seen_urls = set(), set(), set()
    for paper in papers:
        label = paper.get('id', '<missing ID>')
        for field in ('id', 'title', 'short_name', 'url', 'venue', 'role', 'acceptance_url',
                      'acceptance_status', 'acceptance_label', 'bottleneck', 'mechanism', 'limitations'):
            if not isinstance(paper.get(field), str) or not paper[field].strip():
                raise ValueError(f'{label}: missing or empty {field}')
        if not re.fullmatch(r'P\d{3,}', label):
            raise ValueError(f'Invalid paper ID: {label}')
        title = re.sub(r'\W+', '', paper['title']).casefold()
        for value, seen, field in ((label, seen_ids, 'ID'), (title, seen_titles, 'title'),
                                   (paper['url'], seen_urls, 'paper URL')):
            if value in seen:
                raise ValueError(f'{label}: duplicate {field}')
            seen.add(value)
        for field in ('url', 'acceptance_url'):
            url = urlsplit(paper[field])
            if url.scheme != 'https' or not url.netloc or any(c.isspace() for c in paper[field]):
                raise ValueError(f'{label}: invalid {field}')
        if paper['category'] not in categories or paper['role'] not in taxonomy['roles']:
            raise ValueError(f'{label}: unknown category or role')
        if paper['venue'] not in VENUES or not isinstance(paper['year'], int):
            raise ValueError(f'{label}: invalid venue or year')
        for field, allowed in (('related_tasks', categories), ('designs', designs)):
            if not isinstance(paper[field], list) or len(paper[field]) != len(set(paper[field])):
                raise ValueError(f'{label}: invalid or duplicate {field}')
            if any(value not in allowed for value in paper[field]):
                raise ValueError(f'{label}: unknown {field}')
        if paper['category'] in paper['related_tasks']:
            raise ValueError(f'{label}: primary category repeated as a related task')
        if paper['acceptance_status'] not in ('conference-listed', 'author-confirmed'):
            raise ValueError(f'{label}: invalid acceptance status')
        if paper['year'] == 2027 and paper['acceptance_status'] != 'author-confirmed':
            raise ValueError(f'{label}: the 2026-10-12 snapshot uses author confirmation for 2027')
    # Keep the immutable source snapshot and its stable IDs available for auditing.
    source = (ROOT / 'docs/source-corpus.md').read_text(encoding='utf-8')
    source_rows = [line for line in source.splitlines() if line.startswith('| [')]
    if len(source_rows) != corpus['source_count']:
        raise ValueError('Original source count changed')
    by_id = {paper['id']: paper for paper in papers}
    for number in range(1, corpus['source_count'] + 1):
        if f'P{number:03}' not in by_id:
            raise ValueError(f'Original corpus ID P{number:03} is missing')
    return corpus, taxonomy


def md_cell(text):
    return text.replace('|', '\\|').replace('\n', ' ')


def evidence_link(paper, prefix=''):
    return f"[{paper['short_name']}]({prefix}evidence.md#{paper['id'].lower()})"


def venue_label(paper):
    suffix = ' · 作者/机构确认录用' if paper['acceptance_status'] == 'author-confirmed' else ''
    return f"{paper['venue']} {paper['year']}{suffix}"


def build_readme(corpus, taxonomy):
    papers = corpus['papers']
    counts = Counter(p['category'] for p in papers)
    roles = Counter(p['role'] for p in papers)
    lines = [
        '# Awesome Agentic Systems for Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)',
        '',
        '> A curated collection of research papers on agentic systems for security, organized by security tasks and aligned with our SoK.',
        '',
        '**Agentic System 如何解决传统安全技术面临的困难？** 本仓库整理 LLM 与安全工具结合的研究，覆盖漏洞检测、动态测试、漏洞复现、形式化验证、漏洞修复、渗透测试与安全运维。',
        '',
        f"收录 **{len(papers)} 篇**，文献快照截至 **{corpus['snapshot_date']}**。以 2025–2026 年安全四大会议为主，补充 2 篇作者或机构确认录用的 2027 年论文。",
        '',
        f"文献属性：**{roles['研究系统与反馈流程']} 项研究系统与反馈流程 · {roles['边界对照']} 项边界对照 · {roles['评测与方法背景']} 项评测与方法背景**。这些属性沿用原始文献附表；系统的控制方式和反馈阶段见逐篇分析。",
        '',
        '[SoK 全文](docs/sok.md) · [逐篇证据与局限](docs/evidence.md) · [任务与技术设计映射](docs/mapping.md) · [按会议与年份浏览](docs/venues.md) · [数据](data/papers.json) · [贡献指南](CONTRIBUTING.md)',
        '',
        '## Contents',
        '',
    ]
    for category in taxonomy['categories']:
        lines.append(f"- [{category['name']} · {category['english']}](#{category['id']})（{counts[category['id']]}）")
    lines += ['- [Scope and Organization](#scope-and-organization)',
              '- [Contributing](#contributing)', '- [License](#license)', '',
              '## Scope and Organization', '',
              '一级目录对应 SoK 第 2 节的七类安全任务，跨任务研究按主要产出归类；相邻主题及评测背景单列。每篇论文只在首页出现一次，关联任务和五项技术设计可在[映射表](docs/mapping.md)中交叉检索。', '',
              '原附表通过会议名单、作者页面和公开全文核对录用与技术内容。本次仓库整理保留其标题、来源、机制和局限，并新增任务分类与 SoK 映射。详细检索口径与未纳入候选见[来源说明](docs/provenance.md)。', '',
              '条目按年份降序、同年标题字母序排列。**研究系统**包含固定反馈流程；**边界对照**用于比较模型辅助方法；**评测背景**用于讨论评价方法。标签不表示自主程度或实验强弱。', '']
    short_roles = {'研究系统与反馈流程': '研究系统', '边界对照': '边界对照', '评测与方法背景': '评测背景'}
    for category in taxonomy['categories']:
        lines += [f'<a id="{category["id"]}"></a>', '',
                  f"## {category['name']} · {category['english']}", '', category['description'], '']
        group = sorted((p for p in papers if p['category'] == category['id']),
                       key=lambda p: (-p['year'], p['title'].casefold()))
        for paper in group:
            alias = f"（{paper['short_name']}）" if paper['short_name'].casefold() not in paper['title'].casefold() else ''
            lines += [f"- **[{paper['title']}]({paper['url']})**{alias} · {venue_label(paper)} · `{short_roles[paper['role']]}` · [录用依据]({paper['acceptance_url']}) · [分析](docs/evidence.md#{paper['id'].lower()})",
                      f"  {paper['mechanism']}", '']
    lines += ['## Contributing', '',
              '欢迎通过 Issue 或 Pull Request 补充论文、修正分类和报告链接问题。请同时提供全文、录用依据，以及与具体安全任务的关系。更新方式见[贡献指南](CONTRIBUTING.md)。', '',
              '## License', '',
              '文献整理、分类与原创说明采用 [CC BY 4.0](LICENSE)。构建脚本采用 [MIT](scripts/LICENSE)。被引用论文与第三方材料保留各自的版权和许可证。', '']
    return '\n'.join(lines)


def build_evidence(corpus, taxonomy):
    categories = {c['id']: c['name'] for c in taxonomy['categories']}
    designs = {d['id']: d['name'] for d in taxonomy['designs']}
    lines = ['# 逐篇证据与局限', '', '[返回首页](../README.md) · [SoK 映射](mapping.md) · [来源说明](provenance.md)', '',
             '瓶颈、机制与局限原样保留自文献附表；任务和设计标签是本仓库新增的编辑分类。原始顺序决定稳定编号，后续新增论文继续递增编号。', '']
    for paper in corpus['papers']:
        tags = '、'.join(f"[{tag} · {designs[tag]}](mapping.md#{tag.lower()})" for tag in paper['designs']) or '未强行映射到五项技术设计'
        related = '、'.join(categories[c] for c in paper['related_tasks']) or '—'
        lines += [f'<a id="{paper["id"].lower()}"></a>', '', f"## {paper['id']} · {paper['short_name']}", '',
                  f"**[{paper['title']}]({paper['url']})**", '',
                  f"{venue_label(paper)} · {paper['role']} · [录用依据]({paper['acceptance_url']})", '',
                  f"- **主分类：** {categories[paper['category']]}",
                  f'- **关联任务：** {related}', f'- **技术设计：** {tags}', '',
                  f"**具体瓶颈。** {paper['bottleneck']}", '',
                  f"**技术机制。** {paper['mechanism']}", '',
                  f"**结果解释与局限。** {paper['limitations']}", '']
    return '\n'.join(lines)


def build_mapping(corpus, taxonomy):
    papers = corpus['papers']
    categories = {c['id']: c['name'] for c in taxonomy['categories']}
    lines = ['# SoK 分类与文献映射', '', '[返回首页](../README.md) · [SoK 全文](sok.md) · [逐篇分析](evidence.md)', '',
             '## 与正文结构对应', '',
             '| SoK 部分 | 本仓库入口 |', '| --- | --- |',
             '| [1 研究范围与文献检索](sok.md#sok-1) | [来源与筛选口径](provenance.md)、[会议索引](venues.md) |',
             '| [2 传统安全任务及其技术挑战](sok.md#sok-2) | 首页七类任务，另列相邻主题与评测背景 |',
             '| [3 关键技术设计](sok.md#sok-3) | 下文 D1–D5 跨任务索引 |',
             '| [4 实验设计与有效性评估](sok.md#sok-4) | 逐篇分析的“结果解释与局限” |',
             '| [5 技术贡献与发展方向](sok.md#sok-5) | 结合机制、验证条件和局限归纳贡献 |', '',
             '## 分类规则', '',
             '主分类按研究的主要任务目标确定，每篇只计数一次。`related_tasks` 记录次要任务，`designs` 允许多选。两类交叉标签都不用于计算论文总数。文献属性沿用原附表，独立于任务类别。', '',
             '边界条目的处理：LinkDiff 按补丁完整性审计归入修复，LLMBisect 按根因定位支撑归入修复，Kintsugi 按运行时缓解归入运维；SelfOp 按已评估的 CyberGym 漏洞复现任务归类。Chimera 支撑事件检测评估，列在安全事件类。硬件 IP、汽车风险建模与隐私合规等列入相邻主题。', '',
             '技术标签表示与 SoK 讨论维度的对应关系，既可用于主体系统，也可用于比较方法或评测。D4 包含固定流程中的反馈修正、证据获取和离线技能改进；D5 包含不同强度的工具检查和日志证据核对。具体控制权、发生阶段和验证强度以逐篇机制与局限为准。空标签表示不强行套入五项设计。', '',
             '## 按技术设计查阅', '']
    for design in taxonomy['designs']:
        lines += [f'<a id="{design["id"].lower()}"></a>', '', f"### {design['id']} · {design['name']}", '',
                  f"[SoK §{design['sok_section']}](sok.md#sok-{design['id'].lower()}) · {design['english']}", '', design['description'], '',
                  '、'.join(evidence_link(p) for p in papers if design['id'] in p['designs']), '']
    lines += ['## 完整映射', '', '| 编号 | 论文 / 系统 | 主分类 | 关联任务 | 技术设计 |', '| --- | --- | --- | --- | --- |']
    for paper in papers:
        related = '、'.join(categories[c] for c in paper['related_tasks']) or '—'
        tags = ' '.join(f'[{d}](#{d.lower()})' for d in paper['designs']) or '—'
        lines.append(f"| {paper['id']} | {md_cell(evidence_link(paper))} | {categories[paper['category']]} | {related} | {tags} |")
    return '\n'.join(lines) + '\n'


def build_venues(corpus):
    papers = corpus['papers']
    years = sorted({p['year'] for p in papers})
    lines = ['# 按会议与年份浏览', '', '[返回首页](../README.md) · [来源说明](provenance.md)', '',
             '| 会议 | ' + ' | '.join(map(str, years)) + ' | 合计 |',
             '| --- | ' + ' | '.join('---:' for _ in years) + ' | ---: |']
    for venue in VENUES:
        counts = [sum(p['venue'] == venue and p['year'] == year for p in papers) for year in years]
        lines.append('| ' + venue + ' | ' + ' | '.join(map(str, counts)) + f' | {sum(counts)} |')
    lines.append('| 合计 | ' + ' | '.join(str(sum(p['year'] == y for p in papers)) for y in years) + f' | {len(papers)} |')
    lines += ['', '2027 年条目按作者或机构确认录用单独标识；该快照不覆盖完整年度。', '']
    for venue in VENUES:
        lines += [f'## {venue}', '']
        for year in reversed(years):
            group = sorted((p for p in papers if p['venue'] == venue and p['year'] == year), key=lambda p: p['title'].casefold())
            if group:
                lines += [f'### {year}', '']
                lines += [f"- {evidence_link(p)} — [{p['title']}]({p['url']}) · {p['role']}" for p in group]
                lines.append('')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate data and check that generated files are current.')
    args = parser.parse_args()
    corpus, taxonomy = load_data()
    outputs = {
        'README.md': build_readme(corpus, taxonomy),
        'docs/evidence.md': build_evidence(corpus, taxonomy),
        'docs/mapping.md': build_mapping(corpus, taxonomy),
        'docs/venues.md': build_venues(corpus),
    }
    stale = []
    for filename, text in outputs.items():
        path = ROOT / filename
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                stale.append(filename)
        else:
            path.write_text(text, encoding='utf-8')
    if stale:
        raise SystemExit('Run python3 scripts/build.py to update: ' + ', '.join(stale))
    print(f"{'Checked' if args.check else 'Built'} {len(corpus['papers'])} papers and {len(outputs)} Markdown indexes.")


if __name__ == '__main__':
    main()
