##################### Library ##################
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go


##################### Judul & Latar Belakang ##################
st.set_page_config(layout="wide")

# Judul
st.title("Fenomena *NEET* : Kaula Muda Negeri Ini *Hopeless* ?")

# Header 1
st.header("Apa Itu NEET ?")

# Deskripsi 1
st.markdown(
    """
    NEET (*Not in Employment, Education or Training*) muncul pertama kali di Jepang pada tahun 1990 yang menggambarkan seseorang yang tidak bekerja dan tidak mencari pekerjaan, serta bukan merupakan seorang yang tengah menempuh pendidikan ataupun mengurus rumah tangga.
    
    Awal kemunculan NEET memang belum dianggap sebagai masalah, namun seiring dengan berjalannya waktu, jumlah kaula muda yang tergolong NEET ini terus meningkat sehingga perlu diantisipasi oleh semua pihak karena akan berdampak negatif baik bagi pemuda itu sendiri, keluarga karena akan menanggung beban ekonomi dan sosial, masyarakat dan pemerintah atau negara karena keberlanjutan laju pertumbuhan ekonomi suatu bangsa akan terpengaruh akibat semakin meningkatnya pemuda produktif yang enggan untuk berada di pasar kerja, dan semakin sedikitnya stok pemuda kompeten karena mereka enggan berada di dunia pendidikan ataupun pelatihan kerja.
    
    **Ciri NEET :**
    - Perempuan
    - Pedesaan
    - Pendidikan rendah
    """ 
    )

##################### Bagian 1 - Tren: remaja (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan ##################
# st.sidebar.markdown("### Unggah Dataset : ")
st.sidebar.title("Unggah Dataset")
# with st.expander("Dataset Pertama") :
uploaded_file = st.sidebar.file_uploader("Dataset Pertama")
if uploaded_file is not None:
    df1 = pd.read_excel(uploaded_file, sheet_name = 'Indo')
    # st.write(df)
    
uploaded_file = st.sidebar.file_uploader("Dataset Kedua")
if uploaded_file is not None:
    df2 = pd.read_csv(uploaded_file, sep = ',')
    
uploaded_file = st.sidebar.file_uploader("Dataset Ketiga")
if uploaded_file is not None:
    df3 = pd.read_excel(uploaded_file)

uploaded_file = st.sidebar.file_uploader("Dataset Keempat")
if uploaded_file is not None:
    df4 = pd.read_excel(uploaded_file)
    
uploaded_file = st.sidebar.file_uploader("Dataset Kelima")
if uploaded_file is not None:
    df5 = pd.read_excel(uploaded_file).drop(columns='Year')
 
# st.dataframe(df) 
# Membaca Dataset : API_SL.UEM.NEET.ZS_DS2_en_excel_v2_4530053.xls (https://ilostat.ilo.org/data/)
# df1 = pd.read_csv('youth-not-in-education-employment-training.csv', sep=',')
# df1 = pd.read_excel('API_SL.UEM.NEET.ZS_DS2_en_excel_v2_4530053.xls', sheet_name = 'Indo')


# Drop Misssing Value
# df1.dropna()

# Mengubah Nama Kolom
# df1.set_axis(['Country', 'Country_ID', 'Year', 'NEET (% of youth population)'], axis='columns', inplace=True)

# DataFrame NEET Indonesia
# neet_indo = df1.query('Country == "Indonesia"').drop(columns='Country_ID').sort_values(by='Year').set_index("Year")

# Sub-Header 1
#st.subheader("Tren: remaja (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan")

with st.expander("Tren: kaula muda (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan") :
    # Line Plot NEET Indonesia
    fig1, ax1 = plt.subplots(figsize=(20,9))
    
    sns.lineplot(x='Year', y='NEET total (% of youth population)', data=df1 , ax=ax1, color='red')
    ax1.set_title('Tingkat NEET Kaula Muda (Usia 15-24, %)')
    ax1.set_xlabel('Tahun')
    ax1.set_ylabel('NEET (% Populasi Kaula Muda)')
    ax1.set_ylim(ymin=0, ymax=40)
    ax1.text(1, -0.1, 'Sumber data: ilostat.ilo.org', color='blue', ha='right', transform=ax1.transAxes)

    st.pyplot(fig1)

    # Penjelasan Grafik 1
    st.markdown(
        """
        - Tahun 2006-2019 persentase NEET di Indonesia *trend*-nya menurun, tapi belum mendekati 15%.
        - NEET kemungkinan mengalami kenaikan akibat COVID-19 mulai tahun 2020.
        """ 
        )


##################### Bagian 2 - Analisis NEET ##################

# Header 2
st.header("Analisa NEET")

# Deskripsi 2
st.markdown(
    """
    Menurut ILO (*International Labour Organization*), kaula muda perempuan lebih berpotensi menjadi NEET dibandingkan dengan kaula muda laki-laki. Perempuan memiliki resiko relatif 3.4 kali lebih besar dibandingkan laki-laki untuk menjadi NEET. Persepsi orang tua terhadap pendidikan, pekerjaan, serta kesulitan untuk masuknya pasar tenaga kerja perempuan mempengaruhi tingkat NEET perempuan.
    """ 
    )


##################### Bagian 2.1 - Perempuan dalam NEET ##################

# Membaca Dataset : Share of youth not in employment, education or training (%).csv (https://data.worldbank.org/)
# df2 = pd.read_csv('Share of youth not in employment, education or training (%).csv', sep=',')

# Drop Kolom
df2.drop(columns=['indicator.label','source.label','obs_status.label','note_indicator.label', 'note_source.label'], inplace=True)

# Rename Kolom
df2.set_axis(['Country', 'Sex', 'Year', 'NEET'], axis='columns', inplace=True)

# Menghapus Total
df2 = df2.sort_values(by='Sex').set_index('Sex')
df2 = df2.drop(df2.index[6:])
df2 = df2.reset_index()

# Sub-Header 2
st.subheader("Perempuan dalam NEET")

with st.expander("NEET Berdasarkan Jenis Kelamin"):
    # Bar Plot Neet Indonesia by Sex
    fig2, ax2 = plt.subplots(figsize=(15,9))

    sns.barplot(data=df2, x='Year', y='NEET', hue='Sex', ax=ax2, palette = 'husl')
    ax2.set_title('Tingkat NEET Berdasarkan Jenis Kelamin')
    ax2.set_xlabel('Tahun')
    ax2.set_ylabel('NEET (% Populasi Kaula Muda)')
    ax2.set_ylim(ymin=0, ymax=40)
    ax2.text(1, -0.1, 'Sumber data: data.worldbank.org', color='blue', ha='right', transform=ax2.transAxes)

    st.pyplot(fig2)

    # Penjelasan Grafik 2
    st.markdown(
        """
        - NEET perempuan berada disekitar angka 26%.
        - NEET laki-laki setiap tahun mengalami kenaikan 1-2%.
        """ 
        )


##################### Bagian 2.2 - Angkatan Kerja vs Pengangguran Terbuka ##################

# Sub_Header 3
st.subheader("Angkatan Kerja vs Pengangguran Terbuka")

# Deskripsi 3
st.markdown(
    """
    - Pada Februari 2022, terdapat sekitar 144.01 juta Angkatan Kerja (AK) di Indonesia atau sekitar 69.06% dari total penduduk usia kerja di Indonesia yang berpartisipasi aktif dalam pasar kerja.
    - Pada Februari 2022, terdapat sekitar 8.40 juta orang Pengangguran Terbuka (PT) di Indonesia atau sebesar 5.83% dari total angkatan kerja di Indonesia yang tidak terserap dalam pasar kerja.
    """ 
    )

    # Membaca Dataset Angkatan Kerja : AK20Indonesia.xlsx
# df3 = pd.read_excel('AK20Indonesia.xlsx')
# Membaca Dataset Pengangguran Terbuka : PT20Nasional.xlsx
# df4 = pd.read_excel('PT20Nasional.xlsx')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Klasifikasi", "Kategori Umur", "Pendidikan tertinggi yang ditamatkan", "Kategori pengangguran terbuka", "Sebaran PT Provinsi"])

with tab1 :
    ##################### Bagian 2.2.1 - Klasifikasi ##################
    
    # Klasifikasi
    klasifikasi1 = df3.query('Karakteristik == "Klasifikasi"').drop(columns='Karakteristik')
    klasifikasi2 = df4.query('Karakteristik == "Klasifikasi"').drop(columns='Karakteristik')

    # Bar Plot Angkatan Kerja (Klasifikasi)
    fig3 = px.bar(
        klasifikasi1,
        x='Kategori',
        y=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Klasifikasi (AK)',
        height=800, width=800)

    # Bar Plot Pengangguran Terbuka (Klasifikasi)
    fig4 = px.bar(
        klasifikasi2,
        x='Kategori',
        y=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Klasifikasi (PT)',
        height=800, width=800)

    # Layout Klasifikasi
    container1 = st.container()
    col1, col2 = st.columns(2)

    with container1 :
        with col1 :
            st.plotly_chart(fig3)
        with col2 :
            st.plotly_chart(fig4)
    
    # Penjelasan Grafik Klasifikasi
    st.markdown(
        """
        - Proporsi perempuan AK lebih rendah di pedesaan.
        - Proporsi perempuan PT lebih rendah di pedesaan.
        """ 
        )
    
with tab2 :
    ##################### Bagian 2.2.2 - Kelompok Umur ##################

    # Kelompok Umur
    kelompok_umur1 = df3.query('Karakteristik == "Kelompok Umur"').drop(columns='Karakteristik')
    kelompok_umur2 = df4.query('Karakteristik == "Kelompok Umur"').drop(columns='Karakteristik')

    # Bar Plot Angkatan Kerja (Kelompok Umur)
    fig5 = px.bar(
        kelompok_umur1,
        y='Kategori',
        x=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Kelompok Umur (AK)',
        orientation = 'h',
        height=800, width=800)

    # Bar Plot Pengangguran Terbuka (Kelompok Umur)
    fig6 = px.bar(
        kelompok_umur2,
        y='Kategori',
        x=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Kelompok Umur (PT)',
        orientation = 'h',
        height=800, width=800)

    # Layout Kelompok Umur
    container2 = st.container()
    col3, col4 = st.columns(2)

    with container2 :
        with col3 :
            st.plotly_chart(fig5)
        with col4 :
            st.plotly_chart(fig6)
    
    # Penjelasan Grafik Kategori Umur
    st.markdown(
        """
        - Proporsi perempuan usia NEET (15-24 tahun) lebih besar di PT.
        """ 
        )
    
with tab3 :
    ##################### Bagian 2.2.3 - Pendidikan tertinggi yang ditamatkan ##################
      
    # Pendidikan tertinggi yang ditamatkan
    pendidikan1 = df3.query('Karakteristik == "Pendidikan tertinggi yang ditamatkan"').drop(columns='Karakteristik')
    pendidikan2 = df4.query('Karakteristik == "Pendidikan tertinggi yang ditamatkan"').drop(columns='Karakteristik')

    # Bar Plot Angkatan Kerja (Pendidikan tertinggi yang ditamatkan)
    fig7 = px.bar(
        pendidikan1,
        y='Kategori',
        x=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Pendidikan tertinggi yang ditamatkan (AK)',
        orientation = 'h',
        height=800, width=800)

    # Bar Plot Pengangguran Terbuka (Pendidikan tertinggi yang ditamatkan)
    fig8 = px.bar(
        pendidikan2,
        y='Kategori',
        x=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Pendidikan tertinggi yang ditamatkan (PT)',
        orientation = 'h',
        height=800, width=800)

    # Layout Pendidikan tertinggi yang ditamatkan
    container3 = st.container()
    col5, col6 = st.columns(2)

    with container3 :
        with col5 :
            st.plotly_chart(fig7)
        with col6 :
            st.plotly_chart(fig8)
    
    # Penjelasan Grafik Pendidikan tertinggi yang ditamatkan
    st.markdown(
        """
        - Proporsi PT lebih banyak di tingkat pendidikan SLTA.
        """ 
        )

with tab4 :
    ##################### Bagian 2.2.4 - Kategori pengangguran terbuka ##################
      
    # Kategori pengangguran terbuka
    kpt = df4.query('Karakteristik == "Kategori pengangguran terbuka"').drop(columns='Karakteristik')

    # Bar Plot Pengangguran Terbuka (Kategori pengangguran terbuka)
    fig9 = px.bar(
        kpt,
        x='Kategori',
        y=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Kategori pengangguran terbuka (PT)',
        orientation = 'v',
        height=800, width=1200)
    
    st.plotly_chart(fig9)
    
with tab5 :
    ##################### Bagian 2.2.5 - Sebaran PT Provinsi ##################
    
    # Sebaran PT Provinsi
    pt_prov = df4.query('Karakteristik == "Nama Provinsi"').drop(columns='Karakteristik')
    
    # Bar Plot Sebaran PT Provinsi
    fig10 = px.bar(
        pt_prov,
        x='Kategori',
        y=['Laki-laki', 'Perempuan', 'Total'],
        barmode='group',
        title='Sebaran Provinsi (PT)',
        orientation = 'v',
        height=800, width=1600)
    
    st.plotly_chart(fig10)

##################### Bagian 3 - Pembahasan ##################
st.subheader("Beberapa Faktor Mungkin Mempengaruhi Kaula Muda NEET")

with st.expander("° Pendidikan") :
    st.markdown(
            """
            - Putus pendidikan
            - Biaya pendidikan atau pelatihan
            - Norma dan persepsi sosial terhadap pendidikan atau pelatihan
            """ 
            )

with st.expander("° Peralihan") :
    st.markdown(
            """
            - Keterampilan tidak sesuai
            - Kurang informasi pasar tenaga kerja
            - Layanan ketengakerjaan sederhana
            """ 
            )

with st.expander("° Pasar tenaga kerja") :
    st.markdown(
            """
            - Pekerjaan tidak memadai
            - Pesimis
            - Peluang meningkatkan keterampilan terbatas
            """ 
            )

st.subheader("ML Regresi Berganda")
st.markdown(
            """
            *Pengaruh Jenis Kelamin dan Usia terhadap NEET*
            
            - H0 : Jenis kelamin dan usia tidak berpengaruh terhadap NEET
            - H1 : Jenis kelamin dan usia berpengaruh terhadap NEET
            """ 
            )
# Mengimpor library yang diperlukan
import numpy as np
import pandas as pd

# Mengimpor dataset
# df5 = pd.read_excel('EIP_NEET_SEX_AGE_RT_A-filtered-2022-10-10.xlsx').drop(columns='Year')

df5_1 = df5.loc[(df5['Gender'] != 'Total') & (df5['Age'] != 'Total')]

n = pd.get_dummies(df5_1)

X = n[['Gender_Female', 'Age_15-19']].values

y = n['NEET total (% of youth population)'].values

# Membagi data menjadi the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Membuat model Multiple Linear Regression dari Training set
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Memprediksi hasil Test set
y_pred = regressor.predict(X_test)

with st.expander("° Machine Learning") :
    #Evaluate Model Performance
    st.write('Training Accuracy :', regressor.score(X_train, y_train))  
    st.write('Testing Accuracy :', regressor.score(X_test, y_test))

with st.expander("° Statistik") :
    # Memilih model multiple regresi yang paling baik dengan metode backward propagation
    import statsmodels.api as sm

    def backwardElimination(x, sl):
        jum_kol = len(x[0])
        for i in range(0, jum_kol):
            regressor_OLS = sm.OLS(endog = y, exog = x).fit()
            p_val = regressor_OLS.pvalues.astype(float)
            max_index = np.argmax(p_val, axis = 0)
            nilai_max = max(regressor_OLS.pvalues).astype(float)
            if nilai_max > sl:
                x = np.delete(x, max_index, 1)
        st.write(regressor_OLS.summary())
    SL = 0.05
    X_new = sm.add_constant(X)
    X_opt = X_new[:, [0, 1, 2]]
    X_Modeled = backwardElimination(X_opt, SL)
st.markdown(
            """
            Nilai p = 0
            
            Dari hasil regresi berganda, didapatkan bahwa nilai p = 0 < *alpha* (0.05). Hal ini berarti kita dapat menolak H0. Dengan demikian Jenis Kelamin (x1) dan Usia (x2) berpengaruh terhadap kasus NEET.
            """ 
            )
    
st.subheader("Simpulan")
st.markdown(
            """
            Karena jumlah NEET cenderung meningkat, kemudian perlu diantisipasi segera dan ditangani secara serius. Oleh karenanya salah satu tujuan yang bisa diimplementasikan adalah mempromosikan pertumbuhan ekonomi yang berkelanjutan dan inklusif, lapangan kerja penuh dan produktif, serta pekerjaan yang layak untuk semua dengan target secara substansial mengurangi proporsi pemuda yang tidak bekerja, tidak sedang mengikuti pendidikan atau pelatihan.
            """ 
            )

##################### Bagian 3.2 - Pembahasan 2 ##################    
st.subheader("Beberapa Kebijakan Mungkin Bisa Diterapkan")

with st.expander("° Dijangkau dan Didukung") :
    st.markdown(
            """
            Pendekatan yang dibuat khusus untuk menjangkau dan membawa dukungan kepada kaula muda *NEET*
            - Sosialisasi dan menarik *NEET* kepada layanan yang tersedia
            - Program integrasi pasar tenaga kerja
            """ 
            )

with st.expander("° Magang") :
    st.markdown(
            """
            Setelah krisis ketenagakerjaan kaula muda yang dipicu oleh krisis keuangan global 2007/08, magang dipromosikan sebagai solusi (G20, ILO, Komisi Eropa, dll.)
            - Mengembangkan keterampilan yang sesuai dengan pekerjaan sembari menghasilkan
            - Mengurangi ketidakcocokan keterampilan
            """ 
            )

with st.expander("° Orientasi Karir dan Bimbingan Pekerjaan") :
    st.markdown(
            """
            Sekolah, pusat pelatihan dan layanan ketenagakerjaan publik yang mengarahkan kaula muda untuk pekerjaan masa depan
            - Membentuk harapan realistis terhadap pekerjaan masa depan
            - Memotivasi kaula muda
            """ 
            )
with st.expander("° Kewirausahaan dan Akses Keuangan") :
    st.markdown(
            """
            - Memotivasi kaula muda berbakat untuk memulai bisnis dan melatih mereka
            - Skema pembiayaan inovatif : *Platform* pinjaman *peer-to-peer*
            """ 
            )

# Header Simpulan dan Saran
#st.header("Simpulan & Saran")


# Header Dapus
st.header("Daftar Pustaka")


st.markdown(
        """
        - International Labour Organization (ILO). (2020). *Youth not in employment, education or training*. Diakses pada Oktober 2022, dari [https://ilostat.ilo.org](https://ilostat.ilo.org).
        - *NEET's in Japan: What Does It Mean?* (2015, Juni). Japan Info. Diakses dari [https://jpinfo.com](https://jpinfo.com).
        - Satu Data Ketenagakerjaan. (2022). *Angkatan Kerja (AK) Periode Februari 2022 di Indonesia*. Diakses pada Oktober 2022, dari [https://satudata.kemnaker.go.id/](https://satudata.kemnaker.go.id/).
        - Satu Data Ketenagakerjaan. (2022). *Pengangguran Terbuka Periode Februari 2022 di Indonesia*. Diakses pada Oktober 2022, dari [https://satudata.kemnaker.go.id/](https://satudata.kemnaker.go.id/).
        - The World Bank. (2022). *Share of youth not in education, employment or training, total (% of youth population) - Indonesia*. Diakses dari [https://data.worldbank.org](https://data.worldbank.org).
        """ 
        )

#Plotting y_test dan y_pred
#plt.scatter(y_test, y_pred, c = 'green')
#plt.xlabel('Price Actual')
#plt.ylabel('Predicted value')
#plt.title('True value vs predicted value : Linear Regression')
#plt.show()

# scatter_fig = plt.figure(figsize=(15,9))
# scatter_ax = scatter_fig.add_subplot(111)

# plt.scatter(y_test, y_pred, color='green')
# plt.ylim(ymin=0, ymax=50)
# ax11.set_ylim(ymin=0, ymax=40)
# ax11.text(1, -0.1, 'Sumber data: ilostat.ilo.org', color='blue', ha='right', transform=ax1.transAxes)

# st.pyplot(scatter_fig)