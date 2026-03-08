#version 150

in vec3 normal;
in vec3 frag_pos;
in vec4 color;

uniform vec3 camera_pos;

out vec4 fragColor;

void main()
{
    vec3 light_dir = normalize(vec3(0.3, 0.7, 0.6));
    vec3 N = normalize(normal);

    float intensity = dot(N, light_dir);

    float shade;

    if (intensity > 0.8)
        shade = 1.0;
    else if (intensity > 0.5)
        shade = 0.7;
    else if (intensity > 0.25)
        shade = 0.45;
    else
        shade = 0.25;

    vec3 toon_color = color.rgb * shade;

    // rim light
    vec3 view_dir = normalize(camera_pos - frag_pos);
    float rim = pow(1.0 - max(dot(view_dir, N), 0.0), 2.5);

    toon_color += rim * 0.25;

    fragColor = vec4(toon_color, color.a);
}