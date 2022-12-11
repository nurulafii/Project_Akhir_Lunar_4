<?php

// koneksi ke database
$host = 'localhost';
$user = 'root';
$pass = '';
$db = 'nurvalbiky';

$koneksi = mysqli_connect($host,$user,$pass,$db) or die("Database Error");

// ambil pesan dari ajax
$pesan = mysqli_real_escape_string($koneksi, $_POST['isi_pesan']);

// cek pertanyaan ke dalam tabel
$cek_data = mysqli_query($koneksi, "SELECT jawaban FROM chatbot WHERE pertanyaan LIKE '%$pesan%' ");

// jika pertanyaan ditemukan, maka tampilkan jawaban
if (mysqli_num_rows($cek_data) > 0) { 
    // hasil query tampung ke dalam variabel data
    $data = mysqli_fetch_assoc($cek_data);
    // tampung jawaban ke dalam variabel untuk dikirim ke ajax
    $balasan = $data['jawaban'];
    echo $balasan;
} else {
    echo "Maaf, saya belum menemukan jawaban yang kamu maksud :( ";
}
?>