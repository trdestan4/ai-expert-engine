# 3D, Video and Motion Assets

Design 3D/video/motion from the product surface backward. Define where the asset appears, viewport size, scroll/interaction relationship, duration/loop, camera path, focal subject, fallback frame and performance ceiling before building a high-complexity render.

Maintain the visual system across 3D and 2D: materials, lighting temperature, shadow softness, camera perspective, color palette and motion personality should reinforce the same creative direction. Avoid adding 3D merely as a generic 'premium' signal.

For video, create intentional opening/closing frames, safe crops and poster images. Looping assets should hide seams and avoid visible lighting/camera jumps. Encode audio only when needed; provide captions/transcripts for meaningful spoken content.

For web 3D, optimize geometry, textures, draw calls, material complexity and loading strategy. Use progressive/static fallbacks when hardware/network conditions do not justify full realtime rendering. Heavy interactive scenes require measured device testing and a performance specialist handoff.

Motion should communicate hierarchy/state rather than delay navigation. Coordinate with `motion-direction`; provide reduced-motion/static behavior for essential experiences. Avoid scroll-linked motion that breaks focus, reading order or mobile control.

Export variants by actual delivery need rather than one oversized master everywhere. Validate compression artifacts, color/gamma, alpha edges, poster-to-video transition and layout shift in the target implementation.

Keep source project/render settings, license/source assets and reusable scene/components separate from final compressed outputs so future edits do not require reverse-engineering delivery files.