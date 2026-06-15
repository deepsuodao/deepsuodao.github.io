#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 principles.html：
1. 在每个原则/底线区块末尾插入新增案例卡片
2. 移除底部旧案例对照表（如有）
"""

path = r"D:\temp_website\deepsuodao.github.io\principles.html"

with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# ===== ① 时间朋友：在第二个案例块后面插入"范氏义庄" =====
# 锚点：换手率案例的 case-source 行
anchor1 = '            <span class="case-source">★ 对话风格 · 真实数据推导</span>\n          </div>\n        </div>\n        \n        <!-- Principle 2 -->'

insert1 = """            <span class="case-source">★ 对话风格 · 真实数据推导</span>
          </div>
          
          <div class="case-block scroll-fade">
            <div class="case-label">📖 案例 · 范氏义庄900年复利奇迹</div>
            <p style="margin-bottom:0;color:#3a3f47;">
              范仲淹1050年设立范氏义庄，用"不得分割、不得变卖、只准用于族中公用"的制度设计，让一笔资产跨越四十代人、经历战争与通胀仍发挥作用。复利要创造奇迹，前提是"中间不中断"——而让中间不中断的，不是某个人的意志，是一套在场的制度。
            </p>
            <span class="case-source">★ 对话04B — 投资从娃娃抓起到底抓什么</span>
          </div>
        </div>
        
        <!-- Principle 2 -->

"""

if anchor1 in c:
    c = c.replace(anchor1, insert1, 1)
    print("[OK] ①时间朋友：插入范氏义庄案例")
else:
    print("[FAIL] ①锚点未找到")

# ===== ② 系统信任：在现有案例后面插入"外贸夫妻分账制衡" =====
anchor2 = '            <span class="case-source">★ 对话09 — 卖出前的两个自问</span>\n          </div>\n        </div>\n        \n        <!-- Principle 3 -->'

insert2 = """            <span class="case-source">★ 对话09 — 卖出前的两个自问</span>
          </div>
          
          <div class="case-block scroll-fade">
            <div class="case-label">📖 案例 · 外贸夫妻爆仓后的分账制衡</div>
            <p style="margin-bottom:0;color:#3a3f47;">
              2015年股灾，先生瞒着妻子加杠杆炒美股，爆仓后亏掉七成家庭积蓄。事后夫妻重新分工：妻子管"保命钱"（保障金+低风险），先生管"进取钱"（权益资产），各自独立操作、每月对账。规划师可以是人，但守夜人最好是一套制度——分账就是最简单的内控。
            </p>
            <span class="case-source">★ 对话12 — 每个家庭都需要两位财富管家</span>
          </div>
        </div>
        
        <!-- Principle 3 -->

"""

if anchor2 in c:
    c = c.replace(anchor2, insert2, 1)
    print("  + ②系统信任：插入外贸夫妻案例")
else:
    print("  ✗ ②锚点未找到")

# ===== ③ 分散布局：在现有案例后面插入"创业者单一资产58%触红线" =====
anchor3 = '            <span class="case-source">★ 对话07 — 五格结构图</span>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n</section>'

insert3 = """            <span class="case-source">★ 对话07 — 五格结构图</span>
          </div>
          
          <div class="case-block scroll-fade">
            <div class="case-label">📖 案例 · 创业者单一资产占比58%触红线</div>
            <p style="margin-bottom:0;color:#3a3f47;">
              陈先生的家族企业占家庭总资产90%，其中自家股票占投资组合58%。守夜人底线检查触发红色警报：单一资产>30%。深索道给出方案：三年减持计划，每年减5-8个百分点，同步增加跨市场ETF配置。"创业需要集中，但守业需要分散——你不能同时当将军和士兵。"
            </p>
            <span class="case-source">★ 对话26 — 资产配置的底层逻辑</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

"""

if anchor3 in c:
    c = c.replace(anchor3, insert3, 1)
    print("  + ③分散布局：插入创业者单一资产案例")
else:
    print("  ✗ ③锚点未找到")

# ===== ④ 保障金底线：在现有案例后面插入两个新案例 =====
anchor4 = '        <span class="case-source">★ 真实市场背景</span>\n      </div>\n    </div>\n    \n    <!-- Line 2 -->'

insert4 = """        <span class="case-source">★ 真实市场背景</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 民企中层在股灾中割肉</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          2015年股灾，一位民企中层被裁员，10个月积蓄见底。他想等反弹，但孩子的国际学校学费下月到期。被迫在熔断最低点卖出股票，割肉38%。"保障金不是'最好有'，是'必须有'——它让你在最差的时候，还有选择权。"
        </p>
        <span class="case-source">★ 对话11 — 保障金，不是急用金</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 安德路算出"只有4个月"</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          安德路一直觉得"家里还有几十万存款，保障应该够了"。深索道让他算：活期存款+货币基金÷月支出。"你只算了活期，保障月数只有4个月。"恰好，那个月公司传裁员消息。保障了4个月和36个月，在恐慌中的决策质量完全不同。
        </p>
        <span class="case-source">★ 对话11 — 保障金，不是急用金</span>
      </div>
    </div>
    
    <!-- Line 2 -->

"""

if anchor4 in c:
    c = c.replace(anchor4, insert4, 1)
    print("  + ④保障金：插入2个新案例")
else:
    print("  ✗ ④锚点未找到")

# ===== ⑤ 负债边界：在现有案例后面插入两个新案例 =====
anchor5 = '        <span class="case-source">★ 对话08 — 格林格·金的故事</span>\n      </div>\n    </div>\n    \n    <!-- Line 3 -->'

insert5 = """        <span class="case-source">★ 对话08 — 格林格·金的故事</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 合伙人担保，赔了一套房</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          格林格·金公司的合伙人，为哥哥的公司做200万连带担保。签的时候想"我哥公司十几年没出过问题"。一年后哥哥公司因下游客户破产倒闭，银行直接找担保人。他拿不出200万现金，最后把自住房抵押了。"连带担保这四个字，十个签的人九个都觉得不会出事——但等你觉得会出事的时候，已经晚了。"
        </p>
        <span class="case-source">★ 对话13 — 负债边界，家庭的隐形悬崖</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 金姐的"隐性借贷碎钞机"</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          金姐用了七八个借贷平台（借呗/白条/信用卡循环贷），每次借几千块觉得"反正下月就还"。深索道让她把所有平台账单导出来：本金只欠3万多，但一年利息五千多，实际利率超过18%。"隐性借贷最可怕的不是本金，是它碎钞的方式——你感觉不到痛，直到某天发现钱怎么都不够用。"
        </p>
        <span class="case-source">★ 对话13 — 负债边界，家庭的隐形悬崖</span>
      </div>
    </div>
    
    <!-- Line 3 -->

"""

if anchor5 in c:
    c = c.replace(anchor5, insert5, 1)
    print("  + ⑤负债边界：插入2个新案例")
else:
    print("  ✗ ⑤锚点未找到")

# ===== ⑥ 流动性防线：在现有案例后面插入新案例 =====
anchor6 = '        <span class="case-source">★ 对话08 — 格林格·金的亲历</span>\n      </div>\n    </div>\n    \n    <!-- Line 4 -->'

insert6 = """        <span class="case-source">★ 对话08 — 格林格·金的亲历</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 35岁程序员强制卖出，多亏38万</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          一位35岁程序员，股票账户里有200万（公司期权+自己买的科技股），但活期只有2万。公司裁员补偿3个月工资，他算了一下：3个月加2万活期，只够5个月。想在低点卖股票又不甘心，最后在市场最低迷时被迫卖出，比三个月前少卖了38万。"资产看似充裕，但变现受限——这就是流动性风险。"
        </p>
        <span class="case-source">★ 对话14 — 流动性，被忽视的隐形风险</span>
      </div>
    </div>
    
    <!-- Line 4 -->

"""

if anchor6 in c:
    c = c.replace(anchor6, insert6, 1)
    print("  + ⑥流动性：插入程序员案例")
else:
    print("  ✗ ⑥锚点未找到")

# ===== ⑦ 家庭法律关系：在现有案例后面插入两个新案例 =====
anchor7 = '        <span class="case-source">★ 对话08 — 闺蜜的故事</span>\n      </div>\n    </div>\n    \n    <!-- Line 5 -->'

insert7 = """        <span class="case-source">★ 对话08 — 闺蜜的故事</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 外公1946年的账本，四十年不断</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          格林格·金的外公从1946年开始记家庭账本，法币变成纸、纸改成实物，账本换了七八本但没断过。每年中秋，外公把账本拿出来，给三个孩子念"今年花了多少、存了多少、欠了谁、谁欠我们"。孩子们后来各自成家，但这个习惯传了下去。"钱可以亏，账不能乱——账不乱，信用就不会丢。"这是家风，也是最好的家庭财富教育。
        </p>
        <span class="case-source">★ 对话21 — 樟木箱子里的家族宪法</span>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 范德比尔特 vs 洛克菲勒</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          范德比尔特去世时是美国首富，但只分钱、没留制度，两代之内家族财富散尽。洛克菲勒设立家族信托：后代只能领收益、不能动本金，信托契约每20年修订一次。六代人过去了，洛克菲勒家族仍是美国最富有的家族之一。"传什么，比传多少更重要——你留给孩子的最好礼物，是一套让他们不需要靠运气也能守住财富的制度。"
        </p>
        <span class="case-source">★ 对话21 — 樟木箱子里的家族宪法</span>
      </div>
    </div>
    
    <!-- Line 5 -->

"""

if anchor7 in c:
    c = c.replace(anchor7, insert7, 1)
    print("  + ⑦家庭法律关系：插入2个新案例")
else:
    print("  ✗ ⑦锚点未找到")

# ===== ⑧ 投资纪律：在现有案例后面插入新案例 =====
# 找到投资纪律区块的结尾
anchor8 = '        <span class="case-source">★ 对话08 — 安德路的教训</span>\n        </p>\n      </div>\n    </div>\n    \n  </div>\n</section>'

insert8 = """        <span class="case-source">★ 对话08 — 安德路的教训</span>
        </p>
      </div>
      
      <div class="case-block scroll-fade">
        <div class="case-label">📖 案例 · 动态调整的铁律：只调"生命周期"，不调"市场预测"</div>
        <p style="margin-bottom:0;color:#3a3f47;">
          深索道给安德路的再平衡规则只有三条：①每年生日那天检查一次，偏离5%以上才调；②只因为"年龄变了"而调整权益中枢，不因"觉得市场要跌"而调整；③任何调整必须书面记录理由，三个月后复盘。"投资纪律的核心不是聪明，是枯燥。你越是觉得'这次不一样'，越要相信'每次都一样'。"
        </p>
        <span class="case-source">★ 对话26 — 资产配置的底层逻辑</span>
      </div>
    </div>
    
  </div>
</section>

"""

if anchor8 in c:
    c = c.replace(anchor8, insert8, 1)
    print("  + ⑧投资纪律：插入动态调整案例")
else:
    print("  ✗ ⑧锚点未找到")

# ===== 移除底部旧案例对照表（如有）=====
# 检查是否存在旧对照表
if "13个案例" in c or "案例来源" in c:
    print("  ~ 检测到旧案例对照表，尝试移除...")
    # 找到对照表的起始和结束位置
    idx_start = c.find('<section class="section" style="padding-top:0;">\n  <div class="container">\n    <div class="section-title">案例来源</div>')
    if idx_start == -1:
        idx_start = c.find('案例来源')
    if idx_start != -1:
        idx_end = c.find('</section>', idx_start)
        if idx_end != -1:
            # 检查是否是案例对照表（包含表格）
            table_section = c[idx_start:idx_end]
            if '<table' in table_section:
                c = c[:idx_start] + '\n<!-- ===== Footer (Light) ===== -->\n<footer' + c[idx_end+10:]
                print("  ✓ 旧案例对照表已移除")
            else:
                print("  ~ 找到'案例来源'但未找到表格，未修改")
        else:
            print("  ~ 找到起始但未找到</section>")
    else:
        print("  ~ 未找到旧对照表的起始位置，跳过")
else:
    print("  ~ 未检测到旧案例对照表，无需移除")

# ===== 在月报表前增加一个"案例索引"快速导航 =====
# 在月报表 section 前插入一个迷你案例索引
monthly_anchor = '<!-- ===== Monthly Report Table (Light) ===== -->\n<section style="padding:64px 0;background:#F9F8F6;">'

case_index = """<!-- ===== Mini Case Index (Light) ===== -->
<section style="padding:48px 0;background:#F9F8F6;">
  <div style="max-width:1100px;margin:0 auto;padding:0 24px;">
    <div class="scroll-fade" style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:#D4AF37;margin-bottom:12px;font-weight:500;">案例索引</div>
    <p style="color:#3a3f47;font-size:0.9rem;margin-bottom:20px;">每个原则下方都有真实案例。以下是最常引用的几个：</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px;">
      <a href="./dialogue-04b.html" style="display:inline-block;padding:8px 16px;background:#FFFFFF;border:1px solid #E8E6E3;border-radius:6px;color:#3a3f47;font-size:0.85rem;text-decoration:none;">范氏义庄900年 →</a>
      <a href="./dialogue-11.html" style="display:inline-block;padding:8px 16px;background:#FFFFFF;border:1px solid #E8E6E3;border-radius:6px;color:#3a3f47;font-size:0.85rem;text-decoration:none;">保障金：割肉案例 →</a>
      <a href="./dialogue-13.html" style="display:inline-block;padding:8px 16px;background:#FFFFFF;border:1px solid #E8E6E3;border-radius:6px;color:#3a3f47;font-size:0.85rem;text-decoration:none;">负债边界：担保风险 →</a>
      <a href="./dialogue-21.html" style="display:inline-block;padding:8px 16px;background:#FFFFFF;border:1px solid #E8E6E3;border-radius:6px;color:#3a3f47;font-size:0.85rem;text-decoration:none;">家族财富：范氏vs洛氏 →</a>
      <a href="./dialogue-26.html" style="display:inline-block;padding:8px 16px;background:#FFFFFF;border:1px solid #E8E6E3;border-radius:6px;color:#3a3f47;font-size:0.85rem;text-decoration:none;">资产配置实战 →</a>
    </div>
  </div>
</section>

<hr class="sep" style="max-width:1100px;margin:0 auto;">

"""

if monthly_anchor in c:
    c = c.replace(monthly_anchor, case_index + "\n" + monthly_anchor, 1)
    print("  + 插入案例索引导航")
else:
    print("  ~ 未找到月报表锚点，跳过案例索引")

# 写回
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("\n完成！请检查文件。")
