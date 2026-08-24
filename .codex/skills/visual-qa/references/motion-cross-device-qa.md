# Motion, 3D, and Cross-device Visual QA

Animated experiences need state-based evidence, not a random screenshot taken mid-transition.

## Motion state contract
For each signature sequence define deterministic checkpoints: before trigger, key reveal, midpoint or meaningful label, completed state, and reversed/return state if relevant. For scroll timelines use semantic scroll positions/labels rather than arbitrary milliseconds. Record viewport and reduced-motion variant.

Test interruption: fast scroll, reverse direction, route navigation during animation, repeated click, resize/orientation, and background/foreground. The end state must remain correct even when the perfect choreography is interrupted.

## Scroll QA
Inspect sticky/pinned boundaries, content before/after the sequence, scrollbar/travel length, focus/anchor navigation through the section, mobile replacement, and late-loading layout changes. Check that users are not trapped and that content does not remain hidden because a trigger failed.

## 3D QA
Capture a deterministic camera/object state after assets are ready. Verify framing, model scale, material/color, environment, clipping, texture readiness, object visibility, overlay alignment, pointer/touch hit regions, and fallback/poster. For regressions, exact frame/pixel comparison is only meaningful if camera/time/randomness and renderer environment are controlled.

Check route revisit and resize for duplicate canvases or stale frames. Test failed/slow asset load and no-WebGL/fallback state. Reduced motion may keep a static 3D frame or poster rather than continuous camera/object movement.

## Device/browser matrix
Prioritize meaningful differences: touch vs pointer, narrow vs wide composition, high/normal DPR, Safari/WebKit vs Chromium/Firefox as required by support policy, mobile browser chrome/viewport behavior, and constrained GPU/device classes for ambitious 3D. The matrix should be risk-based rather than an exhaustive brand list.

## Smoothness versus fidelity
Visual QA verifies state/choreography and obvious judder, but performance evidence should measure frame/long-task/GPU behavior. A sequence can look correct at 15 fps in screenshots and still fail performance; conversely a fast sequence can have incorrect hierarchy.

## Reduced motion
Inspect the reduced-motion page as its own designed state: no giant hidden gaps from removed pins, content in correct order, state feedback still visible, no perpetual canvas/video distortion, and no essential information dependent on watching the original sequence.

## Evidence report
Include candidate build/commit, browser/device/viewport, motion preference, data/theme/locale, checkpoint definition, capture/video references, defects, accepted variance, and missing automation. If a sequence cannot be deterministic, require manual/video comparison with clear checkpoints rather than a misleading pixel threshold.
