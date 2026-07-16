import streamlit as st
from github_api import buscar_repositorios

st.title("Meus repositórios no GitHub")
usuario = st.text_input("Usuário do GitHub", "devnoggal")

if usuario:
    repositorios = buscar_repositorios(usuario)
    if repositorios:
        st.write(f"Total de repositórios:  {len(repositorios)}")
        for repo in repositorios:
            with st.expander(repo['name']):
                st.write(f"**Linguagem** {repo['language']}")
                st.write(f"**Estrelas** {repo['stargazers_count']}")
                st.write(f"**Descrição** {repo['description']}")
                st.write(f"**[Ver no GitHub]** {repo['html_url']}")
    else:
        st.warning("Nenhum repositório encontrado ou usuário inválido.")
