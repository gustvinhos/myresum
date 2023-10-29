from pathlib import Path

import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from resumo import Resumo



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Thiago Reis"
PAGE_ICON = ":wave:"
NAME = "Thiago Reis"
DESCRIPTION = """
Analista de BI | Analista de Dados | Ciência de Dados | Power BI | SQL | Python | Bacharelado em Engenharia de Software
"""
EMAIL = "thiagoreis181310@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)





# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

    
menu = option_menu(None, ["Resumo", "Experiências", "Certificações",  "Projetos", "Outras Realizações"], 
    icons=['file-earmark-person','person-workspace', 'patch-check', "database", "award"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles = {
        "container": {
            "background-color": "rgba(0, 0, 0, 0)",  # Cor de fundo escura
            "padding": "20px",  # Mais espaço interno
            "border-radius": "10px",  # Cantos arredondados
        
        },
        "icon": {
            "color": "white",  # Ícones em branco
            "font-size": "20px",  # Tamanho ligeiramente maior
        },
        "nav-link": {
            "font-size": "18px",  # Tamanho da fonte menor
            "text-align": "center",  # Centralize o texto
            "margin": "0 20px",  # Espaçamento horizontal
            "color": "lightgray",  # Cor do texto mais clara
            "transition": "color 0.3s",  # Transição de cor suave
            "font-weight": "normal",
        },
        "nav-link-selected": {
            "background-color": "#d1566a",
            "color": "white",  # Cor do texto branco
        },
        "nav-link:hover": {
            "color": "orange",  # Cor do texto laranja ao passar o mouse
        },
    }

)


if menu == "Resumo":
    # Criar uma instância da classe Resumo
    resumo_instance = Resumo()

    col1, col2, col3, col4 = st.columns(4)
    with st.container():
        with col1:
            # Criar um gráfico de barras
            resumo_instance.big_number_work()

        with col2:
            # Criar um gráfico de barras
            resumo_instance.big_number_companies()

        with col3:
            # Criar um gráfico de barras
            resumo_instance.big_number_courses()    

        with col4:
            # Criar um gráfico de barras
            resumo_instance.big_number_institu()

    col1, col2 = st.columns(2)
    with st.container():
        with col1:
            st.subheader("Sobre os cursos:")
            resumo_instance.bar_chart_areacourses()
            

        with col2:
            st.subheader("Sobre as instituições:")
            
      

    
    
    


if menu == "Experiências":
    with st.expander("🍞 **Analista de BI | Wickbold | 09/2023 - Hoje**"):
        st.subheader("Resumo da experiência")
        st.write    (
            """
        - ► Usei Power BI para construir dashboards para toda a empresa, permitindo que os usuários finais visualizassem e interagissem com os dados.
        - ► SQL para extrair dados de bancos de dados relacionais, consultar dados, mapear relacionamentos e criar views.
        - ► Python para automatizar tarefas repetitivas, extrair dados de APIs e sites.
             - ► Utilizado bibliotecas como Pandas, Numpy, StreamLit, Requests, Selenium, Pyautogui.


        """
        )
        
    
    with st.expander("🍞 **Analista de Dados - Trade Marketing | Wickbold | 08/2021 - 09/2023**"):
        st.subheader("Resumo da experiência")
        st.write(
            """
            - ► Utilizei Power BI para a construção de dashboards em toda a empresa, proporcionando aos usuários finais a capacidade de visualizar e interagir com os dados.
            - ► Automatizei tarefas utilizando Python, desenvolvendo scripts para lidar com tarefas repetitivas e para a extração de dados de APIs.
                - ► Utilizei bibliotecas como Pandas, Numpy, StreamLit, Requests, Selenium e Pyautogui.
            - ► Utilizado o Excel para a criação de relatórios complementares e análises de dados.
            - ► Desenvolvi relatórios de análise de mercado, incluindo informações sobre distribuição, giro, volume, faturamento, consumo e market share.
            - ► Realizei a extração e tratamento de dados de vendas (sell in e sell out) e informações de mercado, utilizando ferramentas como Nielsen, Scanntech, Mercanet e Involves Stage.
            - ► Apoiei o desenvolvimento de planos estratégicos de categorias, considerando dados de mercado e o comportamento do shopper.
            - ► Prestei suporte no planejamento dos Planos Trimestrais e no processo S&OP (Sales and Operations Planning).
            - ► Participei do desenvolvimento do Guia de Execução, colaborando com as equipes de Trade Canal, Merchandising e Comercial para atender às necessidades de diferentes tipos de canais de venda e regiões em nível nacional.
            - ► Contribuí para a entrega do Selling Story adaptado para Marca, Categoria e Projetos de Trade Marketing On Premise.
            """
        )

        st.subheader("Principais realizações")
        st.write(
            """
            - ► Desenvolvi o "Loja Perfeita" é a descrição do cenário ideal de execução de uma loja, com base em dados de mercado e comportamento do shopper, prevendo um aumento de mais de 20% nas vendas.
            - ► Criei um Dashboard Geral para o Comercial com informações macros de mercado mostrando o desempenho da empresa em relação aos concorrentes e conectando os dados internos de venda para mostrar o desempenho de cada canal e equipes de venda.
            - ► Criei um sistema de monitoramento de displays, permitindo que a equipe de merchandising acompanhasse a execução de displays e monitorasse cada um, evitando perdas.
            - ► Realizei alguns treinamentos para a equipe de vendas, ensinando-os a utilizar o Power BI e a interpretar os dados de mercado.
            - ► Criei um sistema de SAC, que permitiu que a equipe de vendas e marketing acompanhasse os problemas dos produtos antes de chegar ao consumidor e tomasse medidas para resolvê-las.
            """
        )



    with st.expander("☕ **Assistente de Inteligência de Mercado | Rancheiro | 08/2017 - 08/2021**"):
        st.subheader("Resumo da experiência")
        st.write(
            """
            - ► Utilizei o Excel para a construção de dashboards em toda a empresa, proporcionando aos usuários finais a capacidade de visualizar e interagir com os dados.
            - ► Criei relatórios de preço, share, margem, markup, ruptura que foram utilizados pela equipe de vendas para a tomada de decisão.
            - ► Fazia a gestão de promotores de venda através de relatórios de produtividade e eficiência.
            - ► Fiz parte de um projeto de inteligência artificial que utilizava reconhecimento por imagem para identificar rupturas, desvios de preço entre outros.

"""
        )

        st.subheader("Principais realizações")
        st.write(
            """
            - ► Criei um sistema de monitoramento de ruptura, que permitiu que a equipe de vendas acompanhasse a execução de displays e monitorasse cada um, evitando perdas.
            - ► Realizei alguns treinamentos para a equipe de vendas e promotores, ensinando-os a ler e interpretar os dados de mercado.
            - ► Criado um sistema de pontuação para as lojas que permitiu a equipe de vendas identificar as lojas que precisavam de mais atenção e onde deveriam focar seus esforços.
            - ► Criei um sistema de SAC, que permitiu que a equipe de vendas e marketing acompanhasse os problemas dos produtos antes de chegar ao consumidor e tomasse medidas para resolvê-las.
            """
        )





        


elif menu == "Certificações":
    st.subheader("Certificações")
    st.write("---")
    st.write("🚧", "**Senior Data Analyst | Ross Industries**")
    st.write("02/2020 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )


















# # --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qulifications")
# st.write(
#     """
# - ✔️ 7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )


# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )


# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")