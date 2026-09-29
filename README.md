# lhg-debug · 系统化调试

[English](#english) | [中文](#中文)

---

## English

**Systematic Debugging** turns debugging from a black art into an executable scientific method. No guessing, no "try this and see" — every diagnosis must be backed by experimental evidence. And the job isn't done at the fix: each bug is archived into a defect knowledge base.

### Workflow

1. **Reproduce** — make it fail reliably first. A bug you can't reproduce is a bug you can't fix. Record minimal reproduction steps (they become tomorrow's regression tests). For intermittents, find the uncontrolled condition behind them.
2. **Isolate** — hypothesis → prediction → experiment → observation, looped. Read the full error message and stack trace *word by word*; verify the dumbest assumptions first (right code? right DB? right branch?); binary-search between working and failing states (bisect versions, minimize inputs — delta-debugging thinking); change one variable at a time; keep an audit trail of everything tried.
3. **Confirm root cause** — counterfactual verification: remove the suspected cause and the failure must disappear; bring it back and it reappears. Assertion is not evidence. Run Five Whys down to the *process* layer ("no test covered this branch" is a root cause; "the variable was null" is a symptom). Fix at the defect layer, not the failure layer (Zeller's defect → infection → failure chain).
4. **Fix & verify** — one bug at a time; add a regression test (from the reproduction steps) and assertions where the infection could return. **If you didn't verify it, it ain't fixed**: re-run the original reproduction, confirm the failure is gone and nothing new broke. Stuck for 30+ minutes? Re-read the error message word by word, or explain it out loud.
5. **Archive** — every fixed bug becomes a defect knowledge-base entry: symptoms → minimal reproduction → root cause (with experimental evidence) → fix diff → regression test location → process-layer lesson. Next bug: search the base first.

### Output

Minimal reproduction steps · root cause (defect layer + experimental evidence) · fix diff + regression test · audit trail (hypotheses, experiments, observations) · knowledge-base entry.

### Compatibility

Pure process description in Markdown — no dependency on any specific agent platform. Portable to any environment that supports Markdown instructions (Claude Code, Codex, Doubao, Workbuddy, etc.).

### Operating principles

- No code changes without reproduction; never change more than one variable at a time.
- Every root-cause claim needs experimental backing.
- The audit trail and knowledge-base entry are deliverables, not optional.

### Theoretical grounding

Zeller, *Why Programs Fail* (2nd ed. 2009); delta debugging (Zeller 1999; Zeller & Hildebrandt 2002); Agans, *Debugging: The 9 Indispensable Rules* (2002); Five Whys (Toyota Production System); Kernighan on debugging.

### License

MIT — see [LICENSE](LICENSE).

---

## 中文

**系统化调试**：把调试从"黑艺术"变成可执行的科学方法。不靠猜、不靠"试一下"，每个诊断结论都必须有实验证据；修完不走人，沉淀为可复用的缺陷知识库。

### 流程

1. **复现** — 先让它稳定失败。无法复现的 bug 无法修复。记录最小复现步骤（即日后的回归测试种子）。偶发问题要找到背后的不受控条件，把"偶发"变成"可刺激"。
2. **定位** — 假设→预测→实验→观察，循环。报错信息和堆栈逐字读；先查最蠢的假设（跑的是最新代码吗？连的库对吗？分支对吗？）；在"正常"与"异常"之间二分（版本 bisect、输入最小化，delta debugging 思想）；一次只改一个变量；全程记审计日志。
3. **根因确认** — 反事实验证：去掉它故障必须消失，加回来重现；断言不算证据。Five Whys 问到**流程层**（"没有测试覆盖这个分支"是根因，"变量是 null"是现象）。按 Zeller 因果链修在 defect 层，不只擦 failure 层。
4. **修复与验证** — 一次修一个 bug；加回归测试与断言。**没验证就不算修好**：用原始复现步骤重跑。卡住 30 分钟没进展就把报错逐字重读一遍，或讲出来。
5. **沉淀** — 每个修好的 bug 落一条缺陷知识库条目：症状 → 最小复现 → 根因（带实验证据）→ 修复 diff → 回归测试位置 → 流程层教训。下次先查库再动手。

### 产出

最小复现步骤 · 根因（defect 层定位 + 实验证据）· 修复 diff + 回归测试 · 审计日志 · 缺陷知识库条目。

### 兼容性

纯流程 Markdown，不依赖任何特定平台，可移植到豆包智能体、Workbuddy 等支持 Markdown 指令的环境。

### License

MIT — 详见 [LICENSE](LICENSE)。

---

## 作者

![刘洪光](docs/avatar.png)

**刘洪光** · 安徽合肥

微信联系：

![微信二维码](docs/wechat-qr.png)
