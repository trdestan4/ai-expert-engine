# GPU Effects, Render Targets, and Performance

## Render targets
Every offscreen pass allocates texture storage and consumes bandwidth when rendered/read. A full-screen RGBA target at high DPR can be large; multiple ping-pong targets, depth textures, MSAA, mipmaps, or high-precision formats multiply memory. Match target dimensions/format to the effect rather than blindly mirroring the main canvas.

Use lower-resolution buffers for blur, fluid-like distortion, bloom masks, or feedback when perceptually acceptable. Resize deliberately and dispose old targets. Avoid reallocating targets every frame.

## Feedback and simulation
Ping-pong techniques render the previous state into the next state. Define deterministic initialization, simulation timestep, resize/reset behavior, and pause/offscreen policy. Large simulations can consume significant fill rate even if the scene geometry is simple.

## Particles
For many particles prefer batched/instanced/point-style GPU-friendly representations over thousands of independent scene objects. Decide which attributes are static, per-instance, or simulated. Overdraw from large transparent particles can dominate cost; particle count alone is not the full metric.

## Post effects
A custom post pass touches much or all of the screen. Count texture samples, render passes, target resolutions, and blend/overdraw. Combine compatible operations when it meaningfully reduces passes without creating an unmaintainable mega-shader. Expensive effects can use quality tiers.

## Interaction-driven effects
Pointer/scroll uniforms should be smoothed only when the motion design calls for it. Do not run heavy raycasts or readbacks from the GPU each frame merely to feed a visual. GPU→CPU readbacks can stall pipelines and should be avoided in hot interaction paths.

## Quality tiers
Define graceful levels such as:
- full: intended DPR/pass count/simulation detail;
- constrained: lower DPR/target resolution/particles/octaves/passes;
- fallback: standard material, static image, or simplified CSS treatment.

Choose tier from capability/performance evidence rather than device-name guessing when possible. The page must remain usable if the effect is disabled.

## Profiling
Separate CPU and GPU symptoms. A low frame rate may come from JavaScript/layout, draw-call submission, vertex work, fragment fill rate, shader complexity, texture bandwidth, or post passes. Reduce one variable at a time and compare. Desktop discrete-GPU performance is weak evidence for mobile.

## Accessibility and comfort
High frame rate does not make a visual comfortable. Large continuous distortion, parallax, rapid zoom, or flicker may require a reduced-motion/static path. Avoid unsafe flashing. Ensure effects never obscure focus, text, status, or controls.

## Lifecycle
Shader materials, textures, render targets, simulation buffers, event listeners, and timers belong to a runtime owner and must be cleaned up or intentionally cached. Repeated route entry/exit is a required leak test for SPA experiences.
