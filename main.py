import streamlit as st
from PIL import Image
import webbrowser

# Configurações da página
st.set_page_config(
    page_title="Meu Portfólio Wilmes",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded",
)

SOCIAL_LINKS = {
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/wilmes-chaves-322344228/",
        "icon": "fab fa-linkedin",
    },
    "GitHub": {"url": "https://github.com/WilmesChaves", "icon": "fab fa-github"},
    "Instagram": {
        "url": "https://www.instagram.com/wilmeschaves/",
        "icon": "fab fa-instagram",
    },
    "WhatsApp": {"url": "https://wa.me/5582996424505", "icon": "fab fa-whatsapp"},
    "Facebook": {
        "url": "https://www.facebook.com/wilmeschaves/",
        "icon": "fab fa-facebook",
    },
}

# Font Awesome
st.markdown(
    """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

SKILLS = {
    "Frontend": ["HTML", "CSS", "JavaScript"],
    "Backend": ["Python", "Django", "Node.js"],
    "Banco de Dados": ["MySQL", "PostgreSQL", "MongoDB"],
}

# Projetos
PROJECTS = [
    {
        "title": "Projeto 1 - E-commerce",
        "description": "Desenvolvimento de uma plataforma de e-commerce utilizando Django e React.",
        "technologies": ["Django", "React", "PostgreSQL"],
        "link": "https://github.com/WilmesChaves/ecommerce-django-react",
    },
    {
        "title": "Projeto 2 - Blog Pessoal",
        "description": "Criação de um blog pessoal com Flask e SQLite, permitindo publicação de artigos e comentários.",
        "technologies": ["Flask", "SQLite", "Bootstrap"],
        "link": "https://github.com/WilmesChaves/blog-flask-sqlite",
    },
    {
        "title": "Projeto 3 - API de Tarefas",
        "description": "Desenvolvimento de uma API RESTful para gerenciamento de tarefas usando Node.js e Express.",
        "technologies": ["Node.js", "Express", "MongoDB"],
        "link": "https://github.com/WilmesChaves/api-tarefas-node-express",
    },
]


def load_css():
    """Carrega todos os estilos CSS"""
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary-color: #1a365d;
                --secondary-color: #2d547d;
                --accent-color: #38bdf8;
                --text-light: #f8fafc;
                --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }


            .project-card {
                background: white;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 0, 0, 0.1);
            }


            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }


            .experience-item {
                padding: 1.5rem;
                background: white;
                border-radius: 10px;
                box-shadow: var(--shadow);
                margin-bottom: 1.5rem;
                transition: all 0.3s ease;
            }


            .experience-item:hover {
                transform: translateY(-3px);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Font Awesome
    st.markdown(
        """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    """,
        unsafe_allow_html=True,
    )


def social_links():
    links_html = "".join(
        f'<a href="{info["url"]}" target="_blank"style="margin: 0 10px; font-size: 1.5rem; color: var(--primary-color);">'
        f'<i class="{info["icon"]}"></i></a>'
        for name, info in SOCIAL_LINKS.items()
    )
    st.markdown(
        f'<div style="text-align:center; margin: 2rem 0;">{links_html}</div>',
        unsafe_allow_html=True,
    )


def main():
    load_css()
    # <img src="ACORDA.png" alt="Foto" style="width: 150px; height: 150px; border-radius: 50%;">

    #  sidebar
    with st.sidebar:
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://scontent.fmcz1-2.fna.fbcdn.net/v/t39.30808-6/479943613_9092569474187058_8628125223242646119_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeG5jjb4K-t6LD3whUcwvFYVAbIZiCDItb8BshmIIMi1vxOPOWzfYLAVucYth3N_JP4Bs9FNOQ-Yfw-o-if7brKA&_nc_ohc=Ez4yrat3c64Q7kNvwGUmYn3&_nc_oc=AdmW0f8gYxzKy5RwnQ1hv3hg_ziSiJVrMxFCgpm-lkQ2-g57D4QwoiNssQRVGhez4Ck&_nc_zt=23&_nc_ht=scontent.fmcz1-2.fna&_nc_gid=fkh458mWQ0v3o4TrvQx8sQ&oh=00_AftFPzRgdu1OXQ8cSgD1NKusWIbXldEmyz8SNzYUu5uS8A&oe=698F6B50" alt="Foto" style="width: 150px; height: 150px; border-radius: 50%;">            
                <h2>🧑‍💻📈 Wilmes Chaves Portfólio</h2>
                <p style="color: var(--accent-color);">Desenvolvedor</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        # contato
        with st.expander("Contato", expanded=True):
            st.markdown(
                """                       
                📧 **Email:** wilmeschaves@gmail.com 
                 
                📞 **Telefone:** (82) 9 9642-4505
                
                📍 **Endereço:** Arapiraca, AL
            
            """,
                unsafe_allow_html=True,
            )

        social_links()

    # Conteúdo principal
    st.title("Wilmes Chaves - Desenvolvedor")
    st.markdown(
        """Bem-vindo ao meu portfólio! Aqui você encontrará uma visão geral dos meus projetos, experiências e habilidades. Sinta-se à vontade para explorar e entrar em contato comigo para discutir oportunidades de colaboração ou para saber mais sobre meu trabalho.""",
        unsafe_allow_html=True,
    )

    # Projetos
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(
                """
                #### 💻 Sobre Mim!
                Sou Wilmes Chaves, um desenvolvedor  Com experiência em diversas tecnologias, estou sempre em busca de novos desafios para aprimorar minhas habilidades e contribuir para projetos impactantes. Meu objetivo é transformar ideias em realidade através do código, entregando resultados de alta qualidade e valor para os usuários.
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.image(
                "https://scontent.fmcz1-2.fna.fbcdn.net/v/t39.30808-6/479943613_9092569474187058_8628125223242646119_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeG5jjb4K-t6LD3whUcwvFYVAbIZiCDItb8BshmIIMi1vxOPOWzfYLAVucYth3N_JP4Bs9FNOQ-Yfw-o-if7brKA&_nc_ohc=Ez4yrat3c64Q7kNvwGUmYn3&_nc_oc=AdmW0f8gYxzKy5RwnQ1hv3hg_ziSiJVrMxFCgpm-lkQ2-g57D4QwoiNssQRVGhez4Ck&_nc_zt=23&_nc_ht=scontent.fmcz1-2.fna&_nc_gid=fkh458mWQ0v3o4TrvQx8sQ&oh=00_AftFPzRgdu1OXQ8cSgD1NKusWIbXldEmyz8SNzYUu5uS8A&oe=698F6B50",
                width=100,
                caption="Foto de Perfil",
            )
        # Habilidades
        st.markdown("## 🛠️ Habilidades Técnicas")
        cols = st.columns(3)
        for idx, (title, items) in enumerate(SKILLS.items()):
            with cols[idx]:
                items_html = "".join(
                    f"<li style='margin-bottom: 0.5rem;'>{item}</li>" for item in items
                )
                st.markdown(
                    f"""
                        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: var(--shadow);">
                            <h3 style="color: var(--primary-color);">{title}</h3>
                            <ul style="list-style-type: none; padding-left: 0;">
                                {items_html}
                            </ul>
                        </div>
                        """,
                    unsafe_allow_html=True,
                )
        # Projetos em 3 colunas
        st.markdown("## 🚀 Projetos Recentes")
        for project in PROJECTS:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{project['title']}</h3>
                    <p>{project['description']}</p>
                    <p><strong>Tecnologias:</strong> {', '.join(project['technologies'])}</p>
                    <a href="{project['link']}" target="_blank" style="color: var(--accent-color);">Ver Projeto</a>
                </div>
                """,
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
