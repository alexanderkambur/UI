import streamlit as st
import streamlit.components.v1 as components

st.title("What's under the hood?")

with st.sidebar:
    st.markdown("This page provides a high-level overview of the architecture of the Chatbot.")

def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """
    ) # , height=600

mermaid(
    """
    stateDiagram-v2

    state UI {
        Query
        Response
    }

    state LLM {
        Prompt --> Mistral
    }

    state Converter {
        PDF --> Extractor 

        state Extractor {
            pyPDF
        }
        
        Extractor --> Chunks

        Chunks --> Embedder
    }

    Chunks --> Retriever 

    state Database{
        state Embedder {
            allMiniLM
        }

        Embedder --> Embdedded_Query

        Embedder --> Embedded_Chunks

        Embedded_Chunks --> Retriever

        Embdedded_Query --> Retriever

        state Retriever {
            LangChain
        }

        Retriever --> Context

        
    }

    Context --> Prompt

    Query --> Embedder

    Query --> Prompt

    Mistral --> Response
    """
)