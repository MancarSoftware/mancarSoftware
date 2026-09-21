<a href="README.md"><img src="assets/languages/es.png" width="120" height="44" alt="Español" /></a>
<a href="README.en.md"><img src="assets/languages/en.png" width="120" height="44" alt="English" /></a>
<a href="README.zh.md"><img src="assets/languages/zh.png" width="120" height="44" alt="简体中文" /></a>
<a href="README.hi.md"><img src="assets/languages/hi.png" width="120" height="44" alt="हिन्दी" /></a>

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-studio-cover-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-studio-cover.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-studio-cover-mobile.gif" />
  <img src="assets/zh/mancar-studio-cover.gif" width="100%" alt="MANCAR SOFTWARE · 独立工作室 / 厄瓜多尔 · 以人为本 · 服务于人。 · 为真实工作 · 而创造。 · 策略 / 设计 / 开发 / 支持 · 由您的业务决定方向。 · 策略。 · 设计。 · 开发。 · 支持。" />
</picture>

# Mancar Software

我们将策略、设计与开发相结合，帮助企业建立信任、简化日常工作，并为未来做好准备。我们位于厄瓜多尔瓜亚基尔，从初次沟通到产品上线和持续支持，始终与企业负责人直接合作。

<a href="#selected-projects"><img src="assets/zh/buttons/selected-projects.png" width="110" height="44" alt="精选项目" /></a>
<a href="#how-we-work"><img src="assets/zh/buttons/our-approach.png" width="110" height="44" alt="合作方式" /></a>
<a href="#the-people-behind-mancar"><img src="assets/zh/buttons/our-team.png" width="124" height="44" alt="我们的团队" /></a>
<a href="#beyond-launch"><img src="assets/zh/buttons/support.png" width="82" height="44" alt="支持" /></a>
<a href="#start-a-conversation"><img src="assets/zh/buttons/contact.png" width="82" height="44" alt="联系" /></a>



<a id="selected-projects"></a>

## 精选项目

<a href="#odontocare"><img src="assets/zh/buttons/01-odontocare.png" width="166" height="44" alt="01 / OdontoCare" /></a>
<a href="#vetcare"><img src="assets/zh/buttons/02-vetcare-pro.png" width="164" height="44" alt="02 / VetCare Pro" /></a>
<a href="#almavet"><img src="assets/zh/buttons/03-alma-vet.png" width="144" height="44" alt="03 / Alma Vet" /></a>
<a href="#casanativa"><img src="assets/zh/buttons/04-casa-nativa.png" width="161" height="44" alt="04 / Casa Nativa" /></a>

### <a id="odontocare"></a>01 / OdontoCare

<a href="https://github.com/MancarSoftware/odonto_care">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/project-odontocare-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/project-odontocare.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/project-odontocare-mobile.gif" />
  <img src="assets/zh/project-odontocare.gif" width="100%" alt="01 / 牙科诊所软件 · 每位患者。 · 全面了解。 · 01  打开档案 · 02  查看病史 · 03  安排下次就诊 · 一份档案汇集诊疗与行政信息。 · 仓库预览 / 演示 · 历次就诊的完整病史。 · 清晰的每日预约安排。 · 01 / 打开档案 · 仓库界面 / 演示内容 · 02 / 查看病史 · 03 / 安排下次就诊" />
</picture>
</a>

一款支持离线使用的 Windows 应用，用于管理患者档案、预约、治疗和付款。

<sub>来自代码仓库的界面截图 · 虚构临床数据 · 原始界面为西班牙语</sub>

<a href="../docs/PROJECT-GALLERY.zh.md#odontocare"><img src="assets/zh/buttons/view-the-still-image-tour.png" width="138" height="44" alt="查看界面截图" /></a>
<a href="https://github.com/MancarSoftware/odonto_care"><img src="assets/zh/buttons/explore-the-repository.png" width="138" height="44" alt="查看代码仓库" /></a>

**适用对象：** 希望集中管理诊疗和行政工作的牙科诊所。

**核心功能：** 病史、预约、牙位图、治疗、付款、库存和报表。文档中的流程还涵盖用户角色、审计记录、备份与恢复。

**技术栈：** Electron、React、TypeScript、NestJS、PostgreSQL 和 Prisma。

<details>
<summary>部署与技术详情</summary>

应用可安装于 Windows，采用本地 PostgreSQL 存储。正式安装程序管理所需服务，使诊所能够离线工作。仓库文档说明了关键流程、打包、备份恢复和安装的验证步骤。

</details>

<a href="https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md"><img src="assets/zh/buttons/read-the-user-guide.png" width="138" height="44" alt="阅读用户指南" /></a>
<a href="https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md"><img src="assets/zh/buttons/review-the-release-checklist.png" width="152" height="44" alt="查看发布检查表" /></a>

<details>
<summary>功能聚焦：临床病史</summary>

**回顾每次就诊的诊疗记录。**

<img src="assets/captures/odontocare-still-02.png" width="100%" alt="OdontoCare: 临床病史. 代码仓库中的原始界面，使用演示内容。" />

病史视图集中展示患者此前的临床记录，帮助团队在记录新一次就诊之前回顾既往诊疗。

</details>

### <a id="vetcare"></a>02 / VetCare Pro

<a href="https://github.com/MancarSoftware/vetCarePro">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/project-vetcare-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/project-vetcare.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/project-vetcare-mobile.gif" />
  <img src="assets/zh/project-vetcare.gif" width="100%" alt="02 / 兽医桌面软件 · 诊疗互联。 · 完整病历。 · 01  查看档案 · 02  追踪病史 · 03  记录就诊 · 一份档案关联宠物与主人。 · 仓库预览 / 演示 · 保留历次就诊的临床信息。 · 结构化流程记录诊疗。 · 01 / 查看档案 · 仓库界面 / 演示内容 · 02 / 追踪病史 · 03 / 记录就诊" />
</picture>
</a>

适用于单机和局域网环境的兽医诊所软件，诊所内可共享病历、日程和付款信息。

<sub>来自代码仓库的界面截图 · 虚构临床数据 · 原始界面为西班牙语</sub>

<a href="../docs/PROJECT-GALLERY.zh.md#vetcare-pro"><img src="assets/zh/buttons/view-the-still-image-tour.png" width="138" height="44" alt="查看界面截图" /></a>
<a href="https://github.com/MancarSoftware/vetCarePro"><img src="assets/zh/buttons/explore-the-repository.png" width="138" height="44" alt="查看代码仓库" /></a>

**适用对象：** 在同一诊所内使用一台或多台电脑的兽医团队。

**核心功能：** 患者档案、病史、预约、疫苗接种、治疗、影像和付款。局域网支持让前台、兽医和收款人员访问同一系统。

**技术栈：** Electron、Node.js 和 PostgreSQL。

<details>
<summary>部署与技术详情</summary>

在 Windows 上支持单机、局域网服务器和客户端模式。一台电脑托管本地服务和数据，其他电脑通过诊所网络连接。此本地工作流程无需互联网。仓库提供安装、网络配置和备份指南。

</details>

<a href="https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md"><img src="assets/zh/buttons/review-the-lan-test-plan.png" width="180" height="44" alt="查看局域网测试计划" /></a>
<a href="https://github.com/MancarSoftware/vetCarePro#readme"><img src="assets/zh/buttons/read-the-setup-guide.png" width="138" height="44" alt="阅读安装指南" /></a>

<details>
<summary>功能聚焦：共享临床信息</summary>

**让病历成为诊疗的核心。**

<img src="assets/captures/vetcare-still-02.png" width="100%" alt="VetCare Pro: 共享临床信息. 代码仓库中的原始界面，使用演示内容。" />

病史视图保留历次就诊的信息。在文档所述的局域网配置中，诊所电脑共享相同的本地服务与数据。

</details>

### <a id="almavet"></a>03 / Alma Vet

<a href="https://github.com/MancarSoftware/veterinaria">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/project-almavet-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/project-almavet.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/project-almavet-mobile.gif" />
  <img src="assets/zh/project-almavet.gif" width="100%" alt="03 / 兽医诊所网站 · 从发现 · 到申请诊疗。 · 01  了解诊所 · 02  查看服务 · 03  申请预约 · 清晰介绍诊所及其诊疗方式。 · 仓库预览 / 演示 · 围绕常见诊疗需求组织服务。 · 供诊所审核的结构化申请。 · 01 / 了解诊所 · 仓库界面 / 演示内容 · 02 / 查看服务 · 03 / 申请预约" />
</picture>
</a>

一个兽医诊所网站，引导宠物主人了解服务并提交信息完整的预约申请。

<sub>来自代码仓库的界面截图 · 演示内容 · 原始界面为西班牙语</sub>

<a href="../docs/PROJECT-GALLERY.zh.md#alma-vet"><img src="assets/zh/buttons/view-the-still-image-tour.png" width="138" height="44" alt="查看界面截图" /></a>
<a href="https://github.com/MancarSoftware/veterinaria"><img src="assets/zh/buttons/explore-the-repository.png" width="138" height="44" alt="查看代码仓库" /></a>

**适用对象：** Alma Vet 诊所及为宠物申请诊疗服务的主人。

**核心功能：** 服务浏览和结构化预约申请，配合服务端验证、机器人防护、申请持久化存储与邮件通知。每份申请均需审核，不会自动确认预约。

**技术栈：** React、Supabase、PostgreSQL、Cloudflare Turnstile 和 Resend。

<a href="https://github.com/MancarSoftware/veterinaria#readme"><img src="assets/zh/buttons/read-the-architecture-and-setup-guide.png" width="152" height="44" alt="架构与安装指南" /></a>

<details>
<summary>功能聚焦：预约申请</summary>

**提前向诊所提供有用信息。**

<img src="assets/captures/almavet-still-03.png" width="100%" alt="Alma Vet: 预约申请. 代码仓库中的原始界面，使用演示内容。" />

申请表收集诊所审核就诊申请所需的信息。提交表单仅代表申请诊疗，不代表预约已确认。

</details>

### <a id="casanativa"></a>04 / Casa Nativa

<a href="https://github.com/MancarSoftware/muebleria">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/project-casanativa-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/project-casanativa.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/project-casanativa-mobile.gif" />
  <img src="assets/zh/project-casanativa.gif" width="100%" alt="04 / 家具商店与数字目录 · 找到心仪家具。 · 为它留出空间。 · 01  了解 · 02  浏览目录 · 03  查看详情 · 04  保存选择 · 精心呈现家具系列。 · 仓库预览 / 演示 · 按类别和价格整理家具。 · 结合场景查看材质、尺寸和颜色。 · 保存心仪之选，方便咨询。 · 01 / 了解 · 仓库界面 / 演示内容 · 02 / 浏览目录 · 03 / 查看详情 · 04 / 保存选择" />
</picture>
</a>

家具零售网站，提供可编辑目录、颜色选项和结构化客户咨询流程。

<sub>来自代码仓库的界面截图 · 演示内容 · 原始界面为西班牙语</sub>

<a href="../docs/PROJECT-GALLERY.zh.md#casa-nativa"><img src="assets/zh/buttons/view-the-still-image-tour.png" width="138" height="44" alt="查看界面截图" /></a>
<a href="https://github.com/MancarSoftware/muebleria"><img src="assets/zh/buttons/explore-the-repository.png" width="138" height="44" alt="查看代码仓库" /></a>

**适用对象：** Casa Nativa 及为家居选购家具的客户。

**核心功能：** 包含产品图片和颜色选项的家具目录、产品发布管理区，以及空间方案和客户咨询工具。

**技术栈：** React、TypeScript、Vite 和 Supabase。

<a href="https://github.com/MancarSoftware/muebleria#readme"><img src="assets/zh/buttons/read-the-catalog-and-administration-guide.png" width="152" height="44" alt="目录与管理指南" /></a>

<details>
<summary>功能聚焦：已保存的精选</summary>

**汇集心仪之选。**

<img src="assets/captures/casanativa-still-04.png" width="100%" alt="Casa Nativa: 已保存的选择. 代码仓库中的原始界面，使用演示内容。" />

“Mi espacio”（我的空间）汇集已选家具，方便客户在咨询前查看自己的选择。

</details>

<a id="when-to-bring-us-in"></a>

## 何时与我们合作

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-starting-points-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-starting-points.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-starting-points-mobile.gif" />
  <img src="assets/zh/mancar-starting-points.gif" width="100%" alt="何时合作 / 您的起点 · 什么需要 · 变得更好？ · 01 · 新的起点 · 您正在启动业务或推出新服务。 · 让体验更清晰。 · 02 · 手动工作太多 · 团队重复操作，或在工具之间搬运信息。 · 连接工作流程。 · 03 · 有潜力的产品 · 现有产品需要更清晰、更实用的体验。 · 改进关键之处。 · 04 · 下一阶段 · 业务变化时，产品也需要维护。 · 持续向前。" />
</picture>

无论您正在启动新业务、被重复工作占用太多时间、改进现有产品，还是寻找持续技术支持，我们都会从实际情况出发，一起确定有价值的下一步。

<a href="#start-a-conversation"><img src="assets/zh/buttons/discuss-your-project.png" width="138" height="44" alt="聊聊您的项目" /></a>

<a id="the-people-behind-mancar"></a>

## Mancar 背后的团队

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-team-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-team.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-team-mobile.gif" />
  <img src="assets/zh/mancar-team.gif" width="100%" alt="走进 MANCAR / 团队 · 各有所长。 · 共同标准。 · AM · Alejandro Mantilla · 全栈开发 · 连接架构、开发与用户体验。 · REACT / NEXT.JS / NODE.JS / UI/UX · JM · Jeremy Macias · 前端开发 · 围绕真实业务流程构建清晰、无障碍的界面。 · REACT / TAILWIND CSS / 无障碍 · 后端与自动化 · 后端团队整合 API、数据库、安全与自动化，使产品易于维护。" />
</picture>

Mancar 汇聚全栈开发、前端设计实现和后端工程能力。Alejandro Mantilla 将技术架构与用户体验相连；Jeremy Macias 将业务流程转化为清晰、易用且无障碍的界面。后端团队开发支撑产品的服务和自动化功能。

<a href="https://ale-mancar.github.io/mancar_software/sobre-nosotros/#equipo"><img src="assets/zh/buttons/meet-the-team.png" width="110" height="44" alt="认识团队" /></a>

<a id="what-we-bring-together"></a>

## 汇聚专业能力

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-disciplines-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-disciplines.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-disciplines-mobile.gif" />
  <img src="assets/zh/mancar-disciplines.gif" width="100%" alt="MANCAR / 专业协同 · 不同专长。 · 成就用心打造的产品。 · 用户体验与界面设计 · 明确下一步。 · 前端 · 让体验生动呈现。 · 后端 · 连接数据与业务规则。 · 自动化 · 减少重复工作。 · 支持 · 推动产品持续进步。 · 您的 · 产品" />
</picture>

用户体验与界面设计、前端开发、后端工程、自动化和支持服务共同服务于一个目标：让产品适合业务，也让使用者容易理解。我们按项目需要整合专业能力，使体验与技术决策相互衔接。

<a id="how-we-work"></a>

## 我们的工作方式

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-approach-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-approach.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-approach-mobile.gif" />
  <img src="assets/zh/mancar-approach.gif" width="100%" alt="02 / 我们如何协作 · 步骤清晰。 · 直接协作。 · 1 · 了解 · 了解业务及其优先事项。 · 2 · 确定 · 商定范围、交付内容与时间。 · 3 · 构建 · 围绕实际流程设计与开发。 · 4 · 迭代 · 上线、支持并改进产品。 · 业务优先，技术服务于目标。" />
</picture>

开发前先商定范围、优先级和时间安排，再按清晰可见的阶段推进。设计质量、性能、安全性和可维护性贯穿上线及后续维护。

我们根据工作流程选择技术，在需要持续运行时采用本地或局域网方案。

<a href="https://ale-mancar.github.io/mancar_software/sobre-nosotros/"><img src="assets/zh/buttons/read-about-mancar.png" width="135" height="44" alt="了解 Mancar" /></a>

<a id="in-focus-casa-nativa"></a>

## 项目详解：Casa Nativa

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-casa-story-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-casa-story.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-casa-story-mobile.gif" />
  <img src="assets/zh/mancar-casa-story.gif" width="100%" alt="项目聚焦 / CASA NATIVA · 从发现 · 到深思熟虑的选择。 · 01 / 探索 · 02 / 评估 · 03 / 收藏 · 找到起点。 · 类别与价格筛选帮助客户缩小范围，找到所需。 · 真实界面 / 仓库演示内容 · 看看家具是否合适。 · 产品页集中展示图片、尺寸、材质和颜色选项。 · 保存可能之选。 · 保存功能让客户在咨询前汇集已选家具。" />
</picture>

家具客户需要的不只是产品名称，还需要足够的信息来判断家具是否适合自己的家。Casa Nativa 将浏览、产品信息和已保存的选择整合为连贯体验。

**客户任务：** 缩小选择范围，了解家具是否适合空间。

**界面设计决策：** 将图片与尺寸、材质和颜色选项放在一起，并通过目录筛选帮助发现产品。

**实现的功能：** 客户可以浏览目录、查看产品，并在咨询前将家具保存到“Mi espacio”。

<sub>来自代码仓库的界面截图 · 演示内容 · 原始界面为西班牙语</sub>

<a href="../docs/PROJECT-GALLERY.zh.md#casa-nativa"><img src="assets/zh/buttons/explore-the-screens.png" width="110" height="44" alt="查看界面" /></a>
<a href="https://github.com/MancarSoftware/muebleria"><img src="assets/zh/buttons/view-the-project.png" width="110" height="44" alt="查看项目" /></a>

<a id="beyond-launch"></a>

## 上线之后

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-support-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-support.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-support-mobile.gif" />
  <img src="assets/zh/mancar-support.gif" width="100%" alt="上线之后 / 支持与维护 · 上线是一个里程碑。 · 工作仍在继续。 · 维护 · 为产品服务 · 诊断 · 可用性、性能与可见错误。 · 更新、安全改进与备份。 · 优化 · 表单、内容与针对性功能改进。 · 诊断问题，商定下一步。" />
</picture>

业务变化时，产品也需要持续关注。我们的支持涵盖可用性与性能问题、表单提交与邮件送达、更新、备份，以及内容或功能的针对性改进。

改动前先了解情况，优先处理影响销售、表单或可用性的问题。诊断后再商定处理范围与后续步骤。

**支持时间：** 周一至周五，厄瓜多尔时间 9:00–18:00（UTC−5）。

<a href="https://ale-mancar.github.io/mancar_software/soporte/"><img src="assets/zh/buttons/explore-support-options.png" width="138" height="44" alt="了解支持服务" /></a>
<a href="mailto:mancarsoftwares@gmail.com"><img src="assets/zh/buttons/email-mancar.png" width="110" height="44" alt="发送邮件" /></a>

<a id="what-happens-after-you-contact-us"></a>

## 联系我们之后会怎样？

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-first-conversation-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-first-conversation.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-first-conversation-mobile.gif" />
  <img src="assets/zh/mancar-first-conversation.gif" width="100%" alt="开始合作 / 三个清晰步骤 · 带来您的实际情况。 · 我们来规划下一步。 · 1 · 介绍您的工作 · 介绍业务、挑战和希望改进的事项。 · 2 · 梳理优先事项 · 讨论人员、现有工具、限制与范围。 · 3 · 明确方案 · 商定交付内容、时间与可行方法。" />
</picture>

请带来一个业务挑战、现有产品，或希望改进事项的简单示例。我们将据此评估工作并制定切实可行的方案。

<a id="working-with-us"></a>

## 与我们合作

<details>
<summary>能否改进现有产品？</summary>

可以。我们会先了解当前体验、工作流程和技术情况，再建议有针对性的改进。

</details>

<details>
<summary>联系前需要准备什么？</summary>

简要介绍业务、希望解决的问题和优先事项即可开始。如有现有产品或示例，也可以一并提供；无需准备技术规格说明。

</details>

<details>
<summary>如何安排持续支持？</summary>

我们先评估问题及其影响，再商定处理方式和后续步骤。支持可涵盖可用性、性能、表单、更新、备份或针对性改进。请联系我们，讨论产品所需的支持范围。

</details>

<a id="start-a-conversation"></a>

## 开启对话

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/zh/mancar-contact-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/zh/mancar-contact.png" />
  <source media="(max-width: 600px)" srcset="assets/zh/mancar-contact-mobile.gif" />
  <img src="assets/zh/mancar-contact.gif" width="100%" alt="MANCAR SOFTWARE / 您的下一篇章 · 还有什么 · 可以更好？ · 聊聊您的工作。 · 一起确定下一步。" />
</picture>


<a href="mailto:mancarsoftwares@gmail.com"><img src="assets/zh/buttons/mancarsoftwares-gmail-com.png" width="250" height="44" alt="mancarsoftwares@gmail.com" /></a>
<a href="tel:+593986951419"><img src="assets/zh/buttons/593-98-695-1419.png" width="172" height="44" alt="+593 98 695 1419" /></a>
<a href="https://ale-mancar.github.io/mancar_software/"><img src="assets/zh/buttons/visit-mancar-software.png" width="198" height="44" alt="访问 Mancar Software" /></a>

<sub>MANCAR SOFTWARE · 厄瓜多尔瓜亚基尔</sub>
