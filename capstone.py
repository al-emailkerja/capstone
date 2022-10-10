##################### Library ##################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


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

# Membaca Dataset : API_SL.UEM.NEET.ZS_DS2_en_excel_v2_4530053.xls (https://ilostat.ilo.org/data/)
# df1 = pd.read_csv('youth-not-in-education-employment-training.csv', sep=',')
df1 = pd.read_excel('API_SL.UEM.NEET.ZS_DS2_en_excel_v2_4530053.xls', sheet_name = 'Indo')
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
df2 = pd.read_csv('Share of youth not in employment, education or training (%).csv', sep=',')

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
df3 = pd.read_excel('AK20Indonesia.xlsx')
# Membaca Dataset Pengangguran Terbuka : PT20Nasional.xlsx
df4 = pd.read_excel('PT20Nasional.xlsx')

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



#st.subheader("Saran")



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
