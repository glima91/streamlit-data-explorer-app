# App que realiza a análise exploratória de dados utilizando o framework Streamlit
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    st.image('imag.jpg',width=700)
    st.title("Explorador de Dados")
    # carrega arquivo
    st.header("Carga de Dados")
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    
    if file is not None:
        st.success("Arquivo lido com sucesso!")
        # cria dataframe
        st.subheader("Escolha o delimitador")
        separator = st.radio("Escolha o delimitador",(",",";","|"))
        df = pd.read_csv(file, delimiter=separator)
        st.write("O dataframe possui ",df.shape[0], " linhas e ", df.shape[1]," colunas!")
        
        st.header("Análise Exploratória")
        st.subheader("Preview do Dataset")
        # escolhe o numero de linhas a serem visualizados
        num_df_rows = st.slider('Escolha o número de linhas que deseja mostrar:', 0, 50, 5)
        # mostra dataframe
        st.dataframe(df.head(num_df_rows))

        # ESTATISTICA BASICA
        st.subheader("Estatística Descritiva")
        st.text("Informações como média, mediana e desvio padrão")
        st.dataframe(df.describe())
        
        #CORRELACAO
        st.subheader("Análise de Correlação")
        #if colunas_numericas is not None:
        lista_colunas_num = list(df.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).columns)
        view_corr_larg = st.slider('Ajuste da largura da view:', 5, 20, 10)
        view_corr_alt = st.slider('Ajuste da altura da view:', 5, 20, 10)
        fig, ax = plt.subplots(figsize=(view_corr_larg, view_corr_alt))
        sns.heatmap(df.corr(), annot=True, ax=ax)
        st.pyplot()

        #HISTOGRAMA
        st.subheader("Distribução dos Dados")
        col = st.selectbox("Escolha um atributo para analisar",lista_colunas_num, key = 'unique')
        view_hist_larg = st.slider('Ajuste da largura da view (histograma):', 5, 20, 10)
        view_hist_alt = st.slider('Ajuste da altura da view (histograma):', 5, 20, 5)
        view_hist_bins = st.slider('Número de bins da view (histograma):', 1, 100, 5)
        if col is not None:
            st.markdown('Histograma da coluna : ' + str(col))
            hist_fig, hist_ax = plt.subplots(figsize=(view_hist_larg, view_hist_alt), sharex=True)
            sns.distplot(df[col] , color="skyblue", ax=hist_ax, bins=view_hist_bins)
            st.pyplot()
        #ANALISE GRÁFICA
        st.subheader("Análise Gráfica")
        col1 = st.selectbox("Escolha o Atributo 1 (eixo x):",df.columns.tolist(), key = 'unique_1')
        col2 = st.selectbox("Escolha o Atributo 2 (eixo y):",df.columns.tolist(), key = 'unique_2')
        col3 = st.selectbox("Escolha o HUE (opcional):",df.columns.tolist(), key = 'unique_2')
        activate_hue = st.checkbox("Utilizar Hue") 
        list_of_graphs = ['Scatterplot','Barplot','Boxplot','Lineplot']
        col4 = st.selectbox("Escolha o Tipo de Gráfico:", list_of_graphs, key = 'unique_2')
        view_plot_larg = st.slider('Ajuste da largura da visualização:', 5, 20, 10)
        view_plot_alt = st.slider('Ajuste da altura da visualização:', 5, 20, 5)
    
        if (col1 != None) and (col2 != None) :
            st.markdown("Gráfico escolhido: " + col4)
            figs, axs = plt.subplots(figsize=(view_plot_larg, view_plot_alt), sharex=True)
            if col4 =="Scatterplot":
                if activate_hue:
                    sns.scatterplot(ax=axs, x=df[col1], y=df[col2], hue=df[col3])
                else:
                    sns.scatterplot(ax=axs, x=df[col1], y=df[col2])    
            if col4 =="Barplot":
                if activate_hue:
                    sns.barplot(ax=axs, x=df[col1], y=df[col2], hue=df[col3])
                else:
                    sns.barplot(ax=axs, x=df[col1], y=df[col2])    
            if col4 == "Boxplot":
                sns.boxplot(ax=axs, x=df[col1], y=df[col2]) 
            if col4 =="Lineplot":
                if activate_hue:
                    sns.lineplot(ax=axs, x=df[col1], y=df[col2], hue=df[col3])
                else:
                    sns.lineplot(ax=axs, x=df[col1], y=df[col2])    

            st.pyplot()


       

if __name__ == '__main__':
    main()