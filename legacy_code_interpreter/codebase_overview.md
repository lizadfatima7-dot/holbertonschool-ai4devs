\# Codebase Overview - Legacy Task Manager Application (jQuery + PHP)



\## Age

First release in 2011, last major update in 2017. The jQuery and PHP stack used

has not received significant architectural updates since then, making it effectively

legacy by modern web development standards.



\## Size

\~4,100 LOC across PHP, JavaScript, HTML, and CSS files.

\- PHP: \~2,400 LOC

\- JavaScript: \~900 LOC

\- HTML templates: \~500 LOC

\- CSS: \~300 LOC



\## Dependencies

\- PHP 5.6 (end of life since December 2018, no longer receiving security updates)

\- jQuery 1.9.1 (outdated major version with known security vulnerabilities)

\- MySQL 5.5 (end of life since December 2018)

\- Bootstrap 2.3.2 (outdated major version, incompatible with modern browsers)

\- PDO with no query parameterization in several modules



\## Known Issues and Pain Points



\### Architecture

\- No MVC pattern; business logic mixed directly inside HTML template files

\- No separation of concerns between database queries and presentation layer

\- Global variables used extensively for state management across pages



\### Code Quality

\- No automated tests of any kind (unit, integration, or end-to-end)

\- Inconsistent coding style mixing procedural PHP and early OOP patterns

\- Heavy reliance on jQuery for all DOM manipulation instead of modern APIs

\- Callback-based async patterns with no use of Promises or async/await



\### Security

\- jQuery 1.9.1 contains known XSS vulnerabilities

\- Several SQL queries use string concatenation instead of prepared statements

\- No input sanitization on user-submitted task fields

\- Passwords stored using MD5 hashing instead of bcrypt or Argon2



\### Performance

\- Full page reload triggered on every form submission with no AJAX fallback

\- No caching layer; every request hits the database directly

\- All CSS and JavaScript files loaded synchronously without minification



\### Maintainability

\- No TypeScript or type annotations; runtime errors are hard to catch early

\- Documentation is minimal and outdated

\- No linting or formatting tools configured

\- Build tooling relies on manual FTP deployment with no CI/CD pipeline

