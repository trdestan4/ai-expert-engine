# Accessibility Testing and Regression

Automated tools are useful for detectable issues such as missing names, some ARIA misuse and contrast, but they cannot prove WCAG conformance or task usability. Combine automation with manual keyboard, focus, zoom/reflow and assistive-technology testing.

For critical journeys, test keyboard-only navigation and operation, visible/unobscured focus, screen-reader names/roles/states, form instructions/errors, dynamic status announcements and modal/menu focus behavior. Include 200%+ zoom/reflow and reduced-motion where relevant.

Use browser accessibility trees/devtools to debug semantic mismatches. Test at least representative screen readers/browser combinations for high-value experiences when possible; behavior can differ across stacks.

Add automated component/page checks in CI for regressions that tools can reliably detect. Keep manual acceptance cases for interactions automation cannot judge. Treat inaccessible authentication, navigation or core form submission as release blockers proportional to product requirements and severity.

A passing accessibility scanner score is evidence only; document remaining manual coverage and known limitations.