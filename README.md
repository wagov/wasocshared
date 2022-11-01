# wasocshared
Blob content for wasocshared site, built with [docsify](https://docsify.js.org)

Minor enhancements include a custom content router to preserve SAS container url so that a container level SAS_TOKEN can be used to easily share any content within that container.

```javascript
// This fixes tokens in urls so blob content etc works.
var patchLinking = function (hook, vm) {
    hook.beforeEach(function (markdown) {
        // workaround for stripping .md from internal urls, see https://github.com/docsifyjs/docsify/blob/v4.13.0/src/core/router/history/base.js#L74
        return markdown.replace(/(\([\w/][^):]*\.md)\)/gm, "$1.md)");
    });
};
// Docsify Configuration
window.$docsify = {
    loadSidebar: "_sidebar.md",
    loadNavbar: "_navbar.md",
    auto2top: true,
    subMaxLevel: 3,
    relativePath: true,
    ext: "", // workaround for adding .md to all links
    plugins: [patchLinking], // add plugin to docsify configuration
    alias: {
        // use alias to preserve token in url
        "/": "/README.md",
        "/([^?]*)": "/$1" + window.location.search,
    },
};
```
