#version 150

in vec3 normal;
in vec3 frag_pos;
in vec4 color;

uniform vec3 camera_pos;

out vec4 fragColor;

void main() {

    vec3 light_dir = normalize(vec3(0.3, 0.6, 1.0));

    vec3 N = normalize(normal);

    float diff = max(dot(N, light_dir), 0.0);

    vec3 view_dir = normalize(camera_pos - frag_pos);
    vec3 reflect_dir = reflect(-light_dir, N);

    float spec = pow(max(dot(view_dir, reflect_dir), 0.0), 32.0);

    float rim = pow(1.0 - max(dot(view_dir, N), 0.0), 2.0);

    vec3 final_color =
        color.rgb * (0.25 + diff) +   // diffuse
        spec * 0.5 +                  // highlight
        rim * 0.2;                    // rim glow

    fragColor = vec4(final_color, color.a);
}