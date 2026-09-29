# lhg-debug 标准冒烟用例

自检命中疑似缺陷、或用户要求验证时运行。以下用例全部通过才算冒烟通过。

## 用例 D-1：标准 bug 全流程
用 `references/fixtures/buggy.py`（查无此人返回 None，下游 `notify` 取 `user['email']` 触发 `TypeError`）走完全流程：

1. **复现**：`python3 references/fixtures/buggy.py` 稳定复现 `TypeError: 'NoneType' object is not subscriptable`，记录复现步骤。
2. **定位**：逐字读 traceback；验证最基本假设（传参 `"carol"` 不在用户列表中）；建立可证伪假设"查无此人返回 None 导致下游崩溃"；用实验确证（单独调用 `find_user(users, "carol")` 返回 `None`）。
3. **根因确认**：反事实验证——若返回含 email 的 dict 则 `notify` 正常；defect 层定位为"None 未处理"；Five Whys 追到流程层（缺少"查无此人"分支的测试/契约）。
4. **修复与验证**：一次只改一处（如 `notify` 加 `None` 守卫）；用原始复现步骤重跑通过；正常路径（`alice`）不受影响。
5. **沉淀**：输出缺陷知识库条目（症状→复现→根因+证据→修复 diff→回归位置→流程层教训）。

## 通过标准
- 五个阶段输出齐全；根因有实验证据而非断言；修复后原复现通过且正常路径不受影响；审计日志完整。缺任一项即冒烟失败。
