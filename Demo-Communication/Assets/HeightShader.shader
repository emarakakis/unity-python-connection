Shader "Custom/HeightColor"
{
    Properties
    {
        _MinHeight ("Min Height", Float) = 0.0
        _MaxHeight ("Max Height", Float) = 0.25

        _LowColor ("Low Color", Color) = (0, 0, 1, 1)
        _HighColor ("High Color", Color) = (1, 0, 0, 1)
    }

    SubShader
    {
        Tags
        {
            "RenderType" = "Opaque"
            "RenderPipeline" = "UniversalPipeline"
        }

        Pass
        {
            HLSLPROGRAM

            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
            };

            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float height : TEXCOORD0;
            };

            float _MinHeight;
            float _MaxHeight;

            float4 _LowColor;
            float4 _HighColor;

            Varyings vert(Attributes input)
            {
                Varyings output;

                output.positionHCS = TransformObjectToHClip(
                    input.positionOS.xyz
                );

                output.height = input.positionOS.y;

                return output;
            }

            half4 frag(Varyings input) : SV_Target
            {
                float t = saturate(
                    (input.height - _MinHeight) /
                    (_MaxHeight - _MinHeight)
                );

                return lerp(
                    _LowColor,
                    _HighColor,
                    t
                );
            }

            ENDHLSL
        }
    }
}