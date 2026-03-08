#version 150

uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelMatrix;

in vec4 p3d_Vertex;
in vec3 p3d_Normal;
in vec4 p3d_Color;

out vec3 normal;
out vec3 frag_pos;
out vec4 color;

void main()
{
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;

    frag_pos = (p3d_ModelMatrix * p3d_Vertex).xyz;
    normal = normalize(mat3(p3d_ModelMatrix) * p3d_Normal);

    color = p3d_Color;
}