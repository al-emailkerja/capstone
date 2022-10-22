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
# st.set_page_config(layout="wide")

# Judul
st.title("Fenomena *NEET* : Kaula Muda Negeri Ini *Hopeless* ?")

# Header 1
st.header("Apa Itu NEET ?")

# Deskripsi 1
st.markdown(
    """
    NEET (*Not in Employment, Education or Training*) muncul pertama kali di Jepang pada tahun 1990 yang menggambarkan seseorang yang tidak bekerja dan tidak mencari pekerjaan, serta bukan merupakan seorang yang tengah menempuh pendidikan ataupun mengurus rumah tangga.
    
    Awal kemunculan NEET memang belum dianggap sebagai masalah, namun seiring dengan berjalannya waktu, jumlah kaula muda yang tergolong NEET ini terus meningkat sehingga perlu diantisipasi oleh semua pihak karena akan berdampak negatif baik bagi pemuda itu sendiri, keluarga karena akan menanggung beban ekonomi dan sosial, masyarakat dan pemerintah atau negara karena keberlanjutan laju pertumbuhan ekonomi suatu bangsa akan terpengaruh akibat semakin meningkatnya pemuda produktif yang enggan untuk berada di pasar kerja, dan semakin sedikitnya stok pemuda kompeten karena mereka enggan berada di dunia pendidikan ataupun pelatihan kerja.
    
    **Ciri NEET (Kemenaker, 2020) :**
    - *Perempuan*
    - *Pedesaan*
    - *Pendidikan rendah*
    
    `Pertanyaan : Masih kah ?`
    """ 
    )
#st.caption("")
##################### Bagian 1 - Tren: remaja (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan ##################

 
# st.dataframe(df) 
# Membaca Dataset : API_SL.UEM.NEET.ZS_DS2_en_excel_v2_4530053.xls (https://ilostat.ilo.org/data/)

# Sub-Header 1
#st.subheader("Tren: remaja (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan")

df1 = pd.read_csv(r'https://raw.githubusercontent.com/al-emailkerja/capstone/main/dataset/df1.csv')

with st.expander("Tren: kaula muda (berusia 15-24 tahun) tidak dalam pendidikan, pekerjaan, atau pelatihan") :
    # Line Plot NEET Indonesia
    fig1, ax1 = plt.subplots(figsize=(10,5))
    
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
st.header("Sudut Pandang")

# Sub-Header 2
st.subheader("Perempuan, Masih Kah ?")

# Deskripsi 2
st.markdown(
    """
    Menurut ILO (*International Labour Organization*), kaula muda perempuan lebih berpotensi menjadi NEET dibandingkan dengan kaula muda laki-laki. Perempuan memiliki resiko relatif 3.4 kali lebih besar dibandingkan laki-laki untuk menjadi NEET. Persepsi orang tua terhadap pendidikan, pekerjaan, serta kesulitan untuk masuknya pasar tenaga kerja perempuan mempengaruhi tingkat NEET perempuan.
    """ 
    )


##################### Bagian 2.1 - Perempuan dalam NEET ##################

# Membaca Dataset : Share of youth not in employment, education or training (%).csv (https://data.worldbank.org/)
# df2 = pd.read_csv('Share of youth not in employment, education or training (%).csv', sep=',')
df2 = pd.read_csv(r'https://raw.githubusercontent.com/al-emailkerja/capstone/main/dataset/df2.csv')
# Drop Kolom
df2.drop(columns=['indicator.label','source.label','obs_status.label','note_indicator.label', 'note_source.label'], inplace=True)

# Rename Kolom
df2.set_axis(['Country', 'Jenis Kelamin', 'Year', 'NEET'], axis='columns', inplace=True)

# Menghapus Total
df2 = df2.sort_values(by='Jenis Kelamin').set_index('Jenis Kelamin')
df2 = df2.drop(df2.index[6:])
df2 = df2.reset_index()

with st.expander("NEET Berdasarkan Jenis Kelamin"):
    # Bar Plot Neet Indonesia by Sex
    fig2, ax2 = plt.subplots(figsize=(10,5))

    sns.barplot(data=df2, x='Year', y='NEET', hue='Jenis Kelamin', ax=ax2, palette="Paired")
    ax2.set_title('Tingkat NEET Berdasarkan Jenis Kelamin')
    ax2.set_xlabel('Tahun')
    ax2.set_ylabel('NEET (% Populasi Kaula Muda)')
    #ax2.legend(['Perempuan', 'Laki-laki'])
    ax2.set_ylim(ymin=0, ymax=40)
    ax2.text(1, -0.1, 'Sumber data: data.worldbank.org', color='blue', ha='right', transform=ax2.transAxes)

    st.pyplot(fig2)
    
    st.markdown(
        """
        Memang benar NEET perempuan lebih tinggi dibandingkan dengan laki-laki. Nilai dari NEET perempuan berada disekitar angka 26%, sedangkan laki-laki 15-18%. Akan tetapi jika dilihat lebih teliti, NEET laki-laki selalu naik sekitar 1-2% setiap tahun. 
        
        `Pertanyaan : Akan berbalik kah ?`
        """ 
        )
    
    # Penjelasan Grafik 2
    #st.markdown(
       # """
        #- NEET perempuan berada disekitar angka 26%.
        #- NEET laki-laki setiap tahun mengalami kenaikan 1-2%.
        #""" 
        #)
 
 
 
    
 
# Sub-Header 3
st.subheader("Isu Pengangguran")

# Deskripsi 3
st.markdown(
    """
    Terkait isu pengangguran dimana sering timbul pertanyaan apakah NEET dan pengangguran adalah hal yang sama? Secara teknis bisa diartikan sama karena baik penganggur maupun kaula muda yang berada dalam katagori NEET sama-sama tidak bekerja. Mereka yang tidak bekerja ini dapat diartikan sebagai menganggur atau tidak aktif di pasar kerja. Pada Februari 2022, terdapat sekitar 144.01 juta Angkatan Kerja (AK) di Indonesia atau sekitar 69.06% dari total penduduk usia kerja di Indonesia yang berpartisipasi aktif dalam pasar kerja. Terdapat sekitar 8.40 juta orang Pengangguran Terbuka (PT) di Indonesia atau sebesar 5.83% dari total angkatan kerja di Indonesia yang tidak terserap dalam pasar kerja.
    """ 
    )

df3 = pd.read_csv(r'https://raw.githubusercontent.com/al-emailkerja/capstone/main/dataset/df3.csv')

#st.dataframe(df3)

default_color = 'lightsteelblue'

with st.expander("Kelompok Umur"):
    colors2 = {'Laki-laki': 'steelblue'}

    color_discrete_map = {
        c: colors2.get(c, default_color) 
        for c in df3.query('Karakteristik == "Kelompok Umur"').drop(columns='Karakteristik')}

    fig4 = px.bar(
            df3.query('Karakteristik == "Kelompok Umur"').drop(columns='Karakteristik'),
            x='Kategori',
            y=['Laki-laki', 'Perempuan'],
            barmode='group',
            title='Kelompok Umur PT (%)',
            labels={'value':'Jenis Kelamin (PT %)', 'Kategori':'Kelompok Umur', 'variable':'Jenis Kelamin'},
            color_discrete_map=color_discrete_map,
            height=700, width=700).update_traces(marker_line_width=0).update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    st.plotly_chart(fig4)

    # Penjelasan Grafik 4
    #st.markdown(
        #"""
        #- Disetiap kelompok umur, penganggur Laki-laki lebih besar dibandingkan Perempuan.
        #- Di kelompok umur NEET (15-24 tahun), memiliki proporsi terbesar.
        #""" 
        #)
        
with st.expander("Kategori pengangguran terbuka"):
    colors4 = {'Laki-laki': 'steelblue'}

    color_discrete_map = {
        c: colors4.get(c, default_color) 
        for c in df3.query('Karakteristik == "Kategori pengangguran terbuka"').drop(columns='Karakteristik')}

    fig6 = px.bar(
            df3.query('Karakteristik == "Kategori pengangguran terbuka"').drop(columns='Karakteristik'),
            x='Kategori',
            y=['Laki-laki', 'Perempuan'],
            barmode='group',
            title='Kategori pengangguran terbuka (%)',
            labels={'value':'Jenis Kelamin (PT %)', 'Kategori':'Status', 'variable':'Jenis Kelamin'},
            color_discrete_map=color_discrete_map,
            height=700, width=700).update_traces(marker_line_width=0).update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    st.plotly_chart(fig6)

    # Penjelasan Grafik 6
    #st.markdown(
        #"""
        #- Status mencari pekerjaan dan laki-laki memiliki proporsi terbesar.
        #""" 
        #)

#st.caption("katagori yang sedang mencari pekerjaan paling dominan")
st.markdown("""
           Kategori mencari pekerjaan paling dominan jika dilihat dari keempat kategori yang digambarkan pada grafik di atas. Ada kemungkinan yang masuk ke kategori ini berusia 15-24 tahun. Hal ini mungkin karena mereka yang ada pada kelompok usia ini biasanya tidak lagi berada di dunia pendidikan (sudah lulus dan/atau sedang mencari pekerjaan) dan mayoritas laki-laki.
           """)   
# Sub-Header 4
st.subheader("Pedesaan, Masih Kah ?")

with st.expander("Klasifikasi Desa-Kota"):
    colors1 = {'Laki-laki': 'steelblue'}

    color_discrete_map = {
        c: colors1.get(c, default_color) 
        for c in df3.query('Karakteristik == "Klasifikasi"').drop(columns='Karakteristik')}

    fig3 = px.bar(
            df3.query('Karakteristik == "Klasifikasi"').drop(columns='Karakteristik'),
            x='Kategori',
            y=['Laki-laki', 'Perempuan'],
            barmode='group',
            title='Klasifikasi PT (%)',
            labels={'value':'Jenis Kelamin (PT %)', 'Kategori':'Wilayah', 'variable':'Jenis Kelamin'},
            color_discrete_map=color_discrete_map,
            height=700, width=700).update_traces(marker_line_width=0).update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    st.plotly_chart(fig3)

    # Penjelasan Grafik 3
    #st.markdown(
        #"""
        #- Baik di Perkotaan maupun di Pedesaan, penganggur Laki-laki lebih besar dibandingkan Perempuan.
        #""" 
        #)

with st.expander("Sebaran PT Provinsi"):
    colors5 = {'Laki-laki': 'steelblue'}

    color_discrete_map = {
        c: colors5.get(c, default_color) 
        for c in df3.query('Karakteristik == "Nama Provinsi"').drop(columns='Karakteristik')}

    fig7 = px.bar(
            df3.query('Karakteristik == "Nama Provinsi"').drop(columns='Karakteristik'),
            y='Kategori',
            x=['Laki-laki', 'Perempuan'],
            orientation='h',
            barmode='group',
            title='Penyebaran PT Provinsi (%)',
            labels={'value':'Jenis Kelamin (PT %)', 'Kategori':'Nama Provinsi', 'variable':'Jenis Kelamin'},
            color_discrete_map=color_discrete_map,
            height=700, width=700).update_traces(marker_line_width=0).update_layout(xaxis_showgrid=False, yaxis_showgrid=False, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig7)

    # Penjelasan Grafik 7
    #st.markdown(
        #"""
        #- Di setiap provinsi, penganggur Laki-laki lebih besar dibandingkan Perempuan.
        #- Provinsi Jawa Barat memiliki proporsi terbesar, diikuti dengan provinsi lain di pulau Jawa.
        #""" 
        #)
#st.caption("katagori yang sedang mencari pekerjaan paling dominan")
st.markdown(
    """
    Laki-laki mendominasi tingkat pengangguran baik di pedesaan maupun di perkotaan dan penganggur lebih banyak berada di perkotaan. Jika dilihat penyebarannya, penganggur paling banyak ada di Pulau Jawa. Hal ini mungkin karena banyak orang yang berpikir untuk mengadu nasib di kota-kota besar di Pulau Jawa. Dengan adanya dampak pandemi COVID-19, tidak sedikit pekerja yang mengalami PHK dan mungkin masih bertahan di perantauan. Hal ini mungkin yang menjadi penyebab dari tingginya tingkat pengangguran tersebut. 
    """
)

# Sub-Header 5
st.subheader("Pendidikan Rendah, Masih Kah ?")

st.markdown(
    """
    Secara umum, semakin tinggi tingkat pencapaian seseorang dalam pendidikan maka semakin memperkecil peluang seseorang tersebut untuk menjadi NEET. Saat dilakukan analisis lanjutan dengan peubah jenis kelamin, diperoleh infomasi bahwa penurunan kemungkinan menjadi NEET seiring semakin tingginya pendidikan seseorang lebih tinggi terjadi pada perempuan dibanding laki-laki (Pattinasarany, 2019).
    """
)
    
with st.expander("Pendidikan tertinggi yang ditamatkan"):
    colors3 = {'Laki-laki': 'steelblue'}

    color_discrete_map = {
        c: colors3.get(c, default_color) 
        for c in df3.query('Karakteristik == "Pendidikan tertinggi yang ditamatkan"').drop(columns='Karakteristik')}

    fig5 = px.bar(
            df3.query('Karakteristik == "Pendidikan tertinggi yang ditamatkan"').drop(columns='Karakteristik'),
            x='Kategori',
            y=['Laki-laki', 'Perempuan'],
            barmode='group',
            title='Pendidikan tertinggi yang ditamatkan PT (%)',
            labels={'value':'Jenis Kelamin (PT %)', 'Kategori':'Tingkat Pendidikan', 'variable':'Jenis Kelamin'},
            color_discrete_map=color_discrete_map,
            height=700, width=700).update_traces(marker_line_width=0).update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    st.plotly_chart(fig5)

    # Penjelasan Grafik 5
    st.markdown(
        """
        - Kecuali di tingkat Diploma/Akademi, penganggur Laki-laki lebih besar dibandingkan Perempuan.
        - Tingkat SLTA sederajat memiliki proporsi terbesar.
        """ 
        )
    
#st.caption("katagori yang sedang mencari pekerjaan paling dominan")
#st.markdown(
    #"""
    #Laki-laki masih mendominasi tingkat pengangguran disetiap tingkat pendidikan, kecuali ditingkat Diploma/Akademi.
    #"""
#)

st.subheader("Faktor yang Mungkin Berpengaruh")

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
            - Jika ditinjau dari segi Pengangguran Terbuka (PT), ada kemungkinan NEET kaula muda laki-laki akan lebih tinggi dibandingkan dengan perempuan.
            - Jumlah NEET cenderung meningkat, kemudian perlu diantisipasi segera dan ditangani secara serius.
            - Jenis kelamin, usia, tingkat pendidikan, dan mungkin berbagai faktor lain dapat mempengaruhi seseorang untuk cenderung menjadi atau tidak menjadi NEET.
            """ 
            )

##################### Bagian 3.2 - Pembahasan 2 ##################    
st.subheader("Rekomendasi")

st.markdown(
            """
            - Perlu perhatian semua pihak untuk menyadari dan memahami keberadaan fenomena NEET di Indonesia dan dampak negatif yang ditimbulkannya, untuk kemudian diantisipasi segera dan dicarikan solusi yang efektif.
            
            - Meningkatkan TPAK laki-laki : pendidikan dan keterampilan untuk dapat lebih mudah mengerjakan tugas dan pekerjaan yang fleksibel (teknologi).
            
            - Kesempatan kerja yang tersedia perlu diperluas lagi antara lain melalui fasilitasi penumbuhan dan pengembangan wirausaha.
            
            - Penyesuaian kurikulum di dunia pendidikan dan pelatihan kerja dengan jenis dan tingkat kompetensi yang dibutuhkan pasar kerja.
            
            - Agar fenomena NEET dapat diantisipasi dengan efektif dan efisien, diperlukan penelitian lebih lanjut mengenai fenomena NEET di Indonesia.
            """ 
            )




# Header Dapus
st.header("Daftar Pustaka")


st.markdown(
        """
        - International Labour Organization (ILO). (2020). *Youth not in employment, education or training*. Diakses pada Oktober 2022, dari [https://ilostat.ilo.org](https://ilostat.ilo.org).
        - *NEET's in Japan: What Does It Mean?* (2015, Juni). Japan Info. Diakses dari [https://jpinfo.com](https://jpinfo.com).
        - Pattinasarany, I. R. I. (2019). *Not in Employment, Education or Training (NEET) Among the Youth in Indonesia: The Effects of Social Activities, Access to Information, and Language Skills on NEET Youth*. MASYARAKAT: Jurnal Sosiologi, 1-25.
        - Satu Data Ketenagakerjaan. (2022). *Angkatan Kerja (AK) Periode Februari 2022 di Indonesia*. Diakses pada Oktober 2022, dari [https://satudata.kemnaker.go.id/](https://satudata.kemnaker.go.id/).
        - Satu Data Ketenagakerjaan. (2022). *Pengangguran Terbuka Periode Februari 2022 di Indonesia*. Diakses pada Oktober 2022, dari [https://satudata.kemnaker.go.id/](https://satudata.kemnaker.go.id/).
        - The World Bank. (2022). *Share of youth not in education, employment or training, total (% of youth population) - Indonesia*. Diakses dari [https://data.worldbank.org](https://data.worldbank.org).
        """ 
        )

