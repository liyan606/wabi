# Wabi 静态站点仓库

## 仓库概览
本仓库包含 Wabi 官网的静态导出版本，入口 `wabi.ai/index.html` 内含完整的着陆页结构、SEO 元数据以及 TailwindCSS 打包后的样式，用于展示 "The first personal software platform is arriving soon." 等核心文案。【F:wabi.ai/index.html†L1-L1】Next.js 构建生成的运行时代码与组件被保存在 `wabi.ai/_next/static/chunks` 等目录中，例如 `page-e7f18f5caa462839.js` 中包含页面组件、动画状态与交互逻辑。【F:wabi.ai/_next/static/chunks/app/page-e7f18f5caa462839.js†L1-L4】

## 目录结构
- `wabi.ai/`：站点主体文件夹，除首页外还包含 `manifesto` 目录下的图片、音频等素材资源，以及导出的隐私政策与条款 HTML 页面。
- `cdn.usefathom.com/`：本地化保存的 Fathom Analytics 脚本，用于在离线环境复现生产站点所用的统计代码。【F:cdn.usefathom.com/script.js†L1-L1】
- `www.iubenda.com/`：Iubenda 生成的隐私政策与条款文档快照，可直接嵌入或部署为独立页面。【F:www.iubenda.com/privacy-policy/16478163.html†L1-L30】
- `translate-pa.googleapis.com/` 与 `translate.googleapis.com/`：保留了 Google 翻译返回的多语言文案数组，可用于重建本地化内容或调试多语言呈现。【F:translate-pa.googleapis.com/v1/translateHtml.html†L1-L18】
- 其他诸如 `www.gstatic.com/`、`fonts.gstatic.com/` 目录则镜像了第三方字体与脚本资源，确保在离线或封闭网络中仍能完整渲染页面。

## 本地预览
1. 安装任一静态文件服务器（如未安装可使用 `pip install --user webpreview` 或直接借助 Python 内置模块）。
2. 在仓库根目录执行 `cd wabi.ai && python -m http.server 3000`。
3. 浏览器访问 `http://localhost:3000`，即可预览页面及其静态资源。

## 部署到腾讯云 EdgeOne
1. **准备源站**：将 `wabi.ai` 目录及需要的第三方资源目录（如 Fathom、Iubenda、Google 翻译镜像等）打包上传至对象存储（推荐腾讯云 COS）或自建的静态 Web 服务器，保证 EdgeOne 能通过公网访问这些文件。
2. **创建 EdgeOne 站点**：登录腾讯云控制台，进入 EdgeOne，添加新的加速域名，选择“网站加速”类型，并指向上述源站地址或 COS 源站域名。
3. **配置回源规则**：在源站设置中启用自定义 Host（如需），并将根目录指向 `wabi.ai`，同时根据是否需要外部脚本决定是否将其他镜像目录一并上传或改写引用路径。
4. **缓存与性能优化**：在 EdgeOne 的“缓存配置”中设置静态文件的缓存策略，对 `.html`、`.js`、`.css`、`.png` 等设置合适的缓存时间；开启 Brotli/Gzip 压缩以及 HTTP/2 以提升加载速度。
5. **安全与证书**：在“证书管理”模块绑定已有的 HTTPS 证书或申请腾讯云免费证书，并在安全设置中按需启用 WAF、速率限制等功能。
6. **发布与验证**：完成配置后保存并等待下发，使用 EdgeOne 提供的调试功能或第三方测速工具确认 CDN 节点可正确返回页面，若需要绑定自有域名，别忘了在 DNS 中将域名解析到 EdgeOne 分配的 CNAME。

## 后续维护建议
- 当页面内容更新时，重新执行静态导出或替换对应文件，再触发 EdgeOne 缓存刷新即可生效。
- 若未来重新接入在线第三方资源，可将引用 URL 恢复为官方地址，减少维护本地镜像的工作量。
