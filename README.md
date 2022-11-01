# WA Cyber Security Unit Technical Content

Blob content for wasocshared site, built with [docsify](https://docsify.js.org). The [public](public) folder gets hosted at [WA Cyber Security Unit (github pages)](https://wagov.github.io/wasocshared/) and the [tlp-green](tlp-green) folder gets hosted on the [wasocshared tlp-green (blob container)](https://wasocshared.blob.core.windows.net/tlp-green).

Minor enhancements include a custom content router to preserve SAS container url so that a container level SAS_TOKEN can be used to easily share any content within that container.

Note that attachments that are directly downloadable have to be in the noCompileLinks section, and paths for them should all be relative to the index.html file (not the markdown document the links are in).

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
        noCompileLinks: [
        ".*\.pdf" // allow pdf downloads (use path relative to index.html)
    ]
};
```
