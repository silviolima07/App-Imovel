import streamlit as st

from bokeh.models.widgets import Div

import pandas as pd

from PIL import Image

pd.set_option('precision',2)

import base64


def download_link(df, texto1, texto2):
    if isinstance(df,pd.DataFrame):
        object_to_download = df.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{texto1}">{texto2}</a>'
    

def main():

    """Indeed App """

    # Titulo do web app
    html_page = """
    <div style="background-color:blue;padding=30px">
        <p style='text-align:center;font-size:30px;font-weight:bold;color:white'>Imoveis Online</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)
   
    html_page = """
    <div style="background-color:white;padding=20px">
        <p style='text-align:center;font-size:20px;font-weight:bold;color:blue'>Scrap de Anúncios de Imoveis</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)

   
    aguia1 = Image.open("Images/aguia1.png")
    aguia2 = Image.open("Images/aguia2.png") 
    aguia3 = Image.open("Images/aguia3.png")
    scrap  = Image.open("Images/webscrap.jpeg")

    st.sidebar.image(scrap,caption="", width=300)

    #activities = ["Home",'VivaReal', 'ImovelWeb', 'Zap',"About"]
    #file_csv = ['VivaReal.csv','ImovelWeb.csv', 'Zap.csv']
    #choice = st.sidebar.selectbox("Selecione uma opção",activities)

    activities = ["Home",'VivaReal', 'ImovelWeb', 'Zap',"About"]
    file_csv = ['VivaReal.csv','ImovelWeb.csv', 'Zap.csv']
    cidades_estado = ['Sao-Paulo-SP','Porto-Alegre-RGS', 'Rio-de-Janeiro-RJ', 'Belo-Horizonte-MG']
    cidades_csv = ['sao-paulo.csv','porto-alegre.csv', 'rio-de-janeiro.csv', 'belo-horizonte.csv']
    choice = st.sidebar.selectbox("Selecione uma opção",activities)

    # Definir a data da última atualização


    #f = open("update", "r")
    #data_update = f.read()
   
    #if choice != 'About':
    #    st.write('Última atualizacao: '+ data_update)


    

    if choice == 'Home':
       
        col1, col2, col3 = st.beta_columns(3)
        
        col1.header("VivaReal")
        col1.image(aguia1, width=200, height=300)
        
        col2.header("ImovelWeb")
        col2.image(aguia2, width=200, height=200)

        col3.header("Zap")
        col3.image(aguia3, width=200, height=300)
        
    elif choice == activities[1]:
        
        cidade = st.sidebar.selectbox("Selecione uma cidade",cidades_estado)
        if cidade == cidades_estado[0]: # Sao Paulo - SP
            df = pd.read_csv('CSV-Cidade/'+activities[1]+'/'+cidades_csv[0])
            total = str(len(df))
            st.title(activities[1] + " : "+cidades_estado[0])
            st.sidebar.image(aguia1,caption="", width=300)
            st.subheader("Total de anuncios: "+total)
            st.table(df)
            if st.button('Download Dataframe as CSV'):
                filename = cidades_csv[0]
                tmp_download_link = download_link(df, filename, 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
       
        elif cidade == cidades_estado[1]: # Porto Alegre - RGS
            df = pd.read_csv('CSV-Cidade/'+activities[1]+'/'+cidades_csv[1])
            total = str(len(df))
            st.title(activities[1] + " : "+cidades_estado[1])
            st.sidebar.image(aguia1,caption="", width=300)
            st.subheader("Total de anuncios: "+total)
            st.table(df)
            if st.button('Download Dataframe as CSV'):
                filename = cidades_csv[1]
                tmp_download_link = download_link(df, filename, 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
            

        elif cidade == cidades_estado[2]: # Rio de Janeiro - RJ
            df = pd.read_csv('CSV-Cidade/'+activities[1]+'/'+cidades_csv[2])
            total = str(len(df))
            st.title(activities[1] + " : "+cidades_estado[2])
            st.sidebar.image(aguia1,caption="", width=300)
            st.subheader("Total de anuncios: "+total)
            st.table(df)
            if st.button('Download Dataframe as CSV'):
                filename = cidades_csv[2]
                tmp_download_link = download_link(df, filename, 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)

        elif cidade == cidades_estado[3]: # Belo Horizonte - MG
            df = pd.read_csv('CSV-Cidade/'+activities[1]+'/'+cidades_csv[3])
            total = str(len(df))
            st.title(activities[1] + " : "+cidades_estado[3])
            st.sidebar.image(aguia1,caption="", width=300)
            st.subheader("Total de anuncios: "+total)
            st.table(df)
            if st.button('Download Dataframe as CSV'):
                filename = cidades_csv[0]
                tmp_download_link = download_link(df, filename, 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)

        
    elif choice == activities[2]:
        st.sidebar.image(aguia2,caption="", width=300)
        df = pd.read_csv('CSV/'+file_csv[1])
        #df.drop(['Area'], axis=1, inplace=True)
        total = str(len(df))
        st.title(activities[2])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            filename = file_csv[1]
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)     
   
    elif choice == activities[3]:
        st.sidebar.image(aguia3,caption="", width=300)
        df = pd.read_csv('CSV/'+file_csv[2])
        #df.drop(['Area'], axis=1, inplace=True)
        total = str(len(df))
        st.title(activities[3])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            filename = file_csv[2]
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

  
    elif choice == 'About':
        #st.sidebar.image(about,caption="", width=300, height= 200)
        st.subheader("Built with Streamlit")
        
        
        st.write("Dados coletados via scrap usando: Selenium e BeautifulSoup.")
        #st.markdown("A coleta dos dados é feita às 9h, 12h, 15h e 18h")
        #st.write("Executados via crontab scripts realizam o scrap e atualização do app.")
        #st.write("Foram definidos 4 cargos apenas para validar o processo.")
        #st.write("O scrap para o cargo de Engenheiro de Machine Learning trouxe poucas linhas.")
        #st.write("Para os demais cargos, foram encontradas mais de 100 vagas, distribuídas em diversas páginas.")
        #st.write("Esse app traz as 10 primeiras páginas apenas.")
        #st.subheader("Versão 02")
        #st.write(" - incluído o link encurtado da vaga")
        #st.subheader("by Silvio Lima")
        
        #if st.button("Linkedin"):
        #    js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
        #    html = '<img src onerror="{}">'.format(js)
        #    div = Div(text=html)
        #    st.bokeh_chart(div)

        
    

       

   
    
    
if __name__ == '__main__':
    main()
