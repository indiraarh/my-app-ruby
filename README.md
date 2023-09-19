Nama    : Indira Arifia Rahmah

NPM     : 2206811846

Kelas   : PBP B

# Tugas 2
## POST vs. GET

# Tugas 1
Nama Aplikasi: Ruby (tautan adaptable.io: https://my-app-ruby.adaptable.app/)

Pengerjaan tugas ini adalah hasil pembelajaran dari tutorial yang telah diajarkan saat sesi lab di kuliah. Cara saya menuntaskan tugas ini adalah melalui pembuatan proyek lain sebagai latihan terlebih dulu sebelum mengerjakan proyek ini. Dengan demikian, saya memahami langkah demi langkahnya dengan membiasakan diri membuat suatu proyek.

![request client Django](request-client-Django.png)
Dalam bagan tersebut, berikut adalah penjelasannya:

1. Client mengirimkan HTTP Request ke Load Balancer.
2. Load Balancer meneruskan request tersebut ke Django Web App.
3. Django Web App menggunakan urls.py untuk pemetaan URL dan menentukan view mana yang harus dipanggil.
4. views.py dapat melakukan query ke database melalui models.py.
5. models.py bertugas untuk mengambil data dari Database.
6. views.py juga bertugas untuk merender template yang ada di HTML Template.
7. Setelah itu, Django Web App mengirimkan HTTP Response kembali ke Client.

Virtual Environment adalah alat yang membantu memisahkan dependensi yang diperlukan oleh berbagai proyek dengan membuat lingkungan virtual python terisolasi untuk proyek tersebut.
Jika kita menggunakan virtual environment dalam membuat web aplikasi, beberapa manfaat yang kita dapatkan, yaitu:
1. Dependensi yang terisolasi. Artinya setiap proyek dapat memiliki dependensi yang berbeda dengan versi yang berbeda. Hal ini berfungsi untuk menghindari konflik antar versi.
2. Keamanan. Jika ada suatu pustaka pada proyek kita yang rentan keamanannya maka risiko keamanan hanya dimiliki oleh pustaka itu saja, lingkungan lainnya tidak.
3. Virtual environment memungkinkan kita untuk menggunakan versi Python yang berbeda untuk proyek yang berbeda.
4. Memudahkan dalam berbagi proyek. Requirements.txt memudahkan kolaborasi antarpengembang karena dapat dengan muda mengintall semua dependensi yang diperlukan dalam virtual environment mereka sendiri.

Virtual environment penting dalam membuat proyek seperti web aplikasi ini. Akan tetapi, kita juga dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Tentu saja hal ini diikuti oleh beberapa risiko, seperti (1) rentan akan konolik antardependensi; (2) Jika ingin memperbarui atau menghapus pustaka tertentu maka harus dengan cara manual; (3) 
Jika ada proyek yang rentan keamanannya, maka akan memengaruhi proyek lainnya juga.


Model-View-Controller (MVC), Model-View-Template (MVT), dan Model-View-ViewModel (MVVM) adalah pola desain yang digunakan dalam pengembangan perangkat lunak, khususnya aplikasi web dan aplikasi berbasis GUI. Berikut ini penjelasan singkat dan perbedaan dari ketiga pola desain tersebut:

Model-View-Controller (MVC)
Model: Bagian ini bertanggung jawab atas data dan aturan bisnis. Ini mewakili struktur data dan menyediakan mekanisme untuk membaca, menyimpan, dan memperbarui data.
View: Bagian ini menampilkan data untuk pengguna. Dalam aplikasi web, view biasanya adalah halaman HTML yang dihasilkan.
Controller: Menerima input dari pengguna melalui view, memprosesnya (dengan interaksi dengan model), dan mengembalikan tampilan output yang sesuai.
Aplikasi yang sering menggunakan pola ini: Rails, ASP.NET MVC, dan banyak framework web lainnya.

Model-View-Template (MVT)
Mirip dengan MVC, namun dengan sedikit perbedaan dalam pendekatan.
Model: Sama seperti di MVC.
View: Bertanggung jawab untuk memproses model dan mengembalikannya ke template. Dalam konteks Django (yang menggunakan MVT), "view" lebih seperti controller dalam MVC.
Template: Ini adalah bagian yang menggambarkan bagaimana data harus ditampilkan. Ini mirip dengan "view" dalam MVC.
Django adalah contoh framework yang menggunakan pola MVT. Meskipun sering disebut sebagai "MVC", Django sebenarnya lebih mendekati MVT.

Model-View-ViewModel (MVVM)
Sering digunakan dalam aplikasi berbasis GUI, seperti yang dibuat dengan WPF, Angular, atau Knockout.js.
Model: Sama seperti di MVC dan MVT.
View: Hanya bertanggung jawab untuk menampilkan UI. Tidak memiliki logika bisnis.
ViewModel: Bertindak sebagai penghubung antara Model dan View. ViewModel menyajikan data dari Model dalam format yang dapat dengan mudah ditampilkan oleh View, dan juga menerima perintah dari View.
MVVM memungkinkan pemisahan yang lebih baik antara logika bisnis dan tampilan UI, memudahkan pengujian, dan mendukung pemrograman reaktif.
Perbedaan Utama:

MVC: Pemisahan antara data (Model), tampilan (View), dan logika bisnis (Controller).
MVT: Sebuah varian dari MVC di mana "View" dalam MVT bertindak lebih seperti "Controller" dalam MVC, dan "Template" bertindak seperti "View" dalam MVC.
MVVM: Didesain untuk aplikasi berbasis GUI. ViewModel bertindak sebagai perantara antara Model dan View, memungkinkan pengikatan data dua arah dan pemisahan antara logika UI dan logika bisnis.
Meskipun ada perbedaan dalam struktur dan terminologi, tujuan utama dari semua pola desain ini adalah memisahkan tanggung jawab dalam aplikasi, sehingga memudahkan pemeliharaan, pengembangan, dan pengujian.