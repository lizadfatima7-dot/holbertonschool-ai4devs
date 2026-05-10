# Risk Assessment – Legacy Todo Application (TodoMVC - Backbone.js)

| Risk | Severity | Notes |
|------|----------|-------|
| XSS vulnerability via unsanitized input | High | User-submitted todo titles are stored and rendered without sanitization, allowing script injection attacks |
| jQuery 1.11.1 known security vulnerability | High | CVE-2015-9251 allows XSS attacks through jQuery's DOM manipulation methods in this version |
| No automated tests of any kind | High | Zero unit, integration, or end-to-end tests mean any change can silently break existing functionality |
| Client-side only data persistence | High | All data stored in localStorage is lost if the user clears browser storage or switches devices |
| Deprecated and unmaintained dependencies | High | Backbone.js, RequireJS, and Bower are no longer actively maintained, leaving security patches unaddressed |
| Full DOM re-render on every model change | Medium | Entire todo list is rebuilt from scratch on each update, causing serious performance issues at scale |
| No Content Security Policy headers | Medium | Absence of CSP headers increases the attack surface for XSS and code injection exploits |
| Tight coupling between Views and Models | Medium | Changes to data structure require modifications across multiple tightly coupled files, increasing refactoring risk |
| Global state management via Backbone events | Medium | Event-driven global state is difficult to trace, debug, and reason about in complex scenarios |
| No TypeScript or type annotations | Medium | Runtime type errors are not caught at compile time, making bugs harder to detect before deployment |
| localStorage 5MB quota with no error handling | Medium | Storage quota exceeded errors are not caught, causing silent data loss without user notification |
| No input validation on todo title length | Low | Extremely long titles can break the UI layout without any enforced character limit |
| No logging or error monitoring | Low | Runtime errors and edge cases are invisible in production with no logging or monitoring integration |
| Inconsistent coding style mixing ES5 and ES6 | Low | Mixed syntax patterns make the codebase harder to read and maintain across different contributors |
| No linting or formatting tools configured | Low | Absence of ESLint and Prettier leads to inconsistent code style and allows common errors to go undetected |