# HMM-learn-kdd-network-traffic-dataset
HMM Learn Using KDD Cup 1999 Network Traffic Dataset
http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

Tugas Pembuatan Software Machine Learning
Kelompok 7:
1. Muhammad Akbar Yasin [23216322]
2. Rd. Rakha Agung [23216316]
3. Muhardi Saputra [23215329]
4. Lukman Nur Hakim [23215345]

Mata Kuliah Manajemen Keamanan Informasi

KDD Cup 1999 Data

# Abstrak
Dataset KDD Cup 1999 digunakan sebagai bahan untuk kompetisi data mining pada ajang KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. Kompetisi bertujuan untuk menghasilkan aplikasi yang dapat mendeteksi gangguan pada jaringan komputer.
http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

# Overview
Aplikasi ini menggunakan dataset KDD 1999, untuk masing-masing label traffic normal/serangan menggunakan maksimal 100 dataset acak dari dataset yang tersedia untuk dilatih. Lalu untuk pengujian mengambil masing-masing 1 dataset uji (acak) dari untuk tiap label. File utama yang digunakan adalah hmm_network_dataset.py. 
Penggunanaan 'python -W ignore hmm_network_dataset.py'
yang dieksekusi dari virtualenv yang telah dipersiapkan sebelumnya.

# Kebutuhan Aplikasi:
1. python versi 3
2. python virtual env
  - numpy
  - hmmlearn
  - pandas
  
 
# Tutorial penggunaan
https://youtu.be/MFjUgplCoTw

# Resource
https://github.com/jadianes/kdd-cup-99-spark
http://machinelearningmastery.com/machine-learning-in-python-step-by-step/
https://github.com/muhakbaryasin/Python-Real-World-Machine-Learning
