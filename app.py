import gradio as gr

from security import build_rails, secure_generate

# NeMo Guardrails : rails d'entrée + rails de sortie, définis dans ./config
rails = build_rails("./config")


def chat(message, history=None):
    return secure_generate(rails, message)


if __name__ == "__main__":
    demo = gr.ChatInterface(
        fn=chat,
        title="Secure AI Assistant",
        description="Assistant conversationnel sécurisé avec NeMo Guardrails + Ollama",
    )
    demo.launch()